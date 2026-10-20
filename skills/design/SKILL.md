______________________________________________________________________

## name: design description: > Create or refine a UI design-system document from a product's actual visual implementation, design tokens, and accessibility evidence. Use for apps with a rendered user interface.

# Product Design

Create or update `docs/design.md` only for a product with a rendered web,
mobile, or desktop interface. The catalog and the output template have
different roles: `references/catalog.md` helps select a system; the template
defines the project document. Keep selection guidance in the catalog and
project-specific decisions in the generated document.

## Preflight

- Check whether `docs/design.md` exists. Preserve current project decisions,
  tokens, and asset links; update the relevant sections in place.
- Inspect actual UI code, styles, design tokens, component libraries,
  accessibility checks, and assets before making claims.
- If no UI exists, do not create `docs/design.md`. If a new UI repository has
  no implemented system yet, document `Not selected` rather than inventing a
  design system, palette, or assets.

## Create the design document

- Prefer an existing design system or component library evidenced by code.
  Use the catalog only when the project needs a selection; explain platform,
  stack, accessibility, and brand fit briefly.
- Record existing tokens and components from implementation. Mark unknown
  values `Not documented`; do not fill the document with generic token values.
- Describe interaction and accessibility behavior with concrete evidence.
  State a conformance target only when the product owner has chosen it.
- Keep it readable to design, product, engineering, and accessibility
  stakeholders: plain-language rationale first, token/component details in
  concise tables.
- Keep related-document links only when their target files exist; use the
  README as the shared documentation index.
- This skill documents the design system. Change UI code only when separately
  requested.

Use [templates/design.md](./templates/design.md) and consult
[references/catalog.md](./references/catalog.md) only when design-system
selection is needed.

## README agent-entry links

After this skill runs, if root `README.md` exists, ensure
`AGENTS.md` and `CLAUDE.md` are relative symbolic links to it. Inspect each
path first. Preserve regular files or links to other targets; merge unique
instructions into the README before replacing only when safe. If preservation
is uncertain or symlink creation is unsupported, do not replace the path and
report the conflict. Never create broken links or copied-file substitutes;
remove README links to absent aliases and report the missing links.
Update the README's documentation index to include `docs/design.md`. If
README is absent, report that `ai-init` is needed to create the shared index.
