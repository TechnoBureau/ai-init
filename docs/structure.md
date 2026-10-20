# Repository Structure

This map must match the repository tree. It lists primary directories and key
active components, and omits generated or ignored content.

## Verified Tree

```text
.
├── .github/
│   ├── CODEOWNERS
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── dependabot.yml
│   └── workflows/
│       └── validate.yml
├── docs/
│   ├── README.md
│   ├── PRD.md
│   ├── architecture.md
│   ├── decisions.md
│   ├── governance.md
│   ├── security.md
│   ├── skill-standard.md
│   ├── structure.md
│   ├── style.md
│   ├── rules.md
│   ├── tests.md
│   ├── threat-model.md
│   └── usage.md
├── evals/
│   ├── README.md
│   └── <skill>.yaml            # one fixture per skill
├── scripts/
│   ├── check_links.py
│   └── validate_skills.py
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
│   │   ├── references/catalog.md
│   │   ├── references/accessibility.md
│   │   └── templates/docs/design.md
│   └── code-quality/references/engineering-practices.md
├── tests/
│   ├── test_check_links.py
│   ├── test_docs_state.py
│   ├── test_pinning.py
│   ├── test_secret_scanning.py
│   ├── test_template_links.py
│   ├── test_validate_skills.py
│   └── test_working_example.py
├── AGENTS.md -> README.md
├── CLAUDE.md -> README.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── requirements-dev.txt
└── configuration files (.editorconfig, .gitattributes, .gitignore,
    .markdownlint-cli2.yaml, .pre-commit-config.yaml, .secrets.baseline)
```

## Components

| Path | Responsibility | Active entry point |
|---|---|---|
| `skills/*/SKILL.md` | Skill entry point, frontmatter, workflow, operating constraints | Loaded by an agent host |
| `skills/*/templates/` | Output templates whose directory layout mirrors the target repository | Copied into a target by the skill |
| `skills/*/references/` | Detailed standards loaded on demand | Linked from `SKILL.md` |
| `skills/ai-init/files/` | `.gitignore`, IBM detect-secrets baseline, EditorConfig, Git attributes, and pre-commit starters | Copied or merged only when absent |
| `evals/*.yaml` | Trigger, non-trigger, and adversarial evaluation cases | `scripts/validate_skills.py` |
| `scripts/validate_skills.py` | Specification and enterprise metadata gate | `python scripts/validate_skills.py --strict` |
| `scripts/check_links.py` | Local Markdown link integrity | `python scripts/check_links.py` |
| `tests/` | Regression tests for the validators, the working example, pinning, documentation state, and the secret-scanning policy | `python -m unittest discover -s tests` |
| `.github/workflows/validate.yml` | CI enforcement of every gate | Push and pull request |
| `docs/` | Generated documentation, this folder | Regenerated from `skills/*/templates/` |

## Build and Generated Content

| Path / pattern | Type | Source | Committed? | Notes |
|---|---|---|---|---|
| `docs/*.md` | Generated | `skills/*/templates/` | Yes | Committed so readers and agents see the example output |
| `__pycache__/`, `*.pyc` | Build | Python | No | Ignored by `.gitignore` |
| `.venv/` | Local environment | `python -m venv` | No | Ignored by `.gitignore` |

## Exclusions

Generated caches, the local virtual environment, and agent scratch directories
are omitted from the tree above. No vendored or minified code exists in this
repository.

## Naming and Layout Conventions

- Repository root meta files are uppercase: `README.md`, `LICENSE`,
  `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- Documents under `docs/` are lowercase kebab-case; `PRD.md` is the recorded
  acronym exception.
- A template's path under `templates/` mirrors its output path, so
  `templates/docs/PRD.md` produces `docs/PRD.md` and `templates/root/README.md`
  produces `README.md`.
- `CODEOWNERS` lives in `.github/` because that is the template's documented
  output path and the first location GitHub reads.
- Generated code or build output is not used; the only generated content is
  documentation.

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md)
