"""Every Mermaid block must render as written.

A Mermaid fence is not a form. The renderer parses it before any placeholder is
substituted, so a ``{{TOKEN}}`` inside the diagram is a syntax error and the page
shows a red error box instead of the diagram. A template therefore describes the
diagram in prose, and the skill writes a real one from verified evidence.

The same rule protects the working example: `docs/architecture.md` and
`docs/threat-model.md` must carry at least one diagram, because the standard
requires an evidence-based view whenever a relationship exists.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_PARTS = {".git", ".venv", "node_modules", "__pycache__"}

MERMAID_BLOCK = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
MERMAID_FENCE = re.compile(r"^```mermaid$", re.MULTILINE)
# A template token starts with a doubled brace; the init block ends with one.
PLACEHOLDER = re.compile(r"\{\{")
DIAGRAM_TYPE = re.compile(
    r"^(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram-v2|"
    r"stateDiagram|erDiagram|journey|gantt|pie|mindmap|timeline|"
    r"quadrantChart|requirementDiagram|C4Context|gitGraph|block-beta|"
    r"sankey-beta|xychart-beta)\b"
)
INIT_BLOCK = "%%{init:"

# Documents that must demonstrate a rendered diagram when they exist.
EXAMPLE_DOCUMENTS = ("docs/architecture.md", "docs/threat-model.md")


def markdown_files() -> list[Path]:
    return [
        path
        for path in sorted(REPO_ROOT.rglob("*.md"))
        if not EXCLUDED_PARTS.intersection(path.parts)
    ]


def blocks(text: str) -> list[str]:
    return [match.group(1) for match in MERMAID_BLOCK.finditer(text)]


class MermaidTests(unittest.TestCase):
    def test_every_fence_is_closed(self) -> None:
        offenders = []
        for path in markdown_files():
            text = path.read_text(encoding="utf-8")
            opened = len(MERMAID_FENCE.findall(text))
            if opened != len(blocks(text)):
                offenders.append(f"{path.relative_to(REPO_ROOT)}: {opened} fence(s)")
        self.assertEqual(
            [],
            offenders,
            "an unclosed mermaid fence swallows the rest of the page:\n"
            + "\n".join(offenders),
        )

    def test_blocks_contain_no_template_token(self) -> None:
        offenders = []
        for path in markdown_files():
            for body in blocks(path.read_text(encoding="utf-8")):
                for line in body.splitlines():
                    if PLACEHOLDER.search(line):
                        offenders.append(
                            f"{path.relative_to(REPO_ROOT)}: {line.strip()}"
                        )
        self.assertEqual(
            [],
            offenders,
            "a Mermaid block is parsed as written; a template token in it is a "
            "syntax error, not a gap:\n" + "\n".join(offenders),
        )

    def test_blocks_declare_a_diagram_type(self) -> None:
        offenders = []
        for path in markdown_files():
            for body in blocks(path.read_text(encoding="utf-8")):
                lines = [
                    line.strip()
                    for line in body.splitlines()
                    if line.strip() and not line.strip().startswith("%%")
                ]
                if not lines or not DIAGRAM_TYPE.match(lines[0]):
                    offenders.append(
                        f"{path.relative_to(REPO_ROOT)}: {lines[0] if lines else '(empty)'}"
                    )
        self.assertEqual(
            [],
            offenders,
            "a diagram starts with a Mermaid diagram type:\n" + "\n".join(offenders),
        )

    def test_every_diagram_uses_the_init_block(self) -> None:
        offenders = []
        for path in markdown_files():
            for body in blocks(path.read_text(encoding="utf-8")):
                first = body.splitlines()[0] if body.splitlines() else ""
                if not first.startswith(INIT_BLOCK):
                    offenders.append(f"{path.relative_to(REPO_ROOT)}: {first}")
        self.assertEqual(
            [],
            offenders,
            "start every Mermaid diagram with the canonical init block:\n"
            + "\n".join(offenders),
        )

    def test_working_example_documents_render_a_diagram(self) -> None:
        offenders = []
        for relative in EXAMPLE_DOCUMENTS:
            document = REPO_ROOT / relative
            if document.is_file() and not blocks(document.read_text(encoding="utf-8")):
                offenders.append(relative)
        self.assertEqual(
            [],
            offenders,
            "a generated architecture or threat model shows its verified view:\n"
            + "\n".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
