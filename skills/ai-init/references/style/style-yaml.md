# YAML Style Baseline

Follow the schema and conventions of the consuming tool. The linting and
validation tools below are optional unless configured in the repository's
scripts, hooks, or CI workflows.

## Tooling

- `yamllint` when configured.
- Schema validation where an authoritative schema and supported validator
  exist (for example, Kubernetes manifests).

## Rules

- 2-space indentation, never tabs.
- Use an explicit document start `---` when required by the consumer or
  repository style.
- Use `true`/`false`, never `yes`/`no`/`on`/`off` (yamllint `truthy` rule).
- Keep line lengths readable and follow configured limits.
- Quote strings only when necessary (contain `:`, start with special chars,
  or could be misread as another type).
- Keys: pick one casing convention per file family (e.g., `kebab-case` for
  CI configs, `snake_case` for app configs) and apply consistently.
- Avoid deeply nested anchors/aliases unless documented with a comment
  explaining the reuse.
- No trailing whitespace; file ends with a single newline.
- Used for: GitHub Actions workflows, Kubernetes manifests, docker-compose,
  Helm values, CI/CD configs.
