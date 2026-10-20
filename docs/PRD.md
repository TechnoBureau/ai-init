# Product Requirements Document — AI Init Skills

> **Evidence base:** commit `HEAD` of `arena/94ccada2-ai-init`; files inspected:
> `skills/*/SKILL.md`, `skills/*/references/`, `skills/*/templates/`,
> `scripts/`, `tests/`, `evals/`, `.github/workflows/validate.yml`,
> `.pre-commit-config.yaml`. Existing Markdown is treated as history, not proof
> that behavior is active.

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

| ID | Outcome | Baseline | Target / measure | Verification source |
|---|---|---|---|---|
| G-1 | Every skill is loadable by a compliant agent host | 6 of 6 skills pass the validator | Remain 6 of 6 with zero errors | `scripts/validate_skills.py` |
| G-2 | Generated documents never invent facts | Policy stated in every skill | No unresolved placeholder or fabricated claim found in review | `scripts/validate_skills.py`, review checklist |
| G-3 | Metadata regressions are caught before merge | Validator plus 17 regression tests | CI fails on missing or malformed frontmatter | `tests/`, `.github/workflows/validate.yml` |
| G-4 | The collection demonstrates its own output | `docs/` generated from templates | Every template has a generated counterpart | `tests/test_working_example.py` |
| G-5 | Enterprise standards are applied consistently | 6 skills declare standards and risk | Every skill passes metadata validation | `scripts/validate_skills.py` |

No target date or numeric adoption target is recorded; none has been confirmed.

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

| ID | Status | Decision | Reason | Alternatives Rejected | Evidence | Owner / date |
|---|---|---|---|---|---|---|
| D-1 | Accepted | Six focused skills, not one monolith | Progressive disclosure, independent install | Monolith, nested skills | `skills/` | TechnoBureau / 2026-10-20 |
| D-2 | Accepted | Agent Skills 1.0 with YAML frontmatter | Cross-host discovery | Vendor format, no frontmatter | `docs/skill-standard.md` | TechnoBureau / 2026-10-20 |
| D-3 | Accepted | Validate format in pre-commit, CI, and tests | Human review misses metadata corruption | Guidance only, Markdown lint alone | `scripts/validate_skills.py` | TechnoBureau / 2026-10-20 |
| D-4 | Accepted | Small `SKILL.md`, detail in `references/` | Context economy | Everything inline, external site | Validator size limits | TechnoBureau / 2026-10-20 |
| D-5 | Accepted | Template paths mirror output paths | Self-documenting, avoids ambiguous names | Manifest, flat prefixed names | `skills/*/templates/` | TechnoBureau / 2026-10-20 |
| D-6 | Accepted | Meta files only from confirmed facts | Wrong legal or routing data is harmful | Best-guess defaults, placeholders | `references/licensing.md` | TechnoBureau / 2026-10-20 |
| D-7 | Accepted | Lowercase kebab-case in `docs/` | Link portability | All uppercase, mixed case | `docs/` | TechnoBureau / 2026-10-20 |
| D-8 | Accepted | Generate this repository's `docs/` from templates | Dogfooding, prevents template drift | Separate example repository | `tests/test_working_example.py` | TechnoBureau / 2026-10-20 |
| D-9 | Accepted | No changelog or release numbering initially | Avoids unused version churn | SemVer per skill, repository version | `docs/governance.md` | TechnoBureau / 2026-10-20 |

Full context and consequences are in [decisions.md](./decisions.md).

## 6. User Personas

| Persona | Responsibilities | Needs | Evidence |
|---|---|---|---|
| Platform engineer | Bootstraps repositories, keeps docs current | Safe, repeatable generation that preserves existing content | `skills/ai-init/SKILL.md` |
| Product manager | Owns scope and requirements | Traceable requirement IDs with acceptance criteria | `skills/prd/SKILL.md` |
| Security reviewer | Assesses posture and threats | Evidence-based statuses, no compliance overclaim | `skills/security/SKILL.md` |
| QA engineer | Maintains tests and evidence | Exact commands, coverage gaps, deterministic fixtures | `skills/tests/SKILL.md` |
| Design and accessibility lead | Owns design system and accessibility | Token and WCAG 2.2 evidence without invented conformance | `skills/design/SKILL.md` |
| Maintainer of this collection | Reviews and releases skills | Automated gates and clear authoring rules | `docs/skill-standard.md` |
| AI agent | Executes a skill in a target repository | Unambiguous instructions, scope boundaries, fail-safe rules | `SKILL.md` operating constraints |

