# TypeScript Style Baseline

Follow the repository's TypeScript version, formatter, lint rules, and module
system. Do not assume a particular toolchain or treat recommendations below
as CI gates unless configuration or workflows verify them.

## Tooling options

- Formatter/linter: the repository's configured ESLint, Biome, Prettier, or
  equivalent.
- Type checking: the configured TypeScript compiler and `tsconfig` settings.
- Tests: only the runner and command configured by the repository.

## Guidance

- Prefer explicit domain types at module and service boundaries. Avoid
  `any`; use `unknown` and validate when the input is not trusted.
- Keep modules cohesive and APIs narrow. Make asynchronous work, I/O,
  mutation, and dependencies visible in interfaces.
- Use types to express meaningful input constraints and result variants;
  do not add redundant types that obscure straightforward code.
- Handle rejected promises and errors intentionally. Preserve useful context
  and avoid swallowing failures.
- Document public or non-obvious functions when the signature alone does not
  communicate behavior, constraints, outputs, or thrown/rejected errors.

```typescript
/**
 * Loads an account visible to the caller.
 * @param accountId Stable account identifier; must be non-empty.
 * @returns The account, or `undefined` when it is not visible.
 * @throws `AccountServiceError` when the backing service is unavailable.
 */
async function loadAccount(accountId: string): Promise<Account | undefined> {
  // Implementation follows the repository's established boundaries.
}
```
