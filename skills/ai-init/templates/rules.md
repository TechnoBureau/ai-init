# Repository Rules — {{PROJECT_NAME}}

> Record rules established by repository configuration, maintainer policy, or
> explicit user confirmation. Do not turn conventions from this template into
> project policy without evidence.

## Contribution Workflow

- Branch and review process: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Required approvals and checks: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Commit and release conventions: {{VERIFIED_OR_NOT_DOCUMENTED}}

## Build, Test, and CI

{{LINK_TO_DOCS_TESTS_AND_SUMMARIZE_ONLY_CONFIGURED_GATES}}

## Security and Data Handling

{{CONFIRMED_RULES_OR_LINK_TO_DOCS_SECURITY}}

## AI Agent Collaboration

- Start from [README.md](../README.md), the shared documentation index.
- Follow root [AGENTS.md](../AGENTS.md) and any more specific repository
  instructions.
- Verify behavior and commands from source, manifests, and configuration.
- Keep affected documentation current when behavior, interfaces, or
  architecture changes.

## Documentation Maintenance

- Preserve permanent requirement and decision IDs when updating documents.
- Keep generated project documentation under `docs/`, except root
  `README.md`, `AGENTS.md`, and `CLAUDE.md`.
- Do not present recommendations or assumptions as current repository facts.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Security](./security.md) · [Style](./style.md)
