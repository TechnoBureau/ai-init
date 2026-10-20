# Documentation

This directory holds the project documentation. [README.md](../README.md) is the
root entry point for people and AI agents; this page is the index for `docs/`.

## Documents

| Document | Purpose | Evidence base |
|---|---|---|
| [Architecture](./architecture.md) | Collection structure, validation pipeline, and design decisions | Skills, scripts, workflows |
| [Skill authoring standard](./skill-standard.md) | Normative frontmatter, body, eval, and review rules | Agent Skills specification, validator |
| [Governance](./governance.md) | Roles, change classes, review cadence, deprecation | Repository policy |
| [Threat model](./threat-model.md) | Assets, trust boundaries, threats, and controls | Skills, scripts, CI configuration |

## Documentation conventions

- Derive current behavior from code, configuration, tests, and workflows.
  Existing Markdown is history, not proof that behavior is active.
- Mark unknowns `Not documented`, `Not assessed`, `Not decided`, or `TBD`.
  Never invent owners, controls, commands, dates, or compliance status.
- Use one H1 per page, sequential headings, descriptive link text, and table
  header rows.
- Link only to files that exist. Keep links relative and verify them.
- Diagrams must be evidence-based, compact, and explained in text nearby.
- Record the commit SHA where a document makes claims about current behavior.
- Do not add a per-document changelog or control block. Change history lives in
  Git and the pull request.

## Adding or renaming a document

1. Create the document under `docs/` in lowercase kebab-case (`PRD.md` is the
   recorded acronym exception).
2. Add a row to the table above.
3. Update any related links in [README.md](../README.md).
4. Remove rows for documents that are deleted or renamed; leave no dead links.

## Ownership and review

- Ownership and review routing: [CODEOWNERS](../CODEOWNERS).
- Review process and cadence: [Governance](./governance.md).
- Review security and architecture documents at least quarterly.
- Re-verify commands, paths, links, and control statuses when reviewing.
