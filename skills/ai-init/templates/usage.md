# Usage — {{PROJECT_NAME}}

> **Document control** — Owner: {{OWNER_OR_NOT_DOCUMENTED}} · Status:
> {{DRAFT_REVIEWED_APPROVED}} · Version: {{SEMVER}} · Last reviewed:
> {{YYYY-MM-DD}} · Classification: {{PUBLIC_INTERNAL_CONFIDENTIAL_RESTRICTED}}
>
> Include only commands and configuration verified in manifests, scripts,
> workflows, or deployment files. Omit sections that do not apply. Never
> include secret values; reference the secret-store path instead.

## Prerequisites

- Runtime and supported versions: {{VERIFIED_RUNTIME_AND_VERSION}}
- Package manager and version: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Required system packages or services: {{VERIFIED_OR_NOT_CONFIGURED}}
- Required access or credentials (location only): {{SECRET_STORE_REFERENCE_OR_NOT_DOCUMENTED}}

## Installation

```bash
{{VERIFIED_INSTALL_COMMANDS}}
```

State the shell and working directory when it is not obvious. Do not publish a
command that was not run or confirmed by project configuration.

## Configuration

| Setting | Purpose | Required? | Default / source | Secret? |
|---|---|---|---|---|
| `{{EXACT_CONFIG_KEY}}` | {{VERIFIED_PURPOSE}} | {{YES_NO}} | {{VERIFIED_DEFAULT_OR_NOT_DOCUMENTED}} | {{YES_NO}} |

Document environment-variable precedence and configuration file locations only
where verified.

## Run Locally

```bash
{{VERIFIED_RUN_COMMAND}}
```

- Expected startup indicator: {{VERIFIED_LOG_OR_PORT_OR_NOT_DOCUMENTED}}
- Local dependencies (database, queue, cache): {{VERIFIED_OR_NOT_CONFIGURED}}

## Validate

```bash
{{VERIFIED_TEST_AND_LINT_COMMANDS_OR_NOT_CONFIGURED}}
```

Detailed test inventory belongs in `docs/tests.md` only if the optional
`tests` skill has created that document. Report commands exactly as configured;
do not infer a gate from a script name.

## Deployment

{{VERIFIED_DEPLOYMENT_COMMANDS_OR_TARGETS}}

| Environment | Method | Required approvals | Evidence |
|---|---|---|---|
| {{ENVIRONMENT}} | {{CONFIGURED_MECHANISM}} | {{CONFIRMED_OR_NOT_DOCUMENTED}} | `{{PATH}}` |

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Resolution |
|---|---|---|---|
| {{VERIFIED_SYMPTOM}} | {{CONFIRMED_CAUSE}} | `{{COMMAND_OR_LOG_QUERY}}` | {{ACTION}} |

Include only issues that were observed or are documented by the project.

## Operational and Security Notes

- Backup/restore implications: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Data created locally and cleanup: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Network egress and external services: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Safe defaults and dangerous options: {{CONFIRMED_OR_NOT_DOCUMENTED}}

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Security](./security.md)
