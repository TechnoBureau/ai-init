# Tests and Verification — AI Init Skills

This document records the verification mechanisms that exist in the repository.
It does not infer quality gates from tool names; every command below is
defined in a manifest, workflow, or hook configuration.

## Scope and Strategy

- Systems covered: the skill validator, the link checker, the
  template-to-document correspondence, the pinning policy, the secret-scanning
  baseline, and the documentation state checks.
- Levels in use: unit tests, static validation, and CI enforcement. No
  integration, end-to-end, performance, or accessibility automation runs
  against a runtime, because there is no runtime.
- Risk priorities: frontmatter integrity (skill discovery), link integrity,
  template drift, and secret hygiene.
- Environments: local Python 3.11 virtual environment and GitHub Actions
  `ubuntu-latest`.
- Out of scope: model-behavior scoring, target repositories, and any deployed
  service.

## Test Layout

| Path / pattern | Scope | Level | Framework or tool |
|---|---|---|---|
| `tests/test_validate_skills.py` | Frontmatter, metadata, links, size, eval rules | Unit | `unittest` |
| `tests/test_check_links.py` | Link resolution and template exclusion | Unit | `unittest` |
| `tests/test_working_example.py` | Template-to-`docs/` and starter-file correspondence | Unit | `unittest` |
| `tests/test_secret_scanning.py` | IBM detect-secrets baseline policy, exclusions, hook flags, and dependency wiring | Unit | `unittest` |
| `tests/test_pinning.py` | Version-tag pinning for hooks and actions, and Dependabot coverage | Unit | `unittest` |
| `tests/test_docs_state.py` | Documents describe current state; no frozen runs, duplicated pins, or bookkeeping columns, and the structure doc lists every reference | Unit | `unittest` |
| `scripts/validate_skills.py` | Every checked-in skill and eval fixture | Static | Project script |
| `scripts/check_links.py` | All non-template Markdown | Static | Project script |
| `.pre-commit-config.yaml` | Format, hygiene, secrets, lint | Static | pre-commit |

## Commands

| Purpose | Exact command | Defined in | Enforced by |
|---|---|---|---|
| Unit tests | `python -m unittest discover -s tests -v` | `tests/` | CI job `validate` |
| Skill validation | `python scripts/validate_skills.py --strict` | `scripts/validate_skills.py` | CI job `validate`, pre-commit hook |
| Link check | `python scripts/check_links.py` | `scripts/check_links.py` | CI job `validate`, pre-commit hook |
| Markdown lint | `pre-commit run markdownlint-cli2 --all-files` | `.pre-commit-config.yaml` | CI job `validate`, pre-commit hook |
| All hooks | `pre-commit run --all-files` | `.pre-commit-config.yaml` | CI job `validate` |
| Secret scan | `pre-commit run detect-secrets --all-files` | `.pre-commit-config.yaml` | CI job `validate`, pre-commit hook |
| Install tooling | `python -m pip install -r requirements-dev.txt` | `requirements-dev.txt` | CI job `validate` |

`gitleaks` runs in CI. In a restricted environment where the hook cannot
download its runtime, it must be reported as not run rather than as passing.

## CI Verification

| Workflow file | Trigger | Test / validation jobs | Blocking? |
|---|---|---|---|
| `.github/workflows/validate.yml` | `push`, `pull_request`, `workflow_dispatch` | Validate Agent Skills; Check local Markdown links; Run validator regression tests; Run repository hygiene hooks | Configured as the required check; branch protection must enforce it |

A check is only blocking when branch protection requires it. That setting lives
in the hosting platform and is not visible in this tree.

## Requirement Traceability

