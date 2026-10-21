"""Keep generated documentation on the current state of the repository.

Documents describe what exists now and point at the file that owns a value.
They must not freeze a snapshot of one run, must not duplicate a pin that the
configuration already owns, and must not carry bookkeeping metadata beside the
content, because all three go stale without any code change.
"""

from __future__ import annotations

import fnmatch
import re
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
README = REPO_ROOT / "README.md"

# Decision records may quote the value they chose; current-state documents may
# not, because the configuration is the source of truth.
HISTORY = {"decisions.md"}

# A run record belongs to CI, not to a document.
FROZEN_STATE_PATTERNS = (
    re.compile(r"last verified", re.IGNORECASE),
    re.compile(r"local run[,:]?", re.IGNORECASE),
    re.compile(r"environment:\s*python\s+\d+\.\d+\.\d+", re.IGNORECASE),
    re.compile(r"\b\d+\s+tests?\b", re.IGNORECASE),
    re.compile(
        r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+test\s+"
        r"(?:modules?|files?|suites?)\b",
        re.IGNORECASE,
    ),
    re.compile(r"tests?,?\s+ok\b", re.IGNORECASE),
)

# Bookkeeping columns and decision fields record a document's own state, not
# the subject it documents. Nothing consumes them, so they drift.
FORBIDDEN_COLUMNS = frozenset(
    name.lower()
    for name in (
        "Status",
        "Date",
        "Owner",
        "Owner / date",
        "Owner / target",
        "Evidence",
        "Evidence / gap",
        "Evidence / owner",
        "Evidence / verification",
        "Evidence / target / gap",
        "Evidence-based description",
        "Active entry point / evidence",
        "Claim type",
        "Verification",
        "Verification source",
        "Verification criteria",
        "Verification / owner",
        "Baseline",
        "Target",
        "Target / measure",
        "Measure",
        "Alternatives rejected",
        "Supersedes / superseded by",
        "Review date",
        "Expiry",
        "Expiry / review date",
        "Required evidence",
        "Configuration evidence",
        "Scanner/version",
        "Impact / evidence",
        "Residual risk / evidence",
    )
)

# The only fields a decision record may carry.
DECISION_FIELDS = frozenset({"context", "decision", "consequences", "reason"})

DECISION_RECORDS = (
    DOCS / "decisions.md",
    REPO_ROOT / "skills" / "ai-init" / "templates" / "docs" / "decisions.md",
)

TABLE_SEPARATOR = re.compile(r"^\|(?:\s*:?-{3,}:?\s*\|)+$")

# Paths whose basenames must appear in the structure document.
STARTERS = REPO_ROOT / "skills" / "ai-init" / "files"


def exact_pins() -> list[str]:
    """Return the exact version strings the configuration owns."""

    pins: list[str] = []

    requirements = REPO_ROOT / "requirements-dev.txt"
    for line in requirements.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s*([A-Za-z0-9_.\-]+)==(\S+)\s*$", line)
        if match:
            pins.append(match.group(2))

    for path in (
        REPO_ROOT / ".pre-commit-config.yaml",
        REPO_ROOT / "skills" / "ai-init" / "files" / ".pre-commit-config.yaml",
    ):
        config = yaml.safe_load(path.read_text(encoding="utf-8"))
        for repo in config["repos"]:
            rev = repo.get("rev")
            if rev:
                pins.append(str(rev))

    return sorted(set(pins))


def current_state_documents() -> list[Path]:
    documents = [README]
    documents.extend(
        document
        for document in sorted(DOCS.glob("*.md"))
        if document.name not in HISTORY
    )
    return documents


