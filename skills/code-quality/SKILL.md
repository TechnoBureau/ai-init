______________________________________________________________________

## name: code-quality description: > Improve maintainability by safely removing verified dead code and applying modular, documented, testable code practices. Use for explicit cleanup, refactoring, or code-standard tasks.

# Code Quality

Use the target repository's instructions, architecture, language standards,
and configured tooling as the source of truth. Use
[references/engineering-practices.md](./references/engineering-practices.md)
for adaptable decision criteria; do not impose one universal coding standard
on unrelated projects.

## Safe dead-code cleanup

1. Inspect repository instructions, status, build manifests, code generation,
   module exports, entry points, tests, plugins, dependency injection,
   reflection, dynamic imports, serialization, configuration, and deployment
   references before choosing candidates. Review the working-tree diff and
   preserve unrelated or pre-existing user changes; do not overwrite files
   wholesale.
1. Remove only unused declarations supported by reliable evidence such as a
   compiler, configured linter, static analyzer, or a complete reference and
   call-path search. Include unused imports, local variables, private
   functions/classes, dead branches, and dependencies when their removal is
   safe.
1. Treat public APIs, command entry points, event handlers, registered
   plugins, reflection targets, generated code, migrations, and externally
   referenced symbols as live unless usage can be ruled out. Ask or report
   uncertainty before deleting a public contract or behavior.
1. Keep cleanup focused and separate from behavior changes where practical.
   Preserve observable behavior and remove obsolete comments or tests only
   when their associated code is proven obsolete.
1. Follow existing verification instructions and use targeted checks
   appropriate to the touched code. Do not add an unrelated toolchain or
   reformat entire files as part of a narrow cleanup.

## Modular code standard

- Keep modules cohesive around a domain responsibility and expose narrow,
  explicit interfaces. Put parsing, validation, policy, I/O, and orchestration
  at clear boundaries where the codebase supports that separation.
- Use focused functions with clear names and explicit inputs, outputs, errors,
  and side effects. Prefer pure functions where they improve reasoning and
  tests; do not fragment logic into trivial wrappers or add speculative
  abstractions.
- Validate untrusted inputs at trust boundaries. Make error handling
  intentional; preserve useful context and never silently discard failures.
- Avoid hidden mutable global state. Follow the language's type system and
  established patterns for dependency boundaries.
- Add or update behavior tests with behavior changes when required by the
  repository. For refactors, preserve behavior and use existing tests or
  checks when available.

## Function and API documentation

Use language-native doc comments for public APIs and non-obvious functions.
Document the contract, not every line of implementation:

- purpose and relevant preconditions;
- inputs and constraints that are not obvious from names and types;
- return/output semantics;
- errors that callers can handle;
- meaningful side effects, resource ownership, concurrency, or security
  assumptions.

Comments in function bodies should explain why a non-obvious decision or
constraint exists. If code requires comments to describe ordinary control
flow, simplify the code or improve names instead. Do not duplicate type
signatures in prose.

## Scope boundary

This is a code-change skill. Do not run it as a side effect of documentation
generation. The user must have requested cleanup, refactoring, or code
standards work. If code ownership, dynamic use, public compatibility, or
security impact is unclear, preserve the code and report the uncertainty.

## README agent-entry links

After this skill runs, if root `README.md` exists, ensure
`AGENTS.md` and `CLAUDE.md` are relative symbolic links to it. Inspect each
path first. Preserve regular files or links to other targets; merge unique
instructions into the README before replacing only when safe. If preservation
is uncertain or symlink creation is unsupported, do not replace the path and
report the conflict. Never create broken links or copied-file substitutes;
remove README links to absent aliases and report the missing links.
If README is absent, report that `ai-init` is needed to create the shared
index. Do not otherwise edit README content for a code-only change; preserving
unique instructions or removing links to absent aliases while satisfying the
requested alias behavior is the only exception.
