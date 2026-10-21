# Spec-Driven Development

## Purpose and adoption

This collection supports Spec-Driven Development (SDD) when a project has
adopted the practice or the user requests it; the skills do not impose SDD on
every change. A specification defines intended behavior, not proof that code
implements or verifies it. For a target repository, its existing specification
format and approval process take precedence.

This collection uses `docs/PRD.md` for product-level scope and permanent
requirements. A target project may keep feature specifications in its existing
location or, when requested and no convention exists, use
`docs/specs/<feature-slug>.md`.

## Sources of truth and skill ownership

| Artifact | Role in the workflow |
|---|---|
| [Product requirements](./PRD.md) | Product goals, scope, permanent requirements, and acceptance criteria |
| Existing feature specifications | Detailed behavior for a bounded feature; preserve the established location and ID scheme |
| [Decisions](./decisions.md) | Material decisions, rationale, and consequences |
| [Security profile](./security.md) | Applicable security controls and security requirements |
| Design specification | Applicable interaction, design-system, and accessibility requirements; create only when a UI exists |
| [Test strategy](./tests.md) | Configured test strategy and verification evidence |
| Task plan | Optional task breakdown linked to requirement IDs; create only when requested or already used |

Use `$prd` for product and feature requirements, `$security` for security
requirements, `$design` for interface requirements, `$tests` for verification,
and `$ai-init` for shared documentation and indexes. Each skill changes only
its owned artifacts and sections affected by the request.

## Spec-driven workflow

1. **Discover:** identify the requested behavior, affected paths, existing spec
   source, direct dependencies, and relevant decisions. Ask when scope or
   required behavior cannot be established; do not start with a repository-wide
   inventory for a narrow change.
2. **Specify:** state the problem and outcome, in-scope and out-of-scope
   behavior, scenarios and edge cases, constraints, dependencies, and open
   questions. Give new requirements permanent IDs and observable acceptance
   criteria.
3. **Review:** resolve contradictions and material open questions with the
   requester or documented project approval process. Separate confirmed
   requirements from proposed options; do not invent policy or approval.
4. **Plan:** split accepted requirements into tasks only when the project uses
   a task board or the user requests one. Each task references its requirement
   IDs and has a verifiable completion criterion.
5. **Implement:** make changes against the accepted scope. If evidence requires
   a scope or behavior change, update the specification and obtain any required
   approval before proceeding.
6. **Verify:** map relevant tests or manual checks to acceptance criteria. A
   passing test supports only the behavior it exercises; a specification alone
   never proves implementation.
7. **Maintain:** preserve permanent IDs and update affected specs, decisions,
   security/design guidance, tests, and indexes when behavior changes. Leave
   unrelated documents untouched.

## Feature specification outline

Use the project's established format. If SDD or a separate feature spec is
explicitly requested and no location exists, `$prd` uses
`docs/specs/<feature-slug>.md`. Ask when scope or behavior is unclear.

- **Context and outcome:** the problem, desired user/system outcome, and
  evidence for the need.
- **Scope:** in-scope behavior, non-goals, interfaces, dependencies, and
  compatibility constraints.
- **Scenarios:** normal, boundary, failure, and abuse cases in observable terms.
- **Requirements:** atomic functional and non-functional requirements with
  permanent IDs where the project has an ID scheme.
- **Acceptance and verification:** observable criteria and the test, inspection,
  analysis, or demonstration that verifies each one.
- **Cross-cutting constraints:** applicable security, privacy, accessibility,
  reliability, performance, data, migration, and operational requirements.
- **Design and decisions:** link to existing architecture; record material
  decisions in the decision log, not as duplicate requirements.
- **Risks and open questions:** unresolved choices and their impact; request a
  decision when implementation depends on them.
- **Rollout and recovery:** migration, observability, compatibility, and
  rollback criteria when applicable.

Use RFC 2119/8174 terms only for normative obligations. Prefer explicit
scenarios and acceptance criteria to vague labels such as “secure”, “fast”, or
“user-friendly”. Do not add status, date, owner, evidence, or verification
bookkeeping columns to specification tables.

## Security and cross-cutting requirements

When security is in scope, `$security` derives requirements from the actual
boundary. Consider cryptography/PQC, TLS and certificate validation, container
or Kubernetes/Helm hardening, shell-script safety/logging, identity, secrets,
dependencies, and other controls only when the feature uses them. Do not make a
technology-specific control universal or claim it is enforced unless code,
configuration, or a configured gate proves it.

## Related Docs

[PRD](./PRD.md) · [Decisions](./decisions.md) · [Security](./security.md) · [Tests](./tests.md) · [Usage](./usage.md)
