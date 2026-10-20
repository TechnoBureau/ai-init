______________________________________________________________________

## name: ai-init description: > Bootstrap or refresh an evidence-grounded, stakeholder-readable repository documentation set. Use for new or existing repositories; route PRDs, security, tests, design, and code-quality work to dedicated skills.

# AI Init

Create the shared root `README.md` and common project documentation. Keep
domain-specific PRD, security, test, design, and code-quality guidance in the
dedicated `prd`, `security`, `tests`, `design`, and `code-quality` skills.

## Preflight and preservation

1. Inspect the repository tree, source, manifests, workflows, tests, deployment
   and security configuration before using Markdown as evidence.
1. Check every output path before writing. Preserve user-authored sections,
   valid IDs, local conventions, and unrelated working-tree changes. Update in
   place; do not replace an existing file wholesale merely because a template
   exists.
1. Detect root README names case-insensitively. If only `readme.md` exists,
   preserve useful content while migrating the index to uppercase `README.md`.
   If both spellings exist, merge unique information before removing a
   duplicate. Do not silently discard content or leave two competing indexes.
1. Compare `.editorconfig`, `.gitattributes`, and `.pre-commit-config.yaml`
   before adding starter files; never copy over an existing configuration.

## Root README and agent links

- Create or refresh root `README.md` from [the README template](./templates/README.md).
  It is the one shared project summary and documentation index for people and
  agents.
- Create root relative symbolic links `AGENTS.md -> README.md` and
  `CLAUDE.md -> README.md` as separate paths at execution time. There are no
  AGENTS or CLAUDE templates.
- Before creating either link, inspect that exact path. Leave an existing
  symlink to `README.md` unchanged. If a regular file or a link to another
  target exists, preserve its unique instructions by merging them into the
  README before replacing it with the requested link. If safe preservation is
  uncertain, do not replace it; report the conflict. Never make a broken link.
- Use relative symlink targets. On POSIX use `ln -s README.md AGENTS.md` and
  `ln -s README.md CLAUDE.md`; on Windows use the equivalent symbolic-link
  operation. If the platform cannot create symlinks, report that constraint;
  do not silently substitute copied files. Remove links to absent aliases from
  `README.md` so it has no broken links, and report the missing aliases.

## Default documentation set

Always create or refresh, preserving existing content:

- Root `README.md`, plus the two agent-entry symbolic links described above.
- `docs/PRD.md` with `$prd`.
- `docs/structure.md` — verified directory tree and active component map.
- `docs/decisions.md` — confirmed decisions distinguished from observations.
- `docs/security.md` with `$security` — modular, evidence-based security
  posture.

Do not create or refresh `docs/tests.md` by default. Use `$tests` only when
the user asks for test creation, test strategy, test documentation, or
`docs/tests.md` specifically. Do not add fake test commands to other files.

Create `docs/design.md` with `$design` only when a rendered UI exists. Create
`docs/rules.md` and `docs/style.md` only when repository evidence makes them
useful; `docs/usage.md` only when verified usage commands exist;
`docs/Architecture.md` only for material component, data-flow, deployment, or
pipeline complexity. Every generated Architecture document must include at
least one compact, verified high-level diagram. Use `TB` for flowcharts by
default; add workflow, sequence, or mind-map diagrams only when they clarify
verified behavior, and split large views for normal GitHub / Markdown preview
readability. Follow the full rules in
[`references/architecture/mermaid-standard.md`](./references/architecture/mermaid-standard.md).
Create tasks or memory documents only when requested or clearly useful to
ongoing work.

## Empty or scaffold-only repositories

When there is no application source or meaningful build/deployment
configuration, create the initial documentation set above. Mark unknowns as
`Not decided`, `Not documented`, or `Not assessed`. State that no runtime,
tests, deployment, or workflow has been selected when that is true. Do not
invent product goals, personas, requirements, architecture, security controls,
test commands, or decisions. Record `No decisions recorded yet` where
appropriate. A test document remains opt-in through `$tests`.

If there is an existing security or cryptographic implementation, do not
prescribe new algorithms as part of documentation bootstrap; `$security`
handles its applicable profile and migration assessment.

## Evidence and readability

- Derive current behavior from code, manifests, tests, workflows, deployment
  and security configuration, and the actual tree. Markdown is useful for
  history and ID continuity, not proof that behavior is active.
- Verify filenames, commands, workflow triggers, and targets. Exclude dead or
  obsolete implementation from product and architecture summaries; perform
  code cleanup only when `$code-quality` is requested.
- Write for product, engineering, security, operations, and leadership
  readers: lead with a plain-language summary, expand acronyms, separate
  evidence from observations and unknowns, and use concise tables for detail.
- Link only to files that exist. Keep generated project documentation under
  `docs/`, except root `README.md` and its two symbolic links. Copy linked
  style and architecture references to `docs/references/style/` and
  `docs/references/architecture/` respectively.

## Workflow

1. Inventory the repository and inspect active source/configuration.
1. Check each output and agent-link path; preserve existing content and IDs.
1. Create only the default documents and conditional documents that apply.
   Invoke dedicated skills for PRD, security, design, or requested test/code
   quality tasks. If a required companion is not installed, finish common
   documents, omit that companion-owned output, and report what is missing;
   do not imitate a specialist skill from stale or incomplete instructions.
1. Copy absent starter configurations only after tailoring them to the actual
   stack and tools.
1. Update the README index to include generated documents and omit skipped
   optional documents.
1. Verify uppercase `README.md`, valid relative links, relative symlink
   targets, requirement-ID continuity, and absence of unresolved placeholders
   with [checklist.md](./checklist.md).

## Resources

- `templates/` — common project-document templates; the only root entry
  template is `README.md`.
- `files/` — EditorConfig, Git attributes, and pre-commit starters.
- `references/style/` — adaptable language references.
- `references/architecture/mermaid-standard.md` — Mermaid theme reference.
- `checklist.md` — pre-delivery review.
