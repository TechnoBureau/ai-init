# Pre-Delivery Review

- [ ] Inspected source code, manifests, tests, workflows, deployment, and
  security configuration before using existing Markdown for context.
- [ ] Checked every destination before writing; existing content and
  permanent IDs are preserved rather than replaced wholesale.
- [ ] If a lowercase root `readme.md` exists, its content was reviewed and
  deliberately preserved or migrated into uppercase `README.md`; no new
  lowercase README was created.
- [ ] Empty/scaffold-only repositories use the initial-document format and
  mark unknowns explicitly rather than inventing a stack, goals, tests,
  controls, commands, or architecture.
- [ ] Verified active scripts, commands, file paths, workflow triggers, and
  targets directly from repository files.
- [ ] Existing or unreferenced code is not described as active product
  behavior; relevant exclusions are explained.
- [ ] Root `README.md` is the shared summary and index for humans and AI,
  summarizes goals from `docs/PRD.md`, and links to root `AGENTS.md` and
  `CLAUDE.md`.
- [ ] Root `AGENTS.md` and `CLAUDE.md` are relative symbolic links to
  `README.md` where supported; substantive conflicts are preserved/reported,
  and README contains no links to aliases that could not be created.
- [ ] PRD is at `docs/PRD.md` and has exactly the required ten sections in
  order: Overview; Product Type; Goals and Objectives; Scope; Architectural
  Decisions; User Personas; Functional Requirements; Non-Functional
  Requirements; Pipeline / Workflow Inventory; Repository Structure.
- [ ] Permanent G-, D-, FR-, and NFR-IDs are preserved; no priority tiers
  appear in the PRD; each NFR has a verifiable criterion.
- [ ] PRD pipeline filenames, triggers, targets, and repository tree match
  actual configuration and files.
- [ ] `docs/structure.md`, `docs/decisions.md`, and `docs/security.md`
  reflect inspected evidence and do not invent facts.
- [ ] `docs/tests.md` was not created or refreshed by default; a pre-existing
  file is preserved, and requested test documentation is handled by `tests`.
- [ ] Security modules are scoped to repository evidence; NIST/OWASP mappings
  are not presented as certification, compliance, or proof of security.
- [ ] If cryptography is in scope, the inventory and migration profile
  distinguish current algorithms from proposed targets; FIPS algorithm
  specifications are not confused with FIPS 140-3 module validation.
- [ ] Any algorithm switching or fallback is tied to approved configuration,
  versioning, downgrade resistance, staged verification, and bounded fallback
  rules; no fallback or crypto migration was applied without authorization.
- [ ] If OpenSCAP/SCAP or CIS hardening applies, the exact platform, profile,
  content/tool version, findings, exceptions, and remediation evidence are
  identified. A scan alone is not presented as hardening or compliance.
- [ ] Code-quality recommendations favor cohesive modules, narrow interfaces,
  focused functions, and useful contract comments for non-obvious inputs,
  outputs, errors, side effects, and security assumptions.
- [ ] Dead-code removal is performed only when requested and supported by
  static or call-path evidence; dynamic entry points and public contracts
  were checked before removal.
- [ ] `docs/design.md` exists only when the project has a rendered UI.
- [ ] Every generated project document other than root `README.md` and its
  root-level `AGENTS.md` / `CLAUDE.md` symbolic links is under `docs/`.
- [ ] No unresolved `{{PLACEHOLDER}}` tokens remain. `TBD` and
  `Not documented` are used only where repository or confirmed product
  evidence is missing.
- [ ] Every Mermaid diagram begins with the exact block in
  `references/architecture/mermaid-standard.md`; copy it into
  `docs/references/architecture/` when generated docs link to it.
- [ ] A generated `docs/Architecture.md` has at least one compact, verified
  high-level diagram; flowcharts default to `TB`, and optional workflow,
  sequence, or mind-map diagrams are included only when they clarify real
  repository behavior.
- [ ] Diagrams use short labels and one concern per view, are readable at
  normal GitHub / Markdown preview size, and are split rather than overloaded
  when large; no diagram adds unverified components or relationships.
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
- [ ] Relative links resolve to files actually generated; remove links to
  skipped docs.
- [ ] Report unresolved `TBD`s and security controls not detected in the
  repository to the user.
