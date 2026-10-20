"""Every link in a document template must resolve in a generated repository.

`check_links.py` skips templates because they contain placeholders, and
`test_working_example.py` only proves that each template has an output. Neither
reads a template link the way a reader of the generated repository would, so a
template could point at a document that is only sometimes generated, or at a
file in the skill tree that is never copied into the target.

A generated repository always contains `README.md`, the two agent symlinks, and
the default `docs/` set. Everything else is conditional, so a template may name
it in prose or behind `{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}`, never
as a live link.
"""

from __future__ import annotations

import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "skills"

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
PLACEHOLDER = "{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}"
FOOTER_HEADINGS = ("### Related Docs", "## Related documents")

# Created on every run, so a template may link them directly.
ALWAYS_CREATED = {
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "docs/README.md",
    "docs/PRD.md",
    "docs/structure.md",
    "docs/decisions.md",
    "docs/security.md",
}

# Created only when the repository supports them. A link to one of these, or to
# any path outside this set, is broken in the repositories that skip it.
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


def resolve(template: Path, target: str) -> str:
    """Resolve a template link against the generated repository, not the tree."""

    return os.path.normpath(os.path.join(landing_dir(template), target)).replace(
        "\\", "/"
    )


class TemplateLinkTests(unittest.TestCase):
    def test_templates_link_only_to_outputs_that_always_exist(self) -> None:
        offenders = []
        for template in template_files():
            for number, target in relative_links(template.read_text(encoding="utf-8")):
                resolved = resolve(template, target)
                if resolved not in ALWAYS_CREATED:
                    offenders.append(
                        f"{template.relative_to(REPO_ROOT)}:{number}: {target}"
                        f" -> {resolved}"
                    )
        self.assertEqual(
            [],
            offenders,
            "a template link must resolve in every generated repository; "
            "name a conditional document in prose or behind "
            f"{PLACEHOLDER}:\n" + "\n".join(offenders),
        )

    def test_templates_do_not_link_into_the_skill_tree(self) -> None:
        offenders = []
        for template in template_files():
            for number, target in relative_links(template.read_text(encoding="utf-8")):
                if "/skills/" in f"/{resolve(template, target)}" or "references/" in target:
                    offenders.append(
                        f"{template.relative_to(REPO_ROOT)}:{number}: {target}"
                    )
        self.assertEqual(
            [],
            offenders,
            "skill references are not copied into a target repository:\n"
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

    def test_working_example_links_stay_inside_the_repository(self) -> None:
        offenders = []
        for template in template_files():
            output = output_path(template)
            if not output.startswith("docs/"):
                continue
            document = REPO_ROOT / output
            if not document.is_file():
                continue
            for number, target in relative_links(document.read_text(encoding="utf-8")):
                resolved = os.path.normpath(
                    os.path.join("docs", target)
                ).replace("\\", "/")
                if resolved.startswith(".."):
                    offenders.append(f"{output}:{number}: {target}")
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

    def test_working_example_keeps_every_literal_template_link(self) -> None:
        offenders = []
        for template in template_files():
            output = output_path(template)
            if not output.startswith("docs/"):
                continue
            document = REPO_ROOT / output
            if not document.is_file():
                continue
            document_links = {
                resolve(template, target)
                for _number, target in relative_links(
                    document.read_text(encoding="utf-8")
                )
            }
            for number, target in relative_links(template.read_text(encoding="utf-8")):
                resolved = resolve(template, target)
                if resolved not in document_links:
                    offenders.append(
                        f"{template.relative_to(REPO_ROOT)}:{number}: {target} is"
                        f" missing from {output}"
                    )
        self.assertEqual(
            [],
            offenders,
            "the working example must exercise every literal template link, "
            "otherwise the template drifts:\n" + "\n".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
