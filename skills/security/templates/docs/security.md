# Security Profile — {{PROJECT_NAME}}

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

| Area | Evidence-based description |
|---|---|
| System purpose and environments | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Components and trust boundaries | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Identities and access paths | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Data handled and classification | {{CONFIRMED_OR_NOT_DOCUMENTED}} |
| External services and dependencies | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Relevant regulatory or contractual scope | {{CONFIRMED_OR_NOT_DOCUMENTED}} |

### Data classification

| Data type | Classification | Storage / transit | Retention | Evidence |
|---|---|---|---|---|
| {{DATA_TYPE_OR_NONE_IDENTIFIED}} | {{PUBLIC_INTERNAL_CONFIDENTIAL_RESTRICTED}} | {{CONFIRMED_OR_NOT_DOCUMENTED}} | {{CONFIRMED_OR_NOT_DOCUMENTED}} | `{{PATH}}` |

Use the organization's confirmed classification scheme. Do not infer an
obligation from the presence of data alone.

## Threat Model Summary

Link to the full model when one exists; otherwise state `No threat model
recorded` rather than inventing threats as facts.

| Asset / entry point | Threat (STRIDE/LINDDUN) | Existing mitigation | Residual risk / evidence |
|---|---|---|---|
| {{ASSET_OR_INTERFACE}} | {{THREAT_CATEGORY_AND_DESCRIPTION}} | {{CONFIRMED_CONTROL_OR_NONE}} | {{RESIDUAL_RISK_OR_NOT_ASSESSED}} |

Include abuse cases, supply-chain paths, insider risk, and AI/agent-specific
threats where applicable.

## Selected Profiles

| Profile / framework | Exact version | Why selected | Assessed boundary | Evidence |
|---|---|---|---|---|
| NIST SSDF | SP 800-218 v1.1 | Secure development lifecycle mapping | {{BOUNDARY}} | `{{PATH}}` |
| {{CONFIRMED_PROFILE_OR_NONE}} | {{VERSION}} | {{CONFIRMED_OBLIGATION_OR_RATIONALE}} | {{BOUNDARY}} | `{{PATH}}` |

Omit profiles that do not apply instead of listing them as controls. Do not
assume an ISO/IEC 27001, SOC 2, PCI DSS, HIPAA, FedRAMP, or sector obligation
without confirmed scope.

## Control Status

Use only the statuses `Verified`, `Partial`, `Not evidenced`, `Not assessed`,
or `Not applicable`. Every status must include evidence or an explanation.
State whether each row is a design, implementation, or operating-effectiveness
claim.

