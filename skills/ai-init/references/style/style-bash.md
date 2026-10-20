# Bash Style Baseline

Apply this language guidance only to Bash scripts. Existing repository
configuration and team conventions take precedence. The tools below are
options, not assumed CI requirements; document them as gates only when a
workflow or pre-commit configuration runs them.

## Tooling options

- Formatter: `shfmt`
- Static analysis: `shellcheck`

## Guidance

- Use an explicit Bash shebang and enable strict modes where compatible with
  the script's expected behavior.
- Quote expansions, prefer `$(...)` to backticks, use arrays for argument
  lists, and avoid `eval` or parsing `ls` output.
- Keep functions focused. Validate required arguments and environment
  variables at boundaries; send actionable errors to stderr.
- Use local variables in functions and document exit behavior when callers
  depend on it.
- Add comments for purpose, non-obvious assumptions, and side effects; do not
  require repetitive boilerplate when the script is self-explanatory.

## Example header

```bash
#!/usr/bin/env bash
# Purpose: Explain the script's responsibility and any important side effect.
# Usage: ./script.sh <input>
set -euo pipefail
```
