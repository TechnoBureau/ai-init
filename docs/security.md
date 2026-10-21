# Security Profile

## Executive Summary

This repository distributes agent instructions and templates; it runs no
service and handles no personal or customer data. Its material security risks
are integrity and supply chain: a corrupted `SKILL.md` makes a skill
undiscoverable, and a malicious instruction could cause an agent to expose
secrets or take destructive action in a target repository.

The posture is strong for integrity and secret hygiene, because the format and
content are gated automatically. Detection and operating effectiveness are
limited: there is no runtime telemetry, no incident exercise, and no formal
risk-acceptance register. Those areas are marked accordingly rather than
implied to be complete.

**Assessment scope:** the repository tree, skills, templates, references,
scripts, tests, and CI configuration.\
**Assessment type:** design and implementation review of repository content; no
runtime or production testing.\

This document is not a certification, audit opinion, or compliance
attestation.

**Applicable profiles:** NIST SSDF (SP 800-218 v1.1) practice mapping, OWASP
supply-chain and secrets guidance, and CIS-style repository hygiene where it
maps to configured controls.

## System and Data Scope

| Area | Description |
|---|---|
| System purpose and environments | Static content plus Python validation tooling; contributor workstations and GitHub Actions |
| Components and trust boundaries | Skills, templates, scripts, tests, CI; the target repository is untrusted input |
| Identities and access paths | Repository maintainers via GitHub; CI with read-only token; no service accounts |
| Data handled and classification | Public repository content only; no personal, financial, or health data |
| External services and dependencies | PyPI (PyYAML, pre-commit), GitHub Actions, pre-commit hook repositories, npm for markdownlint-cli2 |
| Relevant regulatory or contractual scope | None confirmed |

### Data classification

| Data type | Classification | Storage / transit | Retention |
|---|---|---|---|
| Skill instructions and templates | Public | Git repository | Git history |
| Generated documentation | Public | Git repository | Git history |
| Development dependencies | Public | `requirements-dev.txt`, pinned workflow actions | Updated by Dependabot |
| Secrets or personal data | None identified | Not present | Not applicable |

The classification above describes the system's data. This document carries no
control block or document classification.

## Threat Model Summary

Full detail is in [threat-model.md](./threat-model.md).

| Asset / entry point | Threat (STRIDE/LINDDUN) | Existing mitigation | Residual risk |
|---|---|---|---|
| `SKILL.md` metadata | Tampering | Strict validator, regression test, CI gate | A bypassed hook is caught by CI; a compromised CI is out of scope |
| Agent instructions | Spoofing / Elevation | Operating constraints, scope boundaries, review | Model behavior is probabilistic; instructions reduce, not eliminate |
| Repository secrets | Information disclosure | gitleaks, IBM detect-secrets baseline, private-key detection, explicit prohibition | Secrets already present could be copied; keyword-only secrets are missed |
| CI workflow | Tampering | Version-pinned actions, read-only permissions, Dependabot review | A tag can be moved upstream before the next review |
| Generated documentation | Repudiation (overclaim) | Claim-status vocabulary, anti-overclaim rules, review checklist | Reviewer may accept unsupported prose |

## Selected Profiles

| Profile / framework | Exact version | Why selected | Assessed boundary |
|---|---|---|---|
| NIST SSDF | SP 800-218 v1.1 | Secure development practice mapping | Repository content and CI |
| OWASP Software Supply Chain Security | Current cheat sheet | Dependencies, actions, and hooks are consumed | Dependency and workflow configuration |
| OWASP Secrets Management | Current cheat sheet | Skills may read repositories that contain secrets | Operating constraints and scanning |

ISO/IEC 27001, SOC 2, PCI DSS, FedRAMP, and sector regimes are not in scope;
no obligation has been confirmed for this repository.

## Control Assessment

