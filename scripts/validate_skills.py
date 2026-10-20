#!/usr/bin/env python3
"""Validate this repository's Agent Skills against the open specification.

The validator is intentionally strict. It is the release gate that prevents a
formatter, merge, or manual edit from silently corrupting ``SKILL.md``
frontmatter again -- the failure mode that makes a skill undiscoverable.

Checks implemented
------------------
* ``SKILL.md`` starts with YAML frontmatter delimited by ``---``.
* Required spec fields ``name`` and ``description`` are present and valid.
* ``name`` matches the parent directory and the specification grammar.
* Optional fields (``license``, ``compatibility``, ``metadata``,
  ``allowed-tools``) conform to the specification.
* Enterprise metadata (``spec``, ``standards``, ``risk``) is present as
  strings.
* The body has one H1, stays within progressive-disclosure limits, contains no
  unresolved ``{{PLACEHOLDER}}`` tokens, and every relative link resolves.
* ``evals/<name>.yaml`` exists, matches the skill version, and contains both
  positive and negative trigger cases.

Usage
-----
    python scripts/validate_skills.py
    python scripts/validate_skills.py --format json --strict
    python scripts/validate_skills.py --root /path/to/repository

Exit status is ``0`` when no errors are found, ``1`` otherwise. ``--strict``
also fails on warnings.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without dependencies
    yaml = None  # type: ignore[assignment]


# --------------------------------------------------------------------------
# Specification constants
# --------------------------------------------------------------------------

SPEC_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
REQUIRED_FIELDS = {"name", "description"}

# Enterprise profile: every skill in this repository must declare these.
REQUIRED_METADATA = {
    "spec",
    "standards",
    "risk",
}
# Removed from this collection's standard on purpose. Document-control fields
# belong in CODEOWNERS, governance, and Git history, not in every document.
DISALLOWED_METADATA = {"owner", "reviewed", "classification"}
RISK_LEVELS = {"low", "medium", "high", "critical"}
ALLOWED_TOOLS = {
    "Read",
    "Write",
    "Edit",
    "Glob",
    "Grep",
    "Bash",
    "WebFetch",
    "WebSearch",
}
RESERVED_WORDS = ("anthropic", "claude")
SUPPORTED_SPEC_VERSION = "1.0"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TRIGGER_RE = re.compile(r"\bUse (when|for|to|after|before|only)\b", re.IGNORECASE)
XML_TAG_RE = re.compile(r"<\/?[A-Za-z][^>]*>")
PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")
CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)")
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "ftp://")
MAX_LINES = 500
MAX_DESCRIPTION = 1024
MAX_COMPATIBILITY = 500
MAX_TOKENS = 5000


@dataclass(frozen=True)
class Finding:
    """A single validation result."""

    level: str
    path: Path
    code: str
    message: str

    def __str__(self) -> str:
        return f"{self.level.upper():7} {self.path} [{self.code}] {self.message}"


# --------------------------------------------------------------------------
# Parsing helpers
# --------------------------------------------------------------------------


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return ``(frontmatter, body)`` or ``(None, text)``.

    The opening delimiter must be the very first line of the file. A leading
    blank line, BOM, or formatted horizontal rule is a hard failure: clients
    will not discover the skill.
    """

    if text.startswith("\ufeff"):
        text = text[1:]
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter = "".join(lines[1:index])
            body = "".join(lines[index + 1 :])
            return frontmatter, body
    return None, text


def relative_links(text: str) -> Iterable[str]:
    """Yield local link targets found in Markdown text."""

    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()
        yield target
    for match in REF_DEF_RE.finditer(text):
        yield match.group(1).strip()


def resolve_link(source: Path, target: str) -> Path | None:
    """Return the filesystem target for a local Markdown link."""

    if not target:
        return None
    if target.startswith(EXTERNAL_PREFIXES) or target.startswith("#"):
        return None
    if target.startswith("//") or PLACEHOLDER_RE.search(target):
        return None
    cleaned = target.split("#", 1)[0].split("?", 1)[0]
    if not cleaned:
        return None
    cleaned = cleaned.replace("%20", " ")
    return (source.parent / cleaned).resolve()


