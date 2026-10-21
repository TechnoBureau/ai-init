# Spec-Driven Development

## Purpose and adoption

This collection supports Spec-Driven Development (SDD) when a project has
adopted the practice or the user requests it; the skills do not impose SDD on
every change. A specification describes intended behavior, not proof that code
implements or verifies that behavior. For a target repository, its existing
specification, review, and approval conventions take precedence.

This guide is a working aid, not a fixed process or a checklist to paste into
every task. Scale the detail to the change: a small, isolated update may need a
short spec and one focused test, while changes involving identity, sensitive
data, public interfaces, cryptography, migrations, or production operations may
need deeper design, threat, and recovery analysis. Ask a focused question when
an unresolved decision could materially change behavior, risk, or compatibility.
For low-impact, reversible details, state a clear assumption instead of
inventing policy. If a request conflicts with confirmed security policy or
creates a material risk, explain the concern and offer safer options; do not
silently redefine the requirement or take a high-impact action.

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
| [Architecture](./architecture.md) | Existing system boundaries and design context |
| Design specification | Applicable interaction, design-system, and accessibility requirements; create only when a UI exists |
| [Test strategy](./tests.md) | Configured test strategy and verification evidence |
| Task plan | Optional task breakdown linked to requirement IDs; create only when requested or already used |

Use `$prd` for product and feature requirements, `$security` for security
requirements, `$design` for interface requirements, `$tests` for verification,
and `$ai-init` for shared documentation and indexes. Each skill changes only
its owned artifacts and sections affected by the request. Preserve the PRD as
the product-level source of permanent requirements; a feature spec refines it
rather than creating a competing source of truth.

## Spec-driven workflow

1. **Discover:** identify the requested outcome, affected paths, existing spec
   source, direct dependencies, and relevant decisions. For targeted work,
   inspect only the evidence needed to establish impact. Ask before broadening
   when scope cannot be bounded.
2. **Specify:** describe the problem, intended outcome, scope and non-goals,
   relevant scenarios, constraints, dependencies, and open questions. Give new
   requirements permanent IDs where the project has an ID scheme, and make
   acceptance criteria observable.
3. **Review:** resolve contradictions and decisions that materially affect
   behavior, risk, or compatibility with the requester or documented project
   process. Separate confirmed requirements from proposals; do not invent
   approvals or organizational policy.
4. **Plan:** create tasks only when the project uses them or the user requests
   them. Link each task to the relevant requirement IDs and a completion
   criterion.
5. **Implement:** work only against the accepted scope. If evidence requires a
   material change, update the specification and obtain any required approval
   before proceeding.
6. **Verify:** map relevant tests or manual checks to acceptance criteria. A
   passing test supports only the behavior it exercises; a specification alone
   never proves implementation.
7. **Maintain:** preserve permanent IDs and update affected specs, decisions,
   security/design guidance, tests, and indexes when behavior changes. Leave
   unrelated documents untouched.

Keep these stages lightweight for straightforward work; do not skip resolving
material questions before implementation.

## Feature specification outline

Use the project's established format. If SDD or a separate feature spec is
explicitly requested and no location exists, `$prd` uses
`docs/specs/<feature-slug>.md`. Ask when scope or behavior is unclear.
Include only sections that apply to the feature.

- **Context and outcome:** the problem, desired user or system outcome, and
  evidence for the need.
- **Scope and interfaces:** in-scope behavior, non-goals, dependencies,
  compatibility constraints, and API contracts or data models when applicable.
- **Scenarios:** normal, boundary, failure, and abuse cases relevant to the
  feature.
- **Threat and data flow:** for material security or privacy changes, identify
  actors, trust boundaries, sensitive flows, relevant threats, mitigations, and
  residual risks; link or request a threat review from `$security` as needed.
- **Requirements:** atomic functional and non-functional requirements with
  permanent IDs where the project has an ID scheme.
- **Acceptance and verification:** observable criteria and the tests,
  inspection, analysis, or demonstration that would verify each one.
- **Cross-cutting constraints:** applicable security, privacy, accessibility,
  reliability, performance, data handling, migration, and operational needs.
- **Design and decisions:** link to existing architecture; record material
  decisions in the decision log rather than duplicating requirements.
- **Risks and open questions:** unresolved choices, their impact, and any
  decision needed before implementation.
- **Rollout and recovery:** migration, observability, compatibility, and
  rollback criteria when deployment or persistent state makes them relevant.

Use RFC 2119/8174 terms only for normative obligations. Prefer explicit
scenarios and acceptance criteria to vague labels such as “secure”, “fast”, or
“user-friendly”. Keep the spec concise and useful to the people who will build,
review, test, and operate the change. Do not add status, date, owner, evidence,
or verification bookkeeping columns to specification tables.

