# Documentation — AI Init Skills

This directory holds the project documentation. [README.md](../README.md) is the
root entry point for people and AI agents; this page is the index for `docs/`.

Every document here is generated from the templates in
`skills/*/templates/`, so this folder is also the working example of the
collection's own output.

## Documents

| Document | Purpose |
|---|---|
| [Product requirements](./PRD.md) | Goals, scope, requirements, workflows, product type |
| [Architecture](./architecture.md) | Components, data flows, deployment, trust boundaries |
| [Repository structure](./structure.md) | Verified directory and component map |
| [Decisions](./decisions.md) | Decision records with context and alternatives |
| [Security](./security.md) | Security posture, applicable profiles, gaps |
| [Threat model](./threat-model.md) | Assets, trust boundaries, threats, controls |
| [Tests](./tests.md) | Test layout, commands, coverage gaps |
| [Style](./style.md) | Languages, tooling, conventions |
| [Rules](./rules.md) | Contribution, security, and documentation rules |
| [Usage](./usage.md) | Verified install, validation, and run commands |
| [Governance](./governance.md) | Roles, change classes, review cadence |
| [Skill authoring standard](./skill-standard.md) | Repository-specific skill format and review rules |

`docs/design.md` is intentionally absent: this repository has no rendered user
interface, so the `design` skill does not apply. That conditional output is
documented rather than fabricated.

## Documentation conventions

- Derive current behavior from code, configuration, tests, and workflows.
  Existing Markdown is history, not proof that behavior is active.
- Mark unknowns `Not documented`, `Not assessed`, `Not decided`, or `TBD`.
  Never invent owners, controls, commands, dates, or compliance status.
- Use one H1 per page, sequential headings, descriptive link text, and table
  header rows.
- Link only to files that exist. Keep links relative and verify them.
- Diagrams must be evidence-based, compact, and explained in text nearby.
- Do not add a per-document changelog or control block. Change history lives in
  Git and the pull request.

## Adding or renaming a document

1. Create the document under `docs/` in lowercase kebab-case (`PRD.md` is the
   recorded acronym exception).
2. Add a row to the table above.
3. Update any related links in [README.md](../README.md).
4. Remove rows for documents that are deleted or renamed; leave no dead links.
5. If the document comes from a template, update the template too, otherwise
   the next generation run will diverge.

## Ownership and review

- Ownership and review routing: [CODEOWNERS](../.github/CODEOWNERS).
- Review process and cadence: [Governance](./governance.md).
- Review security and architecture documents at least quarterly.
- Re-verify commands, paths, links, and control statuses when reviewing.
