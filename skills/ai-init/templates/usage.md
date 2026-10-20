# Usage — {{PROJECT_NAME}}

> Include only commands and configuration verified in manifests, scripts,
> workflows, or deployment files. Omit sections that do not apply.

## Prerequisites

- {{VERIFIED_RUNTIME_AND_VERSION}}
- {{VERIFIED_DEPENDENCIES}}

## Installation

```bash
{{VERIFIED_INSTALL_COMMANDS}}
```

## Configuration

| Setting | Purpose | Default / source |
|---|---|---|
| `{{EXACT_CONFIG_KEY}}` | {{VERIFIED_PURPOSE}} | {{VERIFIED_DEFAULT_OR_NOT_DOCUMENTED}} |

## Run Locally

```bash
{{VERIFIED_RUN_COMMAND}}
```

## Test and Validate

Detailed test inventory belongs in `docs/tests.md` only if the optional
`tests` skill has created that document.

## Deployment

{{VERIFIED_DEPLOYMENT_COMMANDS_OR_TARGETS}}

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./Architecture.md)
