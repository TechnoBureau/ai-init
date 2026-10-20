# Decisions

This is the supporting register for the D-IDs summarized in
[docs/PRD.md](./PRD.md). IDs are permanent and records are never renumbered
or deleted. When a record is replaced, the new record names the one it
replaces; there is no separate status field to maintain.

## Decision Index

| ID | Decision |
|---|---|
| D-1 | Publish six focused skills instead of one monolith |
| D-2 | Follow the open Agent Skills specification with YAML frontmatter |
| D-3 | Enforce the format with a validator, not reviewer attention |
| D-4 | Keep `SKILL.md` small and move detail into `references/` |
| D-5 | Mirror output paths inside every `templates/` tree |
| D-6 | Generate repository meta files only from confirmed facts |
| D-7 | Use lowercase kebab-case under `docs/` with `PRD.md` as the exception |
| D-8 | Keep this repository's `docs/` as generated output, not hand-written prose |
| D-9 | No changelog or release numbering at the initial state |
| D-10 | Generated documents carry no branch, revision, or tool-version provenance |
| D-11 | Ship one merged `.gitignore` baseline, not per-language fragments |
| D-12 | Ship an IBM detect-secrets baseline with keyword scanning off |
| D-13 | Pin hooks and actions by version tag, not commit SHA |
| D-14 | Documents describe current state and link the owner of each value |
| D-15 | Documents carry no bookkeeping metadata |
| D-16 | Titles name the document type, and template links resolve in the output |
| D-17 | Templates name documents instead of linking them |

## Decision Records

### D-1 — Publish six focused skills instead of one monolith

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

### D-2 — Follow the open Agent Skills specification with YAML frontmatter

- **Context:** Skill files must be discoverable by multiple agent hosts and the
  Skills CLI. Discovery depends entirely on `name` and `description` in YAML
  frontmatter.
- **Decision:** Conform to Agent Skills 1.0 and add an enterprise metadata
  block (`spec`, `standards`, `risk`).
- **Consequences:** Frontmatter is machine-readable data and must never be
  reformatted as prose. Values must be quoted strings.
- **Reason:** Cross-host portability and reliable retrieval.

### D-3 — Enforce the format with a validator, not reviewer attention

- **Context:** A Markdown formatter can silently convert `---` into a
  horizontal rule and collapse `name`/`description` into a heading. The file
  still renders plausibly, so human review does not reliably catch it.
- **Decision:** Validate frontmatter, metadata, links, size, and eval coverage
  in pre-commit, in CI, and in unit tests.
- **Consequences:** Contributors get fast local feedback, and CI is
  authoritative because hooks can be skipped.
- **Reason:** The failure is structural, so the control must be automated.

### D-4 — Keep `SKILL.md` small and move detail into `references/`

- **Context:** An activated skill consumes context. Long standards in the entry
  point crowd out the task itself.
- **Decision:** Cap the body at 500 lines and roughly 5,000 tokens, and move
  detailed standards into `references/` loaded on demand.
- **Consequences:** The validator rejects oversized entry points. Reference
  material must stay self-contained because a skill may be installed alone.
- **Reason:** Progressive disclosure, D-2.

### D-5 — Mirror output paths inside every `templates/` tree

- **Context:** Flat template directories produced ambiguous names such as
  `docs-README.md` next to a root `README.md`, and an agent could not tell which
  output path a template targeted.
- **Decision:** `templates/docs/x.md` produces `docs/x.md`; `templates/root/x`
  produces `x` at the repository root. `.github/CODEOWNERS` is the recorded
  exception and is named `templates/root/CODEOWNERS`.
- **Consequences:** Adding a template requires creating the directory that
  matches its output. The naming hack disappears.
- **Reason:** Self-documenting mapping, fewer generation errors.

### D-6 — Generate repository meta files only from confirmed facts

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

### D-7 — Use lowercase kebab-case under `docs/` with `PRD.md` as the exception

- **Context:** Mixed-case document names such as `docs/Architecture.md` break
  links on case-sensitive hosts when written in lowercase.
- **Decision:** Documents under `docs/` use lowercase kebab-case; `PRD.md`
  keeps its established acronym spelling.
- **Consequences:** Existing mixed-case files are migrated with a case-safe
  two-step rename and their links updated.
- **Reason:** Portability across case-sensitive and case-insensitive
  filesystems.

### D-8 — Keep this repository's `docs/` as generated output

- **Context:** The collection documents how to produce a document set, but a
  reader could not see the result. Hand-written documents were also drifting
  from the templates.
- **Decision:** Generate this repository's own `docs/` from
  `skills/*/templates/` and enforce the correspondence with a test.
- **Consequences:** A template change requires regenerating the matching
  document. `tests/test_working_example.py` fails when a template has no
  generated counterpart.
- **Reason:** Dogfooding, reviewable output, no template drift.

### D-9 — No changelog or release numbering at the initial state

- **Context:** The collection is at its first published state. Maintaining a
  changelog and per-skill versions adds coordination cost without a release
  process to support them.
- **Decision:** Do not maintain `CHANGELOG.md` or `metadata.version`. Change
  history lives in Git and the pull request.
- **Consequences:** Deprecations are announced in `SKILL.md` and the README. If
  releases are later adopted, the version scheme must be defined in
  governance first.
- **Reason:** Avoid version churn that no process consumes.

### D-10 — Generated documents carry no branch, revision, or tool-version provenance

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

### D-11 — Ship one merged `.gitignore` baseline, not per-language fragments

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

### D-12 — Ship an IBM detect-secrets baseline with keyword scanning off

- **Context:** gitleaks covers regular-expression and entropy patterns but has
  no audited baseline or provider plugins. The IBM detect-secrets keyword
  detector flags ordinary prose such as `password: example`, and dependency
  lockfiles are full of high-entropy hashes, so a default scan produces noise
  that reviewers learn to ignore.
