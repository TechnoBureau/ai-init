# Product Requirements Document — {{PROJECT_NAME}}

> Build this from source code, manifests, workflows, tests, and configuration.
> Existing Markdown can preserve requirement ID history but is not evidence
> that a behavior is implemented. Keep exactly the ten sections below.

## 1. Overview

**Summary:** {{CONCISE_PRODUCT_SUMMARY}}

**Core problem:** {{EVIDENCED_PROBLEM}}

**Value proposition:** {{EVIDENCED_VALUE}}

## 2. Product Type

{{INTERNAL_DEVOPS_PLATFORM_SERVICE_LIBRARY_APP_OR_OTHER}}

## 3. Goals and Objectives

| ID | Outcome | Measure / verification |
|---|---|---|
| G-1 | {{MEASURABLE_OUTCOME}} | {{EVIDENCED_MEASURE_OR_TBD}} |

If no goal is confirmed, replace the example row with `No confirmed goals recorded`; do not assign a G-ID to a placeholder.

## 4. Scope

### In Scope

- {{IN_SCOPE_CAPABILITY}}

### Out of Scope

- {{EXPLICITLY_OUT_OF_SCOPE_OR_NOT_DOCUMENTED}}

## 5. Architectural Decisions

| ID | Decision | Reason | Alternatives Rejected |
|---|---|---|---|
| D-1 | {{DECISION}} | {{EVIDENCE_OR_NOT_DOCUMENTED}} | {{EVIDENCE_OR_NOT_DOCUMENTED}} |

If there are no decisions, state `No decisions recorded yet` and remove the
example row. Do not create a D-ID for an implementation observation unless
the PRD clearly distinguishes it from an approved decision.

See [decisions.md](./decisions.md) for supporting context. Preserve existing
D-IDs when refining this document. Do not invent reasons or rejected
alternatives.

## 6. User Personas

| Persona | Responsibilities | Needs |
|---|---|---|
| {{EVIDENCED_PERSONA}} | {{RESPONSIBILITIES}} | {{NEEDS}} |

If no persona is confirmed or evidenced, state `Not documented` and remove
the example row.

## 7. Functional Requirements

### {{MODULE_NAME}}

| ID | Requirement | Evidence / verification |
|---|---|---|
| FR-1 | {{CLEAR_BEHAVIOR}} | {{CODE_PATH_OR_VERIFICATION}} |

If no functional requirement is confirmed or evidenced, state `No confirmed functional requirements recorded` and remove the example row.

Group requirements by real repository module. Keep FR-IDs permanent and
sequential for new requirements; do not reuse retired IDs.

## 8. Non-Functional Requirements

| ID | Requirement | Verification criteria |
|---|---|---|
| NFR-1 | {{QUALITY_OR_CONSTRAINT}} | {{CONCRETE_CHECK_WITHOUT_INVENTED_THRESHOLD}} |

If no non-functional requirement is confirmed or evidenced, state `No confirmed non-functional requirements recorded` and remove the example row.

## 9. Pipeline / Workflow Inventory

| Filename | Trigger | Target |
|---|---|---|
| `{{EXACT_REPOSITORY_PATH}}` | {{CONFIGURED_EVENT_OR_SCHEDULE}} | {{CONFIGURED_ARTIFACT_SERVICE_OR_ENVIRONMENT}} |

Include only pipelines and workflows found in repository configuration.

## 10. Repository Structure

```text
{{VERIFIED_PRIMARY_DIRECTORY_AND_COMPONENT_TREE}}
```

See [structure.md](./structure.md) for the fuller verified repository map.

______________________________________________________________________

### Related Docs

[README](../README.md) · [Architecture](./Architecture.md) · [Decisions](./decisions.md) · [Security](./security.md)
