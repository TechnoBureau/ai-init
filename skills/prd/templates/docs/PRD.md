# Product Requirements Document

Existing Markdown can preserve requirement ID history but is not evidence that
a behavior is implemented. Keep exactly the ten sections below.

## 1. Overview

**Summary:** {{CONCISE_PRODUCT_SUMMARY}}

**Core problem:** {{EVIDENCED_PROBLEM}}

**Value proposition:** {{EVIDENCED_VALUE}}

**Stakeholders:** {{CONFIRMED_STAKEHOLDERS_OR_NOT_DOCUMENTED}}

**Constraints:** {{CONFIRMED_TECHNICAL_ORGANIZATIONAL_CONSTRAINTS_OR_NONE}}

**Dependencies:** {{CONFIRMED_DEPENDENCIES_OR_NONE}}

**Assumptions:** {{CONFIRMED_ASSUMPTIONS_OR_NONE}}

If the repository is empty or scaffold-only, state that no product goals,
users, requirements, or workflows are recorded yet. Mark unknowns `Not
decided`; do not fill this section with a generic product narrative.

## 2. Product Type

{{INTERNAL_DEVOPS_PLATFORM_SERVICE_LIBRARY_APP_OR_OTHER}}

State the basis for the classification (for example, a deployable service
manifest, a published package, or a UI entry point). If the type is ambiguous,
name the closest supported type and what evidence is missing.

## 3. Goals and Objectives

| ID | Outcome |
|---|---|
| G-1 | {{MEASURABLE_OUTCOME}} |

If no goal is confirmed, replace the example row with `No confirmed goals
recorded`; do not assign a G-ID to a placeholder. State the outcome only; do
not invent a measure, threshold, or date.

## 4. Scope

### In Scope

- {{IN_SCOPE_CAPABILITY}}

### Out of Scope

- {{EXPLICITLY_OUT_OF_SCOPE_OR_NOT_DOCUMENTED}}

### Boundaries and Dependencies

- External systems and interfaces: {{CONFIRMED_OR_NOT_DOCUMENTED}}
- Supported platforms and versions: {{CONFIRMED_OR_NOT_DOCUMENTED}}
- Data handled: {{CONFIRMED_DATA_TYPES_OR_NOT_DOCUMENTED}}

## 5. Architectural Decisions

| ID | Decision | Reason |
|---|---|---|
| D-1 | {{DECISION}} | {{REASON_OR_NOT_DOCUMENTED}} |

If there are no decisions, state `No decisions recorded yet` and remove the
example row. Do not create a D-ID for an implementation observation unless the
PRD clearly distinguishes it from an approved decision. Never recycle a
retired ID.

See `decisions.md` for context and consequences. Preserve
existing D-IDs when refining this document. Do not invent a reason.

## 6. User Personas

| Persona | Responsibilities | Needs |
|---|---|---|
| {{EVIDENCED_PERSONA}} | {{RESPONSIBILITIES}} | {{NEEDS}} |

Include operational, security, audit, and accessibility perspectives when the
evidence supports them. If no persona is confirmed or evidenced, state `Not
documented` and remove the example row. Do not invent demographic detail.

## 7. Functional Requirements

### {{MODULE_NAME}}

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-1 | {{ATOMIC_NORMATIVE_BEHAVIOR}} | {{OBSERVABLE_ACCEPTANCE_CRITERION}} |

If no functional requirement is confirmed or evidenced, state `No confirmed
functional requirements recorded` and remove the example row.

Group requirements by real repository module. Keep FR-IDs permanent and
sequential for new requirements; do not reuse retired IDs. Apply these rules:

- one testable obligation per requirement;
- use `MUST`, `SHOULD`, or `MAY` consistently with RFC 2119/8174;
- define domain terms and units;
- state authorization, validation, data, and error behavior where relevant;
- do not prescribe internal implementation unless it is a confirmed decision;
- do not add priority tiers.

### Traceability Summary

| Requirement | Acceptance criterion | Test | Level | Coverage |
|---|---|---|---|---|
| FR-1 | {{CRITERION}} | `{{TEST_PATH_OR_MANUAL_PROCEDURE}}` | {{LEVEL}} | {{COVERED_PARTIAL_GAP}} |

A `Covered` entry requires a runnable or executed artifact. Do not claim
coverage from a test name alone. Record gaps explicitly in the same cell.

When SDD is adopted, feature specifications refine these product-level
requirements; they do not replace the PRD or duplicate its permanent IDs. Link
features to the relevant FR/NFR IDs and trace their acceptance criteria to tests.

## 8. Non-Functional Requirements

| ID | Category | Requirement | Assessment |
|---|---|---|---|
| NFR-1 | {{SECURITY_PRIVACY_RELIABILITY_PERFORMANCE_ACCESSIBILITY_OPERABILITY}} | {{QUALITY_OR_CONSTRAINT}} | {{VERIFIED_PARTIAL_NOT_EVIDENCED_NOT_ASSESSED}} |

If no non-functional requirement is confirmed or evidenced, state `No
confirmed non-functional requirements recorded` and remove the example row.

Consider and record the disposition of each applicable category. Include only
requirements supported by evidence or a confirmed decision; do not fabricate
SLOs, coverage percentages, latency budgets, or compliance targets.

| Category | Applicable? | Confirmed obligation or gap |
|---|---|---|
| Security | {{YES_NO_NOT_ASSESSED}} | {{CONFIRMED_CONTROL_OR_GAP}} |
| Privacy and retention | {{YES_NO_NOT_ASSESSED}} | {{CONFIRMED_OBLIGATION_OR_NOT_DOCUMENTED}} |
| Reliability and availability | {{YES_NO_NOT_ASSESSED}} | {{SLO_OR_NOT_DECIDED}} |
| Performance and capacity | {{YES_NO_NOT_ASSESSED}} | {{BUDGET_OR_NOT_DECIDED}} |
| Accessibility | {{YES_NO_NOT_ASSESSED}} | {{TARGET_LEVEL_OR_NOT_SELECTED}} |
| Observability | {{YES_NO_NOT_ASSESSED}} | {{SIGNALS_OR_NOT_DOCUMENTED}} |
| Maintainability | {{YES_NO_NOT_ASSESSED}} | {{CONFIGURED_CHECKS_OR_GAP}} |
| Portability and compatibility | {{YES_NO_NOT_ASSESSED}} | {{SUPPORTED_MATRIX_OR_NOT_DOCUMENTED}} |
| Compliance | {{YES_NO_NOT_ASSESSED}} | {{CONFIRMED_SCOPE_OR_NONE}} |
| Localization | {{YES_NO_NOT_ASSESSED}} | {{LOCALES_OR_NOT_DOCUMENTED}} |

## 9. Pipeline / Workflow Inventory

| Filename | Trigger | Deploys to |
|---|---|---|
| `{{EXACT_REPOSITORY_PATH}}` | {{CONFIGURED_EVENT_OR_SCHEDULE}} | {{CONFIGURED_ARTIFACT_SERVICE_OR_ENVIRONMENT}} |

Include only pipelines and workflows found in repository configuration. State
`No pipelines configured` when none exist. Do not infer a trigger from a
workflow name or badge.

## 10. Repository Structure

```text
{{VERIFIED_PRIMARY_DIRECTORY_AND_COMPONENT_TREE}}
```

See `structure.md` for the fuller verified repository map.

______________________________________________________________________

### Related Docs

{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}
