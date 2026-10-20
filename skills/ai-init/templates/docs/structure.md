# Repository Structure — {{PROJECT_NAME}}

> This map must match the repository tree. Include primary directories and
> key active components; omit generated, vendored, and obsolete content unless
> its role is important to understand the build.

## Verified Tree

```text
{{VERIFIED_REPOSITORY_TREE}}
```

## Components

| Path | Responsibility | Active entry point |
|---|---|---|
| `{{EXACT_PATH}}` | {{VERIFIED_PURPOSE}} | `{{REFERENCE_OR_CONFIG_PATH}}` |

## Build and Generated Content

| Path / pattern | Type | Source | Committed? | Notes |
|---|---|---|---|---|
| `{{PATH_OR_PATTERN}}` | {{GENERATED_VENDORED_CACHE_BUILD}} | {{GENERATOR_OR_SOURCE}} | {{YES_NO}} | {{WHY_IT_MATTERS}} |

## Exclusions

{{NOTE_GENERATED_VENDOR_OR_UNREFERENCED_PATHS_OMITTED_AND_WHY_OR_NONE}}

## Naming and Layout Conventions

- Source layout follows: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Test layout follows: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Generated code is handled by: {{VERIFIED_COMMAND_OR_NOT_CONFIGURED}}
- Do not place generated project documentation outside `docs/`, except root
  `README.md` and its symbolic links.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md)