class DocumentationStateTests(unittest.TestCase):
    def test_documents_do_not_freeze_a_run(self) -> None:
        offenders = []
        for document in current_state_documents():
            text = document.read_text(encoding="utf-8")
            for pattern in FROZEN_STATE_PATTERNS:
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    offenders.append(
                        f"{document.relative_to(REPO_ROOT)}:{line}: {match.group(0)}"
                    )
        self.assertEqual([], offenders, "\n".join(offenders))

    def test_documents_do_not_duplicate_configuration_pins(self) -> None:
        pins = exact_pins()
        self.assertGreater(len(pins), 0, "no pins found in configuration")
        offenders = []
        for document in current_state_documents():
            text = document.read_text(encoding="utf-8")
            for pin in pins:
                if pin in text:
                    offenders.append(f"{document.relative_to(REPO_ROOT)}: {pin}")
        self.assertEqual(
            [],
            offenders,
            "pins belong in the configuration, not in documents: "
            + ", ".join(offenders),
        )

    def test_structure_document_lists_every_reference_and_starter(self) -> None:
        structure = (DOCS / "structure.md").read_text(encoding="utf-8")
        referenced = sorted((REPO_ROOT / "skills").glob("*/references/**/*.md"))
        self.assertTrue(referenced, "no reference documents found")
        starters = sorted(path for path in STARTERS.iterdir() if path.is_file())
        self.assertTrue(starters, "no starter files found")

        # Accept a tree entry that names the file, optionally under its own
        # directory, and a grouped entry such as `style/style-*.md` for the
        # documents it actually covers.
        tokens = re.findall(r"[A-Za-z0-9_.*/-]+\.md", structure)

        def listed(name: str, relative: str) -> bool:
            for token in tokens:
                segments = token.split("/")
                pattern = segments[-1] if len(segments) == 1 else "/".join(segments[-2:])
                if fnmatch.fnmatch(name if len(segments) == 1 else relative, pattern):
                    return True
            return False

        missing = []
        for path in referenced:
            relative = f"{path.parent.name}/{path.name}"
            if not listed(path.name, relative):
                missing.append(str(path.relative_to(REPO_ROOT)))
        for path in starters:
            if path.name not in structure:
                missing.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual(
            [],
            missing,
            "structure.md does not list: " + ", ".join(missing),
        )


    def test_security_profile_covers_scoped_hardening_domains(self) -> None:
        template = (
            REPO_ROOT
            / "skills"
            / "security"
            / "templates"
            / "docs"
            / "security.md"
        ).read_text(encoding="utf-8")
        generated = (DOCS / "security.md").read_text(encoding="utf-8")
        baseline = (
            REPO_ROOT
            / "skills"
            / "security"
            / "references"
            / "security-baseline.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## Cryptographic Inventory and Migration",
            "## Network Transport and TLS",
            "## Container Image and Runtime Hardening",
            "## Kubernetes and Helm Hardening",
            "## Shell Script Security and Logging",
            "## Spec-Driven Security Requirements",
        )
        for heading in headings:
            with self.subTest(heading=heading):
                self.assertIn(heading, template)
                self.assertIn(heading, generated)
        self.assertIn("TLS_CHACHA20_POLY1305_SHA256", template)
        self.assertIn("Do not require a single public registry", baseline)
        self.assertIn("Avoid floating `latest` tags", baseline)

    def generated_documents(self) -> list[Path]:
        documents = [README, *sorted(DOCS.glob("*.md"))]
        documents.extend(sorted((REPO_ROOT / "skills").glob("*/templates/**/*.md")))
        return [document for document in documents if document.is_file()]

    def test_documents_carry_no_bookkeeping_columns(self) -> None:
        offenders = []
        for document in self.generated_documents():
            lines = document.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines[:-1]):
                if not line.lstrip().startswith("|"):
                    continue
                if not TABLE_SEPARATOR.match(lines[index + 1].strip()):
                    continue
                for cell in re.split(r"(?<!\\)\|", line.strip())[1:-1]:
                    name = cell.strip().lower()
                    if name in FORBIDDEN_COLUMNS:
                        offenders.append(
                            f"{document.relative_to(REPO_ROOT)}:{index + 1}: {cell.strip()}"
                        )
        self.assertEqual(
            [],
            offenders,
            "bookkeeping columns belong in Git or the owning config: "
            + ", ".join(offenders),
        )

    def test_decision_records_carry_only_narrative_fields(self) -> None:
        offenders = []
        for document in DECISION_RECORDS:
            for index, line in enumerate(document.read_text(encoding="utf-8").splitlines()):
                match = re.match(r"^- \*\*(.+?):\*\*", line.strip())
                if match and match.group(1).lower() not in DECISION_FIELDS:
                    offenders.append(
                        f"{document.relative_to(REPO_ROOT)}:{index + 1}: {match.group(1)}"
                    )
        self.assertEqual(
            [],
            offenders,
            "a decision record is context, decision, consequences, and reason: "
            + ", ".join(offenders),
        )

if __name__ == "__main__":
    unittest.main()
