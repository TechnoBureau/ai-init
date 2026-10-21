# Security Profile

## Executive Summary

{{PLAIN_LANGUAGE_SUMMARY_OF_SCOPE_AND_EVIDENCED_POSTURE}}

**Assessment scope:** {{REPOSITORY_PATHS_AND_SYSTEM_BOUNDARY}}\
**Assessment type:** {{DESIGN_REVIEW / IMPLEMENTATION_REVIEW / CONFIGURATION_REVIEW / SCAN_REVIEW}}\

This document is not a certification, audit opinion, or compliance
attestation.

**Applicable profiles:** {{NIST_SSDF_AND_CONFIRMED_CONDITIONAL_PROFILES}}

Spell out acronyms and framework names at first mention, including the
National Institute of Standards and Technology (NIST), Federal Information
Processing Standards (FIPS), Security Content Automation Protocol (SCAP),
Center for Internet Security (CIS), International Organization for
Standardization (ISO), Open Worldwide Application Security Project (OWASP),
Application Security Verification Standard (ASVS), and post-quantum
cryptography (PQC). For example: NIST Secure Software Development Framework
(SSDF), SP 800-218, version 1.1. Name the selected version for every
additional framework or benchmark.

State plainly what this review did **not** cover: runtime behavior, production
configuration, staffing, third-party operations, legal compliance, or
penetration testing, as applicable.

## System and Data Scope

| Area | Description |
|---|---|
| System purpose and environments | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Components and trust boundaries | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Identities and access paths | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Data handled and classification | {{CONFIRMED_OR_NOT_DOCUMENTED}} |
| External services and dependencies | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Relevant regulatory or contractual scope | {{CONFIRMED_OR_NOT_DOCUMENTED}} |

### Data classification

| Data type | Classification | Storage / transit | Retention |
|---|---|---|---|
| {{DATA_TYPE_OR_NONE_IDENTIFIED}} | {{PUBLIC_INTERNAL_CONFIDENTIAL_RESTRICTED}} | {{CONFIRMED_OR_NOT_DOCUMENTED}} | {{CONFIRMED_OR_NOT_DOCUMENTED}} |

Use the organization's confirmed classification scheme. Do not infer an
obligation from the presence of data alone.

## Threat Model Summary

Link to the full model when one exists; otherwise state `No threat model
recorded` rather than inventing threats as facts.

| Asset / entry point | Threat (STRIDE/LINDDUN) | Existing mitigation | Residual risk |
|---|---|---|---|
| {{ASSET_OR_INTERFACE}} | {{THREAT_CATEGORY_AND_DESCRIPTION}} | {{CONFIRMED_CONTROL_OR_NONE}} | {{RESIDUAL_RISK_OR_NOT_ASSESSED}} |

Include abuse cases, supply-chain paths, insider risk, and AI/agent-specific
threats where applicable.

## Selected Profiles

| Profile / framework | Exact version | Why selected | Assessed boundary |
|---|---|---|---|
| NIST SSDF | SP 800-218 v1.1 | Secure development lifecycle mapping | {{BOUNDARY}} |
| {{CONFIRMED_PROFILE_OR_NONE}} | {{VERSION}} | {{CONFIRMED_OBLIGATION_OR_RATIONALE}} | {{BOUNDARY}} |

Omit profiles that do not apply instead of listing them as controls. Do not
assume an ISO/IEC 27001, SOC 2, PCI DSS, HIPAA, FedRAMP, or sector obligation
without confirmed scope.

## Control Assessment

Use only `Verified`, `Partial`, `Not evidenced`, `Not assessed`, or
`Not applicable` in the single `Assessment` column, and state the claim type
and its basis in the same cell, for example `Partial (implementation) — CI
logs only`. Do not add separate status, evidence, verification, or owner
columns.