## Production quality, security, and operations

Use the following areas as prompts for the specification and implementation,
not as requirements that apply to every repository. Select controls based on
the feature boundary, data, architecture, threat, confirmed policy, and
available evidence. OWASP, OpenSSF, CWE, NIST, and SRE guidance are useful
references when relevant; naming a framework does not establish compliance.

- **Identity, input, and APIs:** when identities or sessions are in scope,
  specify authentication, session protection, authorization, and least
  privilege; define token handling and relevant expiry, rotation, or revocation
  behavior. Treat external inputs and service boundaries as untrusted. Network
  location or client-side checks alone do not establish trust. Use layered
  controls where risk warrants them; enforce authorization server-side. At
  input boundaries, define schema, type, range, length, encoding, and allowed
  values as appropriate. Consider injection, traversal, SSRF, XSS, or
  deserialization risks only where the feature exposes those paths; prefer safe
  APIs and parameterized queries over string-built commands or queries. For
  APIs, consider rate limits, idempotency, replay protection, pagination, and
  safe error responses where the behavior warrants them. Browser controls such
  as CSP, CORS, CSRF, and upload limits apply to the relevant web surface, not
  to every service.
- **Data and persistence:** identify sensitive data, purpose, access, retention,
  deletion, and migration needs when the feature stores or processes data. For
  database changes, consider transactions, schema migrations, indexes, and
  least-privilege accounts. Encryption at rest is a boundary and policy decision,
  not a universal checkbox.
- **Cryptography and secrets:** never invent cryptography, hard-code secrets,
  commit credentials, or log secrets. When a feature handles secrets, use the
  repository's approved runtime secret mechanism; use a maintained library and
  secure random generation for keys or tokens. Select algorithms and parameters
  based on the actual use, protocol, platform, and policy, and consider key
  rotation where it applies. Do not mandate one cipher, password-hashing scheme,
  or key size across unrelated systems. If password storage is in scope, never
  store plaintext and choose an approved password KDF; if TLS or long-lived
  public-key data is in scope, assess certificate validation or PQC with
  `$security` rather than copying a generic crypto list.
- **Dependencies and delivery:** use the repository's supported toolchain and
  version policy. Consider vulnerability review, lockfiles, SBOMs, signatures,
  and provenance when they fit the dependency and release process. Do not add a
  scanner, service, dependency, or mandatory age threshold merely because a
  checklist names it; record unsupported evidence as a gap.
- **Standards and compliance:** use the version and controls that match the
  confirmed platform, contract, jurisdiction, or organization policy. Do not
  infer a legal obligation from a technology choice or describe a checklist as
  proof of compliance.
- **Reliability and observability:** for runtime behavior, consider bounded
  timeouts, safe retries/backoff, idempotency, circuit breakers where suitable,
  cleanup, concurrency, resource limits, health/readiness checks, and graceful
  failure as applicable. Logging, metrics, and tracing should follow the
  project's platform conventions and help diagnose relevant events without
  exposing secrets or unnecessary personal data. Do not invent a retention
  period or claim monitoring that is not enforced.
- **Testing and maintainability:** choose unit, integration, contract,
  end-to-end, security, performance, load, or resilience tests according to the
  behavior and risk. Cover meaningful positive, boundary, and failure cases;
  do not chase a coverage percentage without an approved target. Follow local
  code, typing, lint, formatting, and architecture conventions; keep changes
  reviewable and do not add a tool or dependency without a reason.
- **Deployment and recovery:** discuss CI gates, container images, IaC,
  environment separation, immutable artifacts, health probes, and rollback only
  when the change has a relevant build or deployment boundary. Do not generate
  a Dockerfile, pipeline, or infrastructure changes unless the project needs
  them and the user authorizes that scope.

## Review and response

Before completing implementation, review the accepted criteria and the relevant
failure, abuse, security, privacy, and operational paths. Run the narrowest
configured checks that provide evidence; expand them when risk warrants it.
For a deployable or stateful change, consider migration safety, rollback, and
runtime signals. Report what changed and was verified, relevant trade-offs,
remaining gaps, material assumptions, and decisions still needed. Offer follow-up
hardening only for concrete gaps and separate it from requested scope. Do not call
a change “production-ready” or “compliant” based on a checklist alone.

Use the response format the user requested. Otherwise keep the summary concise
and include only sections that help explain this change. Do not force a
15-section report, repeat a generic security checklist, or claim a test, scan,
control, or review that was not performed.

## Related Docs

[PRD](./PRD.md) · [Decisions](./decisions.md) · [Architecture](./architecture.md) · [Security](./security.md) · [Tests](./tests.md) · [Usage](./usage.md)
