# Decisions — {{PROJECT_NAME}}

This is the supporting register for the D-IDs summarized in
[docs/PRD.md](./PRD.md). Preserve IDs once assigned. Separate decisions
explicitly recorded by maintainers from choices merely visible in the current
implementation; do not assign unverified rationale.

Use a short ADR-style record: context, decision, consequences, and reason.
Never delete or renumber a record. When a record is replaced, the new record
names the one it replaces.

## Decision Index

| ID | Decision |
|---|---|
| D-1 | {{DECISION}} |

## Decision Records

### D-1 — {{SHORT_DECISION_TITLE}}

- **Context:** {{FORCES_CONSTRAINTS_AND_INPUTS}}
- **Decision:** {{CHOICE}}
- **Consequences:** {{POSITIVE_NEGATIVE_AND_FOLLOW_UP}}
- **Reason:** {{EVIDENCED_RATIONALE_OR_NOT_DOCUMENTED}}

If no explicit decision records or defensible implementation choices are
present, state that here. Do not manufacture D-IDs to fill the page. Record an
observed implementation choice separately from an approved decision.

Do not add status, date, owner, evidence, rejected-option, or supersession
fields. A record that no process consumes is noise, and the justification lives
in the commit and the pull request that made the decision.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Structure](./structure.md)