## 7. Functional Requirements

### Skill entry points (`skills/*/SKILL.md`)

| ID | Requirement | Acceptance criteria | Verification | Evidence | Status |
|---|---|---|---|---|---|
| FR-1 | Each skill MUST declare `name` and `description` in YAML frontmatter, and `name` MUST equal its directory | Frontmatter parses and matches directory | Validator | `skills/*/SKILL.md` | Implemented |
| FR-2 | The `description` MUST state both capability and trigger conditions | Contains an explicit "Use when/for/to" clause | Validator rule `SKILL030` | `skills/*/SKILL.md` | Implemented |
| FR-3 | Each skill MUST declare enterprise metadata `spec`, `standards`, and `risk`, and MUST NOT declare `owner`, `reviewed`, or `classification` | Metadata validates; disallowed keys rejected | Validator rules `SKILL060`–`SKILL073` | `scripts/validate_skills.py` | Implemented |
| FR-4 | Each skill body MUST state operating constraints covering untrusted content, secrets, scope, destructive actions, and evidence honesty | Section present and specific | Review checklist | `skills/*/SKILL.md` | Implemented |
| FR-5 | Each skill MUST stay under 500 lines and roughly 5,000 tokens | No size violation | Validator rules `SKILL044`–`SKILL046` | `scripts/validate_skills.py` | Implemented |

### Documentation generation (`ai-init`)

| ID | Requirement | Acceptance criteria | Verification | Evidence | Status |
|---|---|---|---|---|---|
| FR-6 | `ai-init` MUST create root `README.md` and relative symlinks `AGENTS.md` and `CLAUDE.md` | Links resolve to `README.md`; conflicts reported | Manual check; link checker | `skills/ai-init/SKILL.md` | Implemented |
| FR-7 | `ai-init` MUST create the default `docs/` set: index, PRD, structure, decisions, security | Files generated with no placeholders | `tests/test_working_example.py` | `docs/` | Implemented |
| FR-8 | `ai-init` MUST create conditional documents only when evidence supports them | `docs/design.md` absent without a UI | `docs/README.md` | `docs/` | Implemented |
| FR-9 | `ai-init` MUST generate `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CODEOWNERS`, and `LICENSE` only from confirmed facts | No invented owner, licence, or contact | Checklist section | `skills/ai-init/SKILL.md`, `checklist.md` | Implemented |

### Validation and evaluation

| ID | Requirement | Acceptance criteria | Verification | Evidence | Status |
|---|---|---|---|---|---|
| FR-10 | The validator MUST fail on missing or malformed frontmatter and name the formatter failure | Non-zero exit with `SKILL010`/`SKILL011` | Unit test | `tests/test_validate_skills.py` | Implemented |
| FR-11 | The validator MUST check that every relative link in skills and references resolves | Broken link reported with path | `scripts/check_links.py`, validator rule `SKILL080` | `scripts/` | Implemented |
| FR-12 | Every skill MUST have an eval fixture with trigger, non-trigger, and adversarial cases | Both trigger states present; unique IDs | Validator rules `EVAL001`–`EVAL015` | `evals/*.yaml` | Implemented |
| FR-13 | CI MUST run the validator, link checker, tests, Markdown lint, and hygiene hooks on push and pull request | Workflow green on the default branch | GitHub Actions | `.github/workflows/validate.yml` | Implemented |
| FR-14 | The repository MUST demonstrate its own output | Every template has a generated counterpart or a documented exemption | `tests/test_working_example.py` | `docs/` | Implemented |

### Documentation content

