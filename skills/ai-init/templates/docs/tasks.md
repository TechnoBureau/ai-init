# Tasks — {{PROJECT_NAME}}

> Use for an ongoing project when a shared task board is useful. Link work to
> permanent PRD or decision IDs where applicable; do not add unsupported
> priority tiers.

## Backlog

- [ ] T-001: {{TASK}} (ref: FR-1 or D-1, if applicable)

## In Progress

- [ ] T-002: {{TASK}}

## In Review

- [ ] T-003: {{TASK}} (review reference: {{LINK_OR_NOT_APPLICABLE}})

## Done

- [x] T-000: {{COMPLETED_TASK}}

## Task Format

```text
- [ ] T-XXX: <short description>
  - Ref: <requirement ID, decision ID, incident, or none>
  - Acceptance: <observable completion criterion>
  - Notes: <implementation context and risks>
```

## Definition of Done

- Acceptance criteria are met and evidenced.
- Relevant tests, lint, and type checks pass.
- Security, privacy, and accessibility impacts were considered.
- Public contracts and documentation are updated.
- No secrets or personal data were introduced.
- The change is reviewed per `CODEOWNERS`.

## Board Rules

- Task IDs are permanent; do not renumber completed work.
- Do not invent priority tiers, deadlines, or owners.
- Blocked tasks state the blocker and the next decision needed.
- Completed tasks record the outcome, not just a checkbox.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Decisions](./decisions.md) · [Memory](./memory.md)
