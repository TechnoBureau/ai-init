#!/usr/bin/env python3
"""Check every local Markdown link in this repository.

Templates under ``skills/*/templates/`` are excluded because their links are
resolved after ``ai-init`` copies them into a target repository. All other
Markdown must link only to files that exist so generated documentation never
ships a broken index.

Usage:
    python scripts/check_links.py
    python scripts/check_links.py --root . --format json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Sequence
from urllib.parse import unquote

LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)"
)
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "ftp://")
EXCLUDED_PARTS = {".git", ".venv", "node_modules", "__pycache__"}
EXCLUDED_DIR_NAMES = {"templates"}


@dataclass(frozen=True)
class BrokenLink:
    path: Path
    line: int
    target: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: broken local link: {self.target}"


def markdown_files(root: Path) -> Iterator[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if any(part in EXCLUDED_DIR_NAMES for part in path.relative_to(root).parts):
            continue
        yield path


def iter_targets(text: str) -> Iterator[tuple[int, str]]:
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()
        yield text.count("\n", 0, match.start()) + 1, target
    for match in REF_DEF_RE.finditer(text):
        yield text.count("\n", 0, match.start()) + 1, match.group(1).strip()


def check_file(path: Path, root: Path) -> list[BrokenLink]:
    broken: list[BrokenLink] = []
    text = path.read_text(encoding="utf-8")
    for line, target in iter_targets(text):
        if not target or target.startswith(EXTERNAL_PREFIXES) or target.startswith("#"):
            continue
        if target.startswith("//") or "{{" in target:
            continue
        cleaned = target.split("#", 1)[0].split("?", 1)[0]
        if not cleaned:
            continue
        candidate = (path.parent / unquote(cleaned)).resolve()
        if not candidate.exists():
            try:
                display = path.relative_to(root)
            except ValueError:
                display = path
            broken.append(BrokenLink(display, line, target))
    return broken


def check_repository(root: Path) -> list[BrokenLink]:
    findings: list[BrokenLink] = []
    for path in markdown_files(root):
        findings.extend(check_file(path, root))
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: parent of scripts/)",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    findings = check_repository(root)

    if args.format == "json":
        print(
            json.dumps(
                {
                    "root": str(root),
                    "broken": len(findings),
                    "findings": [
                        {"path": str(item.path), "line": item.line, "target": item.target}
                        for item in findings
                    ],
                },
                indent=2,
            )
        )
    else:
        for item in findings:
            print(item)
        print(f"{len(findings)} broken local link(s) found.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
