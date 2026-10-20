# .gitignore Standard

Use [`../files/.gitignore`](../files/.gitignore) as the baseline. It is a
reviewed starting point, not a policy: every entry must correspond to an
artifact the repository actually produces or a local file its contributors
actually create.

## Merge rules

1. Read the existing file before writing. Preserve every pattern, comment, and
   section ordering the maintainers chose.
2. Add only the sections that match the detected stack and tooling. The
   baseline covers operating-system metadata, editors, swap and temporary
   files, secrets, logs, compiled output, C and C++, Go, shell, Python,
   Node.js, GitHub output, and agent scratch files.
3. Append missing entries inside the matching section. Do not duplicate an
   entry that is already present under a different comment.
4. Never remove an existing entry merely because this standard would not have
   added it. Remove one only when it hides a tracked file or contradicts a
   confirmed project rule, and report the change.
5. Report which sections were added and which were already present.

If the repository has no `.gitignore`, copy the baseline, then delete sections
for languages it does not use. A smaller accurate file is better than a
speculative one.

## Never ignore

| Category | Examples | Why |
|---|---|---|
| Manifests and lockfiles | `go.mod`, `go.sum`, `package-lock.json`, `Cargo.lock`, `requirements*.txt`, `poetry.lock`, `pom.xml` | Reproducible builds and dependency review depend on them |
| Source and headers | `*.c`, `*.h`, `*.cpp`, `*.hpp`, `*.go`, `*.rs`, `*.sh`, `*.py` | Ignoring source hides work from review and from builds |
| Build definitions | `Makefile`, `CMakeLists.txt`, `meson.build`, `BUILD`, `configure.ac` | The build becomes unreproducible |
| CI and repository configuration | `.github/`, `.editorconfig`, `.gitattributes`, `.pre-commit-config.yaml`, `.markdownlint-cli2.yaml` | Gates silently stop running |
| Documentation and policy | `docs/`, `README.md`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS` | Review and legal obligations depend on them |
| Templates and references | `skills/*/templates/`, `skills/*/references/` | Generated output loses its source |

`.gitignore` is not a security control. A committed secret stays in history
after the file is deleted; rotate it, do not just ignore it.

## Verification

Run these after creating or merging the file:

```bash
git ls-files -ci --exclude-standard   # tracked files matched by an ignore rule: must be empty
git check-ignore -v path/to/file      # show the pattern that matches a path
git status --ignored --short          # review what the repository now hides
```

`git ls-files -ci --exclude-standard` is the gate. Any output means a tracked
file is now ignored. Fix the pattern; do not run `git rm --cached` to make the
warning disappear.

## Pattern cautions

| Pattern | Caution |
|---|---|
| `*.d` | Compiler dependency files for C, but source files for D. Remove the line in a D repository. |
| `*.out` | Linker output and coverage profiles, but some projects commit fixtures with this extension. |
| `*.key`, `*.pem` | Test fixtures need an explicit `!` negation, placed after the broad pattern. |
| `*.orig`, `*.rej` | Merge artifacts, but occasionally committed as review evidence. Check before keeping the rule. |
| `vendor/` | Commented out in the baseline because Go projects normally commit dependencies. |
| `go.work`, `go.work.sum` | Local workspace files. Commit them only when the team deliberately shares a workspace. |
| `build/`, `dist/` | Generated in most ecosystems, but confirm no source directory uses the name. |
| `bin/`, `obj/`, `core` | Deliberately absent from the baseline: they frequently hold committed scripts, modules, or Python packages. |
| `.vscode/`, `.idea/` | Ignored by default. Unignore the exact shared settings file when the team commits one. |

## Section catalogue

| Section | Covers |
|---|---|
| Operating-system metadata | Finder, Spotlight, Trash, Windows Explorer, and recycle-bin artifacts |
| Editors and IDEs | JetBrains, Visual Studio, VS Code, Sublime, Eclipse, Vim, Neovim, Emacs |
| Swap, backup, and temporary files | Editor swap files, lock files, backups, patch rejects, temporary output |
| Secrets and local environment | Environment files, keys, certificates, SSH keys, credential files |
| Logs, cores, and crash dumps | Application logs, core dumps, minidumps, stack traces |
| Compiled output | Object files, libraries, shared objects, executables, symbol files |
| C and C++ | Dependency files, CMake, Autotools, libtool |
| Go | Test binaries, profiles, debug binaries, workspace files |
| Shell | Local history and PID files; shell scripts are never ignored |
| Python | Bytecode, virtual environments, test and type-checker caches, coverage, packaging output |
| Node.js | Installed packages, package-manager caches, debug logs |
| GitHub and CI | Local run output and GitHub Pages builds; workflows and CODEOWNERS stay tracked |
| Agent scratch files | Local agent working directories |
