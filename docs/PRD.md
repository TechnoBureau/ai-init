# Product Requirements Document

## 1. Overview

**Summary:** A modular collection of six Agent Skills that produce
evidence-grounded repository documentation, product requirements, security
profiles, test work, design-system documentation, and code-quality changes.

**Core problem:** Repository documentation drifts from the code, AI-generated
documents invent facts, and skill files silently break when machine-readable
metadata is reformatted. Teams need documentation that is reproducible,
auditable, and safe to generate.

**Value proposition:** Every output is derived from inspected evidence, marks
unknowns explicitly, and is gated by an automated validator. The collection
ships its own documentation as the worked example.

**Stakeholders:** Skill maintainers, platform and DevSecOps engineers,
engineering managers, security and compliance reviewers, and AI agent hosts.

**Constraints:** Markdown and YAML only; no runtime service; Python 3.11+ for
validation; agent hosts must support the Agent Skills format.

**Dependencies:** Skills CLI for installation, GitHub Actions for CI,
PyYAML and pre-commit for validation, markdownlint-cli2 for Markdown
consistency.

**Assumptions:** The consuming agent can read files, reason over repository
content, and write documents. Host permission models are outside this
repository.

## 2. Product Type

Internal developer tooling: a distributable content package plus validation
tooling. It is not a hosted service and exposes no runtime API. The basis is
the repository contents — `SKILL.md` instruction files, templates, references,
a Python validator, and CI configuration — with no server, container, or
package entry point.

## 3. Goals and Objectives

| ID | Outcome |
|---|---|
| G-1 | Every skill is loadable by a compliant agent host |
| G-2 | Generated documents never invent facts |
| G-3 | Metadata regressions are caught before merge |
| G-4 | The collection demonstrates its own output |
| G-5 | Enterprise standards are applied consistently |

No adoption target or date has been confirmed.

## 4. Scope

### In Scope

- Repository documentation bootstrap and refresh (`ai-init`).
- Product requirements and traceability (`prd`).
- Security posture, threat modeling, and conditional enterprise profiles
  (`security`).
- Test implementation, strategy, and evidence (`tests`).
- Design-system documentation and accessibility evidence (`design`).
- Dead-code cleanup, modularity, secure coding, and API compatibility
  (`code-quality`).
- Validation tooling, evaluation fixtures, and CI enforcement.

### Out of Scope

- Runtime execution, deployment, or hosting of generated documents.
- Enforcing host-level sandboxing or tool permissions.
- Legal review, certification, or audit attestation.
- Application code generation for the target repository.
- Release versioning and changelog management at this initial state (D-9).

### Boundaries and Dependencies

- External systems: Skills CLI, GitHub Actions, PyPI package index for pinned
  tooling.
- Supported platforms: POSIX and Windows; symlink creation is required for the
  agent entry points.
- Data handled: public repository content only; no personal or customer data.

## 5. Architectural Decisions

| ID | Decision | Reason |
|---|---|---|
| D-1 | Six focused skills, not one monolith | Progressive disclosure, independent install |
| D-2 | Agent Skills 1.0 with YAML frontmatter | Cross-host discovery |
| D-3 | Validate format in pre-commit, CI, and tests | Human review misses metadata corruption |
| D-4 | Small `SKILL.md`, detail in `references/` | Context economy |
| D-5 | Template paths mirror output paths | Self-documenting, avoids ambiguous names |
| D-6 | Meta files only from confirmed facts | Wrong legal or routing data is harmful |
| D-7 | Lowercase kebab-case in `docs/` | Link portability |
| D-8 | Generate this repository's `docs/` from templates | Dogfooding, prevents template drift |
| D-9 | No changelog or release numbering initially | Avoids unused version churn |
| D-10 | No branch, revision, or tool-version provenance in generated documents | Stale metadata invites false precision |
| D-11 | One merged `.gitignore` baseline, not per-language fragments | Reviewable, no composition order to test |
| D-12 | IBM detect-secrets baseline with keyword scanning off and generated files excluded | High-signal scanner; provider and entropy detectors remain |
| D-13 | Pin hooks and actions by exact version tag, not commit SHA | Reviewers can check a release; Dependabot keeps pins current |
| D-14 | Documents describe current state and link the file that owns each value | A duplicated value drifts while still reading as fact |
| D-15 | Documents carry no bookkeeping status, date, owner, evidence, verification, baseline, target, alternative, or supersession data | Nothing consumes those fields, and a stale value reads as fact |
| D-16 | Titles name the document type, and template links resolve in the generated repository | A renamed project or skipped document must not leave a broken reference |
| D-17 | Templates name documents instead of linking them | A template copied elsewhere cannot promise a path that exists only after generation |
| D-18 | A Mermaid block never contains a template token | The renderer parses the block before any substitution |
| D-19 | A diagram template is a valid example, not a blank | The init line must reach the generated document |

