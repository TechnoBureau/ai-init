# Repository-Fit Engineering Practices

Apply the target repository's instructions and architecture first. Use the
language's official documentation, established ecosystem conventions, and
project-configured checks when a decision depends on a specific language or
framework. These criteria are adaptable; they are not a universal policy.

## Quality model

Use ISO/IEC 25010:2023 to name the quality attribute a change affects instead
of arguing from taste. Relevant attributes include functional suitability,
performance efficiency, compatibility, usability, reliability, security,
maintainability, flexibility, and safety. Not every attribute applies to every
change; state the trade-off explicitly.

## Modularity and interfaces

- Keep modules cohesive around a real responsibility and expose narrow,
  explicit interfaces.
- Make data flow, dependencies, I/O, mutation, and trust boundaries visible.
- Prefer focused functions and a clear control flow. Avoid both oversized
  routines and excessive fragmentation into trivial wrappers.
- Avoid speculative abstractions. Extract shared code when there is a stable,
  evidenced reuse pattern or a meaningful boundary.
- Keep dependency direction intentional. Domain policy should not depend on
  transport, persistence, or presentation details unless the existing
  architecture says otherwise.
- Make side effects explicit. Separate calculation from I/O where the language
  and codebase make that practical.

## Complexity and readability

- Prefer guard clauses and early returns to deep nesting.
- Keep functions understandable at a glance. A configurable complexity limit
  (for example cyclomatic complexity at or below 10) is a review trigger, not a
  universal law; use the repository's configured threshold when one exists.
- Name by domain intent, not implementation mechanics. Avoid abbreviations that
  require tribal knowledge.
- Avoid boolean parameter flags that make call sites ambiguous; use named
  options or separate functions when it improves clarity.
- Keep comments about rationale, invariants, compatibility, and security
  decisions. Delete comments that restate the code.
- Do not mix large mechanical reformatting with behavioral change.

## Function and API contracts

Document public APIs and non-obvious functions in the language's native
format. Describe contract details that the signature does not make clear:

- purpose and relevant preconditions;
- input constraints, units, valid ranges, and ownership where relevant;
- return/output semantics, including empty or partial results;
- caller-relevant errors or exceptions;
- meaningful side effects, resource ownership, concurrency, and security
  assumptions;
- deprecation status and replacement.

Use comments to explain rationale, invariants, compatibility constraints, or
security decisions—not to narrate visible code. Improve names or simplify
control flow when comments are needed to explain ordinary operations.

## Secure coding

- Authenticate and authorize at the server or trust boundary that owns the
  resource; do not rely on client behavior.
- Validate untrusted input against an allowlist of expected shape, size, and
  range. Canonicalize paths and identifiers before authorization checks.
- Encode for the destination sink: SQL parameters, HTML/attribute encoding,
  URL encoding, shell argument arrays, and safe deserialization.
- Never construct shell commands, SQL, LDAP filters, or templates from
  untrusted strings.
- Fail closed. Handle denied, expired, and unavailable states without exposing
  protected data.
- Use constant-time comparison and approved cryptographic libraries for secret
  material. Do not invent algorithms, modes, or key derivation.
- Avoid unbounded reads, decompression, recursion, and concurrency. Bound
  resource use and timeouts.
- Redact secrets and personal data from logs, traces, errors, and metrics.
- Check CWE Top 25 and the repository's confirmed OWASP ASVS level when
  reviewing security-relevant code. Do not claim compliance from review alone.

## Error handling and resilience

- Preserve context while wrapping errors; never swallow a failure silently.
- Distinguish retryable from terminal errors. Retry with bounded attempts,
  exponential backoff, jitter, and idempotency protection.
- Set timeouts and cancellation for network and resource operations.
- Avoid retry storms and unbounded queues.
- Make partial failure states explicit; do not report success before durable
  commit where the contract requires it.
- Clean up resources with the language's deterministic mechanism (context
  managers, `defer`, `try-with-resources`, RAII, `using`).

## Concurrency

- Prefer immutable data and message passing where idiomatic.
- Document ownership, locking, and ordering assumptions.
- Avoid holding locks across I/O.
- Ensure shared mutable state is protected and tested under contention.
- Use the race detector or concurrency tests when the language supports them.

## Dependencies

- Prefer the standard library or an existing vetted dependency.
- Check maintenance status, licence, transitive size, and known
  vulnerabilities before adding a dependency.
- Follow the repository's lockfile and pinning policy; never introduce
  floating `latest` versions in reproducible builds.
- Remove unused dependencies after verifying dynamic loading and build tags.
- Record vendored code with upstream source, version, licence, and update
  procedure.

## API and schema compatibility

- Apply Semantic Versioning to published contracts.
- Prefer additive schema changes. Removing or renaming a field, changing a
  type, tightening validation, or changing default behavior is breaking.
- For HTTP, use `Deprecation` and `Sunset` headers (RFC 9745 and RFC 8594) and
  keep a migration window.
- For events, preserve consumer compatibility and document ordering,
  idempotency, and delivery semantics.
- Validate OpenAPI/AsyncAPI/JSON Schema in CI when they are the source of
  truth.
- Keep errors machine-readable and stable; do not leak implementation details.

## Observability

- Use structured logs with stable event names and correlation identifiers.
- Follow the project's metrics and tracing conventions, such as OpenTelemetry
  semantic conventions. Avoid unbounded label cardinality.
- Instrument critical decisions: authorization denials, retries, queue depth,
  saturation, and dependency latency.
- Never log credentials, tokens, session identifiers, full request bodies, or
  personal data.
- Ensure alerts are actionable and linked to a runbook where one exists.

## Dead-code cleanup

- Use configured compilers, analyzers, reference searches, and call-path
  evidence together; no single “unused” warning proves a symbol is safe to
  delete.
- Check dynamic imports, reflection, plugin registration, dependency
  injection, serialization, generated code, public exports, external callers,
  build tags, and platform-specific branches.
- Remove verified unused imports, variables, private functions/types,
  unreachable branches, and dependencies only within the requested scope.
- Preserve behavior, public compatibility, and unrelated local changes. Keep
  cleanup focused, then run the repository's relevant checks.
- Delete tests only when the corresponding behavior is proven obsolete; do not
  remove a test because it is inconvenient.

## Code review checklist

- The change addresses one stated problem and preserves unrelated behavior.
- Boundary conditions, error paths, and authorization are tested.
- Inputs are validated and outputs encoded at the correct boundary.
- Public contracts, versions, and migrations are handled.
- Resource use, timeouts, retries, and concurrency are bounded.
- Logs and errors are useful without exposing sensitive data.
- Dependencies and permissions are necessary and justified.
- The diff is minimal and the commit message explains the why.
