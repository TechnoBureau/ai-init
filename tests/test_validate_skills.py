"""Regression tests for the Agent Skills validator.

The first regression test is the reason this project needs a validator: a
Markdown formatter converted YAML frontmatter into a horizontal rule and a
heading, which made every published skill unloadable.
"""

from __future__ import annotations

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import validate_skills as validator  # noqa: E402


VALID_FRONTMATTER = """---
name: sample-skill
description: >-
  Demonstrates a test skill for the validator. Use when checking that a
  conforming skill passes every structural and metadata rule.
license: MIT
compatibility: Requires Python 3.11 or later.
metadata:
  spec: "1.0"
  standards: "Agent Skills 1.0; RFC 2119"
  risk: "low"
allowed-tools: "Read Grep"
---
"""

VALID_EVAL = """skill: sample-skill
cases:
  - id: positive-case
    prompt: Initialize the repository documentation.
    should_trigger: true
    expected:
      - "Creates documentation only from repository evidence."
  - id: negative-case
    prompt: Explain quantum chromodynamics.
    should_trigger: false
    expected:
      - "Does not activate the repository documentation workflow."
"""


class SkillFixture:
    """Create a temporary repository containing one skill."""

    def __init__(self, body: str = "# Sample Skill\n\nSee [notes](references/notes.md).\n") -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "LICENSE").write_text("MIT License\n", encoding="utf-8")
        self.skill_dir = self.root / "skills" / "sample-skill"
        (self.skill_dir / "references").mkdir(parents=True)
        (self.skill_dir / "references" / "notes.md").write_text(
            "# Notes\n\nReference material.\n", encoding="utf-8"
        )
        (self.skill_dir / "SKILL.md").write_text(
            VALID_FRONTMATTER + "\n" + body, encoding="utf-8"
        )
        (self.root / "evals").mkdir()
        (self.root / "evals" / "sample-skill.yaml").write_text(
            VALID_EVAL, encoding="utf-8"
        )

    def validate(self):
        return validator.validate_skill(self.skill_dir, self.root)

    def close(self) -> None:
        self._tmp.cleanup()


class SkillValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = SkillFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def codes(self, findings) -> set[str]:
        return {finding.code for finding in findings}

    def test_valid_skill_passes(self) -> None:
        self.assertEqual([], self.fixture.validate())

    def test_missing_frontmatter_is_rejected(self) -> None:
        (self.fixture.skill_dir / "SKILL.md").write_text(
            "# Sample Skill\n\nInstructions only.\n", encoding="utf-8"
        )
        findings = self.fixture.validate()
        self.assertIn("SKILL010", self.codes(findings))

    def test_reformatted_frontmatter_regression_is_rejected(self) -> None:
        # Failure mode: a formatter rendered '---' as a rule and joined
        # name/description into a heading.
        (self.fixture.skill_dir / "SKILL.md").write_text(
            textwrap.dedent(
                """\
                ______________________________________________________________________

                ## name: sample-skill description: > Demonstrates a test skill.

                # Sample Skill

                Instructions only.
                """
            ),
            encoding="utf-8",
        )
        codes = self.codes(self.fixture.validate())
        self.assertIn("SKILL010", codes)
        self.assertIn("SKILL011", codes)

    def test_name_must_match_directory(self) -> None:
        content = (self.fixture.skill_dir / "SKILL.md").read_text(encoding="utf-8")
        (self.fixture.skill_dir / "SKILL.md").write_text(
            content.replace("name: sample-skill", "name: different-skill", 1),
            encoding="utf-8",
        )
        self.assertIn("SKILL025", self.codes(self.fixture.validate()))

    def test_description_requires_trigger(self) -> None:
        content = (self.fixture.skill_dir / "SKILL.md").read_text(encoding="utf-8")
        content = content.replace(
            "  Demonstrates a test skill for the validator. Use when checking that a\n"
            "  conforming skill passes every structural and metadata rule.",
            "  Demonstrates a test skill for the validator.",
        )
        (self.fixture.skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
        self.assertIn("SKILL030", self.codes(self.fixture.validate()))

    def test_unknown_frontmatter_field_is_rejected(self) -> None:
        content = (self.fixture.skill_dir / "SKILL.md").read_text(encoding="utf-8")
        (self.fixture.skill_dir / "SKILL.md").write_text(
            content.replace("allowed-tools:", "version: \"9.9.9\"\nallowed-tools:", 1),
            encoding="utf-8",
        )
        self.assertIn("SKILL020", self.codes(self.fixture.validate()))

    def test_document_control_metadata_is_not_required(self) -> None:
        # owner/reviewed/classification were deliberately removed; a skill
        # without them must still validate.
        codes = self.codes(self.fixture.validate())
        for code in ("SKILL060", "SKILL064", "SKILL065", "SKILL066", "SKILL067"):
            self.assertNotIn(code, codes)

    def test_document_control_metadata_is_not_accepted(self) -> None:
        content = (self.fixture.skill_dir / "SKILL.md").read_text(encoding="utf-8")
        (self.fixture.skill_dir / "SKILL.md").write_text(
            content.replace(
                '  standards:', '  reviewed: "2026-10-20"\n  standards:', 1
            ),
            encoding="utf-8",
        )
        self.assertIn("SKILL073", self.codes(self.fixture.validate()))

    def test_broken_relative_link_is_rejected(self) -> None:
        (self.fixture.skill_dir / "SKILL.md").write_text(
            VALID_FRONTMATTER + "\n# Sample Skill\n\nSee [missing](references/missing.md).\n",
            encoding="utf-8",
        )
        self.assertIn("SKILL080", self.codes(self.fixture.validate()))

    def test_body_placeholder_is_rejected(self) -> None:
        (self.fixture.skill_dir / "SKILL.md").write_text(
            VALID_FRONTMATTER + "\n# Sample Skill\n\n{{DO_THE_THING}}\n",
            encoding="utf-8",
        )
        self.assertIn("SKILL043", self.codes(self.fixture.validate()))

    def test_eval_fixture_requires_both_trigger_states(self) -> None:
        (self.fixture.root / "evals" / "sample-skill.yaml").write_text(
            textwrap.dedent(
                """\
                skill: sample-skill
                cases:
                  - id: first-positive
                    prompt: Initialize documentation.
                    should_trigger: true
                    expected:
                      - "Creates documentation."
                  - id: second-positive
                    prompt: Refresh repository documentation.
                    should_trigger: true
                    expected:
                      - "Refreshes documentation."
                """
            ),
            encoding="utf-8",
        )
        findings = validator.validate_evals(
            self.fixture.root, [self.fixture.skill_dir]
        )
        self.assertIn("EVAL015", self.codes(findings))


class RepositoryTests(unittest.TestCase):
    def test_checked_in_skills_are_valid(self) -> None:
        findings = validator.validate_repository(REPO_ROOT)
        errors = [finding for finding in findings if finding.level == "error"]
        self.assertEqual([], errors, "\n".join(str(item) for item in errors))

    def test_repository_requires_eval_fixtures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "skills" / "sample-skill"
            skill_dir.mkdir(parents=True)
            (root / "LICENSE").write_text("MIT License\n", encoding="utf-8")
            (skill_dir / "SKILL.md").write_text(
                VALID_FRONTMATTER + "\n# Sample Skill\n", encoding="utf-8"
            )
            findings = validator.validate_evals(root, [skill_dir])
            self.assertIn("EVAL001", {finding.code for finding in findings})


if __name__ == "__main__":
    unittest.main()
