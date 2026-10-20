# Code Style — {{PROJECT_NAME}}

> Include only languages, formatters, and linters confirmed by source,
> configuration, or CI. Copy and link only the reference guides that apply.

## Languages and Tooling

| Language / format | Formatter | Linter / validator | Configuration evidence |
|---|---|---|---|
| {{LANGUAGE}} | {{VERIFIED_TOOL_OR_NONE}} | {{VERIFIED_TOOL_OR_NONE}} | `{{CONFIG_PATH}}` |

## Repository Conventions

- Indentation and line endings: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Naming and file layout: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Commit conventions: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Diagrams: use the canonical block in
  [`references/architecture/mermaid-standard.md`](./references/architecture/mermaid-standard.md)
  when a Mermaid diagram is present.

## Modular Code and Contracts

- Keep modules cohesive, responsibilities clear, and interfaces narrow;
  follow the architecture already established by the repository.
- Prefer focused functions with explicit inputs, outputs, and error behavior.
  Avoid needless wrappers or abstractions that make control flow harder to
  follow.
- For public APIs and non-obvious functions, document purpose, meaningful
  input constraints, return/output semantics, caller-relevant errors, and
  side effects or security assumptions. Use language-native doc comments.
- Add comments to explain rationale, invariants, or non-obvious constraints,
  not to narrate code that is already clear.
- Remove unused imports, variables, functions, and dependencies only after
  checking configured analyzers and hidden/dynamic entry points. Treat public
  APIs, plugin registrations, generated code, and reflection targets as live
  unless their use is ruled out. Cleanup is a code-change task, not an
  automatic side effect of documenting the repository.

## Language References

Link only guides copied into `docs/references/style/` and relevant to
languages actually used. Treat these as adaptable baselines, not enforced
repository policy unless configuration or CI verifies that:

{{LINKS_TO_APPLICABLE_STYLE_REFERENCES}}

## Testing Conventions

Document only conventions evidenced by project configuration. Do not state
coverage targets unless configured. Keep detailed test inventory and commands
in `docs/tests.md` only when that optional document exists.

______________________________________________________________________

### Related Docs

[README](../README.md) · [Rules](./rules.md) · [Architecture](./Architecture.md)
