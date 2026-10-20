# Code Style — AI Init Skills

Only languages, formatters, and tools that exist in the repository are listed.
Nothing here is enforced unless pre-commit or CI runs it.

## Languages and Tooling

| Language / format | Version | Formatter | Linter / validator | Enforced by | Configuration evidence |
|---|---|---|---|---|---|
| Markdown | CommonMark plus YAML frontmatter | None configured | `markdownlint-cli2` | pre-commit, CI | `.markdownlint-cli2.yaml` |
| YAML | Not pinned | None configured | `check-yaml`, `validate_skills.py` | pre-commit, CI | `.pre-commit-config.yaml` |
| JSON | Not pinned | None configured | `check-json` | pre-commit | `.pre-commit-config.yaml` |
| TOML | Not pinned | None configured | `check-toml` | pre-commit | `.pre-commit-config.yaml` |
| Python | 3.11 or later | None configured | `unittest`, `validate_skills.py` | CI | `requirements-dev.txt`, workflow |
| Plain text (`CODEOWNERS`) | Not applicable | None | Reviewed | Review | `.github/CODEOWNERS` |

No formatter is configured for Python or Markdown. That is deliberate for
Markdown: a formatter that does not understand YAML frontmatter can convert
`---` into a horizontal rule and make every skill undiscoverable.

## Repository Conventions

- Indentation and line endings: two spaces, LF, final newline, per
  `.editorconfig` and `.gitattributes`.
- Trailing whitespace: trimmed except in Markdown, where two trailing spaces
  are a hard line break.
- Naming and file layout: root meta files uppercase; `docs/` lowercase
  kebab-case with `PRD.md` as the recorded acronym exception; template paths
  mirror output paths.
- Commit conventions: Conventional Commits, for example
  `feat(ai-init): generate repository meta files`.
- Branch and merge conventions: work on a branch and merge by pull request;
  direct pushes to the default branch are not part of the documented process.
- Diagrams: use the canonical init block in
  [`mermaid-standard.md`](../skills/ai-init/references/architecture/mermaid-standard.md).
- YAML frontmatter is data and must never be reformatted as prose.

## Modular Code and Contracts

- Each script has one responsibility: `validate_skills.py` validates,
  `check_links.py` checks links.
- Validator rules are small, named checks that emit a stable rule code
  (`SKILL010`, `EVAL015`). Codes are permanent identifiers and are never
  recycled for a different meaning.
- Public behavior of the scripts is their CLI contract: arguments, exit status,
  and output format. Changes to those require a documented migration.
- `unittest` cases isolate one rule each and use temporary directories rather
  than shared fixtures.
- No speculative abstraction is added for a single caller.

## Secure Coding and Reliability

- No shell invocation from Python; scripts use the standard library.
- File paths are resolved relative to the script location or an explicit
  `--root`, never to the process working directory alone.
- Failures return a non-zero exit status; no error is swallowed.
- No network access in the scripts.
- Secrets are never read, printed, or written. `gitleaks` and private-key
  detection guard the tree.
- YAML is parsed with `safe_load` only.
- Caches and virtual environments are ignored, not committed.

## Language References

The `ai-init` skill ships adaptable style baselines for target repositories:
Bash, Go, JSON, Markdown, Python, TypeScript, and YAML under
`skills/ai-init/references/style/`. They are baselines for generated projects,
not enforced policy in this repository.

## Testing Conventions

- Test framework and command: `unittest`, run with
  `python -m unittest discover -s tests -v`.
- Naming and layout: `tests/test_<subject>.py`, one class per subject, one
  assertion focus per test.
- Fixtures and test data policy: synthetic content created in temporary
  directories; no production data and no real credentials.
- Flaky-test/quarantine policy: tests must be deterministic; no quarantine
  mechanism is configured.

## Exceptions

No exceptions to the conventions above are recorded.

## Related Docs

[README](../README.md) · [Rules](./rules.md) · [Architecture](./architecture.md)
