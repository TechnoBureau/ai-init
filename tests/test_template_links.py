"""Document templates must survive the copy into another repository.

A template is written here and copied somewhere else, so a relative link inside
it resolves against this repository's layout, where the generated document does
not exist. Every template therefore names a document in a code span and lets the
skill write the link when it writes the document. `check_links.py` checks the
same files, so a later link cannot slip back in unnoticed.

The tests below also keep the template set and the working example in step: each
template output is classified, each conditional output has a template, and a
document named in a template is linked by the generated page that mirrors it.
"""

from __future__ import annotations

import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "skills"

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
CODE_SPAN = re.compile(r"`([^`\n]+)`")
DOCUMENT_NAME = re.compile(r"^[A-Za-z0-9_./-]+\.md$")
# An index row names a document and its file: "| Security (`security.md`) | ... |".
INDEX_ROW = re.compile(r"^\|\s*[^|`]+?\s*\(`([^`]+)`\)\s*\|")
PLACEHOLDER = "{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}"
FOOTER_HEADINGS = ("### Related Docs", "## Related documents")

# Created on every run, so the skill always writes a link to them.
ALWAYS_CREATED = {
    "README.md",
    "AGENTS.md",
    "docs/README.md",
    "docs/PRD.md",
    "docs/structure.md",
    "docs/decisions.md",
    "docs/security.md",
}

# Created only when the repository supports them, so a template may name one
# but must not link it.
CONDITIONAL = {
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "LICENSE",
    ".github/CODEOWNERS",
    "docs/architecture.md",
    "docs/design.md",
    "docs/tests.md",
    "docs/rules.md",
    "docs/style.md",
    "docs/usage.md",
    "docs/governance.md",
    "docs/threat-model.md",
    "docs/tasks.md",
    "docs/memory.md",
}

# Outputs produced from a reference, not a template file.
REFERENCE_OUTPUTS = {"LICENSE"}

# Template name -> output path, relative to the generated repository root.
ROOT_OUTPUTS = {
    "README.md": "README.md",
    "CONTRIBUTING.md": "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md": "CODE_OF_CONDUCT.md",
    "SECURITY.md": "SECURITY.md",
    "CODEOWNERS": ".github/CODEOWNERS",
}


def heading(path: Path) -> str:
    """Return the first H1 of a Markdown file, or an empty string."""

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line.rstrip()
    return ""


def template_files() -> list[Path]:
    return sorted(TEMPLATES.glob("*/templates/**/*.md"))


def landing_dir(template: Path) -> str:
    """Return the directory the template's output lives in."""

    return "docs" if template.parent.as_posix().endswith("templates/docs") else "."


def output_path(template: Path) -> str:
    """Return where the template lands relative to the generated repo root."""

    if template.parent.as_posix().endswith("templates/docs"):
        return f"docs/{template.name}"
    return ROOT_OUTPUTS.get(template.name, template.name)


def declared_outputs() -> set[str]:
    """Return every output a template or a shipped reference produces."""

    declared = set(REFERENCE_OUTPUTS)
    for template in sorted(TEMPLATES.glob("*/templates/**/*")):
        if template.is_file():
            declared.add(output_path(template))
    return declared


def relative_links(text: str) -> list[tuple[int, str]]:
    """Return line number and target for every non-external Markdown link."""

    found = []
    for number, line in enumerate(text.splitlines(), start=1):
        for _label, target in LINK.findall(line):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            found.append((number, target))
    return found


def index_rows(text: str) -> list[tuple[int, str]]:
    """Return line number and target path for every index row naming a file."""

    found = []
    for number, line in enumerate(text.splitlines(), start=1):
        match = INDEX_ROW.match(line)
        if match:
            found.append((number, match.group(1)))
    return found


def named_documents(text: str) -> list[tuple[int, str]]:
    """Return line number and path for every document named in a code span."""

    found = []
    for number, line in enumerate(text.splitlines(), start=1):
        for token in CODE_SPAN.findall(line):
            if DOCUMENT_NAME.match(token):
                found.append((number, token))
    return found


def resolve(base: str, target: str) -> str:
    """Resolve a path against a directory, relative to the repository root."""

    return os.path.normpath(os.path.join(base, target)).replace("\\", "/")


