"""Check that this repository's `docs/` is a real output of its own templates.

The collection promises that generated documentation comes from
`skills/*/templates/`. This test keeps that promise honest: every template must
have a generated counterpart in this repository, and generated documents must
not contain placeholders or become orphaned from the documentation index.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
TEMPLATES = REPO_ROOT / "skills"
PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")
CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def unresolved_placeholders(text: str) -> list[str]:
    """Return placeholders outside code spans and fenced blocks."""

    cleaned = CODE_BLOCK_RE.sub("", text)
    cleaned = INLINE_CODE_RE.sub("", cleaned)
    return PLACEHOLDER_RE.findall(cleaned)


# Templates whose output is intentionally absent from this repository, with the
# reason. Add an entry only with a documented justification.
EXEMPT_TEMPLATES = {
    "design.md": "This repository has no rendered UI, so docs/design.md is not applicable.",
    "tasks.md": "No maintained task board exists in this repository.",
    "memory.md": "No append-only project log is maintained.",
}

# Template path -> output path, relative to the repository root.
ROOT_OUTPUTS = {
    "README.md": "README.md",
    "CONTRIBUTING.md": "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md": "CODE_OF_CONDUCT.md",
    "SECURITY.md": "SECURITY.md",
    "CODEOWNERS": ".github/CODEOWNERS",
}


def template_dirs() -> list[Path]:
    """Return every ``templates`` directory in the skills tree."""

    return sorted(path for path in TEMPLATES.glob("*/templates") if path.is_dir())


def doc_templates() -> dict[str, Path]:
    """Map output name to template path for every ``templates/docs`` file."""

    found: dict[str, Path] = {}
    for directory in template_dirs():
        docs_dir = directory / "docs"
        if not docs_dir.is_dir():
            continue
        for template in sorted(docs_dir.iterdir()):
            if template.is_file():
                found[template.name] = template
    return found


class WorkingExampleTests(unittest.TestCase):
    def test_templates_exist(self) -> None:
        directories = template_dirs()
        self.assertTrue(directories, "no templates directory found under skills/")

    def test_exemptions_refer_to_real_templates(self) -> None:
        stale = sorted(set(EXEMPT_TEMPLATES) - set(doc_templates()))
        self.assertEqual([], stale, f"stale exemptions: {', '.join(stale)}")

    def test_document_templates_are_mirrored(self) -> None:
        generated = []
        missing = []
        for name, template in doc_templates().items():
            if name in EXEMPT_TEMPLATES:
                continue
            if (DOCS / name).is_file():
                generated.append(name)
            else:
                missing.append(f"{template.relative_to(REPO_ROOT)} has no docs/{name}")
        self.assertTrue(generated, "no document templates are exercised by docs/")
        self.assertEqual([], missing, "\n".join(missing))

    def test_root_templates_are_mirrored(self) -> None:
        missing = []
        exercised = 0
        for directory in template_dirs():
            root_dir = directory / "root"
            if not root_dir.is_dir():
                continue
            for template in sorted(root_dir.iterdir()):
                if not template.is_file():
                    continue
                output = ROOT_OUTPUTS.get(template.name)
                if output is None:
                    missing.append(
                        f"{template.relative_to(REPO_ROOT)} has no documented output path"
                    )
                elif not (REPO_ROOT / output).is_file():
                    missing.append(f"{template.relative_to(REPO_ROOT)} has no {output}")
                else:
                    exercised += 1
        self.assertGreater(exercised, 0, "no root templates are exercised")
        self.assertEqual([], missing, "\n".join(missing))

    def test_generated_documents_have_no_placeholders(self) -> None:
        offenders = []
        for document in sorted(DOCS.glob("*.md")):
            text = document.read_text(encoding="utf-8")
            for token in unresolved_placeholders(text):
                offenders.append(f"{document.name}: {token}")
        self.assertEqual([], offenders, "\n".join(offenders))

    def test_documentation_index_lists_every_document(self) -> None:
        index = (DOCS / "README.md").read_text(encoding="utf-8")
        unlisted = [
            document.name
            for document in sorted(DOCS.glob("*.md"))
            if document.name != "README.md" and f"./{document.name}" not in index
        ]
        message = "documents missing from docs/README.md: " + ", ".join(unlisted)
        self.assertEqual([], unlisted, message)

    def test_templates_declare_no_unresolved_includes(self) -> None:
        # Templates may contain placeholders; they must not reference files that
        # would not exist after generation.
        for template in doc_templates().values():
            text = template.read_text(encoding="utf-8")
            self.assertNotIn("@@include", text, f"unsupported include in {template}")


if __name__ == "__main__":
    unittest.main()
