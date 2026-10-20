"""Tests for the repository Markdown link checker."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import check_links  # noqa: E402


class LinkCheckerTests(unittest.TestCase):
    def test_resolves_relative_links_and_ignores_external(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text(
                "# Readme\n\n[Guide](docs/guide.md)\n[Web](https://example.com)\n"
                "[Anchor](#section)\n",
                encoding="utf-8",
            )
            self.assertEqual([], check_links.check_repository(root))

    def test_reports_broken_link_with_line(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(
                "# Readme\n\n[Missing](docs/missing.md)\n", encoding="utf-8"
            )
            findings = check_links.check_repository(root)
            self.assertEqual(1, len(findings))
            self.assertEqual(3, findings[0].line)
            self.assertEqual("docs/missing.md", findings[0].target)

    def test_template_links_are_checked(self) -> None:
        # A template is copied elsewhere, so a link is broken where it is
        # written even when the generated file will exist somewhere else.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = root / "skills" / "demo" / "templates"
            template.mkdir(parents=True)
            (template / "doc.md").write_text(
                "[Generated](./does-not-exist-yet.md)\n", encoding="utf-8"
            )
            findings = check_links.check_repository(root)
            self.assertEqual(1, len(findings))
            self.assertEqual("does-not-exist-yet.md", findings[0].target.split("/")[-1])

    def test_checked_in_repository_has_no_broken_links(self) -> None:
        findings = check_links.check_repository(REPO_ROOT)
        self.assertEqual([], findings, "\n".join(str(item) for item in findings))


if __name__ == "__main__":
    unittest.main()
