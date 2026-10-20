# Markdown Style Baseline

Use the repository's configured Markdown linting and link-checking tools.
`markdownlint-cli2` and link checkers such as `lychee` are options, not
assumed dependencies or CI gates.

## Rules

- ATX headings (`#`, `##`, ...), exactly one H1 per file, matching the
  filename/title.
- One blank line before and after headings, lists, and fenced code blocks.
- Fenced code blocks always specify a language hint (```` ```bash ````,
  ```` ```python ````, ```` ```mermaid ````, etc.).
- Relative links for in-repo references; reference-style links for URLs
  reused more than twice in the same file.
- Tables for structured comparisons; avoid ASCII art outside of diagrams.
- Soft line-length guidance ~100 chars for prose (not enforced inside
  tables/code).
- When this documentation suite is used, Mermaid diagrams should use the
  canonical block in
  `docs/references/architecture/mermaid-standard.md` if that reference is
  copied into the target repository.
- Add a "Related Docs" section only when it helps navigation; link only to
  files that exist in the target repository.
