# Project Log — {{PROJECT_NAME}}

> Use for ongoing projects that benefit from shared historical context. Keep
> entries append-only: add a dated correction instead of rewriting history.
> Never record secrets, credentials, personal data, or unredacted logs.

## Entry Format

```text
## YYYY-MM-DD — Short title

**Context:** Why this entry exists and what was being decided or observed.
**Decision / outcome:** What changed, or `No decision recorded`.
**Evidence or references:** Commit SHA, paths, issue, or test result.
**Author:** Human or agent identifier.
**Supersedes:** Prior entry or decision ID, when applicable.
```

## Entries

## {{DATE}} — Documentation baseline recorded

**Context:** Documentation was reviewed against repository code and
configuration.\
**Decision / outcome:** {{CONFIRMED_OUTCOME_OR_NO_DECISIONS_RECORDED}}\
**Evidence or references:** {{RELEVANT_FILES_OR_PATHS}}\
**Author:** {{HUMAN_OR_AGENT}}\
**Supersedes:** None

## Maintenance Rules

- Append corrections; do not rewrite prior entries.
- Link evidence that another reviewer can reproduce.
- Keep entries short and factual; move durable rationale into an ADR.
- Record follow-up work in `docs/tasks.md`, not only here.

______________________________________________________________________

### Related Docs

[README](../README.md) · [Agents](../AGENTS.md) · [Decisions](./decisions.md) · [Tasks](./tasks.md)