Full context and consequences are in [decisions.md](./decisions.md).

## 6. User Personas

| Persona | Responsibilities | Needs |
|---|---|---|
| Platform engineer | Bootstraps repositories, keeps docs current | Safe, repeatable generation that preserves existing content |
| Product manager | Owns scope and requirements | Traceable requirement IDs with acceptance criteria |
| Security reviewer | Assesses posture and threats | Claim statuses grounded in inspected files, no compliance overclaim |
| QA engineer | Maintains tests and evidence | Exact commands, coverage gaps, deterministic fixtures |
| Design and accessibility lead | Owns design system and accessibility | Token and WCAG 2.2 evidence without invented conformance |
| Maintainer of this collection | Reviews and releases skills | Automated gates and clear authoring rules |
| AI agent | Executes a skill in a target repository | Unambiguous instructions, scope boundaries, fail-safe rules |

## 7. Functional Requirements

### Skill entry points (`skills/*/SKILL.md`)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-1 | Each skill MUST declare `name` and `description` in YAML frontmatter, and `name` MUST equal its directory | Frontmatter parses and matches directory |
| FR-2 | The `description` MUST state both capability and trigger conditions | Contains an explicit "Use when/for/to" clause |
| FR-3 | Each skill MUST declare enterprise metadata `spec`, `standards`, and `risk`, and MUST NOT declare `owner`, `reviewed`, or `classification` | Metadata validates; disallowed keys rejected |
| FR-4 | Each skill body MUST state operating constraints covering untrusted content, secrets, scope, destructive actions, and evidence honesty | Section present and specific |
| FR-5 | Each skill MUST stay under 500 lines and roughly 5,000 tokens | No size violation |

### Documentation generation (`ai-init`)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-6 | `ai-init` MUST create root `README.md` and a relative symlink `AGENTS.md` | The link resolves to `README.md`; conflicts reported |
| FR-7 | `ai-init` MUST create the default `docs/` set: index, PRD, structure, decisions, security | Files generated with no placeholders |
| FR-8 | `ai-init` MUST create conditional documents only when evidence supports them | `docs/design.md` absent without a UI |
| FR-9 | `ai-init` MUST generate `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CODEOWNERS`, and `LICENSE` only from confirmed facts, and MUST ask whether the project is open source or commercial before writing a licence | No invented owner or contact; open source yields canonical MIT, commercial yields no open-source grant |

### Validation and evaluation

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-10 | The validator MUST fail on missing or malformed frontmatter and name the formatter failure | Non-zero exit with `SKILL010`/`SKILL011` |
| FR-11 | The validator MUST check that every relative link in skills and references resolves | Broken link reported with path |
| FR-12 | Every skill MUST have an eval fixture with trigger, non-trigger, and adversarial cases | Both trigger states present; unique IDs |
| FR-13 | CI MUST run the validator, link checker, tests, Markdown lint, and hygiene hooks on push and pull request | Workflow green on the default branch |
| FR-14 | The repository MUST demonstrate its own output | Every template has a generated counterpart or a documented exemption |
| FR-19 | `ai-init` MUST ship starter configuration for `.gitignore`, the IBM detect-secrets baseline, EditorConfig, Git attributes, and pre-commit, merging into existing files instead of overwriting them | Existing entries preserved; baseline and hook policy match |
| FR-20 | Every remote hook and action MUST be pinned by exact version tag, never by branch or raw commit SHA | No branch or SHA reference remains in configuration |

