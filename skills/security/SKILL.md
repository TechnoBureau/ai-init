______________________________________________________________________

## name: security description: > Create or refine an evidence-based, modular enterprise security profile, including applicable cryptographic agility/PQC, FIPS, OpenSCAP/SCAP, CIS, NIST, and OWASP controls. Use for repository security analysis or posture documentation; implement hardening only when explicitly requested.

# Repository Security

Create or refine `docs/security.md` from repository evidence. Start with a
stakeholder-readable summary, then show technical evidence and applicable
modules. Scope frameworks to the actual system and confirmed organizational
requirements; do not turn a control catalog into a generic compliance claim.

## Preflight

1. Inspect the worktree, repository instructions, source, manifests,
   infrastructure, protocols, identity, secrets, dependencies, build/release,
   logging, and security configuration relevant to the task.
1. Read existing `docs/security.md` and preserve confirmed controls, owners,
   exceptions, prior findings, and user-authored content. Update in place;
   never overwrite it wholesale.
1. Identify system boundaries, data types, environments, and regulatory or
   enterprise scope only from confirmed evidence. Mark unknowns `Not documented` or `Not assessed`.
1. For an empty repository, create an initial profile, not an assertion of
   security. Use `Not assessed` until scope is known and `Not evidenced` only
   after inspecting the relevant repository area.

## Select applicable profiles

Read [the modular baseline](./references/security-baseline.md) when selecting
frameworks or making cryptographic/hardening recommendations.

- If cryptography is present, first inventory algorithms, protocols, libraries and
  providers, modules, certificates and keys, dependencies, data lifetime, and
  configuration surfaces. Assess post-quantum migration readiness and
  cryptographic agility. Do not prescribe a target algorithm or migration
  date without confirmed policy, protocol support, and system requirements.
- Treat configurable algorithm switching as a controlled policy mechanism:
  externalize selection behind a centralized provider or configuration
  surface instead of scattering algorithm literals; allow only explicit
  approved profiles, validate configuration, use staged rollout and
  telemetry, enforce downgrade resistance, and bound fallback with
  owner, expiry, and removal conditions. A rollback must not restore a
  prohibited algorithm. Do not silently fall back to quantum-vulnerable
  public-key cryptography. Treat hybrid operation as conditional on a supported
  protocol and an approved design.
- Map secure development lifecycle evidence to NIST SP 800-218 SSDF.
- Distinguish FIPS algorithm specifications from FIPS 140-3 cryptographic
  module validation. If FIPS is required, verify exact module certificate,
  version, operational environment, and applicable algorithm validation;
  algorithm use alone does not establish a validated module.
- For Linux/host baselines, use OpenSCAP and SCAP Security Guide only where
  the platform/content is supported. Record the exact OS, profile, content
  and scanner versions, results, exceptions, and evidence. Audit first;
  hardening/remediation is a separate code or infrastructure change and must
  not be applied unless requested and safe for the target.
- Add OWASP ASVS for web applications/APIs only with a confirmed version and
  verification level. Add OWASP supply-chain, secrets, and logging guidance
  only when those components exist.
- Add CIS Benchmarks, provider baselines, data/sector requirements, or other
  enterprise controls only when the platform, boundary, and applicable policy
  are confirmed. Do not assume a law, certification, or audit scope.

For every selected profile, name the framework and version, assessed boundary,
control status, repository evidence, verification method, and owner only when
known. Omit irrelevant modules rather than marking every possible control
`Not applicable`.

## Document requirements

- Use only `Verified`, `Partial`, `Not evidenced`, `Not assessed`, or `Not applicable` for control status; explain the evidence behind each status.
- Expand framework acronyms at first use. State the assessment scope and
  limits in plain language before detailed control tables.
- Separate existing controls and scan findings from proposed remediation.
  Do not invent risk ratings, owners, target dates, waivers, or acceptance
  criteria.
- Keep related-document links only when their targets exist; use the README
  as the shared documentation index.
- Do not describe a partial review or a tool's presence as proof that the
  system is secure, FIPS validated, hardened, certified, or compliant.
- Documentation does not authorize changing algorithms, fallback settings,
  cryptographic modules, OS configurations, or live infrastructure. Implement
  such changes only when explicitly requested and after scope is clear.

Use [templates/security.md](./templates/security.md). After this skill runs,
if root `README.md` exists, update its index when this task creates or updates
`docs/security.md`, and ensure `AGENTS.md` and `CLAUDE.md` are relative
symbolic links to it. Inspect
both alias paths first. Preserve regular files or links to other targets;
merge unique instructions into the README before replacing only when safe. If
preservation is uncertain or symbolic-link creation is unsupported, keep the
existing path and report the conflict. Never make broken links or copied-file
substitutes; remove README links to absent aliases and report the missing
links. If README is absent, report that `ai-init` is needed to create the
shared index.
