# {{PROJECT_NAME}}

{{ONE_SENTENCE_DESCRIPTION_BASED_ON_CODE}}

This is the shared starting point for people and AI agents. It summarizes the
project and indexes its documentation. Root `AGENTS.md` and `CLAUDE.md` are
symbolic links to this file, created by the skill at execution time.

## Overview

{{CONCISE_SUMMARY_OF_PURPOSE_AND_CURRENT_CAPABILITIES}}

**Project type:** `{{VERIFIED_PROJECT_TYPE}}`\
**Primary stack:** {{LANGUAGES_AND_RUNTIME}}

**Implementation status:** {{IMPLEMENTED / SCAFFOLD-ONLY / INITIAL REPOSITORY}}

If the repository is empty or scaffold-only, state which product, runtime,
tests, and deployment decisions have not yet been made. Do not present
assumptions as project facts. For unverified commands, omit the code block
and say `Not configured` rather than leaving a runnable-looking placeholder.

## Goals and Objectives

{{BRIEF_SUMMARY_OF_EVIDENCED_GOALS_FROM_DOCS_PRD_MD}}

Full requirements and permanent traceability IDs are in [docs/PRD.md](./docs/PRD.md).

## Quick Start

Use only commands verified from manifests, scripts, or workflow configuration.

```bash
{{VERIFIED_INSTALL_COMMAND}}
{{VERIFIED_RUN_COMMAND}}
```

See [docs/usage.md](./docs/usage.md) for configuration and other verified
commands, if that guide applies.

## Documentation Index

Keep only links to files that were generated.

| Document | Purpose |
|---|---|
| [Product requirements](./docs/PRD.md) | Goals, scope, requirements, workflows, and product type |
| [Architecture](./docs/Architecture.md) | Components, data flows, deployment, and system boundaries |
| [Repository structure](./docs/structure.md) | Verified directory and component map |
| [Decisions](./docs/decisions.md) | Decision IDs, context, and evidence |
| [Security](./docs/security.md) | Evidenced controls and security configuration |
| [Design](./docs/design.md) | UI design system and interaction rules |
| [Style](./docs/style.md) | Repository conventions and applicable language guidance |
| [Rules](./docs/rules.md) | Confirmed contribution and workflow conventions |
| [Tasks](./docs/tasks.md) | Maintained project task board |
| [Memory](./docs/memory.md) | Append-only project context and outcomes |
| [Usage](./docs/usage.md) | Verified installation, configuration, and run commands |

If `docs/tests.md` exists, add this index row; otherwise omit it:

`| [Tests](./docs/tests.md) | Test layout, commands, and configured checks |`

## AI Agent Entry Points

- [AGENTS.md](./AGENTS.md) — symbolic link to this shared README.
- [CLAUDE.md](./CLAUDE.md) — symbolic link to this shared README.

When working in this repository, inspect relevant source, configuration, and
linked documentation before describing behavior or running commands. Follow
confirmed repository-specific instructions and preserve existing user work.

## License

{{LICENSE_OR_NOT_DOCUMENTED}}