| Profile / control area | Claim type | Status | Current implementation | Evidence | Verification / owner |
|---|---|---|---|---|---|
| Governance and policy | {{DESIGN_IMPLEMENTATION_OPERATING}} | {{STATUS}} | {{EVIDENCE_BASED_DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Asset and data inventory | {{TYPE}} | {{STATUS}} | {{DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Identity and access | {{TYPE}} | {{STATUS}} | {{AUTHN_AUTHZ_MFA_LEAST_PRIVILEGE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Secure development (SSDF) | {{TYPE}} | {{STATUS}} | {{REVIEW_AND_SCANNING_EVIDENCE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Supply chain and build integrity | {{TYPE}} | {{STATUS}} | {{SBOM_PROVENANCE_SIGNING_EVIDENCE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Vulnerability management | {{TYPE}} | {{STATUS}} | {{INTAKE_TRIAGE_SLA_OR_NOT_DECIDED}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Logging and detection | {{TYPE}} | {{STATUS}} | {{COVERAGE_RETENTION_INTEGRITY}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Resilience and recovery | {{TYPE}} | {{STATUS}} | {{BACKUP_RESTORE_RTO_RPO}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Incident response and disclosure | {{TYPE}} | {{STATUS}} | {{RUNBOOK_AND_DISCLOSURE_EVIDENCE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Privacy and data protection | {{TYPE}} | {{STATUS}} | {{MINIMIZATION_RETENTION_DPIA}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Third-party and dependency risk | {{TYPE}} | {{STATUS}} | {{VENDOR_AND_LICENCE_EVIDENCE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Platform hardening | {{TYPE}} | {{STATUS}} | {{BASELINE_AND_SCAN_RESULT}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| AI/agent security (if applicable) | {{TYPE}} | {{STATUS}} | {{PROMPT_TOOL_DATA_CONTROLS}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| {{OTHER_CONFIRMED_PROFILE_AND_CONTROL_AREA}} | {{TYPE}} | {{STATUS}} | {{DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |

Add rows only for applicable modules. Name the selected framework or
benchmark and version; omit irrelevant profiles instead of marking every
possible control `Not applicable`.

## Cryptographic Inventory and Migration

Include this section only when the repository or confirmed system boundary
uses cryptography. Record observed state separately from an approved target;
do not invent algorithms, migration dates, or fallback policy.

| Use / protocol | Observed algorithm, key/certificate, library or module | Data lifetime / dependency | Evidence / owner |
|---|---|---|---|
| {{VERIFIED_CRYPTO_USE_OR_NONE}} | {{OBSERVED_IMPLEMENTATION_OR_NOT_ASSESSED}} | {{CONFIRMED_CONTEXT}} | `{{PATH}}` / {{OWNER_OR_UNKNOWN}} |

| Migration property | Current state / approved configuration | Evidence / verification |
|---|---|---|
| Central algorithm profile / provider switch | {{CONFIG_PATH_OR_NOT_CONFIGURED}} | {{VALIDATION_AND_EVIDENCE}} |
| Approved algorithm allowlist and selection policy | {{CONFIRMED_POLICY_OR_NOT_DECIDED}} | {{EVIDENCE}} |
| Fallback allowlist, owner, expiry, and removal condition | {{CONFIRMED_GUARDRAILS_OR_NOT_CONFIGURED}} | {{DOWNGRADE_TEST_OR_NOT_ASSESSED}} |
| Negotiation integrity / downgrade resistance | {{OBSERVED_OR_NOT_ASSESSED}} | {{TEST_OR_EVIDENCE}} |
| Staged rollout, telemetry, rollback, and key/data migration | {{VERIFIED_PLAN_OR_NOT_DECIDED}} | {{VALIDATION_AND_EVIDENCE}} |

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

## Supply Chain and Build Integrity

| Expectation | Observed state | Evidence | Gap / action |
|---|---|---|---|
| Dependencies pinned; lockfiles committed | {{VERIFIED_OR_NOT_EVIDENCED}} | `{{PATH}}` | {{ACTION_OR_NONE}} |
| SBOM generated (SPDX or CycloneDX, NTIA minimum elements) | {{VERIFIED_OR_NOT_CONFIGURED}} | `{{PATH}}` | {{ACTION_OR_NONE}} |
| Artifacts signed and verified | {{VERIFIED_OR_NOT_CONFIGURED}} | `{{PATH}}` | {{ACTION_OR_NONE}} |
| Provenance attestation (SLSA v1.x) | {{VERIFIED_OR_NOT_CONFIGURED}} | `{{PATH}}` | {{ACTION_OR_NONE}} |
| CI token and release permissions minimized | {{VERIFIED_OR_NOT_EVIDENCED}} | `{{PATH}}` | {{ACTION_OR_NONE}} |
| Dependency and licence policy enforced | {{VERIFIED_OR_NOT_CONFIGURED}} | `{{PATH}}` | {{ACTION_OR_NONE}} |

Do not claim a provenance level from a workflow file alone. State which
artifacts are built, which identity signs them, and whether verification is
enforced.

## AI and Agent Security

Include only when models, agents, RAG, or tool calling are in scope.

| Control area | Status | Evidence | Notes |
|---|---|---|---|
| Prompt injection (direct/indirect) | {{STATUS}} | `{{PATH}}` | {{RESIDUAL_RISK}} |
| Tool and file/network permissions | {{STATUS}} | `{{PATH}}` | {{LEAST_PRIVILEGE_EVIDENCE}} |
| Human approval for destructive actions | {{STATUS}} | `{{PATH}}` | {{EVIDENCE_OR_GAP}} |
| Sensitive-data handling in prompts/logs | {{STATUS}} | `{{PATH}}` | {{EVIDENCE_OR_GAP}} |
| Model/provider supply chain and version pinning | {{STATUS}} | `{{PATH}}` | {{EVIDENCE_OR_GAP}} |
| Output validation before privileged sinks | {{STATUS}} | `{{PATH}}` | {{EVIDENCE_OR_GAP}} |
| Evaluation and red-team evidence | {{STATUS}} | `{{PATH}}` | {{EVIDENCE_OR_GAP}} |

A skill or tool allowlist is not a sandbox unless the host enforces it.

## Vulnerability and Incident Management

| Area | Confirmed process | Evidence | Gap |
|---|---|---|---|
| Vulnerability intake channel | {{VERIFIED_OR_NOT_DOCUMENTED}} | `{{PATH}}` | {{GAP_OR_NONE}} |
| Severity and triage method | {{CVSS_EPSS_KEV_OR_NOT_DECIDED}} | `{{PATH}}` | {{GAP_OR_NONE}} |
| Remediation targets | {{CONFIRMED_SLA_OR_NOT_DECIDED}} | `{{PATH}}` | {{GAP_OR_NONE}} |
| Exception and risk acceptance | {{VERIFIED_OR_NOT_CONFIGURED}} | `{{PATH}}` | {{GAP_OR_NONE}} |
| Incident response and disclosure | {{VERIFIED_OR_NOT_DOCUMENTED}} | `{{PATH}}` | {{GAP_OR_NONE}} |

Repository files cannot prove staffing, on-call coverage, or exercised
response. Mark those `Not assessed` unless records exist.

## Platform Hardening Assessment

Include this section only for a supported host/platform profile that is in
scope. A scan is evidence of assessment, not proof that the system is
compliant or hardened.

| Platform / version | SCAP content or CIS/provider profile and version | Scanner/version | Result and exceptions | Evidence |
|---|---|---|---|---|
| {{VERIFIED_PLATFORM_OR_NONE}} | {{SELECTED_PROFILE_OR_NOT_CONFIGURED}} | {{TOOL_VERSION}} | {{SUMMARY_OF_PASS_FAIL_NOT_APPLICABLE_AND_EXCEPTIONS}} | `{{REPORT_OR_CONFIG_PATH}}` |

Keep audit findings separate from remediation. Do not apply SCAP remediation
scripts or host changes without an explicit request and an environment-appropriate
impact review.

## Exceptions and Risk Acceptance

| ID | Control / requirement | Rationale | Compensating control | Owner | Expiry / review date | Status |
|---|---|---|---|---|---|---|
| EX-1 | {{CONTROL_ID_OR_NONE}} | {{CONFIRMED_RATIONALE_OR_NOT_DOCUMENTED}} | {{COMPENSATING_CONTROL_OR_NONE}} | {{OWNER_OR_UNKNOWN}} | {{DATE_OR_NOT_DECIDED}} | {{OPEN_CLOSED_EXPIRED}} |

Never invent an accepted exception. If no register exists, state `No risk
acceptance records found`.

## Gaps and Proposed Actions

| Gap | Impact / evidence | Proposed action | Priority basis | Owner / target |
|---|---|---|---|---|
| {{EVIDENCED_GAP_OR_NO_GAPS_IDENTIFIED}} | {{WHY_IT_MATTERS_OR_NOT_ASSESSED}} | {{ACTION_OR_NONE}} | {{CONFIRMED_RISK_BASIS_OR_NOT_DECIDED}} | {{CONFIRMED_OWNER_AND_DATE_OR_UNKNOWN}} |

Keep proposed actions distinct from existing controls. Do not invent risk
ratings, owners, deadlines, or organization-wide requirements.

## Assessment Limits

{{AREAS_NOT_REVIEWED_AND_REASONS_OR_NONE}}

## References

{{LINKS_TO_APPLICABLE_FRAMEWORKS_AND_VERSIONS}}

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Decisions](./decisions.md)
