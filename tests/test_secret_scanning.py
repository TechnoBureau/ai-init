"""Guard the IBM detect-secrets policy used by this repository and the skill.

The baseline is machine configuration, so drift is silent: a regenerated file
can quietly re-enable keyword scanning or drop an exclusion. These tests pin
the policy, not the findings.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
BASELINE = REPO_ROOT / ".secrets.baseline"
STARTER = REPO_ROOT / "skills" / "ai-init" / "files" / ".secrets.baseline"
PRE_COMMIT = REPO_ROOT / ".pre-commit-config.yaml"
STARTER_PRE_COMMIT = REPO_ROOT / "skills" / "ai-init" / "files" / ".pre-commit-config.yaml"
DETECT_SECRETS_REPO = "https://github.com/IBM/detect-secrets"
# Exact version tag of the IBM fork; the baseline version must match it.
DETECT_SECRETS_REV = "0.13.1+ibm.64.dss"
VERSION_TAG_RE = re.compile(r"^\d+\.\d+\.\d+(\+[0-9A-Za-z.\-]+)?$")

# `detect-secrets scan --update` appends its own path to the exclusion regex.
SELF_EXCLUDE = "|^.secrets.baseline$"

# Generated or dependency files the policy promises to skip.
EXCLUDED_SAMPLES = (
    ".secrets.baseline",
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "bun.lockb",
    "go.mod",
    "go.sum",
    "Cargo.lock",
    "poetry.lock",
    "Pipfile.lock",
    "Gemfile.lock",
    "composer.lock",
    "requirements-dev.txt",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "node_modules/react/index.js",
    "vendor/github.com/acme/lib.go",
    "third_party/lib/x.c",
    "dist/app.js",
    "build/out.o",
    ".venv/lib/python3.11/site-packages/x.py",
    "src/app.min.js",
    "src/app.min.css",
    "src/app.js.map",
    "coverage.sum",
    "schema.snap",
    "design/architecture.drawio",
)

# Files a secret can hide in; the policy must still scan them.
INCLUDED_SAMPLES = (
    "README.md",
    "docs/security.md",
    "src/main.c",
    "src/main.cpp",
    "main.go",
    "scripts/release.sh",
    "tests/test_app.py",
    "tests/fixtures/sample.env",
    ".github/workflows/validate.yml",
    "package.json",
    "pyproject.toml",
)


def load_baseline(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def plugin_names(baseline: dict) -> set[str]:
    return {plugin["name"] for plugin in baseline["plugins_used"]}


def normalized_exclude(baseline: dict) -> str:
    """Drop the self-exclusion the tool appends when it rewrites a baseline."""

    pattern = baseline["exclude"]["files"] or ""
    return pattern.removesuffix(SELF_EXCLUDE)


class SecretScanningTests(unittest.TestCase):
    def test_baseline_has_no_findings_and_no_keyword_scan(self) -> None:
        for path in (BASELINE, STARTER):
            baseline = load_baseline(path)
            self.assertEqual({}, baseline["results"], f"{path.name} records findings")
            names = plugin_names(baseline)
            self.assertNotIn("KeywordDetector", names, f"{path.name} enables keyword scanning")
            # --use-all-plugins is expected, so the baseline records the full set.
            for required in (
                "AWSKeyDetector",
                "AzureStorageKeyDetector",
                "BoxDetector",
                "GitHubTokenDetector",
                "GheDetector",
                "IbmCloudIamDetector",
                "IbmCosHmacDetector",
                "NpmDetector",
                "PrivateKeyDetector",
                "SquareOAuthDetector",
            ):
                self.assertIn(required, names, f"{path.name} dropped {required}")
            self.assertGreaterEqual(len(names), 20, f"{path.name} lost plugins")
            self.assertEqual(
                DETECT_SECRETS_REV,
                baseline["version"],
                f"{path.name} version must match the pinned hook",
            )

    def test_baseline_version_matches_the_hook_rev(self) -> None:
        version = load_baseline(BASELINE)["version"]
        for path in (PRE_COMMIT, STARTER_PRE_COMMIT):
            config = yaml.safe_load(path.read_text(encoding="utf-8"))
            repos = {repo["repo"]: repo for repo in config["repos"]}
            self.assertEqual(
                version,
                str(repos[DETECT_SECRETS_REPO]["rev"]),
                f"{path.name} rev and baseline version diverged",
            )

    def test_repository_baseline_keeps_the_starter_policy(self) -> None:
        root = load_baseline(BASELINE)
        starter = load_baseline(STARTER)
        self.assertEqual(normalized_exclude(starter), normalized_exclude(root))
        by_name = lambda plugins: sorted(plugins, key=lambda plugin: plugin["name"])
        self.assertEqual(by_name(starter["plugins_used"]), by_name(root["plugins_used"]))

    def test_exclusions_cover_generated_files_and_keep_source(self) -> None:
        pattern = load_baseline(BASELINE)["exclude"]["files"]
        regex = re.compile(pattern, re.IGNORECASE)
        missed = [path for path in EXCLUDED_SAMPLES if not regex.search(path)]
        caught = [path for path in INCLUDED_SAMPLES if regex.search(path)]
        self.assertEqual([], missed, "not excluded: " + ", ".join(missed))
        self.assertEqual([], caught, "wrongly excluded: " + ", ".join(caught))

    def test_pre_commit_wires_the_pinned_detect_secrets_hook(self) -> None:
        for path in (PRE_COMMIT, STARTER_PRE_COMMIT):
            config = yaml.safe_load(path.read_text(encoding="utf-8"))
            repos = {repo["repo"]: repo for repo in config["repos"]}
            self.assertIn(DETECT_SECRETS_REPO, repos, f"{path.name} lacks detect-secrets")
            repo = repos[DETECT_SECRETS_REPO]
            self.assertRegex(
                str(repo["rev"]),
                VERSION_TAG_RE,
                f"{path.name} must pin the scanner by exact version tag",
            )
            hooks = {hook["id"]: hook for hook in repo["hooks"]}
            self.assertIn("detect-secrets", hooks, f"{path.name} lacks the hook")
            hook = hooks["detect-secrets"]
            args = hook.get("args", [])
            for expected in (
                "--baseline",
                ".secrets.baseline",
                "--use-all-plugins",
                "--no-keyword-scan",
                "--fail-on-unaudited",
            ):
                self.assertIn(expected, args, f"{path.name} is missing {expected}")
            deps = hook.get("additional_dependencies", [])
            self.assertIn("boxsdk<4", deps, f"{path.name} is missing boxsdk<4")
            self.assertIn("chardet<7", deps, f"{path.name} is missing chardet<7")

    def test_hook_exclude_matches_the_baseline_policy(self) -> None:
        policy = normalized_exclude(load_baseline(BASELINE))
        for path in (PRE_COMMIT, STARTER_PRE_COMMIT):
            config = yaml.safe_load(path.read_text(encoding="utf-8"))
            repos = {repo["repo"]: repo for repo in config["repos"]}
            hooks = {hook["id"]: hook for hook in repos[DETECT_SECRETS_REPO]["hooks"]}
            self.assertEqual(
                policy,
                hooks["detect-secrets"]["exclude"],
                f"{path.name} exclude drifted from .secrets.baseline",
            )

    def test_hook_exclude_skips_generated_files_only(self) -> None:
        config = yaml.safe_load(PRE_COMMIT.read_text(encoding="utf-8"))
        repos = {repo["repo"]: repo for repo in config["repos"]}
        hooks = {hook["id"]: hook for hook in repos[DETECT_SECRETS_REPO]["hooks"]}
        regex = re.compile(hooks["detect-secrets"]["exclude"])
        missed = [path for path in EXCLUDED_SAMPLES if not regex.search(path)]
        caught = [path for path in INCLUDED_SAMPLES if regex.search(path)]
        self.assertEqual([], missed, "hook does not exclude: " + ", ".join(missed))
        self.assertEqual([], caught, "hook wrongly excludes: " + ", ".join(caught))


if __name__ == "__main__":
    unittest.main()
