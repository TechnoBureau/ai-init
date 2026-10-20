# Pre-Delivery Review

Use this checklist before reporting documentation work as complete. A checked
item means it was verified in the current worktree, not assumed.

## Evidence and preservation

- [ ] Inspected source code, manifests, tests, workflows, deployment, and
  security configuration before using existing Markdown for context.
- [ ] Recorded the reviewed commit SHA and inspection date in each generated
  document or its control block.
- [ ] Checked every destination before writing; existing content and
  permanent IDs are preserved rather than replaced wholesale.
- [ ] If a lowercase root `readme.md` exists, its content was reviewed and
  deliberately preserved or migrated into uppercase `README.md`; no new
  lowercase README was created.
- [ ] If `docs/Architecture.md` existed, it was migrated to
  `docs/architecture.md` with content and links preserved; no duplicate index
  remains.
- [ ] Empty/scaffold-only repositories use the initial-document format and
  mark unknowns explicitly rather than inventing a stack, goals, tests,
  controls, commands, or architecture.
- [ ] Verified active scripts, commands, file paths, workflow triggers, and
  targets directly from repository files.
- [ ] Existing or unreferenced code is not described as active product
  behavior; relevant exclusions are explained.

## Standard document controls

- [ ] Every generated document starts with a control line: owner (or
  `Not documented`), status, SemVer version, last-reviewed date,
  classification, and source of truth.
- [ ] Status is `Draft` unless a human review or approval is recorded.
- [ ] Claims are labeled `Verified`, `Observed`, `Planned`, `Not documented`, or
  `Not assessed` as appropriate.
- [ ] RFC 2119/8174 keywords are used only for real requirements; ordinary prose
  does not masquerade as normative.
- [ ] Document classes are not mixed: tutorial, how-to, reference, and
  explanation have distinct purposes and cross-links.
- [ ] Filenames follow the naming rule: root meta files uppercase, `docs/`
  lowercase kebab-case, `PRD.md` as the recorded acronym exception.

## Root README and agent links

- [ ] Root `README.md` is the shared summary and index for humans and AI,
  summarizes goals from `docs/PRD.md`, and links to root `AGENTS.md` and
  `CLAUDE.md`.
- [ ] Root `AGENTS.md` and `CLAUDE.md` are relative symbolic links to
  `README.md` where supported; substantive conflicts are preserved/reported,
  and README contains no links to aliases that could not be created.
- [ ] No nested `AGENTS.md` was invented; any existing agent instruction
  hierarchy is preserved.

## PRD and traceability

- [ ] PRD is at `docs/PRD.md` and has exactly the required ten sections in
  order: Overview; Product Type; Goals and Objectives; Scope; Architectural
  Decisions; User Personas; Functional Requirements; Non-Functional
  Requirements; Pipeline / Workflow Inventory; Repository Structure.
- [ ] Permanent G-, D-, FR-, and NFR-IDs are preserved; no priority tiers
  appear in the PRD; each NFR has a verifiable criterion.
- [ ] Each FR/NFR has acceptance criteria and a verification method, and
  traceability links resolve or gaps are stated.
- [ ] Requirement text is atomic, unambiguous, normative where applicable, and
  free of invented thresholds.
- [ ] PRD pipeline filenames, triggers, targets, and repository tree match
  actual configuration and files.
- [ ] Security, privacy, accessibility, reliability, and observability
  implications were considered; unconfirmed targets are not invented.

## Supporting documents

- [ ] `docs/structure.md`, `docs/decisions.md`, and `docs/security.md`
  reflect inspected evidence and do not invent facts.
- [ ] Decisions use context, decision, consequences, alternatives, status,
  owner, date, and supersession; retired IDs are not recycled.
- [ ] `docs/tests.md` was not created or refreshed by default; a pre-existing
  file is preserved, and requested test documentation is handled by `tests`.
- [ ] `docs/design.md` exists only when the project has a rendered UI and
  records accessibility evidence without claiming unverified conformance.
- [ ] Every generated project document other than root `README.md` and its
  root-level `AGENTS.md` / `CLAUDE.md` symbolic links is under `docs/`.

## Security and compliance integrity

- [ ] Security modules are scoped to repository evidence; NIST/ISO/OWASP/CIS
  mappings are not presented as certification, compliance, or proof of
  security.
- [ ] Design, implementation, and operating-effectiveness claims are
  distinguished; repository review is not described as an audit.
- [ ] If cryptography is in scope, the inventory and migration profile
  distinguish current algorithms from proposed targets; FIPS algorithm
  specifications are not confused with FIPS 140-3 module validation.
- [ ] Any algorithm switching or fallback is tied to approved configuration,
  versioning, downgrade resistance, staged verification, and bounded fallback
  rules; no fallback or crypto migration was applied without authorization.
- [ ] If OpenSCAP/SCAP or CIS hardening applies, the exact platform, profile,
  content/tool version, findings, exceptions, and remediation evidence are
  identified. A scan alone is not presented as hardening or compliance.
- [ ] Exceptions include owner, rationale, compensating control, expiry, and
  review date, or are marked unknown.
- [ ] No secrets, private keys, tokens, customer records, or unredacted
  personal data appear in any generated document.

## Code, style, and tooling

- [ ] Code-quality recommendations favor cohesive modules, narrow interfaces,
  focused functions, and useful contract comments for non-obvious inputs,
  outputs, errors, side effects, and security assumptions.
- [ ] Dead-code removal is performed only when requested and supported by
  static or call-path evidence; dynamic entry points and public contracts
  were checked before removal.
- [ ] Style references are included only for languages actually used and
  copied under `docs/references/style/` when linked.
- [ ] Style guidance is presented as an adaptable baseline, not as a
  repository-enforced rule unless matching configuration or CI evidence
  exists.
- [ ] Coding standards reflect repository instructions, language needs, and
  configured tools; recommendations are distinguished from existing rules.
- [ ] Applicable `.editorconfig`, `.gitattributes`, and
  `.pre-commit-config.yaml` are copied to the target repository root.
- [ ] Pre-commit hooks match the target languages/tools, and required tools or
  baseline files are identified.
- [ ] YAML frontmatter and machine-readable metadata were not reformatted as
  Markdown.

## Readability and links

- [ ] No unresolved `{{PLACEHOLDER}}` tokens remain. `TBD` and
  `Not documented` are used only where repository or confirmed product
  evidence is missing.
- [ ] Relative links resolve to files actually generated; links to skipped
  docs were removed.
- [ ] The README index matches the documents that exist.
- [ ] Every Mermaid diagram begins with the exact block in
  `references/architecture/mermaid-standard.md`; it is copied into
  `docs/references/architecture/` when generated docs link to it.
- [ ] A generated `docs/architecture.md` has at least one compact, verified
  high-level diagram; flowcharts default to `TB`, and optional workflow,
  sequence, or mind-map diagrams are included only when they clarify real
  repository behavior.
- [ ] Diagrams use short labels and one concern per view, are readable at
  normal GitHub / Markdown preview size, and are split rather than overloaded
  when large; no diagram adds unverified components or relationships.
- [ ] Documents use one H1, sequential headings, descriptive link text, alt
  text for meaningful images, and table header rows; meaning is not conveyed
  by color alone.
- [ ] Acronyms are expanded at first use and the summary is understandable to
  a non-specialist stakeholder.

## Final report

- [ ] Report unresolved `TBD`s, missing companion skills, and security
  controls not detected in the repository to the user.
- [ ] Report any path that could not be created or migrated, with the reason.