| Profile / control area | Assessment | Current implementation |
|---|---|---|
| Governance and policy | {{CLAIM_TYPE_AND_STATUS}} | {{IMPLEMENTATION_AND_BASIS}} |
| Asset and data inventory | {{CLAIM_TYPE_AND_STATUS}} | {{DESCRIPTION}} |
| Identity and access | {{CLAIM_TYPE_AND_STATUS}} | {{AUTHN_AUTHZ_MFA_LEAST_PRIVILEGE}} |
| Secure development (SSDF) | {{CLAIM_TYPE_AND_STATUS}} | {{REVIEW_AND_SCANNING_PRACTICE}} |
| Supply chain and build integrity | {{CLAIM_TYPE_AND_STATUS}} | {{SBOM_PROVENANCE_SIGNING_STATE}} |
| Vulnerability management | {{CLAIM_TYPE_AND_STATUS}} | {{INTAKE_TRIAGE_SLA_OR_NOT_DECIDED}} |
| Logging and detection | {{CLAIM_TYPE_AND_STATUS}} | {{COVERAGE_RETENTION_INTEGRITY}} |
| Resilience and recovery | {{CLAIM_TYPE_AND_STATUS}} | {{BACKUP_RESTORE_RTO_RPO}} |
| Incident response and disclosure | {{CLAIM_TYPE_AND_STATUS}} | {{RUNBOOK_AND_DISCLOSURE_PRACTICE}} |
| Privacy and data protection | {{CLAIM_TYPE_AND_STATUS}} | {{MINIMIZATION_RETENTION_DPIA}} |
| Third-party and dependency risk | {{CLAIM_TYPE_AND_STATUS}} | {{VENDOR_AND_LICENCE_STATE}} |
| Network transport and TLS (if applicable) | {{CLAIM_TYPE_AND_STATUS}} | {{TLS_TERMINATION_VERSION_CERTIFICATE_AND_CIPHER_EVIDENCE}} |
| Container image/runtime (if applicable) | {{CLAIM_TYPE_AND_STATUS}} | {{IMAGE_SOURCE_DIGEST_PRIVILEGE_AND_SCAN_STATE}} |
| Kubernetes and Helm (if applicable) | {{CLAIM_TYPE_AND_STATUS}} | {{RENDERED_SECURITY_CONTEXT_RBAC_SECRETS_AND_POLICY}} |
| Shell scripts and logging (if applicable) | {{CLAIM_TYPE_AND_STATUS}} | {{SCRIPT_VALIDATION_ERROR_HANDLING_AND_LOG_SAFETY}} |
| Host and cloud hardening | {{CLAIM_TYPE_AND_STATUS}} | {{HOST_OR_CLOUD_BASELINE_AND_SCAN_RESULT}} |
| AI/agent security (if applicable) | {{CLAIM_TYPE_AND_STATUS}} | {{PROMPT_TOOL_DATA_CONTROLS}} |
| {{OTHER_CONFIRMED_PROFILE_AND_CONTROL_AREA}} | {{CLAIM_TYPE_AND_STATUS}} | {{DESCRIPTION}} |

Add rows only for applicable modules. Name the selected framework or
benchmark and version; omit irrelevant profiles instead of marking every
possible control `Not applicable`.

## Cryptographic Inventory and Migration

Include this section only when the repository or confirmed system boundary
uses cryptography. Record observed state separately from approved
configuration; do not invent algorithms, migration dates, or fallback policy.

| Use / protocol | Observed algorithm, key/certificate, library or module | Data lifetime / dependency |
|---|---|---|
| {{VERIFIED_CRYPTO_USE_OR_NONE}} | {{OBSERVED_IMPLEMENTATION_OR_NOT_ASSESSED}} | {{CONFIRMED_CONTEXT}} |

