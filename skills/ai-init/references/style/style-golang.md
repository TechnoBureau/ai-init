# Go Style Baseline

Use the repository's `gofmt` conventions and configured tools. The following
are optional checks, not assumed CI gates: `go vet`, `go test`,
`golangci-lint`, and the race detector. Verify `go.mod`, tool configuration,
and workflows before documenting commands as active.

## Rules

- Package names: short, lowercase, no underscores, no stutter
  (`http.Client`, not `http.HTTPClient`).
- Document exported identifiers with Go doc comments, especially when
  behavior or constraints are not obvious from the name and type.
- Errors: wrap with context, never swallow:
  `fmt.Errorf("fetching user %d: %w", id, err)`.
- No `panic` in library/application code paths — reserve for truly
  unrecoverable init-time failures.
- When a function accepts `context.Context`, conventionally name it `ctx`
  and place it first.
- Keep interfaces small (prefer 1-3 methods); accept interfaces, return
  structs.
- Avoid hidden global mutable state; make dependencies and side effects
  explicit at module boundaries.
- Use table-driven tests where they make cases clearer. Use parallel tests
  only when shared state and cleanup make that safe.
- Avoid deep nesting — return early on error (guard clauses).
- Struct field alignment/order: group by purpose, not just gofmt spacing.
- Document important performance tradeoffs, concurrency assumptions, and
  caller-visible errors.

## Required file header (internal/proprietary packages)

```go
// Package foo implements ...
package foo
```
