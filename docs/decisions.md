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
| D-10 | Generated documents carry no branch, revision, or tool-version provenance | Accepted | 2026-10-20 | TechnoBureau | `tests/test_working_example.py` |
| D-11 | Ship one merged `.gitignore` baseline, not per-language fragments | Accepted | 2026-10-20 | TechnoBureau | `skills/ai-init/files/.gitignore` |
| D-12 | Ship an IBM detect-secrets baseline with keyword scanning off | Accepted | 2026-10-20 | TechnoBureau | `.secrets.baseline` |
| D-13 | Pin hooks and actions by version tag, not commit SHA | Accepted | 2026-10-20 | TechnoBureau | `.pre-commit-config.yaml` |

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

### D-10 — Generated documents carry no branch, revision, or tool-version provenance

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Generated documents opened with an evidence-base line naming a
  working branch, `HEAD`, and scanner versions. The line goes stale as soon as
  the branch moves, duplicates what Git already records, and implies the
  document is bound to one snapshot.
- **Decision:** Do not emit an evidence-base header, and do not name a branch,
  revision, or tool version as document provenance. Claims cite the path,
  command, or result that supports them; change history stays in Git and the
  pull request.
- **Consequences:** Documents describe current behavior rather than the
  snapshot they were generated from. Reviewers verify the worktree; the pull
  request records what changed.
- **Reason:** Provenance that duplicates Git rots immediately and creates false
  precision about when a document was last correct.
- **Alternatives rejected:** Keeping a revision in a footer instead of a
  header — rejected as the same stale metadata in a different position.
- **Evidence:** `tests/test_working_example.py`,
  `skills/ai-init/references/documentation-standard.md`.
- **Supersedes / superseded by:** None.

### D-11 — Ship one merged `.gitignore` baseline, not per-language fragments

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Repositories mix C, C++, Go, shell, Python, Node.js tooling, and
  editors. Separate per-language ignore files multiply maintenance and leave
  gaps; a single uncommented dump hides rules that contributors cannot safely
  delete.
- **Decision:** Ship one commented baseline in `files/.gitignore`, grouped by
  ecosystem. Copy it when absent; merge missing sections when one exists, and
  never remove an entry the maintainers added.
- **Consequences:** One file to review, and section comments make each rule
  auditable. Unusual build output must be tailored. A pattern that hides a
  tracked file is caught by `git ls-files -ci --exclude-standard`.
- **Reason:** A merged baseline is reviewable and avoids the composition order,
  duplicate patterns, and empty sections of generated fragments.
- **Alternatives rejected:** Per-language fragments assembled at generation
  time — rejected because ordering and duplicates become another thing to
  test. A single uncommented dump — rejected because contributors cannot tell
  which rules are safe to remove.
- **Evidence:** `skills/ai-init/files/.gitignore`,
  `skills/ai-init/references/gitignore-standard.md`,
  `tests/test_working_example.py`.
- **Supersedes / superseded by:** None.

### D-12 — Ship an IBM detect-secrets baseline with keyword scanning off

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** gitleaks covers regular-expression and entropy patterns but has
  no audited baseline or provider plugins. The IBM detect-secrets keyword
  detector flags ordinary prose such as `password: example`, and dependency
  lockfiles are full of high-entropy hashes, so a default scan produces noise
  that reviewers learn to ignore.
- **Decision:** Ship one `.secrets.baseline` for IBM detect-secrets 0.13.1 with
  the keyword detector omitted, dependency and generated paths excluded, and no
  findings. Wire the hook with `--baseline` and `--no-keyword-scan`, pinned by
  commit, and keep gitleaks as the complementary gate.
- **Consequences:** Keyword-only secrets are not detected by this scanner; the
  reference records that trade-off and keeps provider and entropy detectors on.
  Two scanners must be maintained. Tests pin the policy so a regenerated
  baseline cannot silently re-enable keyword scanning.
- **Reason:** Signal quality matters more than rule count: a scanner reviewers
  trust is a control, and a noisy scanner is a ritual.
- **Alternatives rejected:** Keyword detector with a broad exclusion regex —
  rejected as brittle and hard to review. Excluding `tests/` wholesale —
  rejected because a real key pasted into a fixture is the accident the scanner
  exists to catch. Replacing gitleaks — rejected because it scans history and
  detects patterns detect-secrets does not.
- **Evidence:** `skills/ai-init/files/.secrets.baseline`,
  `skills/ai-init/references/secret-scanning.md`,
  `tests/test_secret_scanning.py`.
- **Supersedes / superseded by:** None.

### D-13 — Pin hooks and actions by version tag, not commit SHA

- **Status:** Accepted
- **Date:** 2026-10-20
- **Owner:** TechnoBureau
- **Context:** Commit-SHA pins are immutable but unreadable: a reviewer cannot
  tell which release a hash refers to, and every automated update shows up as
  an opaque hash change. The IBM detect-secrets fork publishes version tags
  such as `0.13.1+ibm.64.dss` that carry the upstream and fork revisions.
- **Decision:** Pin every remote pre-commit hook and GitHub Action by exact
  version tag. Do not float branches, and do not use raw commit SHAs in the
  configuration. Keep Dependabot enabled for Actions, pre-commit, and pip so
  updates arrive as reviewable pull requests.
- **Consequences:** Pins are readable and match a release note. A tag is a
  mutable reference, so an upstream could move it; review the diff and the
  upstream release on every update, and keep the CI token read-only. A
  repository that requires immutability can still pin a SHA for a specific
  hook, but then it must record why.
- **Reason:** Reviewers act on readable references. An unreadable pin gets
  rubber-stamped, which is a weaker control than a tag that is actually read.
- **Alternatives rejected:** SHA pins with the version in a trailing comment —
  rejected because the comment drifts and the hash stays authoritative.
  Branch pins — rejected as unreviewable and unauditable.
- **Evidence:** `.pre-commit-config.yaml`, `.github/workflows/validate.yml`,
  `tests/test_pinning.py`.
- **Supersedes / superseded by:** None.

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Structure](./structure.md)
