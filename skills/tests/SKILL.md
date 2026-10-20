______________________________________________________________________

## name: tests description: > Add, improve, review, or document repository tests using the project's existing test frameworks and verified commands. Use only when test work or docs/tests.md is requested; testing documentation is not part of ai-init's default output.

# Tests

Handle the requested test task using the repository's existing architecture,
test frameworks, and data boundaries. This skill is opt-in; do not create or
refresh `docs/tests.md` as a side effect of ordinary documentation bootstrap.

## Before changes

- Inspect repository instructions, worktree changes, test directories,
  manifests, fixtures, mocks, CI workflows, and exact test commands.
- Preserve existing tests and local changes. Do not replace a suite or test
  configuration wholesale.
- If the user requested test documentation, inspect `docs/tests.md` first and
  preserve useful content. Create it from [the template](./templates/tests.md)
  only when absent.
- If the user requested test code, use the current framework and conventions.
  Do not add dependencies, broad test infrastructure, coverage thresholds, or
  CI gates unless requested or justified by the task.

## Test implementation and execution

- Derive tests from observable behavior and requirements, including relevant
  boundary cases and failures. Avoid asserting private implementation details
  without a clear reason.
- Keep tests isolated and deterministic. Use repository fixtures, fakes, or
  mocks at external boundaries; do not contact production services or mutate
  shared data unless the user explicitly requested and authorized that scope.
- Run the narrowest relevant configured command, expanding to broader checks
  when risk and runtime warrant it. Report the exact command and result; never
  claim tests passed if they were not run.
- For documentation only, record exact configured test, lint, and validation
  commands, workflow filenames/triggers, coverage settings, and gaps. Say
  `Not configured`, `Not evidenced`, or `Not assessed` accurately. Do not
  infer a CI gate from a tool dependency alone.
- In the generated document, retain only related-document links whose target
  files exist; the README remains the main documentation index.

## README agent-entry links

After this skill runs, if root `README.md` exists, ensure
`AGENTS.md` and `CLAUDE.md` are relative symbolic links to it. Inspect each
path first. Leave a correct link unchanged. Preserve regular files or links
with other targets; merge unique instructions into the README before replacing
only when preservation is safe. If uncertain or symlink creation is not
supported, preserve the existing path and report the conflict. Do not create
broken links or copied-file substitutes; remove README links to absent aliases
and report the missing links. If `README.md` is absent, report that
`ai-init` is needed to create the shared index before these aliases can exist.

When the task is test documentation, update root `README.md` to index
`docs/tests.md`; keep it as the single document index and avoid duplicating
the test inventory elsewhere.
