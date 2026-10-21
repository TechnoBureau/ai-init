# Tasks

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

## Spec-driven planning

Use this only when the project has adopted SDD or the user requests it. Derive
tasks from an accepted specification; keep the PRD/feature spec as the source of
requirements. Each task references the applicable permanent requirement IDs and
has an observable acceptance criterion. If a requirement changes, update the
spec before treating implementation tasks as complete.

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

{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}
