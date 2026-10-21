# Spec-Driven Development

## Purpose and adoption

Use this workflow only when the project has adopted Spec-Driven Development
(SDD) or the user requests it. Existing repository conventions take precedence.
A specification defines intended behavior; it is not evidence that the behavior
has been implemented or verified.

**Project convention:** {{CONFIRMED_SPEC_SOURCE_AND_ADOPTION_OR_NOT_DECIDED}}

## Sources of truth and skill ownership

| Artifact | Role in the workflow |
|---|---|
| `docs/PRD.md` | Product goals, scope, permanent requirements, and acceptance criteria |
| Existing feature specifications | Detailed behavior for a bounded feature; preserve the established location and ID scheme |
| `docs/decisions.md` | Material decisions, rationale, and consequences |
| `docs/security.md` | Applicable security controls and security requirements |
| `docs/design.md` | Applicable interaction, design-system, and accessibility requirements |
| `docs/tests.md` | Configured test strategy and verification evidence |
| `docs/tasks.md` | Optional task breakdown linked to requirement IDs |

Use `$prd` for product and feature requirements, `$security` for security
requirements, `$design` for interface requirements, `$tests` for verification,
and `$ai-init` for shared documentation and indexes. Each skill changes only
its owned artifacts and the sections affected by the request.

## Spec-driven workflow

1. **Discover:** identify the requested behavior, affected paths, existing spec
   source, direct dependencies, and relevant decisions. Ask when scope or
   required behavior cannot be established; do not start with a repository-wide
   inventory for a narrow change.
2. **Specify:** state the problem and desired outcome, in-scope and out-of-scope
   behavior, scenarios and edge cases, constraints, dependencies, and open
   questions. Give each new requirement a permanent ID and an observable
   acceptance criterion.
3. **Review:** resolve contradictions and material open questions with the
   requester or the project's documented approval process. Separate confirmed
   requirements from proposed options; do not invent policy or approval.
4. **Plan:** split accepted requirements into tasks only when the project uses
   a task board or the user requests one. Each task references its requirement
   IDs and has a verifiable completion criterion.
5. **Implement:** make changes only against the accepted scope. If evidence
   requires a behavior or scope change, update the specification and obtain any
   required approval before proceeding.
6. **Verify:** map relevant tests or manual checks to acceptance criteria. A
   passing test supports only the behavior it exercises; a specification alone
   never proves implementation.
7. **Maintain:** preserve permanent IDs and update affected specs, decisions,
   security/design guidance, tests, and indexes when behavior changes. Leave
   unrelated documents untouched.

## Feature specification outline

For a feature-level specification, use the project's established format. If
SDD or a separate spec is explicitly requested and no location exists, use
`docs/specs/<feature-slug>.md` with these sections. Ask when the scope or
required behavior is unclear.

- **Context and outcome:** problem, intended user or system outcome, and
  evidence for the need.
- **Scope:** explicit in-scope behavior, non-goals, interfaces, dependencies,
  and compatibility constraints.
- **Scenarios:** normal, boundary, failure, and abuse cases in observable terms.
- **Requirements:** atomic functional and non-functional requirements with
  permanent IDs where the project has an ID scheme.
- **Acceptance and verification:** measurable or observable criteria and the
  test, inspection, analysis, or demonstration that verifies each one.
- **Cross-cutting constraints:** security, privacy, accessibility, reliability,
  performance, data handling, migration, and operational requirements that
  apply to this feature.
- **Design and decisions:** link to existing architecture and decision records;
  record material decisions in the decision log, not as duplicate requirements.
- **Risks and open questions:** state unresolved choices and their impact;
  ask for a decision when implementation depends on them.
- **Rollout and recovery:** include migration, observability, compatibility,
  and rollback criteria when applicable.

Use RFC 2119/8174 requirement terms only for normative obligations. Prefer
clear scenarios and explicit acceptance criteria to vague labels such as
"secure", "fast", or "user-friendly". Do not add status, date, owner,
evidence, or verification bookkeeping columns to specification tables.

## Security and cross-cutting requirements

When security is in scope, use `$security` to derive requirements from the
actual boundary. Cover cryptography/PQC, TLS and certificate validation,
container or Kubernetes/Helm hardening, shell-script safety/logging, identity,
secrets, dependencies, and other controls only when the feature uses them.
Do not make a technology-specific control universal or claim that a control is
enforced unless code, configuration, or a configured gate proves it.

## Related Docs

{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}