| Migration property | Current state / approved configuration |
|---|---|
| Central algorithm profile / provider switch | {{CONFIG_PATH_OR_NOT_CONFIGURED}} |
| Approved algorithm allowlist and selection policy | {{CONFIRMED_POLICY_OR_NOT_DECIDED}} |
| Fallback allowlist, expiry, and removal condition | {{CONFIRMED_GUARDRAILS_OR_NOT_CONFIGURED}} |
| Negotiation integrity / downgrade resistance | {{OBSERVED_OR_NOT_ASSESSED}} |
| Staged rollout, telemetry, rollback, and key/data migration | {{VERIFIED_PLAN_OR_NOT_DECIDED}} |

Identify FIPS 203 (Module-Lattice-Based Key-Encapsulation Mechanism, ML-KEM)
for key encapsulation and FIPS 204 (Module-Lattice-Based Digital Signature
Algorithm, ML-DSA) or FIPS 205 (Stateless Hash-Based Digital Signature
Algorithm, SLH-DSA) for signatures only when applicable and approved. Link the
current standards and errata. If FIPS 140-3 applies, identify the exact
validated module certificate and operational environment; algorithm use alone
does not establish module validation. Treat draft standards and candidate
algorithms as such.

Do not silently downgrade to a quantum-vulnerable algorithm. Fallback must be
explicitly approved, narrowly scoped, observable, time-bounded, and protected
against downgrade attacks. A rollback must not re-enable a prohibited
algorithm. Only document this as an existing control when configuration and
tests prove it; otherwise label it a proposed action.

## Network Transport and TLS

Include this section only when network endpoints or clients are in scope. Record
the TLS termination boundary; do not infer effective transport controls from an
HTTPS URL or library dependency.

| Surface | Assessment | Observed configuration or limit |
|---|---|---|
| TLS termination and protocol versions | {{ASSESSMENT}} | {{ENDPOINT_OWNER_BOUNDARY_AND_VERSION_EVIDENCE}} |
| Certificate chain, hostname, renewal, and trust | {{ASSESSMENT}} | {{VALIDATION_AND_ROTATION_STATE}} |
| Cipher policy by protocol version | {{ASSESSMENT}} | {{PROVIDER_SPECIFIC_CIPHER_CONFIG_OR_NOT_CONFIGURED}} |
| External API transport and timeouts | {{ASSESSMENT}} | {{HTTPS_VALIDATION_AND_BOUNDED_TIMEOUTS}} |

Prefer TLS 1.3; use TLS 1.2 minimum only when compatible with policy and
supported clients, and disable SSL/TLS 1.0/1.1 where the service controls
negotiation. For TLS 1.3, examples of AEAD suites include
`TLS_AES_128_GCM_SHA256`, `TLS_AES_256_GCM_SHA384`, and
`TLS_CHACHA20_POLY1305_SHA256`; for TLS 1.2, prefer supported ECDHE + AEAD
suites. These are examples, not a universal allowlist. Do not mix TLS 1.2 and
TLS 1.3 cipher names. Identify certificate validation and exceptions; see the
modular baseline for selection criteria.

## Container Image and Runtime Hardening

Include only when Dockerfiles, OCI images, or container runtime settings are in
scope. Assess build-time and deployed controls separately.

| Control area | Assessment | Observed state or gap |
|---|---|---|
| Approved image source, lifecycle, immutable digest, signature/provenance | {{ASSESSMENT}} | {{IMAGE_REFERENCE_AND_VERIFICATION}} |
| Build context, layers, dependency and secret handling | {{ASSESSMENT}} | {{BUILD_CONFIG_AND_SECRET_MECHANISM}} |
| Non-root identity and privilege | {{ASSESSMENT}} | {{USER_PRIVILEGE_CAPABILITY_STATE}} |
| Read-only filesystem, capabilities, seccomp/AppArmor, resource limits | {{ASSESSMENT}} | {{RUNTIME_POLICY_OR_GAP}} |
| Vulnerability scan and SBOM | {{ASSESSMENT}} | {{CONFIGURED_SCAN_AND_ARTIFACT_STATE}} |

Prefer supported minimal images from an approved source; do not require one
vendor registry or floating `latest` tags. Verify deployment digest and runtime
policy, not Dockerfile defaults alone. Never place secrets in image layers,
`ARG`, `ENV`, source, or build logs.

