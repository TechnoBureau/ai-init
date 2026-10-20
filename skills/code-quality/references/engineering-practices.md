# Repository-Fit Engineering Practices

Apply the target repository's instructions and architecture first. Use the
language's official documentation, established ecosystem conventions, and
project-configured checks when a decision depends on a specific language or
framework. These criteria are adaptable; they are not a universal policy.

## Modularity and interfaces

- Keep modules cohesive around a real responsibility and expose narrow,
  explicit interfaces.
- Make data flow, dependencies, I/O, mutation, and trust boundaries visible.
- Prefer focused functions and a clear control flow. Avoid both oversized
  routines and excessive fragmentation into trivial wrappers.
- Avoid speculative abstractions. Extract shared code when there is a stable,
  evidenced reuse pattern or a meaningful boundary.

## Function and API contracts

Document public APIs and non-obvious functions in the language's native
format. Describe contract details that the signature does not make clear:

- purpose and relevant preconditions;
- input constraints, units, valid ranges, and ownership where relevant;
- return/output semantics, including empty or partial results;
- caller-relevant errors or exceptions;
- meaningful side effects, resource ownership, concurrency, and security
  assumptions.

Use comments to explain rationale, invariants, compatibility constraints, or
security decisions—not to narrate visible code. Improve names or simplify
control flow when comments are needed to explain ordinary operations.

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
