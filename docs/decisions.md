# Decisions — AI Init Skills

This is the supporting register for the D-IDs summarized in
[docs/PRD.md](./PRD.md). IDs are permanent; superseded decisions are marked,
never renumbered or deleted.

## Decision Index

| ID | Decision | Status | Date | Owner | Evidence |
|---|---|---|---|---|---|
| D-1 | Publish six focused skills instead of one monolith | Accepted | 2026-10-20 | TechnoBureau | `skills/` |
| D-2 | Follow the open Agent Skills specification with YAML frontmatter | Accepted | 2026-10-20 | TechnoBureau | `docs/skill-standard.md` |
| D-3 | Enforce the format with a validator, not reviewer attention | Accepted | 2026-10-20 | TechnoBureau | `scripts/validate_skills.py` |
| D-4 | Keep `SKILL.md` small and move detail into `references/` | Accepted | 2026-10-20 | TechnoBureau | Progressive-disclosure limits in the validator |
| D-5 | Mirror output paths inside every `templates/` tree | Accepted | 2026-10-20 | TechnoBureau | `skills/*/templates/` |
| D-6 | Generate repository meta files only from confirmed facts | Accepted | 2026-10-20 | TechnoBureau | `skills/ai-init/SKILL.md`, `references/licensing.md` |
| D-7 | Use lowercase kebab-case under `docs/` with `PRD.md` as the exception | Accepted | 2026-10-20 | TechnoBureau | This folder |
| D-8 | Keep this repository's `docs/` as generated output, not hand-written prose | Accepted | 2026-10-20 | TechnoBureau | `tests/test_working_example.py` |
| D-9 | No changelog or release numbering at the initial state | Accepted | 2026-10-20 | TechnoBureau | `docs/governance.md` |

## Decision Records

### D-1 — Publish six focused skills instead of one monolith

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Repository documentation, requirements, security, tests, design,
  and code quality are different tasks with different trigger phrases. A single
  skill would either load irrelevant instructions on every activation or grow
  past the recommended size.
- **Decision:** Ship six independently installable skills that share standards
  but no runtime files: `ai-init`, `prd`, `security`, `tests`, `design`, and
  `code-quality`.
- **Consequences:** Each skill can be installed alone, so no skill may depend
  on another skill's reference file at load time. `ai-init` coordinates the
  default documentation set and routes specialist work.
- **Reason:** Progressive disclosure and independent installation.
- **Alternatives rejected:** One monolithic skill — rejected for size and
  irrelevant context; nested skills — rejected because installers do not treat
  nested directories as separate skills.
- **Evidence:** `skills/*/SKILL.md`, `README.md` skill table.
- **Supersedes / superseded by:** None.

### D-2 — Follow the open Agent Skills specification with YAML frontmatter

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Skill files must be discoverable by multiple agent hosts and the
  Skills CLI. Discovery depends entirely on `name` and `description` in YAML
  frontmatter.
- **Decision:** Conform to Agent Skills 1.0 and add an enterprise metadata
  block (`spec`, `standards`, `risk`).
- **Consequences:** Frontmatter is machine-readable data and must never be
  reformatted as prose. Values must be quoted strings.
- **Reason:** Cross-host portability and reliable retrieval.
- **Alternatives rejected:** Vendor-specific formats — rejected for lock-in;
  frontmatter-free Markdown — rejected because skills would be undiscoverable.
- **Evidence:** `docs/skill-standard.md`, `scripts/validate_skills.py`.
- **Supersedes / superseded by:** None.

### D-3 — Enforce the format with a validator, not reviewer attention

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** A Markdown formatter can silently convert `---` into a
  horizontal rule and collapse `name`/`description` into a heading. The file
  still renders plausibly, so human review does not reliably catch it.
- **Decision:** Validate frontmatter, metadata, links, size, and eval coverage
  in pre-commit, in CI, and in unit tests.
- **Consequences:** Contributors get fast local feedback, and CI is
  authoritative because hooks can be skipped.
- **Reason:** The failure is structural, so the control must be automated.
- **Alternatives rejected:** Documentation-only guidance — rejected as
  unenforceable; a Markdown linter alone — rejected because it does not
  validate the schema.
- **Evidence:** `scripts/validate_skills.py`, `tests/test_validate_skills.py`,
  `.github/workflows/validate.yml`.
- **Supersedes / superseded by:** None.

### D-4 — Keep `SKILL.md` small and move detail into `references/`

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** An activated skill consumes context. Long standards in the entry
  point crowd out the task itself.
- **Decision:** Cap the body at 500 lines and roughly 5,000 tokens, and move
  detailed standards into `references/` loaded on demand.