## Kubernetes and Helm Hardening

Include only when Kubernetes manifests, clusters, or Helm charts are in scope.
Inspect rendered manifests as well as chart templates and values.

| Control area | Assessment | Observed state or gap |
|---|---|---|
| Pod/container security context and admission policy | {{ASSESSMENT}} | {{NON_ROOT_PRIVILEGE_CAPABILITY_SECCOMP_STATE}} |
| RBAC, service accounts, and token mounting | {{ASSESSMENT}} | {{LEAST_PRIVILEGE_AND_AUTOMOUNT_STATE}} |
| NetworkPolicy, ingress TLS, and trust boundaries | {{ASSESSMENT}} | {{ENFORCED_POLICY_OR_NOT_ASSESSED}} |
| Image digest, secret source, resources, and probes | {{ASSESSMENT}} | {{RENDERED_WORKLOAD_STATE}} |
| Chart dependencies and rendered-manifest validation | {{ASSESSMENT}} | {{HELM_LINT_SCHEMA_AND_POLICY_CHECKS}} |

Where compatible, verify non-root execution, privilege escalation disabled,
read-only root filesystem, dropped capabilities, and `RuntimeDefault` seccomp.
Record exceptions for host namespaces, host mounts, or privileged workloads.
Keep secrets out of values files and rendered output. A Helm value alone does
not prove cluster enforcement.

## Shell Script Security and Logging

Include only when checked-in scripts or relevant CI shell steps are in scope.

| Control area | Assessment | Observed state or gap |
|---|---|---|
| Input validation, quoting, and command construction | {{ASSESSMENT}} | {{SCRIPT_PATHS_AND_REVIEW_RESULT}} |
| Exit status, error handling, temporary files, cleanup | {{ASSESSMENT}} | {{FAILURE_AND_CLEANUP_BEHAVIOR}} |
| Secret-safe diagnostics and shell tracing | {{ASSESSMENT}} | {{LOGGING_OR_REDACTION_STATE}} |
| Structured logs, access, alerting, and retention | {{ASSESSMENT}} | {{CONFIRMED_RUNTIME_POLICY_OR_NOT_ASSESSED}} |

Never log secrets, tokens, private keys, credentials, or unnecessary personal
data; avoid `set -x` where sensitive values may appear. Prefer safe, concise
stderr diagnostics and explicit exit handling. Use ShellCheck or structured
logging only when configured and supported. Do not invent retention periods.

## Security Requirements for Changes

For security-relevant implementation work, place applicable controls and
observable acceptance criteria in the authoritative PRD, feature spec, issue,
or task before coding. Link relevant requirements to tests. This profile records
control posture; it does not replace the change specification or impose
irrelevant controls.

## Supply Chain and Build Integrity

| Expectation | Observed state | Gap / action |
|---|---|---|
| Dependencies pinned; lockfiles committed | {{VERIFIED_OR_NOT_EVIDENCED}} | {{ACTION_OR_NONE}} |
| SBOM generated (SPDX or CycloneDX, NTIA minimum elements) | {{VERIFIED_OR_NOT_CONFIGURED}} | {{ACTION_OR_NONE}} |
| Artifacts signed and verified | {{VERIFIED_OR_NOT_CONFIGURED}} | {{ACTION_OR_NONE}} |
| Provenance attestation (SLSA v1.x) | {{VERIFIED_OR_NOT_CONFIGURED}} | {{ACTION_OR_NONE}} |
| CI token and release permissions minimized | {{VERIFIED_OR_NOT_EVIDENCED}} | {{ACTION_OR_NONE}} |
| Dependency and licence policy enforced | {{VERIFIED_OR_NOT_CONFIGURED}} | {{ACTION_OR_NONE}} |

Do not claim a provenance level from a workflow file alone. State which
artifacts are built, which identity signs them, and whether verification is
enforced.

## AI and Agent Security

