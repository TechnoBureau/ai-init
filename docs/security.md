# Security Profile — AI Init Skills

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

| Area | Evidence-based description |
|---|---|
| System purpose and environments | Static content plus Python validation tooling; contributor workstations and GitHub Actions |
| Components and trust boundaries | Skills, templates, scripts, tests, CI; the target repository is untrusted input |
| Identities and access paths | Repository maintainers via GitHub; CI with read-only token; no service accounts |
| Data handled and classification | Public repository content only; no personal, financial, or health data |
| External services and dependencies | PyPI (PyYAML, pre-commit), GitHub Actions, pre-commit hook repositories, npm for markdownlint-cli2 |
| Relevant regulatory or contractual scope | None confirmed |

### Data classification

| Data type | Classification | Storage / transit | Retention | Evidence |
|---|---|---|---|---|
| Skill instructions and templates | Public | Git repository | Git history | `skills/` |
| Generated documentation | Public | Git repository | Git history | `docs/` |
| Development dependencies | Public | `requirements-dev.txt`, pinned workflow actions | Updated by Dependabot | `requirements-dev.txt` |
| Secrets or personal data | None identified | Not present | Not applicable | Repository scan and review |

The classification above describes the system's data. This document carries no
control block or document classification.

## Threat Model Summary

Full detail is in [threat-model.md](./threat-model.md).

| Asset / entry point | Threat (STRIDE/LINDDUN) | Existing mitigation | Residual risk / evidence |
|---|---|---|---|
| `SKILL.md` metadata | Tampering | Strict validator, regression test, CI gate | A bypassed hook is caught by CI; a compromised CI is out of scope |
| Agent instructions | Spoofing / Elevation | Operating constraints, scope boundaries, review | Model behavior is probabilistic; instructions reduce, not eliminate |
| Repository secrets | Information disclosure | gitleaks, IBM detect-secrets baseline, private-key detection, explicit prohibition | Secrets already present could be copied; keyword-only secrets are missed |
| CI workflow | Tampering | Pinned action SHAs, read-only permissions, Dependabot review | Upstream compromise before pinning |
| Generated documentation | Repudiation (overclaim) | Evidence taxonomy, anti-overclaim rules, review checklist | Reviewer may accept unsupported prose |

## Selected Profiles

| Profile / framework | Exact version | Why selected | Assessed boundary | Evidence |
|---|---|---|---|---|
| NIST SSDF | SP 800-218 v1.1 | Secure development practice mapping | Repository content and CI | `.pre-commit-config.yaml`, `.github/workflows/validate.yml` |
| OWASP Software Supply Chain Security | Current cheat sheet | Dependencies, actions, and hooks are consumed | Dependency and workflow configuration | `requirements-dev.txt`, `dependabot.yml` |
| OWASP Secrets Management | Current cheat sheet | Skills may read repositories that contain secrets | Operating constraints and scanning | `skills/*/SKILL.md` |

ISO/IEC 27001, SOC 2, PCI DSS, FedRAMP, and sector regimes are not in scope;
no obligation has been confirmed for this repository.

## Control Status

| Profile / control area | Claim type | Status | Current implementation | Evidence | Verification / owner |
|---|---|---|---|---|---|
| Governance and policy | Design | Verified | Governance, authoring standard, CODEOWNERS, security policy | `docs/governance.md`, `.github/CODEOWNERS` | Review; TechnoBureau |
| Asset and data inventory | Design | Verified | Architecture, structure, and this data table | `docs/architecture.md` | Review; TechnoBureau |
| Identity and access | Implementation | Partial | Maintainer access via repository permissions; CI token read-only | `.github/workflows/validate.yml` | Host settings not visible in the tree |
| Secure development (SSDF) | Implementation | Verified | Validator, tests, pre-commit, CI, review requirements | `scripts/`, `tests/`, `.github/workflows/validate.yml` | CI run; TechnoBureau |
| Supply chain and build integrity | Implementation | Partial | Pinned actions and hooks, pinned Python dependencies, Dependabot | `requirements-dev.txt`, `.github/dependabot.yml` | Configuration review; no SBOM or signing yet |
| Vulnerability management | Design | Partial | Dependabot alerts and updates configured; intake and remediation targets not defined | `.github/dependabot.yml` | Not exercised |
| Logging and detection | Implementation | Partial | CI logs and workflow history only; no application telemetry | GitHub Actions | Host-provided |
| Resilience and recovery | Design | Verified | Content recoverable from Git history; no runtime state | `docs/architecture.md` | Review |
| Incident response and disclosure | Design | Verified | Private reporting channel and coordinated disclosure policy | `SECURITY.md` | Not exercised |
| Privacy and data protection | Implementation | Verified | No personal data processed or stored | This document | Review |
| Third-party and dependency risk | Implementation | Partial | Pinned versions and update automation; no SBOM or licence inventory | `requirements-dev.txt` | Not evidenced |
| Platform hardening | Implementation | Not applicable | No host, container, or cluster is operated | `docs/architecture.md` | Not applicable |
| AI/agent security | Design | Verified | Operating constraints on prompt injection, tool scope, data leakage, approvals | `skills/*/SKILL.md`, `docs/threat-model.md` | Review; effectiveness not measured |
| Cryptographic inventory | Implementation | Not applicable | No cryptography implemented by this repository; TLS is provided by the host and package registries | Repository search | Not applicable |