- **Consequences:** The validator rejects oversized entry points. Reference
  material must stay self-contained because a skill may be installed alone.
- **Reason:** Progressive disclosure, D-2.
- **Alternatives rejected:** Everything inline — rejected for context cost;
  external website — rejected because offline agents could not load it.
- **Evidence:** `scripts/validate_skills.py` limits; current bodies are
  155–241 lines.
- **Supersedes / superseded by:** None.

### D-5 — Mirror output paths inside every `templates/` tree

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Flat template directories produced ambiguous names such as
  `docs-README.md` next to a root `README.md`, and an agent could not tell which
  output path a template targeted.
- **Decision:** `templates/docs/x.md` produces `docs/x.md`; `templates/root/x`
  produces `x` at the repository root. `.github/CODEOWNERS` is the recorded
  exception and is named `templates/root/CODEOWNERS`.
- **Consequences:** Adding a template requires creating the directory that
  matches its output. The naming hack disappears.
- **Reason:** Self-documenting mapping, fewer generation errors.
- **Alternatives rejected:** A manifest file mapping templates to outputs —
  rejected as another artifact to keep in sync; flat names with a prefix —
  rejected because it caused the `docs-README.md` duplication.
- **Evidence:** `skills/*/templates/`, D-8.
- **Supersedes / superseded by:** None.

### D-6 — Generate repository meta files only from confirmed facts

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** `LICENSE`, `CODEOWNERS`, `SECURITY.md`, and `CODE_OF_CONDUCT.md`
  carry legal or routing consequences. A guessed licence, owner handle, or
  contact address is worse than a missing file.
- **Decision:** Create these files only when the licence, owner, enforcement
  contact, or security channel is confirmed. Otherwise skip the file and
  report the gap.
- **Consequences:** Some generated repositories will contain fewer meta files,
  with an explicit report explaining what is missing and who must decide.
- **Reason:** Fabrication risk is asymmetric; wrong legal or routing data
  causes real harm.
- **Alternatives rejected:** Best-guess defaults — rejected as unsafe;
  placeholder contacts — rejected because they ship broken channels.
- **Evidence:** `skills/ai-init/SKILL.md`, `references/licensing.md`,
  `skills/ai-init/checklist.md`.
- **Supersedes / superseded by:** None.

### D-7 — Use lowercase kebab-case under `docs/` with `PRD.md` as the exception

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Mixed-case document names such as `docs/Architecture.md` break
  links on case-sensitive hosts when written in lowercase.
- **Decision:** Documents under `docs/` use lowercase kebab-case; `PRD.md`
  keeps its established acronym spelling.
- **Consequences:** Existing mixed-case files are migrated with a case-safe
  two-step rename and their links updated.
- **Reason:** Portability across case-sensitive and case-insensitive
  filesystems.
- **Alternatives rejected:** All uppercase — rejected as noisy; preserving
  mixed case — rejected because of link breakage.
- **Evidence:** `docs/` naming, `skills/ai-init/SKILL.md` migration rule.
- **Supersedes / superseded by:** None.

### D-8 — Keep this repository's `docs/` as generated output

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** The collection documents how to produce a document set, but a
  reader could not see the result. Hand-written documents were also drifting
  from the templates.
- **Decision:** Generate this repository's own `docs/` from
  `skills/*/templates/` and enforce the correspondence with a test.
- **Consequences:** A template change requires regenerating the matching
  document. `tests/test_working_example.py` fails when a template has no
  generated counterpart.
- **Reason:** Dogfooding, reviewable output, no template drift.
- **Alternatives rejected:** A separate example repository — rejected because
  it duplicates maintenance and is not exercised by CI here.
- **Evidence:** `docs/`, `tests/test_working_example.py`.
- **Supersedes / superseded by:** None.

### D-9 — No changelog or release numbering at the initial state

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** The collection is at its first published state. Maintaining a
  changelog and per-skill versions adds coordination cost without a release
  process to support them.
- **Decision:** Do not maintain `CHANGELOG.md` or `metadata.version`. Change
  history lives in Git and the pull request.
- **Consequences:** Deprecations are announced in `SKILL.md` and the README. If
  releases are later adopted, the version scheme must be defined in
  governance first.
- **Reason:** Avoid version churn that no process consumes.
- **Alternatives rejected:** Semantic Versioning per skill — rejected as
  premature; a single repository version — rejected for the same reason.
- **Evidence:** `docs/governance.md`, `docs/skill-standard.md`.
- **Supersedes / superseded by:** None.

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Structure](./structure.md)
