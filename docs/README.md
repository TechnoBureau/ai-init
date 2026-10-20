# Documentation

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
| [Decisions](./decisions.md) | Decision records with context and consequences |
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
- Link only to files that exist. Keep links relative and verify them. In a
  template, link only to the documents every generated repository has; name a
  conditional document in backticks until it is generated.
- Diagrams must be evidence-based, compact, and explained in text nearby.
- Do not add a per-document changelog or control block. Change history lives in
  Git and the pull request.
- Do not add per-row status, date, owner, evidence, verification, baseline,
  target, or measure columns, and do not record rejected options or supersession
  on a decision. Use one `Assessment` (`Coverage`) column when a table must say
  whether a row holds.
- Describe the state that exists now and link the file that owns a value. Do
  not copy exact version pins, hook revisions, test counts, or run dates into
  prose; they drift from the configuration that owns them.

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
- Re-verify commands, paths, links, and control descriptions when reviewing.
