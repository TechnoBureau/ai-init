# Contributing

Thank you for improving this skill collection. Skills are production
instructions that influence how agents modify real repositories, so
contributions are reviewed with code-level rigor.

Read the [skill authoring standard](./docs/skill-standard.md) and
[governance](./docs/governance.md) before changing a skill.

## Before you start

- Search existing issues and pull requests.
- For a new skill, open an issue describing the trigger, target user, output,
  and why an existing skill cannot cover it.
- For security issues, follow [SECURITY.md](./SECURITY.md) instead of opening a
  public issue.
- By participating, you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Development setup

Requirements: Python 3.11 or later, Git, and optionally Node.js for Markdown
tooling.

```bash
git clone https://github.com/TechnoBureau/ai-init.git
cd ai-init
python -m venv .venv
. .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements-dev.txt
pre-commit install
```

## Validate locally

Run all gates before opening a pull request:

```bash
python scripts/validate_skills.py --strict
python scripts/check_links.py
python -m unittest discover -s tests -v
pre-commit run --all-files
```

The validator is the authoritative check for missing or malformed YAML
frontmatter, which makes a skill undiscoverable. Do not bypass it.

Because `docs/` is generated from the templates, a template change requires
regenerating the matching document. `tests/test_working_example.py` fails when
the two diverge.

## Adding a skill

1. Create `skills/<name>/SKILL.md`; the directory name must equal `name`.
2. Add spec-compliant frontmatter with the enterprise metadata block.
3. Write the operating constraints, workflow, scope boundary, and evidence
   rules.
4. Move detailed standards into `references/` and output templates into
   `templates/root/` or `templates/docs/`, mirroring the output path.
5. Add `evals/<name>.yaml` with trigger, non-trigger, and adversarial cases.
6. Update the README skill table.
7. Run the validation gates.

Minimal frontmatter:

```yaml
---
name: example-skill
description: >-
  What the skill does and the outcome it produces. Use when the user asks for
  the specific triggers that should activate it.
license: MIT
compatibility: >-
  Environment and platform requirements.
metadata:
  spec: "1.0"
  standards: "Agent Skills 1.0; RFC 2119"
  risk: "low"
allowed-tools: "Read Grep Glob"
---
```

All metadata values are quoted strings. Unquoted dates and versions are a
common cause of schema failures.

## Changing an existing skill

- Add a regression case for every fixed defect.
- Update any documentation that describes the changed behavior.
- Preserve output paths, permanent IDs, and existing user content.
- Do not mix unrelated formatting or refactoring into a behavior change.
- For a breaking change, include migration guidance and follow the
  [deprecation policy](./docs/governance.md#deprecation).

## What reviewers look for

- Every factual claim is traceable to repository evidence or a named standard.
- The skill fails safe when evidence is missing.
- The skill cannot be induced to expose secrets, expand scope, or destroy work.
- Instructions are unambiguous to an agent with no prior context.
- Tables and prose are readable at normal GitHub width.
- Links resolve, frontmatter is intact, and placeholders exist only in
  templates.
- Tests and evals prove the new behavior.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(security): add supply-chain evidence requirements
fix(ai-init): restore YAML frontmatter regression gate
docs(governance): define quarterly review cadence
```

Keep each commit focused. Explain the why in the body, not just the change.

## Pull requests

Use the pull-request template. A pull request is ready when:

- the validation workflow passes;
- the change class and migration impact are stated;
- security, privacy, and destructive-action impact are addressed;
- reviewers have enough evidence to verify the claims.

Maintainers may request changes for unsupported claims even when CI is green.
CI checks structure; reviewers check truthfulness and safety.

## Documentation changes

Follow the [documentation standard](./docs/skill-standard.md) and keep links
valid. Generated project documentation belongs under `docs/`, except the root
`README.md` and its `AGENTS.md` symbolic link.

## License

By contributing, you agree that your contribution is licensed under the
repository's [MIT License](./LICENSE).
