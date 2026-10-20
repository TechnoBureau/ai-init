# Tests and Verification — {{PROJECT_NAME}}

> Document actual test and validation mechanisms from test files, project
> manifests, CI workflows, and tool configuration. Do not infer coverage or
> quality gates from conventions alone.

## Scope and Strategy

- Systems/components covered: {{VERIFIED_SCOPE}}
- Test levels in use: {{UNIT_INTEGRATION_CONTRACT_E2E_MANUAL}}
- Risk-based priorities: {{HIGH_RISK_PATHS_OR_NOT_ASSESSED}}
- Environments used: {{VERIFIED_ENVIRONMENTS}}
- Explicitly out of scope: {{EXCLUSIONS_OR_NONE}}

## Test Layout

| Path / pattern | Scope | Level | Framework or tool | Evidence |
|---|---|---|---|---|
| `{{EXACT_TEST_PATH_OR_PATTERN}}` | {{TESTED_COMPONENT}} | {{UNIT_INTEGRATION_E2E}} | {{CONFIGURED_TOOL}} | `{{CONFIG_PATH}}` |

## Commands

| Purpose | Exact command | Defined in | Enforced by |
|---|---|---|---|
| Unit tests | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` | {{WORKFLOW_JOB_OR_NOT_IN_CI}} |
| Integration / end-to-end | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` | {{WORKFLOW_JOB_OR_NOT_IN_CI}} |
| Lint / static validation | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` | {{WORKFLOW_JOB_OR_NOT_IN_CI}} |
| Type / schema validation | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` | {{WORKFLOW_JOB_OR_NOT_IN_CI}} |
| Security scans | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` | {{WORKFLOW_JOB_OR_NOT_IN_CI}} |

Do not list a command you did not verify. Use `Not configured` where none
exists. Name the workflow job that enforces a command instead of recording
when it last passed.

## CI Verification

| Workflow file | Trigger | Test / validation jobs | Blocking? |
|---|---|---|---|
| `{{EXACT_WORKFLOW_PATH}}` | {{CONFIGURED_TRIGGER}} | {{CONFIGURED_JOBS}} | {{YES_NO_INFORMATIONAL}} |

A required check is blocking only when branch protection or release policy
enforces it; state the evidence.

## Requirement Traceability

| Requirement | Acceptance criterion | Test / evidence | Level | Status |
|---|---|---|---|---|
| {{FR_OR_NFR_ID}} | {{CRITERION}} | `{{TEST_PATH_OR_MANUAL_PROCEDURE}}` | {{LEVEL}} | {{COVERED_PARTIAL_GAP}} |

`Covered` requires a runnable or executed artifact. Do not claim coverage from
a test name alone.

## Mandatory Verification Areas

| Area | Status | Evidence / gap |
|---|---|---|
| Unit and error paths | {{VERIFIED_PARTIAL_NOT_EVIDENCED}} | `{{PATH_OR_GAP}}` |
| Integration and contracts | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Authentication and authorization | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Input validation and injection | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Dependency and secret scanning | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Accessibility (WCAG 2.2 target) | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Performance and load | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Resilience and recovery | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Migration and rollback | {{STATUS}} | `{{PATH_OR_GAP}}` |
| Backup restore | {{STATUS}} | `{{PATH_OR_GAP}}` |

Record `Not applicable` with a reason; do not leave a blank cell.

## Coverage and Quality Gates

- Configured coverage threshold: {{EXACT_VALUE_OR_NOT_CONFIGURED}}
- Coverage tool and scope: {{VERIFIED_OR_NOT_CONFIGURED}}
- Mutation testing: {{CONFIGURED_OR_NOT_CONFIGURED}}
- Required checks before merge: {{VERIFIED_OR_NOT_CONFIGURED}}
- Flaky-test policy and quarantine owner: {{CONFIRMED_OR_NOT_DOCUMENTED}}
- Components without detected automated tests: {{EVIDENCED_LIST_OR_NONE}}

If no automated test suite is present, state that plainly and list only other
configured validation checks. Do not present coverage as quality by itself.

## Test Data and Environments

- Data source (synthetic/masked): {{VERIFIED_OR_NOT_DOCUMENTED}}
- Production data prohibited: {{CONFIRMED}}
- Secret handling in tests: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Cleanup and isolation: {{VERIFIED_OR_NOT_DOCUMENTED}}
- External services or network dependencies: {{VERIFIED_OR_NOT_DOCUMENTED}}

## Verification Status

State which gates pass and where they are enforced. CI is the record of a run;
do not paste a dated log, a revision, an exact tool version, or a test count
into the document, because each one is stale after the next commit or upgrade.

Record a failure investigation only while it is open, with the command,
environment, and result for that run:

```text
Command: <exact command>
Environment: <OS/runtime>
Result: Failed | Blocked
Failures: <test IDs and short diagnostics>
Not covered: <explicit gaps>
```

## Defects, Gaps, and Actions

| Gap | Risk | Proposed action | Owner / target |
|---|---|---|---|
| {{EVIDENCED_GAP_OR_NONE}} | {{WHY_IT_MATTERS}} | {{ACTION_OR_NONE}} | {{OWNER_OR_UNKNOWN}} |

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Security](./security.md) · [Architecture](./architecture.md)
