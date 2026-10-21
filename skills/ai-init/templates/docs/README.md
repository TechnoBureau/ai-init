# Documentation

This directory holds the project documentation. The repository root
`README.md` summarizes the project; this page indexes the documents under
`docs/`.

## Documents

Keep only the rows for documents that exist. When you write this page, turn
each document name into a link to the path in parentheses and delete the
parenthetical. A broken or aspirational index is worse than a short one.

| Document | Purpose |
|---|---|
| Product requirements (`PRD.md`) | Goals, scope, requirements, workflows, product type |
| Repository structure (`structure.md`) | Verified directory and component map |
| Decisions (`decisions.md`) | Decision records with context and consequences |
| Security (`security.md`) | Security posture, applicable profiles, gaps |

These documents are generated only when the repository supports them:
`architecture.md`, `threat-model.md`, `tests.md`, `design.md`, `style.md`,
`rules.md`, `usage.md`, `governance.md`, `tasks.md`, and
`spec-driven-development.md`. Add a row per document that exists, using the
same two columns, then delete this paragraph.

## Documentation conventions

- Derive current behavior from code, configuration, tests, and workflows.
  Existing Markdown is history, not proof that behavior is active.
- Mark unknowns `Not documented`, `Not assessed`, `Not decided`, or `TBD`.
  Never invent owners, controls, commands, dates, or compliance status.
- Use one H1 per page, sequential headings, descriptive link text, and table
  header rows.
- Link only to files that exist. Keep links relative and verify them. A
  template names a document in a code span; the skill writes the link when it
  writes the document.
- Diagrams must be evidence-based, compact, and explained in text nearby.
- Do not add a per-document changelog or control block unless the project has
  adopted a policy that requires one.
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
3. Update any related links in the root `README.md`.
4. Remove rows for documents that are deleted or renamed; leave no dead links.

## Ownership and review

- Document owners and review expectations: {{LINK_TO_GOVERNANCE_OR_CODEOWNERS_OR_NOT_CONFIGURED}}.
- Review security and architecture documents at least quarterly.
- Re-verify commands, paths, links, and control statuses when reviewing.
