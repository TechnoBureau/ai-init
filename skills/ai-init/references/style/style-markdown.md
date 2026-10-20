# Markdown Style Baseline

Use the repository's configured Markdown linting and link-checking tools.
`markdownlint-cli2` and link checkers such as `lychee` are options, not
assumed dependencies or CI gates.

## Machine-readable frontmatter

- Files may begin with YAML frontmatter delimited by `---`. This is data, not
  Markdown content: never let a formatter turn the delimiter into a horizontal
  rule or merge `name`/`description` into a heading.
- Use a frontmatter-aware formatter, or exclude `.md` files that carry
  frontmatter from automatic formatting.
- Validate frontmatter with the repository's schema or validator before
  committing. A rendered preview is not proof that the metadata still parses.
- Keep metadata values valid YAML: quote dates, versions, and numeric strings.

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
- Use one H1, sequential headings, descriptive link text, and table header rows.
- Provide alt text for meaningful images and a short text explanation for each
  diagram; never convey meaning by color alone.