### Documentation content

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-15 | Generated documents MUST distinguish `Verified`, `Observed`, `Planned`, `Not documented`, and `Not assessed` claims | Vocabulary used consistently |
| FR-16 | Requirement and decision IDs MUST be permanent | A record is never renumbered or deleted |
| FR-17 | PRDs MUST contain exactly the ten required sections in order | Section headings match |
| FR-18 | Security documents MUST use only the defined control statuses and MUST NOT claim certification | Status vocabulary enforced by instruction and template |
| FR-21 | Generated documents MUST NOT carry per-row status, date, owner, evidence, verification, baseline, target, alternative, or supersession metadata | No such column or decision field remains |
| FR-22 | Generated documents MUST link only to files that exist in the target repository, and a title MUST name the document type rather than the project | Every template link resolves to an always-created output; no H1 carries a project name |
| FR-23 | A template MUST NOT contain a relative link; it MUST name the document and the skill MUST write the link only for a file it wrote | `check_links.py` and `tests/test_template_links.py` find no relative link in a template; generated pages link every generated document |
| FR-24 | A generated Mermaid block MUST be valid as written: canonical init block, a diagram type on the first code line, and no template token | `tests/test_diagrams.py` passes and no diagram renders a parse error |
| FR-25 | A template that generates a diagram MUST carry the canonical init line in a valid example block, and the skill MUST replace every example node before delivery | Working example has no `(replace)` label; generated diagrams keep the init line |
| FR-26 | `ai-init` MUST default to targeted scope for identifiable changes, using named paths, worktree/staged diffs, or user-supplied commit/PR ranges; targeted updates MUST inspect and update only affected documents. Bootstrap or an explicit full refresh MUST reconcile all managed documents. When impact cannot be established, `ai-init` MUST ask before widening scope. Both modes MUST preserve permanent IDs and user-authored sections | A targeted change leaves unrelated docs unchanged; a full refresh reconciles the managed set against relevant evidence; an ambiguous scope prompts for clarification |
| FR-27 | Spec-first MUST be the default for every change: identify the authoritative request, issue, task, PRD, or feature spec; state scope and an acceptance check before implementation; preserve IDs and trace criteria to relevant tests. A concise request is sufficient for a small change; substantial features refine a spec before coding, without requiring a separate document for every task | Existing rules and skills describe spec-first as default, keep small changes document-light, and ask about material ambiguity; evals and regression tests cover the workflow |
| FR-28 | The security skill and generated profile MUST assess applicable PQC/cryptography, TLS/certificate/cipher, container, Kubernetes/Helm, and shell-script/logging controls from evidence, distinguishing enforced controls, external dependencies, gaps, and proposed actions | Template and evals cover these domains; the working profile marks absent Docker/Helm/shell assets not applicable and makes no unsupported enforcement claims |
| FR-29 | Spec-first instructions in existing rules, skills, and generated documentation MUST scale detail and artifacts to feature scope, risk, policy, and evidence. Generic checklists MUST be prompts rather than universal deliverables; material ambiguity MUST be surfaced, and low-impact assumptions labeled | Rules and specialist skills use short source-backed guidance; evals and tests reject fixed 15-section output, unnecessary standalone specs, and irrelevant API, database, infrastructure, or security requirements |

## 8. Non-Functional Requirements

| ID | Category | Requirement | Assessment |
|---|---|---|---|
| NFR-1 | Security | Generated documents MUST NOT contain secrets, credentials, private keys, or unredacted personal data | Verified |
| NFR-2 | Security | No skill may present an assessment, scan, or control mapping as certification or compliance | Verified |
| NFR-3 | Privacy | The collection processes only public repository content and stores no personal data | Verified |
| NFR-4 | Reliability | The validator MUST exit non-zero on any error and produce deterministic output for a given tree | Verified |
| NFR-5 | Performance | The full validation suite SHOULD complete within a few seconds locally and under 15 minutes in CI | Verified |
| NFR-6 | Maintainability | Every validator rule MUST have a regression test or an exercised fixture | Verified |
| NFR-7 | Portability | Skills MUST work on POSIX and Windows; symlink failure is reported, never silently copied | Verified |
| NFR-8 | Compatibility | Frontmatter MUST remain valid Agent Skills 1.0 for compliant hosts | Verified |
| NFR-9 | Accessibility | Documentation MUST use one H1, sequential headings, table headers, and text explanations for diagrams | Verified |
| NFR-10 | Observability | CI MUST surface the failing rule identifier and path | Verified |
| NFR-11 | Supply chain | Actions, hooks, and Python dependencies MUST be pinned by exact version and updated by automation | Verified |
| NFR-12 | Localization | Not applicable; the collection ships English-only instructions | Not applicable |
| NFR-13 | Compliance | No certification or regulatory scope has been confirmed for this repository | Not assessed |

Categories that do not apply are recorded rather than omitted silently.

## 9. Pipeline / Workflow Inventory

| Filename | Trigger | Deploys to |
|---|---|---|
| `.github/workflows/validate.yml` | `push`, `pull_request`, `workflow_dispatch` | Ubuntu runner; validator, link check, unit tests, pre-commit hooks |
| `.github/dependabot.yml` | Weekly schedule | Updates for `github-actions`, `pre-commit`, and `pip` ecosystems |
| `.pre-commit-config.yaml` | Local commit hook, and CI `pre-commit run --all-files` | Hygiene, secret scanning, Markdown lint, skill validation, link check, tests |

No deployment pipeline exists; the repository publishes content only.

## 10. Repository Structure

```text
.
├── skills/          # six skills: SKILL.md, references/, templates/, files/
├── docs/            # generated documentation set (this folder)
├── evals/           # evaluation fixtures per skill
├── scripts/         # validate_skills.py, check_links.py
├── tests/           # regression tests for validators, templates, pinning, and scanning
└── .github/         # CI workflow, Dependabot, CODEOWNERS, PR template
```

See [structure.md](./structure.md) for the fuller verified map.

## Related Docs

[README](../README.md) · [Architecture](./architecture.md) · [Decisions](./decisions.md) · [Security](./security.md)
