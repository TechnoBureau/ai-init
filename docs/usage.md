# Usage

Commands below are verified from `requirements-dev.txt`, the scripts, and the
workflow configuration. Commands that do not exist are marked
`Not configured` rather than shown as placeholders.

## Prerequisites

- Python 3.11 or later (verified in CI).
- Git.
- Optional: Node.js with `npx` for the Skills CLI install and for running
  `markdownlint-cli2` through pre-commit.
- Required access or credentials: none for local validation. Publication to a
  registry is not part of this repository.

## Installation

```bash
git clone https://github.com/TechnoBureau/ai-init.git
cd ai-init
python -m venv .venv
. .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements-dev.txt
pre-commit install
```

## Configuration

| Setting | Purpose | Required? | Default / source | Secret? |
|---|---|---|---|---|
| `--root` (validator, link checker) | Repository root to inspect | No | Parent of `scripts/` | No |
| `--strict` (validator) | Treat warnings as errors | No | Off | No |
| `--format text\|json` (validator, link checker) | Output format | No | `text` | No |
| `PYTHONPATH` | Not required; tests add `scripts/` themselves | No | Not set | No |
| Python interpreter | Version used by scripts and tests | Yes | 3.11 or later | No |

No environment variable carries a secret for this repository.

## Run Locally

### Install the skills into an agent

```bash
npx skills add technobureau/ai-init --all --agent '*'
```

Install a single skill:

```bash
npx skills add technobureau/ai-init --skill ai-init --agent claude-code
```

List the skills available in a checkout without installing:

```bash
npx skills add . --list
```

### Use the skills

Skills run inside a compatible host; they are not shell commands. Invoke a skill
by name where supported, or include the skill name in a natural-language task.
For routine documentation updates, name the changed path and desired result so
`ai-init` can inspect only the relevant files. Ask explicitly for a full refresh
when a repository-wide review is intended.

- **Targeted documentation update:** “`$ai-init` Update the README Quick Start
  for the new `dev` script in `package.json`. Inspect the manifest, referenced
  script, and README; leave unrelated documents unchanged.”
- **Full documentation refresh:** “`$ai-init` Perform a full refresh of the
  repository documentation and reconcile all managed documents with current
  source and configuration.”
- **Spec-first change:** “Before implementing billing idempotency, use the
  existing PRD, issue, or task as the source of truth. Clarify scope, relevant
  risks, and an observable acceptance check; update a feature spec if the change
  warrants one. Ask about material ambiguity, label reversible assumptions, and
  don't start implementation until the behavior is clear.”
- **Requirements:** “`$prd` Update the requirements affected by the new account
  recovery flow; preserve existing IDs and inspect only related code and tests.”
- **Tests:** “`$tests` Add coverage for the new account recovery behavior using
  the existing test framework.”
- **Security:** “`$security` Review the changed API-key rotation path and its
  direct storage/auth dependencies; do not inventory unrelated services.”
- **Design:** “`$design` Update the focus-ring token for the shared Button
  component. Check its styles and keyboard behavior; leave other components
  unchanged.”
- **Code quality:** “`$code-quality` Remove the unused helper in
  `src/account.py`; check references, dynamic entry points, and related tests.”

A narrow request does not automatically trigger a full documentation, security,
design, or test audit.

### Validate the repository

```bash
python scripts/validate_skills.py --strict
python scripts/check_links.py
python -m unittest discover -s tests -v
pre-commit run --all-files
```

Expected local result: six skills validated, zero broken links, all tests
passing, and every hook passing. `gitleaks` may be skipped in a restricted
environment where the hook cannot download its runtime; that is reported as
skipped, never as passed.

- Expected startup indicator: `6 skills checked; 0 error(s), 0 warning(s).`
- Secret scanning: IBM detect-secrets runs `--use-all-plugins
  --no-keyword-scan --fail-on-unaudited` against `.secrets.baseline`. If the
  baseline version does not match the pinned hook, the hook rewrites the file
  and exits with status 3; commit the update.
- Hook and action pins are version tags, not commit SHAs. `tests/test_pinning.py`
  fails on a branch pin or a raw SHA.
- Local dependencies: none beyond the pinned Python packages; pre-commit
  installs each hook environment.

## Validate

```bash
python scripts/validate_skills.py --strict
python scripts/check_links.py
python -m unittest discover -s tests -v
```

Detailed test inventory is in [tests.md](./tests.md). Coverage thresholds are
`Not configured`.

## Deployment

There is no deployment step. Distribution is a `git push` followed by the
Skills CLI reading the repository. CI runs on every push and pull request.

| Environment | Method | Required approvals |
|---|---|---|
| Contributor workstation | Local commands above | None |
| CI | GitHub Actions `Validate` workflow | Pull-request review per CODEOWNERS |

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Resolution |
|---|---|---|---|
| `SKILL010 missing YAML frontmatter` | Formatter replaced `---` with a rule | Inspect line 1 of the file | Restore the frontmatter block from Git; never edit the rendered heading |
| `SKILL025 name must match directory` | Directory renamed or name typo | Compare `name` with the folder | Rename one to match the other |
| `SKILL073` for `owner`/`reviewed`/`classification` | Removed document-control metadata reintroduced | Inspect the metadata block | Delete the key; ownership belongs in CODEOWNERS |
| `SKILL080 relative link target does not exist` | Renamed or missing file | Open the reported path | Fix the link target |
| `EVAL001 evals/ directory is missing` | Fixtures not created | `ls evals/` | Add `evals/<skill>.yaml` with trigger and non-trigger cases |
| `gitleaks` hook fails to install | No network access to the hook repository | Hook log | Report the hook as not run; CI executes it |
| `check_links` reports a template path | Template added outside `templates/` | Reported path | Move it under `templates/`; templates are excluded by design |

## Operational and Security Notes

- Backup/restore: the Git history is the recovery mechanism; no local state
  matters.
- Data created locally: virtual environment, `__pycache__`, and pre-commit
  caches. All are ignored by `.gitignore`.
- Network egress: only during dependency installation and the optional Skills
  CLI usage. The scripts perform no network calls.
- Safe defaults: validation is read-only; `--strict` only changes the exit
  status. No command in this repository modifies a target repository.

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Security](./security.md)