def estimate_tokens(text: str) -> int:
    """Approximate token count using the common four-characters heuristic."""

    return max(1, len(text) // 4)


def unresolved_placeholders(text: str) -> list[str]:
    """Return placeholder tokens outside code spans and fenced blocks."""

    cleaned = CODE_BLOCK_RE.sub("", text)
    cleaned = INLINE_CODE_RE.sub("", cleaned)
    return PLACEHOLDER_RE.findall(cleaned)


def error(path: Path, code: str, message: str) -> Finding:
    return Finding("error", path, code, message)


def warning(path: Path, code: str, message: str) -> Finding:
    return Finding("warning", path, code, message)


# --------------------------------------------------------------------------
# Skill validation
# --------------------------------------------------------------------------


def validate_skill(skill_dir: Path, repo_root: Path) -> list[Finding]:
    """Validate one skill directory and return all findings."""

    findings: list[Finding] = []
    skill_file = skill_dir / "SKILL.md"
    rel = skill_file.relative_to(repo_root)

    if not skill_file.is_file():
        return [error(rel, "SKILL001", "SKILL.md is missing")]

    raw = skill_file.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        findings.append(error(rel, "SKILL002", "file must not start with a UTF-8 BOM"))
        raw = raw[3:]
    if b"\r\n" in raw:
        findings.append(error(rel, "SKILL003", "file must use LF line endings"))
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return findings + [error(rel, "SKILL004", f"file is not valid UTF-8: {exc}")]
    if not text.endswith("\n"):
        findings.append(error(rel, "SKILL005", "file must end with a single newline"))

    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        findings.append(
            error(
                rel,
                "SKILL010",
                "missing YAML frontmatter: SKILL.md must begin with '---' on line 1 "
                "followed by name and description, then a closing '---'",
            )
        )
        if re.search(r"^#+\s*name:\s*", text, re.MULTILINE):
            findings.append(
                error(
                    rel,
                    "SKILL011",
                    "frontmatter appears to have been reformatted as Markdown; "
                    "restore the YAML block instead of repairing the rendered heading",
                )
            )
        return findings

    if yaml is None:
        return findings + [
            error(rel, "SKILL012", "PyYAML is required to validate frontmatter")
        ]

    try:
        data = yaml.safe_load(frontmatter)
    except yaml.YAMLError as exc:
        return findings + [
            error(rel, "SKILL013", f"frontmatter is not valid YAML: {exc}")
        ]
    if not isinstance(data, dict):
        return findings + [
            error(rel, "SKILL014", "frontmatter must parse to a mapping")
        ]

    findings.extend(_validate_frontmatter(data, skill_dir, rel, repo_root))

    stem = body.lstrip("\n")
    if not stem.strip():
        findings.append(error(rel, "SKILL040", "skill body is empty"))
    else:
        h1 = re.findall(r"^#\s+\S", stem, re.MULTILINE)
        if len(h1) != 1:
            findings.append(
                error(rel, "SKILL041", f"body must contain exactly one H1, found {len(h1)}")
            )
        if not stem.startswith("# "):
            findings.append(
                warning(rel, "SKILL042", "body should start with an H1 title after the frontmatter")
            )
        if unresolved_placeholders(stem):
            findings.append(
                error(rel, "SKILL043", "body contains unresolved {{PLACEHOLDER}} tokens")
            )
        if len(text.splitlines()) > MAX_LINES:
            findings.append(
                error(
                    rel,
                    "SKILL044",
                    f"SKILL.md is {len(text.splitlines())} lines; keep it under {MAX_LINES} "
                    "and move detail into references/",
                )
            )
        tokens = estimate_tokens(stem)
        if tokens > MAX_TOKENS * 2:
            findings.append(
                error(rel, "SKILL045", f"body is ~{tokens} tokens; move detail into references/")
            )
        elif tokens > MAX_TOKENS:
            findings.append(
                warning(
                    rel,
                    "SKILL046",
                    f"body is ~{tokens} tokens; the recommended maximum is {MAX_TOKENS}",
                )
            )

    findings.extend(_validate_links(skill_file, rel))
    findings.extend(_validate_reference_files(skill_dir, repo_root))
    return findings


def _validate_frontmatter(
    data: dict, skill_dir: Path, rel: Path, repo_root: Path
) -> list[Finding]:
    findings: list[Finding] = []
    unknown = set(data) - SPEC_FIELDS
    if unknown:
        findings.append(
            error(
                rel,
                "SKILL020",
                "unknown frontmatter field(s): "
                + ", ".join(sorted(unknown))
                + f"; allowed: {', '.join(sorted(SPEC_FIELDS))}",
            )
        )
    missing = REQUIRED_FIELDS - set(data)
    if missing:
        findings.append(
            error(rel, "SKILL021", "missing required field(s): " + ", ".join(sorted(missing)))
        )

    name = data.get("name")
    if not isinstance(name, str) or not name:
        findings.append(error(rel, "SKILL022", "name must be a non-empty string"))
    else:
        if len(name) > 64:
            findings.append(error(rel, "SKILL023", "name must be 64 characters or fewer"))
        if not NAME_RE.match(name):
            findings.append(
                error(
                    rel,
                    "SKILL024",
                    "name must use lowercase letters, digits, and single hyphens",
                )
            )
        if name != skill_dir.name:
            findings.append(
                error(rel, "SKILL025", f"name '{name}' must match directory '{skill_dir.name}'")
            )
        if any(word in name for word in RESERVED_WORDS):
            findings.append(
                error(rel, "SKILL026", f"name must not contain reserved word(s): {RESERVED_WORDS}")
            )

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        findings.append(error(rel, "SKILL027", "description must be a non-empty string"))
    else:
        description = description.strip()
        if len(description) > MAX_DESCRIPTION:
            findings.append(
                error(
                    rel,
                    "SKILL028",
                    f"description is {len(description)} characters; maximum is {MAX_DESCRIPTION}",
                )
            )
        if XML_TAG_RE.search(description):
            findings.append(error(rel, "SKILL029", "description must not contain XML tags"))
        if not TRIGGER_RE.search(description):
            findings.append(
                error(
                    rel,
                    "SKILL030",
                    "description must state when to use the skill, e.g. 'Use when ...'",
                )
            )
        if len(description.split()) < 12:
            findings.append(
                warning(rel, "SKILL031", "description is short; include capability and trigger keywords")
            )

    license_value = data.get("license")
    if license_value is not None:
        if not isinstance(license_value, str) or not license_value.strip():
            findings.append(error(rel, "SKILL032", "license must be a non-empty string"))
        elif license_value.upper() == "MIT":
            license_file = repo_root / "LICENSE"
            if not license_file.is_file():
                findings.append(
                    warning(rel, "SKILL033", "license is MIT but the repository LICENSE file is missing")
                )

    compatibility = data.get("compatibility")
    if compatibility is not None:
        if not isinstance(compatibility, str) or not compatibility.strip():
            findings.append(
                error(rel, "SKILL034", "compatibility must be a non-empty string when provided")
            )
        elif len(compatibility) > MAX_COMPATIBILITY:
            findings.append(
                error(
                    rel,
                    "SKILL035",
                    f"compatibility is {len(compatibility)} characters; maximum is "
                    f"{MAX_COMPATIBILITY}",
                )
            )

    allowed_tools = data.get("allowed-tools")
    if allowed_tools is not None:
        if not isinstance(allowed_tools, str):
            findings.append(
                error(rel, "SKILL036", "allowed-tools must be a space-separated string")
            )
        else:
            tokens = allowed_tools.split()
            invalid = [tool for tool in tokens if tool not in ALLOWED_TOOLS]
            if invalid:
                findings.append(
                    error(
                        rel,
                        "SKILL037",
                        "unknown tool(s) in allowed-tools: "
                        + ", ".join(invalid)
                        + f"; allowed: {', '.join(sorted(ALLOWED_TOOLS))}",
                    )
                )
            if not tokens:
                findings.append(error(rel, "SKILL038", "allowed-tools must not be empty"))

    metadata = data.get("metadata")
    if metadata is None:
        findings.append(
            error(
                rel,
                "SKILL060",
                "metadata is required by the enterprise profile: "
                + ", ".join(sorted(REQUIRED_METADATA)),
            )
        )
        return findings
    if not isinstance(metadata, dict):
        findings.append(error(rel, "SKILL061", "metadata must be a mapping of strings to strings"))
        return findings
    for key, value in metadata.items():
        if not isinstance(key, str):
            findings.append(error(rel, "SKILL062", f"metadata key {key!r} must be a string"))
        if not isinstance(value, str):
            findings.append(
                error(
                    rel,
                    "SKILL063",
                    f"metadata.{key} must be a string (quote dates, versions, and numbers)",
                )
            )
    for key in sorted(DISALLOWED_METADATA & set(metadata)):
        findings.append(
            error(
                rel,
                "SKILL073",
                f"metadata.{key} is not part of this collection's standard; "
                "document-control metadata was removed deliberately",
            )
        )
    missing_meta = REQUIRED_METADATA - set(metadata)
    if missing_meta:
        findings.append(
            error(
                rel,
                "SKILL064",
                "missing enterprise metadata: " + ", ".join(sorted(missing_meta)),
            )
        )

    spec = metadata.get("spec")
    if isinstance(spec, str) and spec != SUPPORTED_SPEC_VERSION:
        findings.append(
            error(
                rel,
                "SKILL069",
                f"metadata.spec must be '{SUPPORTED_SPEC_VERSION}'",
            )
        )
    standards = metadata.get("standards")
    if isinstance(standards, str) and not standards.strip():
        findings.append(error(rel, "SKILL072", "metadata.standards must not be empty"))
    if isinstance(standards, str) and "agent skills" not in standards.lower():
        findings.append(
            warning(rel, "SKILL070", "metadata.standards should name the Agent Skills specification")
        )
    return findings


def _validate_links(skill_file: Path, rel: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = skill_file.read_text(encoding="utf-8")
    for target in relative_links(text):
        resolved = resolve_link(skill_file, target)
        if resolved is not None and not resolved.exists():
            findings.append(
                error(rel, "SKILL080", f"relative link target does not exist: {target}")
            )
    return findings


def _validate_reference_files(skill_dir: Path, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(skill_dir.rglob("*.md")):
        if path == skill_dir / "SKILL.md" or "templates" in path.parts:
            continue
        rel = path.relative_to(repo_root)
        text = path.read_text(encoding="utf-8")
        if unresolved_placeholders(text):
            findings.append(
                error(rel, "SKILL081", "reference file contains unresolved {{PLACEHOLDER}} tokens")
            )
        for target in relative_links(text):
            resolved = resolve_link(path, target)
            if resolved is not None and not resolved.exists():
                findings.append(
                    error(rel, "SKILL082", f"relative link target does not exist: {target}")
                )
        if not text.endswith("\n"):
            findings.append(error(rel, "SKILL083", "file must end with a newline"))
    return findings


# --------------------------------------------------------------------------
# Evaluation fixtures
# --------------------------------------------------------------------------


def validate_evals(repo_root: Path, skills: Sequence[Path]) -> list[Finding]:
    findings: list[Finding] = []
    evals_dir = repo_root / "evals"
    if not evals_dir.is_dir():
        return [error(Path("evals"), "EVAL001", "evals/ directory is missing")]

    for skill_dir in skills:
        eval_file = evals_dir / f"{skill_dir.name}.yaml"
        rel = eval_file.relative_to(repo_root)
        if not eval_file.is_file():
            findings.append(error(rel, "EVAL002", f"missing evaluation fixture for {skill_dir.name}"))
            continue
        if yaml is None:
            findings.append(error(rel, "EVAL003", "PyYAML is required to validate evals"))
            continue
        try:
            data = yaml.safe_load(eval_file.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            findings.append(error(rel, "EVAL004", f"invalid YAML: {exc}"))
            continue
        if not isinstance(data, dict):
            findings.append(error(rel, "EVAL005", "evaluation file must be a mapping"))
            continue
        if data.get("skill") != skill_dir.name:
            findings.append(
                error(rel, "EVAL006", f"skill must be '{skill_dir.name}'")
            )

        cases = data.get("cases")
        if not isinstance(cases, list) or len(cases) < 2:
            findings.append(error(rel, "EVAL007", "cases must contain at least two entries"))
            continue
        ids: set[str] = set()
        trigger_values: set[bool] = set()
        for index, case in enumerate(cases, start=1):
            if not isinstance(case, dict):
                findings.append(error(rel, "EVAL008", f"case {index} must be a mapping"))
                continue
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id.strip():
                findings.append(error(rel, "EVAL009", f"case {index} has no id"))
            elif case_id in ids:
                findings.append(error(rel, "EVAL010", f"duplicate case id '{case_id}'"))
            else:
                ids.add(case_id)
            if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
                findings.append(error(rel, "EVAL011", f"case {index} has no prompt"))
            should_trigger = case.get("should_trigger")
            if not isinstance(should_trigger, bool):
                findings.append(
                    error(rel, "EVAL012", f"case {case_id or index} must set should_trigger")
                )
            else:
                trigger_values.add(should_trigger)
            expected = case.get("expected")
            if not isinstance(expected, list) or not expected:
                findings.append(
                    error(rel, "EVAL013", f"case {case_id or index} must list expected behaviors")
                )
            forbidden = case.get("forbidden", [])
            if not isinstance(forbidden, list):
                findings.append(
                    error(rel, "EVAL014", f"case {case_id or index} forbidden must be a list")
                )
        if trigger_values != {True, False}:
            findings.append(
                error(rel, "EVAL015", "evals must include both trigger and non-trigger cases")
            )
    return findings


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def validate_repository(root: Path) -> list[Finding]:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return [error(Path("skills"), "REPO001", "skills/ directory is missing")]

    skills = sorted(
        path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not skills:
        return [error(Path("skills"), "REPO002", "no skills found")]

    findings: list[Finding] = []
    seen: dict[str, Path] = {}
    for skill_dir in skills:
        findings.extend(validate_skill(skill_dir, root))
        skill_file = skill_dir / "SKILL.md"
        if skill_file.is_file():
            frontmatter, _ = split_frontmatter(skill_file.read_text(encoding="utf-8"))
            if frontmatter and yaml is not None:
                try:
                    data = yaml.safe_load(frontmatter)
                except yaml.YAMLError:
                    data = None
                if isinstance(data, dict) and isinstance(data.get("name"), str):
                    name = data["name"]
                    if name in seen:
                        findings.append(
                            error(
                                skill_file.relative_to(root),
                                "SKILL090",
                                f"duplicate skill name '{name}' also declared by {seen[name]}",
                            )
                        )
                    else:
                        seen[name] = skill_file.relative_to(root)
    findings.extend(validate_evals(root, skills))
    findings.sort(key=lambda item: (str(item.path), item.code))
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--format", choices=("text", "json"), default="text", help="output format"
    )
    parser.add_argument(
        "--strict", action="store_true", help="treat warnings as errors"
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    findings = validate_repository(root)
    errors = [item for item in findings if item.level == "error"]
    warnings = [item for item in findings if item.level == "warning"]

    if args.format == "json":
        print(
            json.dumps(
                {
                    "root": str(root),
                    "errors": len(errors),
                    "warnings": len(warnings),
                    "findings": [
                        {
                            "level": item.level,
                            "path": str(item.path),
                            "code": item.code,
                            "message": item.message,
                        }
                        for item in findings
                    ],
                },
                indent=2,
            )
        )
    else:
        for item in findings:
            print(item)
        skill_count = len(list((root / "skills").glob("*/SKILL.md")))
        print(
            f"\n{skill_count} skills checked; {len(errors)} error(s), "
            f"{len(warnings)} warning(s)."
        )

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
