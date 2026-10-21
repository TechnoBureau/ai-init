# Modular Enterprise Security Baseline

Select profiles from the actual system boundary, data, deployment, and
confirmed organizational policy. A framework is a vocabulary and verification
source—not evidence of implementation, certification, or compliance.

## Quantum-resistant cryptography and algorithm agility

When the system uses cryptography, inventory where it is used before
recommending an algorithm or migration. Include protocols, libraries,
providers, cryptographic modules, certificates, key types and sizes, stored
ciphertext/signatures, external dependencies, and expected data lifetime.
Prioritize long-lived confidential data and public-key operations based on
business impact and confirmed risk—not on a guessed quantum-computing date.

Use [Federal Information Processing Standard (FIPS) 203 (Module-Lattice-Based
Key-Encapsulation Mechanism, ML-KEM)](https://csrc.nist.gov/pubs/fips/203/final)
for key encapsulation and [FIPS 204 (Module-Lattice-Based Digital Signature
Algorithm, ML-DSA)](https://csrc.nist.gov/pubs/fips/204/final) or [FIPS 205
(Stateless Hash-Based Digital Signature Algorithm, SLH-DSA)](https://csrc.nist.gov/pubs/fips/205/final)
for digital signatures when they fit the application, protocol,
implementation, and approved policy. Check current standard revisions and
errata before selecting an implementation. Do not treat a candidate or draft
algorithm as a final standard.

For a FIPS-regulated boundary, distinguish algorithm approval from module
validation. [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) sets
cryptographic-module requirements; verify the exact module certificate,
version, operational environment, and applicable algorithm validation in
NIST's [Cryptographic Module Validation Program](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules).
Merely using a FIPS-specified algorithm does not
make a product or module FIPS 140-3 validated.

Use the current NIST [Cybersecurity White Paper (CSWP) 39upd1 guidance on
cryptographic agility](https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final)
and [post-quantum cryptography (PQC) transition publications](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/publications).
Record the selected publication and revision, and re-check the publication
pages during each assessment. Check the current status of NIST IR 8547 or its
successor; label any draft transition material as informative, not a binding
schedule.

For configurable migration and fallback, document these properties only when
supported or explicitly proposed:

- central, versioned, policy-controlled algorithm profiles and providers;
  validate configuration and reject unknown or unapproved identifiers;
  never expose arbitrary algorithm selection to untrusted users;
- authorized rollout, audit, telemetry, and a rollback condition that does
  not re-enable a prohibited algorithm;
- protocol negotiation integrity and downgrade resistance;
- fallback limited to an explicit, approved allowlist, with owner, scope,
  expiry, and removal criteria; no silent or indefinite fallback to a
  quantum-vulnerable option;
- hybrid operation only where the protocol, implementations, and policy
  support it; identify both components and their transition/retirement plan;
- staged interoperability, performance, key/certificate, backup/restore, and
  data re-encryption or signature-validation testing.

Do not hard-code an arbitrary algorithm, strength, timeline, or fallback.
These are organization- and protocol-specific decisions. Do not execute a
migration or change a live cryptographic policy unless the user asks for that
implementation.

## Network transport, TLS, and cipher suites

Assess only endpoints and clients in the requested boundary. Identify who
terminates TLS and where the configuration is enforced; a repository may rely
on an external proxy, ingress, service mesh, runtime, or hosting provider.

- Prefer TLS 1.3. Require TLS 1.2 or later where compatible with supported
  clients and confirmed policy; disable SSL and deprecated TLS versions when
  the application controls negotiation.
- Validate the certificate chain and requested hostname. Do not disable
  certificate verification or accept arbitrary self-signed certificates in
  production. Assess trust-store, expiry, renewal, and mutual TLS only where
  applicable.
- Choose cipher suites by protocol version, crypto provider, platform, and
  policy. Prefer authenticated encryption with forward secrecy. For TLS 1.3,
  commonly supported AEAD suites include `TLS_AES_128_GCM_SHA256`,
  `TLS_AES_256_GCM_SHA384`, and `TLS_CHACHA20_POLY1305_SHA256`. For TLS 1.2,
  prefer supported ECDHE suites with AES-GCM or ChaCha20-Poly1305. Do not treat
  TLS 1.3 and TLS 1.2 names as interchangeable or copy a cipher list without
  checking the implementation.
- Reject obsolete or weak suites such as NULL, EXPORT, anonymous, RC4, 3DES,
  static RSA key exchange, and CBC suites unless a documented compatibility
  exception is required. Record the exception and compensating control.
- Use HTTPS for external APIs, verify hostnames, and set bounded connect/read
  timeouts. Configure service binding for the intended network boundary;
  `0.0.0.0` inside a container is not by itself proof of public exposure, so
  assess ingress, firewall, and network policy as well.
- Record versions, effective configuration, scan/handshake evidence, and
  external termination boundaries. Do not claim TLS or cipher enforcement from
  a URL scheme or dependency alone.

## Container image and runtime hardening

When Dockerfiles, OCI images, or container runtime policy are in scope, assess
both image construction and deployment. Use an approved, maintained vendor or
organization registry and an image compatible with the supported platform;
Red Hat is one option only when the target policy requires it. Prefer minimal
images and pin deployments to an immutable digest or the project's controlled
release policy. Avoid floating `latest` tags and EOL images; verify lifecycle,
provenance/signature, and vulnerability-scan evidence rather than assuming the
newest tag is safest.

- Build with minimal context and multi-stage builds where useful; do not pass
  credentials through Dockerfile `ARG`, `ENV`, build logs, or committed files.
  Use the platform's build-secret mechanism and remove unnecessary tools from
  runtime layers.
- Run as a non-root user. Avoid privileged mode and unnecessary host mounts,
  namespaces, devices, and Linux capabilities. Where supported, drop all
  capabilities then add only those required; use `no-new-privileges`, a
  read-only root filesystem, seccomp/AppArmor, and resource limits.
- Scan the image and dependencies before release; verify signatures/provenance
  when the deployment platform supports enforcement. Record the image digest,
  tool/policy versions, findings, and exceptions.
- Validate runtime controls at deployment as well as Dockerfile defaults.
  A non-root Dockerfile does not prove the orchestrator preserves the setting.

Do not require a single public registry or vendor for every project. Prefer the
organization-approved source and the exact platform-supported image.

## Kubernetes and Helm hardening

When Kubernetes manifests or Helm charts are in scope, inspect rendered
manifests as well as chart defaults and values. Select a confirmed Kubernetes
Pod Security Standards level or organization baseline. For applicable
workloads, check:

- `runAsNonRoot`, explicit user/group where supported,
  `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem` where compatible,
  dropped capabilities, and `seccompProfile: RuntimeDefault`;
- absence of privileged containers, host PID/IPC/network namespaces, and
  `hostPath` mounts unless a documented platform requirement justifies them;
- least-privilege RBAC and service accounts, with token automount disabled
  when the workload does not need Kubernetes API access;
- default-deny and workload-specific NetworkPolicies where the cluster
  enforces them; TLS and certificate validation at ingress/service boundaries;
- images from approved sources, immutable digests or controlled release pins,
  resource requests/limits, health probes, and safe termination behavior;
- secrets kept out of chart values, source control, rendered output, and logs;
  use the cluster's approved secret-management integration;
- chart dependency provenance, schema validation, `helm lint`, rendered-manifest
  checks, and configured policy scanners.

Do not claim a control is enforced from a Helm value alone. Verify the rendered
workload and cluster admission/runtime policy. Do not prescribe a particular
scanner or Pod Security level unless the platform or policy confirms it.

## Shell scripts, logging, and error handling

When shell scripts or CI shell steps are in scope, inspect the interpreter,
inputs, commands, environment, and execution context. Use ShellCheck where the
project configures it; quote expansions, prefer arrays to constructed command
strings, avoid `eval`, validate external input, handle exit codes explicitly,
and clean temporary files safely. Use strict-mode options only with
understanding of the script's shell and error semantics.

- Use restrictive permissions for temporary files (`umask` where appropriate),
  safe temporary-file creation, and cleanup traps for sensitive artifacts.
- Never log secrets, access tokens, private keys, credentials, or unnecessary
  personal data. Avoid shell tracing (`set -x`) around sensitive values and
  redact command arguments where tools echo them.
- Emit concise, actionable diagnostics to stderr with a nonzero exit on failure;
  include operation and safe context without dumping environments, full request
  bodies, or secret-bearing command lines. Use structured logs only when the
  runtime or project convention supports them.
- Set log access, integrity, alerting, and retention according to confirmed
  operational policy. Do not invent a universal retention period or claim
  monitoring from log output alone.

## Core secure-development profile

Map repository evidence to the four practice groups in the [National Institute
of Standards and Technology (NIST) SP 800-218 Secure Software Development
Framework (SSDF), version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final):

- **Prepare the Organization:** roles, policy, tools, and secure development
  environments.
- **Protect the Software:** source, build, artifact, and release integrity.
- **Produce Well-Secured Software:** secure design, implementation, review,
  testing, and dependency practices.
- **Respond to Vulnerabilities:** intake, triage, remediation, and disclosure.

For security-relevant behavior changes, put applicable controls and observable
acceptance criteria in the authoritative PRD, feature spec, issue, or task before
implementation. Link to this profile and trace criteria to tests; do not copy
generic controls or claim they are active without configuration evidence.

### Dependency lifecycle and version selection

- Prefer a supported, security-maintained version that satisfies compatibility
  and reproducibility requirements; do not blindly upgrade to the newest release.
- Check vendor lifecycle/EOL notices, security advisories, release provenance,
  and the repository's lockfile/update policy. Treat recent commits as one signal,
  not a universal six-month maintenance gate.
- Use lockfiles or immutable constraints where supported. Review dependency
  updates, test them, and avoid floating `latest` references in production.
- Do not suppress security warnings or pin an old vulnerable version merely to
  avoid a breaking change. If an update is blocked, document the evidence-based
  risk, mitigation, and decision needed; do not invent a remediation deadline.
- Apply the project's confirmed license and vendor policy. Do not assume a
  particular corporation's policy applies to an unrelated repository.

## Enterprise governance and assurance profiles

Select these only when a confirmed obligation exists. Record the exact edition,
scope, control identifiers, and evidence owner.

| Obligation or trigger | Profile | What repository evidence can support |
|---|---|---|
| Organization operates an information security management system | [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) Annex A | Control implementation evidence, not certification |
| Governance and risk program | [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework) | Govern, Identify, Protect, Detect, Respond, Recover activities |
| Service organization controls report | SOC 2 Trust Services Criteria (2017, revised 2022) | Control design and evidence; report issuance requires an auditor |
| US federal or controlled baseline | [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Selected control families only |
| General control hygiene | [CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls) | Implemented safeguards, not a certification |
| Secure development program maturity | [OWASP SAMM 2.0](https://owaspsamm.org/) or BSIMM | Practice evidence and gaps |
| Software supply chain | [SLSA v1.x](https://slsa.dev/) and [OpenSSF Scorecard](https://securityscorecards.dev/) | Build provenance, project posture signals |
| SBOM program | SPDX 3.x or CycloneDX 1.6+, NTIA minimum elements | Generated SBOM and dependency inventory |
| Vulnerability disclosure | ISO/IEC 29147 or a confirmed policy | Public policy and intake channel |
| Incident response | NIST SP 800-61 Rev. 3 (2025) or ISO/IEC 27035 | Plan and exercise records, not staffing claims |
| Business continuity | ISO 22301:2019 | Tested recovery evidence |
| Privacy management | NIST Privacy Framework 1.0, ISO/IEC 27701 (current edition), ISO/IEC 29100 | Data flows, retention, and DPIA records |
| Sector or statutory regime | GDPR, India DPDP Act 2023, CCPA/CPRA, HIPAA, PCI DSS 4.0.1, EU CRA (Regulation (EU) 2024/2847), sector rules | Only the controls and data flows confirmed in scope |

Do not apply a whole framework by default. A repository review cannot establish
audit readiness, legal compliance, or operating effectiveness by itself.

## Conditional enterprise and application profiles

| Repository or system signal | Profile to select | Boundary and inputs |
|---|---|---|
| Web application or application programming interface (API) | [OWASP Application Security Verification Standard (ASVS)](https://github.com/OWASP/ASVS/releases) | Select a version (ASVS 5.0 when confirmed) and verification level; assess implemented application behavior. |
| Continuous integration / continuous delivery (CI/CD), package publishing, or artifact build | [OWASP Software Supply Chain Security](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html) | Review source control, build identity, dependencies, artifacts, and release permissions present in the system. |
| Secrets or credential flows | [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) | Review lifecycle, access, rotation, exposure, storage, and logging evidence. |
| Application security logging | [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Assess coverage, sensitive-data handling, integrity, and access for configured logging. |
| Network endpoints or TLS clients | NIST SP 800-52 Rev. 2 and TLS RFCs 8446/5246 | Record endpoint, termination boundary, effective protocol/cipher policy, certificate validation, and evidence. |
| Linux or other supported host configuration | [OpenSCAP](https://www.open-scap.org/) with [Security Content Automation Protocol (SCAP) Security Guide](https://www.open-scap.org/security-policies/scap-security-guide/) | Record OS/version, content version, selected profile, scanner version, results, exceptions, and remediation evidence. Audit first; apply remediation only when requested and safe for the environment. |
| Ubuntu, RHEL, or other platform baseline | CIS Benchmark or DISA Security Technical Implementation Guide (STIG) for the exact product version | Record benchmark/STIG version, profile, exceptions, and scan date. |
| Cloud or infrastructure-as-code | Confirmed provider baseline or relevant [Center for Internet Security (CIS) Benchmark](https://www.cisecurity.org/cis-benchmarks) | Name provider, service, asset version, benchmark/profile, and deployed boundary. |
| Docker / OCI image build or runtime | NIST SP 800-190, CIS Docker Benchmark, vendor guidance, and organization policy | Assess base image provenance/lifecycle, digest, build secrets, non-root runtime, capabilities, filesystem, signatures, and scans. |
| Kubernetes manifests or Helm charts | Kubernetes Pod Security Standards, CIS Kubernetes Benchmark, NSA/CISA guidance, and Helm chart guidance | Assess rendered workloads, security contexts, RBAC, secrets, network policy, image integrity, and enforced admission controls. |
| Shell scripts or CI shell steps | ShellCheck and project shell/security conventions | Assess input handling, quoting, command execution, exit status, temporary files, and secret-safe logging. |
| Identity and access configuration | Relevant OWASP ASVS or confirmed identity-provider/cloud baseline | Assess authentication, authorization, least privilege, identity lifecycle, and privileged access where configured. |
| Sensitive or regulated data | Confirmed data classification and organization-selected legal/sector profile | Record data type, residence, retention, key management, and boundaries; do not infer a regulatory obligation from data alone. |
| Runtime monitoring or incident response | OWASP Logging plus confirmed operational procedure | Repository files cannot prove external staffing, service levels, or operational execution. |
| Organization-selected enterprise control framework | Confirmed NIST/CIS or sector control profile | Name exact framework, release, selected controls, scope, and owner; do not apply a whole framework by default. |

### OpenSCAP / SCAP hardening workflow

For applicable systems, choose a profile that matches the exact platform and
confirmed requirement. First inspect scanner/content versions and run an
assessment that produces reviewable results. Separate passing checks,
failures, not-applicable items, and accepted exceptions. Assess the impact and
dependencies of each remediation; do not apply blanket fixes or claim
hardening solely because a scan ran. Treat remediation scripts as code changes
and require the authorization and validation appropriate to the target
environment.

## Mandatory control domains

Assess each domain that applies. `Not assessed` is a valid result when access
or evidence is insufficient; omission requires a reason that the domain is
irrelevant.

| Domain | Core questions |
|---|---|
| Governance | Who owns the system and security decisions? Is there policy, review cadence, and an exception register? |
| Asset and data inventory | What components, services, stores, and data classes exist? Where does data reside and how long is it retained? |
| Identity and access | How are humans and workloads authenticated? Is least privilege enforced? Are sessions, tokens, and secrets scoped and rotated? |
| Secure development | Is there a threat model, secure design review, code review, and SAST/SCA/secret/IaC scanning? Are gates enforced? |
| Supply chain | Are dependencies pinned? Is there an SBOM, provenance, signing, and verification? Who can publish? |
| Vulnerability management | What is the intake channel, severity method, remediation target, exception process, and evidence of closure? |
| Cryptography and keys | What algorithms, protocols, providers, keys, certificates, and lifetimes exist? Is rotation tested? Is PQC migration assessed? |
| Network transport | Which endpoints and clients are in scope? What TLS versions, certificate checks, and version-appropriate cipher policy are evidenced? |
| Logging and detection | Which security events are logged? Are secrets and personal data excluded? What are retention, integrity, access, and alerting? |
| Shell and automation | Are scripts and CI commands safely quoted, validated, error-checked, and free of secret-bearing logs or tracing? |
| Container and Kubernetes/Helm | Are image source, digest, privilege, security context, RBAC, secrets, and network controls verified in the built/rendered workload? |
| Resilience and recovery | Are backups encrypted and restore-tested? Are RTO/RPO confirmed? Are failure modes bounded? |
| Incident response | Is there a plan, severity model, contact path, disclosure process, and postmortem? Has it been exercised? |
| Privacy | Is data minimized? Is there a lawful basis, retention rule, subject-rights path, and DPIA for high-risk processing? |
| Third-party risk | Which vendors, APIs, data processors, and open-source licences are in scope? Is there due diligence evidence? |
| AI and agent systems | Are prompt injection, tool abuse, data leakage, model supply chain, evaluation, and human oversight addressed? |
| Host and cloud hardening | Which OS, host, and provider baselines are enforced? What is the exact version and scan result? |

## AI and agent security baseline

Use this when prompts, models, RAG, agents, or tool calling are in scope.

- Treat all model-visible content as untrusted input: retrieved documents,
  repository files, tool output, web pages, and user messages.
- Separate instructions from data. Where the host supports it, enforce policy
  outside the model; never rely on the model to police itself.
- Apply least agency: minimal tools, scoped filesystem/network access,
  allowlisted commands, and explicit approval for destructive or external
  actions.
- Validate model output before it reaches a shell, SQL engine, browser,
  privileged API, or filesystem operation. Do not execute generated code
  without review.
- Protect data in prompts, logs, traces, embeddings, caches, and provider
  requests. Confirm retention, training-use, and residency terms.
- Pin model and prompt versions where reproducibility matters. Maintain an
  evaluation set covering normal, adversarial, and refusal behavior.
- Log tool calls and approvals without logging secrets or unnecessary
  personal data.
- Consider NIST AI Risk Management Framework 1.0, NIST AI 600-1 Generative AI
  Profile, ISO/IEC 42001:2023, and the EU AI Act only when confirmed in scope.
- Agent Skills and tool allowlists are declarative unless the host enforces
  them. Do not present them as a sandbox.

## Privacy baseline

- Map personal and sensitive data flows, purposes, storage locations,
  recipients, retention, and deletion.
- Confirm the applicable legal basis and jurisdiction; do not infer one from
  data type.
- Apply data minimization and purpose limitation to logs, analytics, and test
  data.
- Provide a subject-rights path when required by confirmed policy or law, and
  test deletion including backups where applicable.
- Run a DPIA or equivalent for high-risk processing when the organization
  requires it.
- Never place personal data in documentation, tickets, examples, or source
  comments.

## Vulnerability and incident management

- Define intake, triage ownership, severity method, and remediation targets.
  NIST SP 800-61 Rev. 3 provides an incident-response vocabulary; ISO/IEC
  29147 covers disclosure.
- Combine CVSS v4.0 with exploitability and business context such as EPSS and
  CISA KEV. Do not equate a high score with automatic exploitation.
- Track exceptions with owner, rationale, compensating control, expiry, and
  review date.
- Preserve the scanner version, database date, affected artifact digest, and
  the verification of the fix.
- Do not publish live exploit details or sensitive reproduction steps in a
  broadly circulated project document.

## Claim types and statuses

- **Verified:** direct evidence plus a suitable validation method/result
  supports the claim.
- **Partial:** some evidence exists, but implementation or validation is
  incomplete.
- **Not evidenced:** repository inspection found no evidence; external
  controls may still exist.
- **Not assessed:** scope, access, or evidence was insufficient to evaluate.
- **Not applicable:** explain why the profile does not apply.

State the claim type as well as the status:

- **Design claim:** an approved design or policy describes the control.
- **Implementation claim:** code or configuration implements it in the
  inspected code.
- **Operating-effectiveness claim:** evidence shows it works over time; rarely
  supportable from a repository review.

Keep current controls, observations, exceptions, and proposed actions
separate. Record owners, dates, risk ratings, and acceptance criteria only
when supplied or confirmed.

## Anti-overclaim rules

- A scan, SBOM, policy, or checkbox is not proof of security.
- Algorithm choice is not module validation.
- A control catalog is not a certification.
- A passing pipeline is not an audit opinion.
- A workflow file is not evidence that a release process is followed.
- A threat model is not evidence that mitigations are implemented.
- Documentation is not authorization to change production.