- **Decision:** Ship one `.secrets.baseline` for the IBM detect-secrets fork
  with the keyword detector omitted, dependency and generated paths excluded,
  and no findings. Run the hook with `--baseline`, `--use-all-plugins`,
  `--no-keyword-scan`, and `--fail-on-unaudited`; keep gitleaks as the
  complementary gate. D-13 governs how the hook is pinned.
- **Consequences:** Keyword-only secrets are not detected by this scanner; the
  reference records that trade-off and keeps provider and entropy detectors on.
  Two scanners must be maintained. Tests pin the policy so a regenerated
  baseline cannot silently re-enable keyword scanning.
- **Reason:** Signal quality matters more than rule count: a scanner reviewers
  trust is a control, and a noisy scanner is a ritual.

### D-13 — Pin hooks and actions by version tag, not commit SHA

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

### D-14 — Documents describe current state and link the owner of each value

- **Context:** Documents copied exact tool pins, hook revisions, test counts,
  local run dates, and environment lines into prose and into the tests
  template. Every one of those values belongs to a file that changes it, so the
  prose was stale after any upgrade or commit while still reading as fact. A
  "Last verified" column turned a green run into a permanent claim.
- **Decision:** A document states behavior as it exists now and links the file
  that owns a volatile value: `requirements-dev.txt`, `.pre-commit-config.yaml`,
  the workflow, or the manifest. Do not duplicate exact pins, hook revisions,
  test counts, run dates, coverage percentages, or environment lines. Templates
  do not ask a copier to record them. Only an unresolved failure investigation
  may record the command, environment, and result of that run.
- **Consequences:** A version bump changes one configuration file, and no
  document needs editing to stay true. A reader who needs the pin follows one
  link to the source of truth. Decision records remain the exception: a record
  may quote the value it chose, because the choice is history rather than a
  claim about the current tree.
- **Reason:** A duplicated value is a second source of truth that no test or
  automation updates, so it decays silently. Linking the owner keeps the
  document correct by construction.

### D-15 — Documents carry no bookkeeping metadata

- **Context:** Decision records carried status, date, owner, evidence, rejected
  options, and a supersession field; generated tables carried evidence,
  verification, baseline, target, and owner columns. Every one of those values
  is either constant (all records are accepted) or owned by Git, the pull
  request, or the configuration file. Maintaining them was manual work that no
  reader or automation consumed, and a wrong value looked as authoritative as a
  right one.
- **Decision:** A generated document states a subject and a finding. It does not
  carry per-row status, date, owner, evidence, verification, baseline, target,
  measure, rejected-option, or supersession data, and a decision record has only
  context, decision, consequences, and reason. Where a table must say whether a
  row holds, it uses one `Assessment` column (`Coverage` for requirement
  traceability) holding the claim and its basis.
- **Consequences:** Records are shorter and cannot contradict each other about a
  document's own state. A reader who wants history reads the commit or the pull
  request; a reader who wants a value follows the link to its owning file. Two
  records that were previously distinguishable only by date now rely on their
  IDs and text, so IDs remain permanent.
- **Reason:** Bookkeeping that nothing consumes drifts, and a stale status is
  worse than no status because it reads as fact. This extends D-10 from
  document headers to table columns and decision fields.

### D-16 — Titles name the document type, and template links resolve in the output

- **Context:** Every generated title ended with an em dash and the project name,
  so a renamed repository left a stale name in twelve documents, and the root
  README had no title of its own. Templates also linked documents that are created only
  when a repository supports them, and two templates linked a Mermaid reference
  that ships with the skill and is never copied. Nothing resolved those links:
  `check_links.py` skipped templates, and the working-example test only proved
  that a template had an output.
- **Decision:** An H1 states the document type — `# Overview`, `# Architecture`,
  `# Product Requirements Document` — with no project name and no separator
  suffix. A template links only to output that every generated repository
  contains; a conditional document is named in backticks or reached through
  `{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}`, which the skill fills with
  links that exist. A template never links into `skills/` or `references/`.
- **Consequences:** Titles survive a rename and read the same in every repository.
  Most templates now contain fewer literal links, and the related-document footer
  becomes a deliberate step rather than a copy of a fixed list. `docs/` keeps real
  links because every generated document exists here.
- **Reason:** A link is a promise that the target exists. Promising a document
  that the same run decided to skip is the defect, and a project name in a title
  is a copy of a value the repository root already states.

### D-17 — Templates name documents instead of linking them

- **Context:** A template is copied into another repository, but its links are
  written in this one. Reading `skills/ai-init/templates/docs/README.md` in the
  repository, `../README.md` resolves to `skills/ai-init/templates/README.md` and
  `./PRD.md` to a directory that holds no such file; the generated page is correct
  and the source is broken. `check_links.py` skipped every `templates/` directory,
  so nineteen of twenty-two template links were never verified. A link checker
  that treats `readme.md` as a host name reports `http://readme.md`.
- **Decision:** A template contains no relative link. It names a document in a
  code span and the skill writes the link when it writes that document, only for
  files that exist. An index row names the document and its file in parentheses;
  the skill turns the name into a link and deletes the parenthetical. This
  replaces the link clause of D-16 and keeps its title rule.
- **Consequences:** Every template link is now a link that exists, so
  `check_links.py` covers the templates and the no-link rule has its own test.
  Generated pages still carry links, and the working example shows the result.
  A template reader sees a path, not a dead link.
- **Reason:** A link is a promise that the target exists. A template cannot know
  which repository it will be copied into, so it cannot promise a target; the
  skill can, at the moment it writes the file.

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Structure](./structure.md)