Include only when models, agents, RAG, or tool calling are in scope.

| Control area | Assessment |
|---|---|
| Prompt injection (direct/indirect) | {{ASSESSMENT}} — {{RESIDUAL_RISK}} |
| Tool and file/network permissions | {{ASSESSMENT}} — {{LEAST_PRIVILEGE_STATE}} |
| Human approval for destructive actions | {{ASSESSMENT}} — {{BASIS_OR_GAP}} |
| Sensitive-data handling in prompts/logs | {{ASSESSMENT}} — {{BASIS_OR_GAP}} |
| Model/provider supply chain and version pinning | {{ASSESSMENT}} — {{BASIS_OR_GAP}} |
| Output validation before privileged sinks | {{ASSESSMENT}} — {{BASIS_OR_GAP}} |
| Evaluation and red-team evidence | {{ASSESSMENT}} — {{BASIS_OR_GAP}} |

A skill or tool allowlist is not a sandbox unless the host enforces it.

## Vulnerability and Incident Management

| Area | Confirmed process | Gap |
|---|---|---|
| Vulnerability intake channel | {{VERIFIED_OR_NOT_DOCUMENTED}} | {{GAP_OR_NONE}} |
| Severity and triage method | {{CVSS_EPSS_KEV_OR_NOT_DECIDED}} | {{GAP_OR_NONE}} |
| Remediation timeline | {{CONFIRMED_SLA_OR_NOT_DECIDED}} | {{GAP_OR_NONE}} |
| Exception and risk acceptance | {{VERIFIED_OR_NOT_CONFIGURED}} | {{GAP_OR_NONE}} |
| Incident response and disclosure | {{VERIFIED_OR_NOT_DOCUMENTED}} | {{GAP_OR_NONE}} |

Repository files cannot prove staffing, on-call coverage, or exercised
response. Mark those `Not assessed` unless records exist.

## Platform Hardening Assessment

Include this section only for a supported host/OS/cloud profile in scope;
Docker and Kubernetes/Helm are assessed above. A scan is evidence of assessment,
not proof that the system is compliant or hardened.

| Platform / version | Profile and version | Result and exceptions |
|---|---|---|
| {{VERIFIED_PLATFORM_OR_NONE}} | {{SELECTED_PROFILE_OR_NOT_CONFIGURED}} | {{SUMMARY_OF_PASS_FAIL_NOT_APPLICABLE_AND_EXCEPTIONS}} |

Keep audit findings separate from remediation. Do not apply SCAP remediation
scripts or host changes without an explicit request and an environment-appropriate
impact review.

## Exceptions and Risk Acceptance

| ID | Control / requirement | Rationale | Compensating control |
|---|---|---|---|
| EX-1 | {{CONTROL_ID_OR_NONE}} | {{CONFIRMED_RATIONALE_OR_NOT_DOCUMENTED}} | {{COMPENSATING_CONTROL_OR_NONE}} |

Never invent an accepted exception. If no register exists, state `No risk
acceptance records found`. Record the rule, rationale, and compensating
control only; approval history lives in the pull request.

## Gaps and Proposed Actions

| Gap | Impact | Proposed action | Priority basis |
|---|---|---|---|
| {{EVIDENCED_GAP_OR_NO_GAPS_IDENTIFIED}} | {{WHY_IT_MATTERS_OR_NOT_ASSESSED}} | {{ACTION_OR_NONE}} | {{CONFIRMED_RISK_BASIS_OR_NOT_DECIDED}} |

Keep proposed actions distinct from existing controls. Do not invent risk
ratings, deadlines, or organization-wide requirements.

## Assessment Limits

{{AREAS_NOT_REVIEWED_AND_REASONS_OR_NONE}}

## References

{{LINKS_TO_APPLICABLE_FRAMEWORKS_AND_VERSIONS}}

______________________________________________________________________

### Related Docs

{{RELATED_DOC_LINKS_TO_EXISTING_FILES_OR_NONE}}
