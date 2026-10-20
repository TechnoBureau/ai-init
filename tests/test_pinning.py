"""Enforce the version-tag pinning policy.

Every remote dependency this repository runs — GitHub Actions and pre-commit
hooks — must name an exact version tag, not a branch and not a raw commit SHA.
A tag is still a mutable reference, which is why Dependabot review matters, but
it is the readable, greppable reference a reviewer can check against a release.

`tests/test_secret_scanning.py` adds the flags and baseline rules for the IBM
detect-secrets hook specifically.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PRE_COMMIT_FILES = (
    REPO_ROOT / ".pre-commit-config.yaml",
    REPO_ROOT / "skills" / "ai-init" / "files" / ".pre-commit-config.yaml",
)
WORKFLOWS = sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml"))

# v1, v1.2, v1.2.3, 0.13.1+ibm.64.dss — a tag, not a branch and not a SHA.
VERSION_TAG_RE = re.compile(r"^v?\d+\.\d+(\.\d+)?(\+[0-9A-Za-z.\-]+)?$")
COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class PinningTests(unittest.TestCase):
    def test_pre_commit_repos_use_version_tags(self) -> None:
        offenders = []
        checked = 0
        for path in PRE_COMMIT_FILES:
            config = yaml.safe_load(path.read_text(encoding="utf-8"))
            for repo in config["repos"]:
                url = repo["repo"]
                if not url.startswith(("https://", "http://")):
                    continue  # local hooks have no rev
                checked += 1
                rev = str(repo.get("rev", ""))
                if not VERSION_TAG_RE.match(rev):
                    offenders.append(f"{path.name}: {url} rev {rev!r}")
        self.assertGreater(checked, 0, "no remote pre-commit hooks found")
        self.assertEqual(
            [], offenders, "pre-commit revs must be version tags: " + "; ".join(offenders)
        )

    def test_workflow_actions_use_version_tags(self) -> None:
        offenders = []
        checked = 0
        for path in WORKFLOWS:
            text = path.read_text(encoding="utf-8")
            for match in re.finditer(r"uses:\s*([^\s#]+)", text):
                reference = match.group(1)
                if reference.startswith(("./", "docker://")):
                    continue
                checked += 1
                if "@" not in reference:
                    offenders.append(f"{path.name}: {reference} has no version")
                    continue
                ref = reference.rsplit("@", 1)[1]
                if not VERSION_TAG_RE.match(ref):
                    offenders.append(f"{path.name}: {reference}")
        self.assertGreater(checked, 0, "no remote actions found")
        self.assertEqual(
            [], offenders, "action refs must be version tags: " + "; ".join(offenders)
        )

    def test_no_raw_commit_shas_remain_in_ci_configuration(self) -> None:
        scanned = [*PRE_COMMIT_FILES, *WORKFLOWS]
        offenders = []
        for path in scanned:
            for number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                for token in re.findall(r"[0-9a-f]{40}", line):
                    if COMMIT_SHA_RE.match(token):
                        offenders.append(f"{path.relative_to(REPO_ROOT)}:{number}")
        self.assertEqual(
            [],
            offenders,
            "raw commit SHAs found; use a version tag: " + ", ".join(offenders),
        )

    def test_dependabot_covers_every_pinned_ecosystem(self) -> None:
        config = yaml.safe_load(
            (REPO_ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
        )
        ecosystems = {update["package-ecosystem"] for update in config["updates"]}
        self.assertTrue(
            {"github-actions", "pre-commit", "pip"} <= ecosystems,
            f"dependabot does not cover every pinned ecosystem: {sorted(ecosystems)}",
        )


if __name__ == "__main__":
    unittest.main()
