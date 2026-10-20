# Governance

This document defines how the project is owned, changed, reviewed, and
supported. It applies to source code, skill instructions, documentation,
configuration, and automation.

## Scope and principles

- Decisions are recorded with their context, consequences, and reason in
  [decisions.md](./decisions.md).
- Changes are reviewable, reversible, and traceable through Git history.
- Safety and correctness take precedence over speed.
- Security and privacy concerns can block a change until resolved.
- No document in this repository is a certification, audit opinion, or
  compliance attestation.

## Roles

| Role | Accountability |
|---|---|
| Maintainer | Repository settings, merges, security response, final decision on disputed changes |
| Reviewer | Technical and editorial review; may be a maintainer |
| Security reviewer | Threat model, destructive instructions, secret handling, supply chain, vulnerability response |
| Contributor | Proposes changes, supplies evidence, updates tests and documentation |

Accountability is recorded once in
[.github/CODEOWNERS](../.github/CODEOWNERS), not repeated per document. Roles
may be combined in a small project; the review requirements below still apply.

## Decision making

- Routine changes use pull-request review and lazy consensus.
- A disagreement is resolved by the maintainer after documenting the options,
  evidence, and decision in the pull request or in
  [decisions.md](./decisions.md).
- Changes that alter a public contract — a skill name, a template output path,
  or the meaning of a rule code — require migration guidance.
- Security and privacy concerns escalate to the security reviewer.

## Change classes

| Class | Examples | Required checks |
|---|---|---|
| Editorial | Typos, link repair, clarity without behavior change | Validator and link check |
| Capability | New check, new optional section, new reference or template | Tests, eval case, review |
| Behavior | Changed workflow, new mandatory output, stricter safety rule | Tests, eval cases, threat-model update, two reviewers |
| Contract | Skill rename or removal, output path change, ID or rule-code semantics | Migration plan and deprecation notice |
| Security fix | Secret exposure, destructive instruction, injection risk | Private report, regression test, advisory if needed |

## Pull-request requirements

- Pass the validation workflow.
- State the problem, evidence, and change class.
- Add a regression test for every fixed defect.
- Regenerate the affected `docs/` document when a template changes.
- Preserve unrelated work and permanent requirement, decision, and rule IDs.
- Avoid secrets, personal data, customer identifiers, and live credentials.
- Update documentation that describes the changed behavior.

Reviewers check substance: Is every claim traceable to evidence? Is the scope
boundary explicit? Does it fail safe when evidence is missing? Are security,
privacy, and destructive-action impacts stated?

## Review cadence

| Review | Frequency | Scope |
|---|---|---|
| Security and architecture documents | Quarterly | Controls, boundaries, threat model, dependencies |
| Dependencies and automation | Monthly or automated | Pinned actions, hooks, packages |
| Skills and templates | Per change | Frontmatter, safety rules, links, size |
| Post-incident | After any security or integrity incident | Root cause, regression test, process change |

## Approval and exceptions

An exception requires the rule being waived, a documented rationale and
compensating control, and maintainer approval. For security rules, the security reviewer must also
approve. Undocumented exceptions are defects. The current known gaps are
recorded in [security.md](./security.md#exceptions-and-risk-acceptance); they
are gaps, not approved exceptions.

## Release process

This collection has no release versioning or changelog at its initial state
(D-9). A release is a snapshot of the default branch that passes the validation
workflow.

1. Confirm the validation workflow is green on the commit to publish.
2. Update documentation affected by the change.
3. Tag the reviewed commit if a downloadable snapshot is needed.
4. Verify the published archive contains `SKILL.md` files that start with YAML
   frontmatter.

A snapshot is not valid because a tag exists; it is valid because the tagged
tree passed the gates.

## Deprecation

- Announce the deprecation in the skill's `SKILL.md` and the README.
- Name the replacement and the migration steps.
- Keep the deprecated skill for at least one review cycle.
- Do not delete historical documentation or recycle IDs.
- Remove the skill only after the deprecation period.

## Security response

- Report vulnerabilities through [SECURITY.md](../SECURITY.md), not a public
  issue.
- Triage, fix, regression-test, and disclose through a coordinated process.
- Do not include exploit details, secrets, or personal data in a public
  advisory.
- A prompt-injection or destructive-instruction report is a security issue even
  when no code executes, because skills influence agent behavior.

## Repository settings expected by this policy

These settings live in the hosting platform, not in the tree. Maintainers must
keep them aligned with this document:

- default branch protected against force-push and deletion;
- required status checks from the `Validate` workflow;
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
- [Rules](./rules.md)
