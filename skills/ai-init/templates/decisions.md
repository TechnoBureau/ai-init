# Decisions — {{PROJECT_NAME}}

> **Document control** — Owner: {{OWNER_OR_NOT_DOCUMENTED}} · Status:
> {{DRAFT_REVIEWED_APPROVED}} · Version: {{SEMVER}} · Last reviewed:
> {{YYYY-MM-DD}} · Classification: {{PUBLIC_INTERNAL_CONFIDENTIAL_RESTRICTED}}

This is the supporting register for the D-IDs summarized in
[docs/PRD.md](./PRD.md). Preserve IDs once assigned. Separate decisions
explicitly recorded by maintainers from choices merely visible in the current
implementation; do not assign unverified rationale or alternatives.

Use an ADR/MADR-style record. A proposal that has not been approved is
`Proposed`, not `Accepted`. Never delete a decision: mark it `Superseded` and
link the replacement.

## Decision Index

| ID | Decision | Status | Date | Owner | Evidence |
|---|---|---|---|---|---|
| D-1 | {{DECISION}} | {{PROPOSED_ACCEPTED_SUPERSEDED_DEPRECATED}} | {{DATE_OR_NOT_DOCUMENTED}} | {{OWNER_OR_UNKNOWN}} | `{{EXACT_PATH_OR_NOT_DOCUMENTED}}` |

## Decision Records

### D-1 — {{SHORT_DECISION_TITLE}}

- **Status:** {{Proposed / Accepted / Superseded / Deprecated; approval not documented}}
- **Date:** {{YYYY-MM-DD_OR_NOT_DOCUMENTED}}
- **Owner:** {{ROLE_OR_PERSON_OR_UNKNOWN}}
- **Context:** {{FORCES_CONSTRAINTS_AND_EVIDENCE}}
- **Decision:** {{CHOICE}}
- **Consequences:** {{POSITIVE_NEGATIVE_AND_FOLLOW_UP}}
- **Reason:** {{EVIDENCED_RATIONALE_OR_NOT_DOCUMENTED}}
- **Alternatives rejected:** {{EVIDENCED_ALTERNATIVES_AND_WHY_OR_NOT_DOCUMENTED}}
- **Evidence:** `{{CODE_CONFIG_OR_CONFIRMED_SOURCE}}`
- **Supersedes / superseded by:** {{D_XX_OR_NONE}}

If no explicit decision records or defensible implementation choices are
present, state that here. Do not manufacture D-IDs to fill the page. Record an
observed implementation choice separately from an approved decision and mark
its approval status `Not documented`.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Structure](./structure.md)
