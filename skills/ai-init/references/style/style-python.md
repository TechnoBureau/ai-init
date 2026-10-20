# Python Style Baseline

Use the project's configured formatter, linter, type checker, and test runner.
Possible tools include Black or Ruff, mypy or Pyright, and pytest, but none is
assumed to be installed or enforced. Check project configuration and CI.

## Rules

- Use type hints and docstrings where they improve public API contracts and
  align with repository conventions. Document meaningful inputs, outputs,
  errors, side effects, and security assumptions.
- Naming: `snake_case` functions/vars, `PascalCase` classes,
  `UPPER_SNAKE_CASE` constants, `_leading_underscore` for internal use.
- Prefer clear, consistent string formatting; follow configured lint rules.
- Use `pathlib.Path`, not `os.path`, for filesystem operations.
- Use context managers (`with`) for all resource handling (files, locks,
  DB connections).
- No mutable default arguments (`def f(x: list = None)`, not `= []`).
- Define public exports explicitly when the package needs a stable API.
- Prefer composition and small pure functions; avoid deep inheritance.
- Use structured/configured logging for application events; reserve `print`
  for command-line output or scripts where appropriate.
- Dataclasses / Pydantic models for structured data, not raw dicts, at
  module boundaries.

## Example module docstring (where useful)

```python
"""Module purpose in one line.

Longer description if needed.
"""
from __future__ import annotations
```