| ID | Requirement | Acceptance criteria | Verification | Evidence | Status |
|---|---|---|---|---|---|
| FR-15 | Generated documents MUST distinguish `Verified`, `Observed`, `Planned`, `Not documented`, and `Not assessed` claims | Vocabulary used consistently | Review | `skills/ai-init/references/documentation-standard.md` | Implemented |
| FR-16 | Requirement and decision IDs MUST be permanent and never recycled | Supersession recorded instead of renumbering | Review | `docs/decisions.md` | Implemented |
| FR-17 | PRDs MUST contain exactly the ten required sections in order | Section headings match | Template review | `skills/prd/templates/docs/PRD.md` | Implemented |
| FR-18 | Security documents MUST use only the defined control statuses and MUST NOT claim certification | Status vocabulary enforced by instruction and template | Review | `skills/security/templates/docs/security.md` | Implemented |

## 8. Non-Functional Requirements

| ID | Category | Requirement | Verification criteria | Status |
|---|---|---|---|---|
| NFR-1 | Security | Generated documents MUST NOT contain secrets, credentials, private keys, or unredacted personal data | gitleaks, private-key detection, and review find no secret | Verified |
| NFR-2 | Security | No skill may present an assessment, scan, or control mapping as certification or compliance | All templates avoid certification claims; review | Verified |
| NFR-3 | Privacy | The collection processes only public repository content and stores no personal data | Data inventory shows no personal data | Verified |
| NFR-4 | Reliability | The validator MUST exit non-zero on any error and produce deterministic output for a given tree | Repeated runs produce identical findings | Verified |
| NFR-5 | Performance | The full validation suite SHOULD complete within a few seconds locally and under 15 minutes in CI | CI job completes in about one minute | Verified |
| NFR-6 | Maintainability | Every validator rule MUST have a regression test or an exercised fixture | `tests/test_validate_skills.py`, `tests/test_check_links.py` | Verified |
| NFR-7 | Portability | Skills MUST work on POSIX and Windows; symlink failure is reported, never silently copied | Constraint documented and handled | Verified |
| NFR-8 | Compatibility | Frontmatter MUST remain valid Agent Skills 1.0 for compliant hosts | Skills CLI lists all six skills | Verified |
| NFR-9 | Accessibility | Documentation MUST use one H1, sequential headings, table headers, and text explanations for diagrams | markdownlint plus review | Verified |
| NFR-10 | Observability | CI MUST surface the failing rule identifier and path | Validator output includes code and path | Verified |
| NFR-11 | Supply chain | Actions, hooks, and Python dependencies MUST be pinned and updated by automation | Pinned SHAs and Dependabot configuration | Verified |
| NFR-12 | Localization | Not applicable; the collection ships English-only instructions | No locale files | Not applicable |
| NFR-13 | Compliance | No certification or regulatory scope has been confirmed for this repository | No compliance claim made | Not assessed |

Categories that do not apply are recorded rather than omitted silently.

## 9. Pipeline / Workflow Inventory

| Filename | Trigger | Target | Evidence |
|---|---|---|---|
| `.github/workflows/validate.yml` | `push`, `pull_request`, `workflow_dispatch` | Ubuntu runner; validator, link check, unit tests, pre-commit hooks | Workflow file |
| `.github/dependabot.yml` | Weekly schedule | Updates for `github-actions`, `pre-commit`, and `pip` ecosystems | Configuration file |
| `.pre-commit-config.yaml` | Local commit hook, and CI `pre-commit run --all-files` | Hygiene, secret scanning, Markdown lint, skill validation, link check, tests | Configuration file |

No deployment pipeline exists; the repository publishes content only.

## 10. Repository Structure

```text
.
├── skills/          # six skills: SKILL.md, references/, templates/, files/
├── docs/            # generated documentation set (this folder)
├── evals/           # evaluation fixtures per skill
├── scripts/         # validate_skills.py, check_links.py
├── tests/           # validator and working-example regression tests
└── .github/         # CI workflow, Dependabot, CODEOWNERS, PR template
```

See [structure.md](./structure.md) for the fuller verified map.

## Related Docs

[README](../README.md) · [Architecture](./architecture.md) · [Decisions](./decisions.md) · [Security](./security.md)
