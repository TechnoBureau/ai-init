# Overview

A modular, evidence-grounded Agent Skills collection for repository
documentation, product requirements, enterprise security, test work, design
systems, and code quality. Every skill follows the open
[Agent Skills specification](https://agentskills.io/specification) and adds an
enterprise metadata, safety, and validation profile.

Install the full collection for the complete workflow or a single skill for
focused work.

## Install

Install every skill with the Skills CLI for a supported host:

```bash
npx skills add technobureau/ai-init --all --agent '*'
```

For a global install, add `-g`:

```bash
npx skills add technobureau/ai-init --all --agent '*' -g
```

To install one skill, replace `--all` with `--skill` and one of: `ai-init`,
`prd`, `security`, `tests`, `design`, or `code-quality`. See the [Skills CLI
documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
for supported host integrations and options.

## Skills

| Skill | Use it for | Guide |
|---|---|---|
| `ai-init` | Bootstrap, targeted updates, spec-first documentation, and explicit full refresh of managed documentation and meta files | [SKILL.md](./skills/ai-init/SKILL.md) |
| `prd` | Evidence-grounded PRD, requirement quality, and traceability | [SKILL.md](./skills/prd/SKILL.md) |
| `security` | Security posture, threat model, supply chain, PQC, FIPS, CIS, NIST, ISO/IEC 27001, OWASP | [SKILL.md](./skills/security/SKILL.md) |
| `tests` | Test implementation, strategy, security/accessibility/performance coverage | [SKILL.md](./skills/tests/SKILL.md) |
| `design` | Design systems, tokens, WCAG 2.2 accessibility, localization | [SKILL.md](./skills/design/SKILL.md) |
| `code-quality` | Dead-code cleanup, modularity, secure coding, API compatibility | [SKILL.md](./skills/code-quality/SKILL.md) |

Invoke a skill by name where supported, or describe the task. For example:

> `$ai-init` Update the README Quick Start for the new `dev` script in
> `package.json`. Inspect the manifest, the script it invokes, and the README;
> leave unrelated documents unchanged.

Use `$prd`, `$security`, `$tests`, `$design`, or `$code-quality` for their
corresponding work. See the [Usage guide](./docs/usage.md) for installation,
invocation, and local validation examples.

## What `ai-init` generates

`ai-init` owns the complete repository baseline, not just the README. This
table describes Bootstrap and explicit full refresh; targeted updates touch only
affected outputs.

Template paths mirror output paths, so there is no separate mapping to keep in
sync: `templates/root/x` produces `x`, and `templates/docs/x.md` produces
`docs/x.md`.

| Output | Source template | Created when |
|---|---|---|
| `README.md` | `templates/root/README.md` | Always |
| `LICENSE` | `references/licensing.md` | A licence is confirmed by file, manifest, or user |
| `CONTRIBUTING.md` | `templates/root/CONTRIBUTING.md` | The repository accepts contributions or the user asks |
| `CODE_OF_CONDUCT.md` | `templates/root/CODE_OF_CONDUCT.md` | A private enforcement contact is confirmed |
| `SECURITY.md` | `templates/root/SECURITY.md` | A private reporting channel is confirmed |
| `.github/CODEOWNERS` | `templates/root/CODEOWNERS` | Owners are confirmed by the user or existing configuration |
| `.gitignore` | `files/.gitignore` | Always; merge missing sections into an existing file |
| `.secrets.baseline` | `files/.secrets.baseline` | When the project adopts IBM detect-secrets; policy must match the pinned hook |
| `docs/README.md` | `templates/docs/README.md` | Always, alongside the first generated document |
| `docs/PRD.md` | `skills/prd/templates/docs/PRD.md` | Always |
| `docs/structure.md`, `docs/decisions.md` | `templates/docs/` | Always |
| `docs/security.md` | `skills/security/templates/docs/security.md` | Always |
| `docs/architecture.md`, `docs/design.md`, `docs/tests.md` | Dedicated templates | When the repository evidence warrants it |
| `docs/rules.md`, `docs/style.md`, `docs/usage.md`, `docs/governance.md`, `docs/threat-model.md` | `templates/docs/` | When evidence or the user requires them |

Missing evidence is never invented. If an owner, licence, security contact, or
approval is unknown, the file is not fabricated; the skill reports the gap.

### The `docs/` folder is a working example

This repository's [`docs/`](./docs/README.md) is generated from the same
templates it ships, so every template is exercised by a real document.
`tests/test_working_example.py` fails when a template has no generated
counterpart, when a generated document still contains a placeholder, or when a
document is missing from the index. `docs/design.md` is intentionally absent
because this repository has no UI.

## What every skill declares

```yaml
metadata:
  spec: "1.0"
  standards: "Agent Skills 1.0; <applicable standards>"
  risk: "low"   # low | medium | high | critical
```

The skill bodies add:

- **Operating constraints** — untrusted repository content, secret handling,
  read/write scope, destructive-action limits, and evidence honesty.
- **Enterprise standards** — ISO/IEC/IEEE 29148, ISO/IEC 25010, NIST SSDF and
  CSF, ISO/IEC 27001, OWASP ASVS, SLSA, WCAG 2.2, DTCG tokens, RFC 2119/8174,
  and conditional frameworks only when scope is confirmed.
- **Mandatory outputs** — claim status, traceability, acceptance criteria,
  control status vocabulary, exceptions, and assessment limits.
- **Fail-safe behavior** — unknowns stay `Not documented`, `Not assessed`, or
  `TBD`; no invented owners, licences, controls, test results, or compliance.
- **Evaluation cases** — trigger, non-trigger, and adversarial fixtures in
  [`evals/`](./evals).

## Quality gates

Every change runs:

```bash
python scripts/validate_skills.py --strict
python scripts/check_links.py
python -m unittest discover -s tests -v
pre-commit run --all-files
```

| Gate | What it enforces |
|---|---|
| [`validate_skills.py`](./scripts/validate_skills.py) | Spec frontmatter, name/directory match, description triggers, enterprise metadata, body limits, relative links, eval coverage |
| [`check_links.py`](./scripts/check_links.py) | Every local Markdown link resolves, including links in templates |
| [`tests/`](./tests) | Validator rules and a regression that reproduces frontmatter corruption |
| [markdownlint-cli2](./.markdownlint-cli2.yaml) | Markdown structure and consistency without rewriting YAML frontmatter |
| [pre-commit](./.pre-commit-config.yaml) | YAML/JSON/TOML validity, whitespace, merge markers, large files, private keys, gitleaks, IBM detect-secrets, Markdown lint, skill validation |
| `tests/test_pinning.py` | Every remote hook and action pinned by version tag, never a branch or raw commit SHA |
| `tests/test_working_example.py` | Every template has a generated counterpart in `docs/`; no placeholders or orphan documents |
| `tests/test_secret_scanning.py` | Baseline policy: no keyword scan, no findings, standard files excluded, hook flags, dependencies, and exclude parity |
| `tests/test_docs_state.py` | Documents describe current state: no frozen run, duplicated pin, bookkeeping column, or extra decision field |
| `tests/test_template_links.py` | Every template title names the document type, and every template link resolves in a generated repository |
| [CI](./.github/workflows/validate.yml) | All of the above on push and pull request with version-pinned actions and read-only permissions |

The validator is deliberately strict: a missing `---` on line 1 is a blocking
error, and the error message names the formatter failure directly.

## Enterprise controls

- **Documentation index** — every project document in [docs/README.md](./docs/README.md).
- **Governance** — roles, change classes, review cadence, release process,
  deprecation, and exceptions in [docs/governance.md](./docs/governance.md).
- **Authoring standard** — normative frontmatter schema, body rules, formatter
  safety, evals, and review depth in
  [docs/skill-standard.md](./docs/skill-standard.md).
- **Threat model** — prompt injection, secret exposure, destructive actions,
  metadata corruption, supply chain, and overclaim risks in
  [docs/threat-model.md](./docs/threat-model.md).
- **Security policy** — private reporting, response targets, coordinated
  disclosure, and safe harbor in [SECURITY.md](./SECURITY.md).
- **Contribution** — setup, gates, commit conventions, and review expectations
  in [CONTRIBUTING.md](./CONTRIBUTING.md).
- **Code of conduct** — [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).
- **Ownership** — [CODEOWNERS](./.github/CODEOWNERS).
- **Architecture** — [docs/architecture.md](./docs/architecture.md).

These are engineering controls, not a certification. The collection does not
claim ISO/IEC 27001, SOC 2, FIPS 140-3, or any other certification.

## Defaults and safeguards

- During Bootstrap or Full refresh, `ai-init` reconciles the root `README.md`
  and common documentation. Targeted tasks touch only affected outputs. It does
  not create `docs/tests.md`; use `$tests` when test work or that document is
  requested.
- Repository meta files are generated only from confirmed evidence. A licence
  is never chosen on the user's behalf; an owner handle is never invented.
- Documentation is grounded in source and configuration. Existing content,
  permanent IDs, and unrelated work are preserved; empty repositories get a
  clearly labeled initial format rather than invented project facts.
- Documentation updates are scoped to the request: targeted changes verify
  only affected documents and direct evidence, while bootstrap or an explicit
  full refresh reconciles the complete managed set.
- Claims use an explicit status vocabulary (`Verified`, `Observed`, `Planned`,
  `Not documented`, `Not assessed`) and requirement language follows RFC
  2119/8174.
- Documents carry no bookkeeping metadata. A table has no status, date, owner,
  evidence, verification, baseline, target, or measure column, and a decision
  record has context, decision, consequences, and reason only. Where a table
  must say whether a row holds, one `Assessment` (`Coverage`) column carries the
  claim and its basis.
- Security profiles are modular. They conditionally map relevant controls to
  NIST, ISO/IEC 27001, FIPS, OWASP, CIS, and OpenSCAP/SCAP without treating a
  partial repository review as a compliance attestation.
- Code conventions are derived from repository instructions, language
  requirements, and configured tooling, with recommendations distinguished
  from existing project rules.
- Generated documentation uses uppercase root `README.md`; other project
  documents belong under `docs/` in lowercase kebab-case, with `PRD.md` as the
  recorded acronym exception.
- A document title names its type, not the project: `# Architecture`, not
  `# Architecture — <project>`. A template contains no relative link: it names
  the document in a code span, and the skill writes the link only when it writes
  that file. A related-document footer starts from a placeholder the skill fills
  in.
- No document contains secrets, credentials, private keys, or unredacted
  personal data.

## Repository layout

```text
.
├── .github/
│   ├── workflows/validate.yml  # CI gate
│   ├── dependabot.yml          # Action and dependency updates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
├── docs/                       # Generated document set, indexed in docs/README.md
├── evals/                      # Trigger/non-trigger/adversarial fixtures
├── scripts/
│   ├── validate_skills.py      # Spec + enterprise gate
│   └── check_links.py          # Local link integrity
├── skills/
│   ├── ai-init/
│   │   ├── SKILL.md
│   │   ├── checklist.md
│   │   ├── files/              # .editorconfig, .gitattributes, .gitignore, .secrets.baseline, .pre-commit-config.yaml
│   │   ├── references/
│   │   │   ├── architecture/mermaid-standard.md
│   │   │   ├── style/style-*.md
│   │   │   ├── documentation-standard.md
│   │   │   ├── gitignore-standard.md
│   │   │   ├── licensing.md
│   │   │   └── secret-scanning.md
│   │   └── templates/
│   │       ├── root/           # README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CODEOWNERS
│   │       └── docs/           # docs/ document set
│   ├── prd/templates/docs/PRD.md
│   ├── security/
│   │   ├── references/security-baseline.md
│   │   └── templates/docs/security.md
│   ├── tests/
│   │   ├── references/test-standard.md
│   │   └── templates/docs/tests.md
│   ├── design/
│   │   ├── references/         # Catalog + accessibility standard
│   │   └── templates/docs/design.md
│   └── code-quality/references/engineering-practices.md
├── tests/                      # Validator, docs-state, pinning, template, and secret-scanning tests
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .markdownlint-cli2.yaml
├── .pre-commit-config.yaml
├── .secrets.baseline
└── requirements-dev.txt
```

## Compatibility

- Skill format: Agent Skills 1.0 (YAML frontmatter, `name`, `description`,
  optional `license`, `compatibility`, `metadata`, `allowed-tools`).
- Python 3.11 or later.
- Exact tool versions are pinned in [`requirements-dev.txt`](./requirements-dev.txt)
  and [`.pre-commit-config.yaml`](./.pre-commit-config.yaml); this list does not
  repeat them, so it cannot drift from the pin.
- Pinning: every remote hook and action uses an exact version tag. Tags are
  mutable references, so dependency updates are reviewed before merge.
- Secret scanning: gitleaks and IBM detect-secrets, both configured in
  `.pre-commit-config.yaml` and described in
  [`skills/ai-init/references/secret-scanning.md`](./skills/ai-init/references/secret-scanning.md).
- Network: skills do not require network access. CI installs pinned tooling.

## Security

Report vulnerabilities privately through
[GitHub Security Advisories](https://github.com/TechnoBureau/ai-init/security/advisories/new).
Do not open a public issue. See [SECURITY.md](./SECURITY.md) and the
[threat model](./docs/threat-model.md).

## Contributing

Read [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[skill authoring standard](./docs/skill-standard.md). Pull requests must pass
the validation workflow and include an evaluation case for behavior changes.

## License

[MIT](./LICENSE) © TechnoBureau