| Requirement | Acceptance criterion | Test | Level | Coverage |
|---|---|---|---|---|
| FR-1 | Frontmatter parses and name matches directory | `test_valid_skill_passes`, `test_name_must_match_directory` | Unit | Covered |
| FR-2 | Description contains a trigger clause | `test_description_requires_trigger` | Unit | Covered |
| FR-3 | Enterprise metadata present; removed keys rejected | `test_document_control_metadata_is_not_required`, `test_document_control_metadata_is_not_accepted` | Unit | Covered |
| FR-5 | Body size limits enforced | Validator rules `SKILL044`–`SKILL046` | Static | Covered |
| FR-10 | Missing frontmatter fails with a specific rule | `test_missing_frontmatter_is_rejected`, `test_reformatted_frontmatter_regression_is_rejected` | Unit | Covered |
| FR-11 | Broken relative links are reported | `test_broken_relative_link_is_rejected`, `test_reports_broken_link_with_line` | Unit | Covered |
| FR-12 | Eval fixtures carry both trigger states | `test_eval_fixture_requires_both_trigger_states` | Unit | Covered |
| FR-13 | CI runs all gates | Workflow definition | Static | Covered |
| FR-14 | Every template has a generated counterpart | `test_every_template_has_generated_document` | Unit | Covered |
| NFR-4 | Validator is deterministic and fails closed | Repeated runs, explicit exit codes | Static | Covered |
| NFR-7 | Symlink failure is reported, not copied | Instruction and checklist | Manual | Partial |

Requirements FR-4, FR-6 through FR-9, FR-15 through FR-18, and most
non-functional requirements are verified by review rather than automation.
They are marked `Partial` where no automated evidence exists.

## Mandatory Verification Areas

| Area | Assessment |
|---|---|
| Unit and error paths | Verified — the modules listed in the table above cover every script and starter policy, including the docs-state rules |
| Integration and contracts | Partial — Skills CLI discovery is verified manually, not in CI |
| Authentication and authorization | Not applicable — no authenticated surface in this repository |
| Input validation and injection | Partial — the validator checks structure; no fuzzing |
| Dependency and secret scanning | Verified — gitleaks, IBM detect-secrets, and private-key detection run in pre-commit and CI |
| Accessibility (WCAG 2.2 target) | Partial — Markdown structure rules only; no target level selected |
| Performance and load | Not applicable — no runtime |
| Resilience and recovery | Not applicable — no runtime state |
| Migration and rollback | Not applicable — no schema or database |
| Backup restore | Not applicable — Git history is the recovery mechanism |

## Coverage and Quality Gates

- Configured coverage threshold: `Not configured`. No coverage tool is wired
  in, and no threshold is claimed.
- Coverage tool and scope: `Not configured`.
- Mutation testing: `Not configured`.
- Required checks before merge: workflow jobs exist; enforcement depends on
  branch protection, which is not asserted here.
- Flaky-test policy: tests must be deterministic; no quarantine mechanism has
  been needed or configured.
- Components without detected automated tests: the human-facing content of the
  skills (safety instructions, evidence rules) is reviewed, not unit-tested.

## Test Data and Environments

- Data source: synthetic fixtures created inside temporary directories.
- Production data: prohibited and not present.
- Secret handling in tests: no real credentials; fixtures use obvious
  placeholders.
- Cleanup and isolation: `tempfile.TemporaryDirectory` per test, removed on
  exit.
- External services: none contacted by the test suite.

## Gate Enforcement

Every command in the table above is defined in a manifest, workflow, or hook
configuration, and the CI job runs each one on every push and pull request. The
workflow run is the record of a result, so this document does not repeat a
timestamp, revision, environment, or test count.

Run the commands above before opening a pull request. `gitleaks` needs network
access to download its runtime; where that is blocked, the hook reports
`Skipped` and must not be described as passing. The IBM detect-secrets hook reads the committed baseline
and requires no network access after its environment is installed.

## Defects, Gaps, and Actions

| Gap | Risk | Proposed action |
|---|---|---|
| No coverage measurement | Unmeasured test completeness | Add coverage reporting for `scripts/` |
| Skill discovery not asserted in CI | A host could reject a valid-looking skill | Add a Skills CLI discovery check to CI |
| No eval harness | Model behavior drift is not measured | Wire `evals/` into a runner |
| Accessibility target not selected | Conformance is unknown | Choose a documentation accessibility target |

No dates or owners are invented; the gaps are recorded for triage.

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Security](./security.md) · [Architecture](./architecture.md)