Operating effectiveness is not claimed for any row. Only design and
implementation evidence exists.

## Cryptographic Inventory and Migration

This repository implements no cryptography. It defines no algorithms, keys,
certificates, or providers, and stores no ciphertext. Transport security is
delegated to GitHub, PyPI, and npm.

No post-quantum migration assessment is required for repository content. If a
skill is applied to a target repository that uses cryptography, the `security`
skill performs the inventory there.

## Supply Chain and Build Integrity

| Expectation | Observed state | Evidence | Gap / action |
|---|---|---|---|
| Dependencies pinned; lockfiles committed | Python dependencies pinned by version; no lockfile | `requirements-dev.txt` | Acceptable for a small tool; add a lockfile if the graph grows |
| Artifacts signed and verified | Not configured | None | No release artifact is published |
| Provenance attestation (SLSA) | Not configured | None | Not required at this stage |
| CI token and release permissions minimized | `contents: read` | `.github/workflows/validate.yml` | Verified |
| Third-party actions pinned | Pinned by commit SHA | Workflow file | Verified |
| Pre-commit hooks pinned | Pinned by commit SHA or exact revision | `.pre-commit-config.yaml` | Verified |
| Secret-scanning baseline policy | Keyword detector disabled; dependency and generated files excluded; no findings | `.secrets.baseline` | Accepted trade-off; provider and entropy detectors remain enabled |
| Dependency update automation | Dependabot for actions, pre-commit, and pip | `.github/dependabot.yml` | Verified |

No SBOM is generated. This is recorded as a gap rather than implied coverage.

## AI and Agent Security

| Control area | Status | Evidence | Notes |
|---|---|---|---|
| Prompt injection (direct/indirect) | Partial | `skills/*/SKILL.md` operating constraints | Instruction-level mitigation only; host enforcement is external |
| Tool and file/network permissions | Partial | `allowed-tools` metadata | Declarative, not enforced by this repository |
| Human approval for destructive actions | Verified | Scope boundaries in `security` and `code-quality` skills | Requires host cooperation to enforce |
| Sensitive-data handling in prompts/logs | Verified | Explicit prohibition and redaction rules | Verified by review, not by runtime monitoring |
| Model/provider supply chain | Not applicable | No model is bundled | Host responsibility |
| Output validation before privileged sinks | Partial | Evidence and review rules | No automated output scanner |
| Evaluation and red-team evidence | Partial | `evals/` fixtures | No automated model-behavior harness yet |

A skill or tool allowlist is not a sandbox. That limitation is documented in
the skills themselves.

## Vulnerability and Incident Management

| Area | Confirmed process | Evidence | Gap |
|---|---|---|---|
| Vulnerability intake channel | GitHub private security advisories | `SECURITY.md` | Host setting must be enabled and verified |
| Severity and triage method | Not decided | `SECURITY.md` targets are project goals only | No formal severity rubric |
| Remediation targets | Project targets documented, not contractual | `SECURITY.md` | No measured history |
| Exception and risk acceptance | Not configured | None | No register established |
| Incident response and disclosure | Coordinated disclosure described | `SECURITY.md` | Process not exercised |

Repository files cannot prove staffing or response execution. Those are marked
`Partial` or `Not assessed` rather than verified.

## Platform Hardening Assessment

Not applicable. The repository operates no host, container image, Kubernetes
cluster, or cloud account. GitHub-hosted runners and repository settings are
platform responsibilities outside this tree. No OpenSCAP, CIS, or STIG scan was
performed, and none is claimed.

## Exceptions and Risk Acceptance

No risk-acceptance records exist. Known accepted limitations are architectural,
not formally accepted risks:

| ID | Control / requirement | Rationale | Compensating control | Owner | Expiry / review date | Status |
|---|---|---|---|---|---|---|
| EX-1 | No SBOM or artifact signing | No release artifact is published | Pinned dependencies and Dependabot review | Not recorded | Not decided | Open |
| EX-2 | No automated model-behavior evaluation | Harness not yet built | Manual eval review plus human review | Not recorded | Not decided | Open |

These entries are recorded as gaps. They are not approved exceptions, and no
owner or expiry has been invented.

## Gaps and Proposed Actions

| Gap | Impact / evidence | Proposed action | Priority basis | Owner / target |
|---|---|---|---|---|
| No SBOM | Dependency inventory is manual | Generate a CycloneDX SBOM in CI when packaging begins | Supply-chain visibility | Not decided |
| No automated eval harness | Model behavior changes are not measured | Wire `evals/` into an evaluation runner | Regression risk | Not decided |
| Incident process not exercised | Response time unknown | Run a tabletop exercise | Readiness | Not decided |
| Dependency lockfile absent | Transitive versions may drift | Add a lockfile for the dev toolchain | Reproducibility | Not decided |
| `allowed-tools` not enforced here | Tool scope depends on the host | Document host enforcement requirement to users | Least agency | Not decided |

No dates or owners are invented. The gaps are recorded so the maintainer can
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
