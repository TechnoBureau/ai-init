# Security Profile — {{PROJECT_NAME}}

> Summarize the current repository security posture for engineering, security,
> operations, product, and leadership readers. This document is not a
> certification or compliance attestation.

## Executive Summary

{{PLAIN_LANGUAGE_SUMMARY_OF_SCOPE_AND_EVIDENCED_POSTURE}}

**Assessment scope:** {{REPOSITORY_PATHS_AND_SYSTEM_BOUNDARY}}\
**Assessment date:** {{DATE}}\
**Applicable profiles:** {{NIST_SSDF_AND_CONFIRMED_CONDITIONAL_PROFILES}}

Spell out acronyms and framework names at first mention, including the
National Institute of Standards and Technology (NIST), Federal Information
Processing Standards (FIPS), Security Content Automation Protocol (SCAP),
Center for Internet Security (CIS), and Open Worldwide Application Security
Project (OWASP), Application Security Verification Standard (ASVS), and
post-quantum cryptography (PQC). For example: NIST Secure Software
Development Framework (SSDF), SP 800-218, version 1.1. Name the selected
version for every additional framework or benchmark.

## System and Data Scope

| Area | Evidence-based description |
|---|---|
| System purpose and environments | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| Data handled and classification | {{CONFIRMED_OR_NOT_DOCUMENTED}} |
| Trust boundaries and identities | {{VERIFIED_OR_NOT_DOCUMENTED}} |
| External services and dependencies | {{VERIFIED_OR_NOT_DOCUMENTED}} |

## Control Status

Use only the statuses `Verified`, `Partial`, `Not evidenced`, `Not assessed`,
or `Not applicable`. Every status must include evidence or an explanation.

| Profile / control area | Status | Current implementation | Evidence | Verification / owner |
|---|---|---|---|---|
| Post-quantum cryptography readiness (if cryptography exists) | {{STATUS}} | {{INVENTORY_AND_GAP}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| Cryptographic agility / algorithm configuration (if applicable) | {{STATUS}} | {{PROFILE_SWITCH_FALLBACK_AND_DOWNGRADE_EVIDENCE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| FIPS 140-3 module validation (only if required) | {{STATUS}} | {{MODULE_CERTIFICATE_AND_SCOPE_OR_NOT_APPLICABLE}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| NIST SSDF — Prepare the Organization | {{STATUS}} | {{EVIDENCE-BASED DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| NIST SSDF — Protect the Software | {{STATUS}} | {{EVIDENCE-BASED DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| NIST SSDF — Produce Well-Secured Software | {{STATUS}} | {{EVIDENCE-BASED DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| NIST SSDF — Respond to Vulnerabilities | {{STATUS}} | {{EVIDENCE-BASED DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| OpenSCAP / SCAP host hardening (only if platform is supported) | {{STATUS}} | {{OS_PROFILE_CONTENT_VERSION_AND_SCAN_RESULT}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| CIS / provider baseline (only if in scope) | {{STATUS}} | {{SELECTED_BASELINE_AND_VERSION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| OWASP application profile (only if applicable) | {{STATUS}} | {{SELECTED_PROFILE_VERSION_AND_LEVEL}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |
| {{OTHER_CONFIRMED_PROFILE_AND_CONTROL_AREA}} | {{STATUS}} | {{DESCRIPTION}} | `{{PATH}}` | {{CHECK_AND_OWNER_OR_UNKNOWN}} |

Add rows only for applicable modules. Name the selected framework or
benchmark and version; omit irrelevant profiles instead of listing them as
controls.

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

## Gaps and Proposed Actions

| Gap | Impact / evidence | Proposed action | Owner / target |
|---|---|---|---|
| {{EVIDENCED_GAP_OR_NO_GAPS_IDENTIFIED}} | {{WHY_IT_MATTERS_OR_NOT_ASSESSED}} | {{ACTION_OR_NONE}} | {{CONFIRMED_OWNER_AND_DATE_OR_UNKNOWN}} |

Keep proposed actions distinct from existing controls. Do not invent risk
ratings, owners, deadlines, or organization-wide requirements.

## Assessment Limits

{{AREAS_NOT_REVIEWED_AND_REASONS_OR_NONE}}

## References

{{LINKS_TO_APPLICABLE_FRAMEWORKS_AND_VERSIONS}}

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./Architecture.md) · [Decisions](./decisions.md)