| Profile / control area | Assessment | Current implementation |
|---|---|---|
| Governance and policy | Verified (design) | Governance, authoring standard, CODEOWNERS, security policy |
| Asset and data inventory | Verified (design) | Architecture, structure, and this data table |
| Identity and access | Partial (implementation) | Maintainer access via repository permissions; CI token read-only |
| Secure development (SSDF) | Verified (implementation) | Validator, tests, pre-commit, CI, review requirements |
| Supply chain and build integrity | Partial (implementation) | Pinned actions and hooks, pinned Python dependencies, Dependabot |
| Vulnerability management | Partial (design) | Dependabot alerts and updates configured; intake and remediation timelines not defined |
| Logging and detection | Partial (implementation) | CI logs and workflow history only; no application telemetry |
| Resilience and recovery | Verified (design) | Content recoverable from Git history; no runtime state |
| Incident response and disclosure | Verified (design) | Private reporting channel and coordinated disclosure policy |
| Privacy and data protection | Verified (implementation) | No personal data processed or stored |
| Third-party and dependency risk | Partial (implementation) | Pinned versions and update automation; no SBOM or licence inventory |
| Network transport and TLS | Not assessed (external boundary) | No repository-owned TLS termination or cipher configuration; GitHub, PyPI, and npm are not independently assessed |
| Container image/runtime | Not applicable | No Dockerfile, Compose file, OCI image, or container runtime policy exists |
| Kubernetes and Helm | Not applicable | No Kubernetes manifests, Helm chart, or cluster policy exists |
| Shell scripts and logging | Partial (implementation) | No standalone shell scripts; CI uses fixed workflow commands and GitHub Actions logs; external retention is not assessed |
| Host and cloud hardening | Not applicable | No host or cloud platform is operated; container and Kubernetes domains are recorded separately |
| AI/agent security | Verified (design) | Operating constraints on prompt injection, tool scope, data leakage, approvals |
| Cryptographic inventory | Not applicable | No cryptography implemented by this repository; TLS is provided by external services |

Operating effectiveness is not claimed for any row; each assessment names a
design or implementation basis only.

## Cryptographic Inventory and Migration

This repository implements no cryptography. It defines no algorithms, keys,
certificates, or providers, and stores no ciphertext. Transport security is
delegated to GitHub, PyPI, and npm.

No post-quantum migration assessment is required for repository content. If a
skill is applied to a target repository that uses cryptography, the `security`
skill performs the inventory there.

## Network Transport and TLS

This repository exposes no application endpoint and contains no TLS termination
or cipher-suite configuration. GitHub Actions and package registries provide
external network services; their protocol negotiation, certificates, and
cipher policies were not independently assessed. No repository-level TLS
control is claimed.

## Container Image and Runtime Hardening

Not applicable. No Dockerfile, Compose file, OCI image build, or container
runtime policy exists in this repository. No image scan or signature verification
was performed or claimed.

## Kubernetes and Helm Hardening

Not applicable. The repository contains no Kubernetes manifests, Helm chart, or
cluster policy to assess. No Pod Security, RBAC, NetworkPolicy, or admission
control enforcement is claimed.

## Shell Script Security and Logging

No standalone shell scripts are present. The CI workflow runs fixed validation
commands in GitHub-hosted runners and does not pass repository secrets to those
steps. GitHub Actions supplies workflow logs; external access controls and log
retention were not assessed. No application logging or shell tracing control is
claimed.

## Spec-Driven Security Requirements

The collection's security-generation behavior is specified by FR-28 in
[the PRD](./PRD.md). The requirement covers evidence-based, conditional
assessment of cryptography/PQC, TLS/ciphers, containers, Kubernetes/Helm, and
shell/logging. It does not assert that this repository operates those
technologies or that generated documentation enforces controls by itself.

## Supply Chain and Build Integrity

| Expectation | Observed state | Gap / action |
|---|---|---|
| Dependencies pinned; lockfiles committed | Python dependencies pinned by version; no lockfile | Acceptable for a small tool; add a lockfile if the graph grows |
| Artifacts signed and verified | Not configured | No release artifact is published |
| Provenance attestation (SLSA) | Not configured | Not required at this stage |
| CI token and release permissions minimized | `contents: read` | Confirmed; no change needed |
| Third-party actions pinned | Pinned by exact version tag | Confirmed; tags are mutable, so updates are reviewed |
| Pre-commit hooks pinned | Pinned by exact version tag | Confirmed; tags are mutable, so updates are reviewed |
| Secret-scanning baseline policy | All plugins except keyword scanning; dependency and generated files excluded; no unaudited entries | Accepted trade-off; `--fail-on-unaudited` keeps suppressions reviewed |
| Dependency update automation | Dependabot for actions, pre-commit, and pip | Confirmed; no change needed |

