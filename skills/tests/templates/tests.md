# Tests and Verification — {{PROJECT_NAME}}

Document actual test and validation mechanisms from test files, project
manifests, CI workflows, and tool configuration. Do not infer coverage or
quality gates from conventions alone.

## Test Layout

| Path / pattern | Scope | Framework or tool | Evidence |
|---|---|---|---|
| `{{EXACT_TEST_PATH_OR_PATTERN}}` | {{TESTED_COMPONENT}} | {{CONFIGURED_TOOL}} | `{{CONFIG_PATH}}` |

## Commands

| Purpose | Exact command | Defined in |
|---|---|---|
| Unit tests | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` |
| Integration / end-to-end | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` |
| Lint / static validation | `{{VERIFIED_COMMAND_OR_NONE}}` | `{{MANIFEST_OR_WORKFLOW}}` |

## CI Verification

| Workflow file | Trigger | Test / validation jobs |
|---|---|---|
| `{{EXACT_WORKFLOW_PATH}}` | {{CONFIGURED_TRIGGER}} | {{CONFIGURED_JOBS}} |

## Coverage and Gaps

- Configured coverage threshold: {{EXACT_VALUE_OR_NOT_CONFIGURED}}
- Components without detected automated tests: {{EVIDENCED_LIST_OR_NONE}}
- If no automated test suite is present, state that plainly and list only
  other configured validation checks.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Security](./security.md)
