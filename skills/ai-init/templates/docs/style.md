# Code Style — {{PROJECT_NAME}}

> Include only languages, formatters, and linters confirmed by source,
> configuration, or CI. Copy and link only the reference guides that apply.

## Languages and Tooling

| Language / format | Version | Formatter | Linter / validator | Enforced by | Configuration evidence |
|---|---|---|---|---|---|
| {{LANGUAGE}} | {{SUPPORTED_VERSION}} | {{VERIFIED_TOOL_OR_NONE}} | {{VERIFIED_TOOL_OR_NONE}} | {{PRE_COMMIT_CI_OR_NOT_ENFORCED}} | `{{CONFIG_PATH}}` |

Record the supported version range, then link the file that pins the exact
version. Do not copy an exact pin into the table; it is stale after the next
update. Do not describe a tool as required unless pre-commit, CI, or review
policy enforces it.

## Repository Conventions

- Indentation and line endings: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Naming and file layout: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Commit conventions: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Branch and merge conventions: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Diagrams: use the canonical block in
  [`references/architecture/mermaid-standard.md`](./references/architecture/mermaid-standard.md)
  when a Mermaid diagram is present.
- YAML frontmatter and other machine-readable metadata must never be
  reformatted as prose.

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

## Secure Coding and Reliability

- Validate untrusted input at trust boundaries and encode output for its sink.
- Enforce authentication and authorization server-side; fail closed.
- Never log secrets, tokens, credentials, or personal data.
- Use bounded timeouts, retries, and resource limits.
- Prefer parameterized queries and safe deserialization.
- Do not invent cryptography or hard-code keys.
- For HTTP APIs, apply Semantic Versioning, a deprecation window, and
  `Deprecation`/`Sunset` fields (RFC 9745/RFC 8594) where applicable.
- Prefer OpenAPI 3.1 or AsyncAPI 3.0 when the repository already uses
  schema-first contracts.
- Follow the project's structured logging and OpenTelemetry conventions where
  configured.

## Language References

Link only guides copied into `docs/references/style/` and relevant to
languages actually used. Treat these as adaptable baselines, not enforced
repository policy unless configuration or CI verifies that:

{{LINKS_TO_APPLICABLE_STYLE_REFERENCES}}

## Testing Conventions

Document only conventions evidenced by project configuration. Do not state
coverage targets unless configured. Keep detailed test inventory and commands
in `docs/tests.md` only when that optional document exists.

- Test framework and command: {{VERIFIED_OR_NOT_CONFIGURED}}
- Naming and layout: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Fixtures and test data policy: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Flaky-test/quarantine policy: {{CONFIRMED_OR_NOT_DOCUMENTED}}

## Exceptions

| Convention | Exception | Rationale | Owner | Review date |
|---|---|---|---|---|
| {{RULE_OR_NONE}} | {{EXCEPTION_OR_NONE}} | {{CONFIRMED_RATIONALE}} | {{OWNER_OR_UNKNOWN}} | {{DATE_OR_NOT_DECIDED}} |

______________________________________________________________________

### Related Docs

[README](../README.md) · [Rules](./rules.md) · [Architecture](./architecture.md)