class TemplateLinkTests(unittest.TestCase):
    def test_templates_contain_no_relative_links(self) -> None:
        offenders = []
        for template in template_files():
            for number, target in relative_links(template.read_text(encoding="utf-8")):
                offenders.append(f"{template.relative_to(REPO_ROOT)}:{number}: {target}")
        self.assertEqual(
            [],
            offenders,
            "a template is copied into another repository, where this link "
            "resolves to nothing; name the document in a code span and let the "
            "skill write the link:\n" + "\n".join(offenders),
        )

    def test_named_documents_are_generated(self) -> None:
        generated = {Path(path).name for path in ALWAYS_CREATED | CONDITIONAL}
        offenders = []
        for template in template_files():
            for number, token in named_documents(template.read_text(encoding="utf-8")):
                if Path(token).name not in generated:
                    offenders.append(
                        f"{template.relative_to(REPO_ROOT)}:{number}: {token}"
                    )
        self.assertEqual(
            [],
            offenders,
            "a template names a document the collection never generates:\n"
            + "\n".join(offenders),
        )

    def test_related_document_sections_use_the_placeholder(self) -> None:
        offenders = []
        for template in template_files():
            lines = template.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines):
                if line.strip() not in FOOTER_HEADINGS:
                    continue
                section = []
                for following in lines[index + 1 :]:
                    if following.startswith("#"):
                        break
                    section.append(following)
                text = "\n".join(section)
                where = template.relative_to(REPO_ROOT)
                if LINK.search(text):
                    offenders.append(f"{where}:{index + 1}: hardcoded link")
                elif PLACEHOLDER not in text:
                    offenders.append(f"{where}:{index + 1}: no {PLACEHOLDER}")
        self.assertEqual(
            [],
            offenders,
            "a related-document footer names only documents that exist:\n"
            + "\n".join(offenders),
        )

    def test_every_template_output_is_classified(self) -> None:
        known = ALWAYS_CREATED | CONDITIONAL
        unclassified = sorted(declared_outputs() - known)
        self.assertEqual(
            [],
            unclassified,
            "classify each new template output as always created or conditional",
        )

    def test_conditional_outputs_correspond_to_a_template(self) -> None:
        stale = sorted(CONDITIONAL - declared_outputs())
        self.assertEqual(
            [], stale, f"conditional outputs with no template: {', '.join(stale)}"
        )

    def test_index_rows_link_the_generated_document(self) -> None:
        offenders = []
        for template in template_files():
            output = output_path(template)
            if not output.startswith("docs/"):
                continue
            document = REPO_ROOT / output
            if not document.is_file():
                continue
            linked = {
                resolve("docs", target)
                for _number, target in relative_links(
                    document.read_text(encoding="utf-8")
                )
            }
            for number, token in index_rows(template.read_text(encoding="utf-8")):
                target = resolve(landing_dir(template), token)
                if not (REPO_ROOT / target).exists():
                    continue
                if target not in linked:
                    offenders.append(
                        f"{template.relative_to(REPO_ROOT)}:{number}: {token} is "
                        f"not linked from {output}"
                    )
        self.assertEqual(
            [],
            offenders,
            "an index row names a file, so the generated index must link it:\n"
            + "\n".join(offenders),
        )

    def test_working_example_links_stay_inside_the_repository(self) -> None:
        offenders = []
        for document in sorted((REPO_ROOT / "docs").glob("*.md")):
            for number, target in relative_links(document.read_text(encoding="utf-8")):
                if resolve("docs", target).startswith(".."):
                    offenders.append(
                        f"{document.relative_to(REPO_ROOT)}:{number}: {target}"
                    )
        self.assertEqual(
            [],
            offenders,
            "a generated document links only inside the repository it describes:\n"
            + "\n".join(offenders),
        )

    def test_titles_state_the_document_type(self) -> None:
        documents = [
            *template_files(),
            *sorted((REPO_ROOT / "docs").glob("*.md")),
            REPO_ROOT / "README.md",
        ]
        offenders = []
        for path in documents:
            title = heading(path)
            if "{{PROJECT_NAME}}" in title:
                offenders.append(f"{path.relative_to(REPO_ROOT)}: {title}")
            elif " — " in title or " - " in title:
                offenders.append(f"{path.relative_to(REPO_ROOT)}: {title}")
        self.assertEqual(
            [],
            offenders,
            "a title names the document type, not the project:\n" + "\n".join(offenders),
        )

    def test_working_example_mirrors_every_title(self) -> None:
        offenders = []
        for template in template_files():
            output = output_path(template)
            document = REPO_ROOT / output
            if not document.is_file():
                continue
            if heading(template) != heading(document):
                offenders.append(
                    f"{output}: {heading(document)!r} != {heading(template)!r}"
                )
        self.assertEqual(
            [],
            offenders,
            "generated titles must match their template:\n" + "\n".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
