# Governance — {{PROJECT_NAME}}

This document defines how the project is owned, changed, reviewed, and
supported. It applies to source code, documentation, configuration, and
automation.

## Scope and principles

- Decisions are recorded with their evidence, alternatives, and consequences.
- Changes are reviewable, reversible, and traceable through Git history.
- Safety and correctness take precedence over speed.
- Security and privacy concerns can block a change until resolved.
- No document in this repository is a certification, audit opinion, or
  compliance attestation.

## Roles

| Role | Accountability |
|---|---|
| Maintainer | Repository settings, merges, releases, security response, final decision on disputed changes |
| Reviewer | Technical and editorial review; may be a maintainer |
| Security reviewer | Threat model, destructive defaults, secret handling, supply chain, vulnerability response |
| Contributor | Proposes changes, supplies evidence, updates tests and documentation |

The current accountable owners are recorded in
{{LINK_TO_CODEOWNERS_OR_NOT_DOCUMENTED}}. Roles may be combined in a small
project; the review requirements below still apply.

## Decision making

- Routine changes use pull-request review and lazy consensus.
- A disagreement is resolved by the maintainer after documenting the options,
  evidence, and decision in the pull request or an architecture decision record.
- Changes that alter a public contract require migration guidance and a
  deprecation period.
- Security and privacy concerns escalate to the security reviewer.

## Change classes

| Class | Examples | Required evidence |
|---|---|---|
| Editorial | Typos, link repair, clarity without behavior change | Build and link checks |
| Capability | New feature, new document section, new optional control | Tests, review |
| Behavior | Changed workflow, stricter validation, changed default | Tests, migration notes, two reviewers |
| Contract | Public API change, renamed or removed interface, ID semantics | Migration plan and deprecation notice |
| Security fix | Secret exposure, destructive behavior, injection risk | Private report, regression test, advisory if needed |

## Pull-request requirements

- Pass the configured build, test, lint, and security checks.
- State the problem, evidence, and change class.
- Add a regression test for every fixed defect.
- Preserve unrelated changes and permanent requirement or decision IDs.
- Avoid secrets, personal data, customer identifiers, and live credentials.
- Update documentation that describes the changed behavior.

Reviewers check substance: Is every claim traceable to evidence? Is the scope
boundary explicit? Does it fail safe when evidence is missing? Are security,
privacy, and destructive-action impacts stated?

## Review cadence

| Review | Frequency | Scope |
|---|---|---|
| Security and architecture documents | Quarterly | Controls, boundaries, threat model, dependencies |
| Dependencies and automation | Monthly or automated | Pinned actions, packages, hooks |
| Code and documentation | Per change | Correctness, evidence, tests, links |
| Post-incident | After any security or integrity incident | Root cause, regression test, process change |

## Approval and exceptions

An exception requires the rule being waived, a documented rationale and
compensating control, an accountable owner, an expiry or review date, and
approval from a maintainer. For security rules, the security reviewer must
approve. Undocumented exceptions are defects.

## Security response

- Report vulnerabilities through [SECURITY.md](../SECURITY.md), not a public
  issue.
- Triage, fix, regression-test, and disclose through a coordinated process.
- Do not include exploit details, secrets, or personal data in a public
  advisory.

## Repository settings expected by this policy

These settings live in the hosting platform, not in the tree. Maintainers must
keep them aligned with this document:

- default branch protected against force-push and deletion;
- required status checks from the CI workflow;
- required review from CODEOWNERS;
- secret scanning and dependency alerts enabled;
- private vulnerability reporting enabled;
- release tags protected;
- no long-lived credentials in repository secrets when short-lived identity
  federation is available.

If a setting cannot be enabled, record the gap and compensating control rather
than claiming the control exists.

## Amending this document

Governance changes follow the same pull-request process. A change that weakens
a safety or security rule requires maintainer and security-reviewer approval.

## Related documents

- [Architecture](./architecture.md)
- [Threat model](./threat-model.md)
- [Security posture](./security.md)
- [Decisions](./decisions.md)
