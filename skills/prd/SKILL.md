______________________________________________________________________

## name: prd description: > Create or refine a concise, implementation-grounded Product Requirements Document with permanent G-, D-, FR-, and NFR-IDs. Use when a repository PRD is requested or when AI Init is documenting a product repository.

# Product Requirements

Produce `docs/PRD.md` from the repository's actual implementation and
confirmed product context. Keep it useful to product, engineering, security,
operations, and leadership readers.

## Before writing

- Inspect code, manifests, build and deployment configuration, CI workflows,
  tests, and the repository tree before treating existing Markdown as facts.
- Check whether `docs/PRD.md` exists. If it does, read it fully and preserve
  valid permanent IDs and useful user-authored content; update it in place
  rather than replacing it wholesale.
- Use prior Markdown only for ID history, confirmed decisions, and context.
  Verify all claims about current behavior against source/configuration.
- For an empty or scaffold-only repository, use the standard ten-section
  structure and clearly label unknowns `Not decided` or `TBD`. Do not invent
  users, goals, features, architecture, workflows, or targets. If no goal,
  requirement, decision, persona, or workflow is confirmed, say none is
  recorded instead of assigning a filler ID.

## Required document structure

Use exactly these ten numbered sections, in this order:

1. **Overview** — concise summary, evidenced problem, and value proposition.
1. **Product Type** — internal DevOps platform, service, library, app, or the
   closest type supported by repository evidence.
1. **Goals and Objectives** — measurable outcomes with permanent G-IDs.
   Include only confirmed or evidence-based goals; use `TBD` where a real
   goal has no defensible measure. If there are no confirmed goals, say so
   without inventing a G-ID.
1. **Scope** — separate `In Scope` and `Out of Scope` lists.
1. **Architectural Decisions** — a single table with permanent D-IDs,
   Decision, Reason, and Alternatives Rejected. Mark missing rationale or
   alternatives `Not documented`.
1. **User Personas** — target audience, responsibilities, and needs grounded
   in repository or confirmed product context.
1. **Functional Requirements** — group by real module; assign permanent
   FR-IDs and include concise verification/evidence. Do not add priority tiers.
1. **Non-Functional Requirements** — assign permanent NFR-IDs and define a
   concrete verification criterion for each. Do not invent numeric targets.
1. **Pipeline / Workflow Inventory** — table of exact filenames, configured
   triggers, and targets.
1. **Repository Structure** — concise tree of existing primary directories
   and key components.

Keep only these numbered sections. Avoid repeated decision tables, speculative
roadmaps, priority labels, filler, or open questions already resolved by
source or the user. Preserve existing IDs; never recycle retired IDs.

## Readability and evidence

- Start each section with plain-language statements, then add technical detail
  and evidence paths where useful.
- Expand acronyms at first use. Prefer concise sentences and tables over dense
  prose.
- Distinguish implemented behavior, confirmed plans, and unknowns.
- Do not claim a requirement is implemented solely because it appears in an
  old PRD or README.
- Use `README.md` with uppercase spelling in all links and references.
- Keep relative links valid and include only documents that exist.

Use [templates/PRD.md](./templates/PRD.md) as the structure. The companion
security skill owns the detailed security posture at `docs/security.md`.

## README agent-entry links

After this skill runs, if root `README.md` exists, ensure
`AGENTS.md` and `CLAUDE.md` are relative symbolic links to it. Inspect each
path first. Preserve regular files or links to other targets; merge unique
instructions into the README before replacing only when safe. If preservation
is uncertain or symlink creation is unsupported, do not replace the path and
report the conflict. Never create broken links or copied-file substitutes;
remove README links to absent aliases and report the missing links.
Update the README's documentation index to include `docs/PRD.md`. If README
is absent, report that `ai-init` is needed to create the shared index.