No SBOM is generated. This is recorded as a gap rather than implied coverage.

## AI and Agent Security

| Control area | Assessment |
|---|---|
| Prompt injection (direct/indirect) | Partial — instruction-level mitigation only; host enforcement is external |
| Tool and file/network permissions | Partial — declarative, not enforced by this repository |
| Human approval for destructive actions | Verified (design) — scope boundaries in the security and code-quality skills; the host must enforce them |
| Sensitive-data handling in prompts/logs | Verified (design) — explicit prohibition and redaction rules; no runtime monitoring |
| Model/provider supply chain | Not applicable — host responsibility |
| Output validation before privileged sinks | Partial — no automated output scanner |
| Evaluation and red-team evidence | Partial — no automated model-behavior harness yet |

A skill or tool allowlist is not a sandbox. That limitation is documented in
the skills themselves.

## Vulnerability and Incident Management

| Area | Confirmed process | Gap |
|---|---|---|
| Vulnerability intake channel | GitHub private security advisories | Host setting must be enabled and verified |
| Severity and triage method | Not decided | No formal severity rubric |
| Remediation targets | Project targets documented, not contractual | No measured history |
| Exception and risk acceptance | Not configured | No register established |
| Incident response and disclosure | Coordinated disclosure described | Process not exercised |

Repository files cannot prove staffing or response execution. Those are marked
`Partial` or `Not assessed` rather than verified.

## Platform Hardening Assessment

Not applicable for host/OS or cloud hardening: this repository operates no
managed host or cloud account. GitHub-hosted runners and repository settings
are platform responsibilities outside this tree. Container and Kubernetes/Helm
profiles are assessed separately above. No OpenSCAP, CIS, or STIG scan was
performed, and none is claimed.

## Exceptions and Risk Acceptance

No risk-acceptance records exist. Known accepted limitations are architectural,
not formally accepted risks:

| ID | Control / requirement | Rationale | Compensating control |
|---|---|---|---|
| EX-1 | No SBOM or artifact signing | No release artifact is published | Pinned dependencies and Dependabot review |
| EX-2 | No automated model-behavior evaluation | Harness not yet built | Manual eval review plus human review |

These entries are recorded as gaps. They are not approved exceptions, and no
approval date has been invented.

## Gaps and Proposed Actions

| Gap | Impact | Proposed action | Priority basis |
|---|---|---|---|
| No SBOM | Dependency inventory is manual | Generate a CycloneDX SBOM in CI when packaging begins | Supply-chain visibility |
| No automated eval harness | Model behavior changes are not measured | Wire `evals/` into an evaluation runner | Regression risk |
| Incident process not exercised | Response time unknown | Run a tabletop exercise | Readiness |
| Dependency lockfile absent | Transitive versions may drift | Add a lockfile for the dev toolchain | Reproducibility |
| `allowed-tools` not enforced here | Tool scope depends on the host | Document host enforcement requirement to users | Least agency |

No deadlines are invented. The gaps are recorded so the maintainer can
prioritise them.

## Assessment Limits

- No penetration test, red-team exercise, or model-behavior evaluation was run.
- GitHub repository settings (branch protection, required checks, private
  vulnerability reporting, secret scanning) were not inspected from this tree.
- IBM detect-secrets was exercised against synthetic inputs locally; gitleaks
  runs in CI. Detection efficacy over this repository's history was not
  measured.
- Operating effectiveness of any control was not measured over time.
- Target repositories that a skill is applied to were not assessed here.

## References

- NIST SP 800-218, Secure Software Development Framework 1.1
- OWASP Software Supply Chain Security Cheat Sheet
- OWASP Secrets Management Cheat Sheet
- Agent Skills specification, <https://agentskills.io/specification>
- [Threat model](./threat-model.md)

## Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Decisions](./decisions.md)
