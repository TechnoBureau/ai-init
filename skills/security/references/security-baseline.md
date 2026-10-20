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

## Conditional enterprise and application profiles

| Repository or system evidence | Profile to select | Boundary and evidence |
|---|---|---|
| Web application or application programming interface (API) | [OWASP Application Security Verification Standard (ASVS)](https://github.com/OWASP/ASVS/releases) | Select a version and verification level only when confirmed; assess implemented application behavior. |
| Continuous integration / continuous delivery (CI/CD), package publishing, or artifact build | [OWASP Software Supply Chain Security](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html) | Review source control, build identity, dependencies, artifacts, and release permissions present in the system. |
| Secrets or credential flows | [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) | Review lifecycle, access, rotation, exposure, storage, and logging evidence. |
| Application security logging | [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Assess coverage, sensitive-data handling, integrity, and access for configured logging. |
| Linux or other supported host configuration | [OpenSCAP](https://www.open-scap.org/) with [Security Content Automation Protocol (SCAP) Security Guide](https://www.open-scap.org/security-policies/scap-security-guide/) | Record OS/version, content version, selected profile, scanner version, results, exceptions, and remediation evidence. Audit first; apply remediation only when requested and safe for the environment. |
| Cloud or infrastructure-as-code | Confirmed provider baseline or relevant [Center for Internet Security (CIS) Benchmark](https://www.cisecurity.org/cis-benchmarks) | Name provider, service, asset version, benchmark/profile, and deployed boundary. |
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

## Evidence status

- **Verified:** direct evidence plus a suitable validation method/result
  supports the claim.
- **Partial:** some evidence exists, but implementation or validation is
  incomplete.
- **Not evidenced:** repository inspection found no evidence; external
  controls may still exist.
- **Not assessed:** scope, access, or evidence was insufficient to evaluate.
- **Not applicable:** explain why the profile does not apply.

Keep current controls, observations, exceptions, and proposed actions
separate. Record owners, dates, risk ratings, and acceptance criteria only
when supplied or confirmed.
