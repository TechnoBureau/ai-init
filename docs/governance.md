# Governance

> **Document control** — Owner: TechnoBureau · Status: Draft · Version: 2.0.0 · Last reviewed: 2026-10-20 · Classification: Public

This document defines how the skill collection is owned, changed, reviewed,
released, and deprecated. It applies to skill content, templates, references,
evaluation fixtures, and repository automation.

## Scope and principles

- Skills are production instructions. They influence how agents modify real
  repositories, so they are reviewed with the same care as code.
- Evidence beats assertion. A claim in a skill must be supportable by the
  repository or a named standard.
- Safety beats completeness. A skill must refuse to invent facts, expose
  secrets, or take destructive action.
- Changes are reversible and traceable. Permanent IDs and released versions are
  never rewritten.
- No compliance claim is implied by this repository. Frameworks referenced in
  skills are vocabularies for evidence, not certifications.

## Roles

| Role | Accountability |
|---|---|
| Maintainer | Releases, repository settings, CODEOWNERS, security response, final decision on disputed changes |
| Reviewer | Technical and editorial review against the skill standard; may be a maintainer |
| Security reviewer | Threat model, destructive defaults, secret handling, supply chain, and vulnerability response |
| Contributor | Proposes changes, supplies evidence, updates tests and evals, responds to review |

The current accountable owner is recorded in [`CODEOWNERS`](../CODEOWNERS).
Roles may be held by the same person in a small project; the review
requirements below still apply.

## Decision making

- Routine changes use pull-request review and lazy consensus.
- A disagreement is resolved by the maintainer after documenting the options,
  evidence, and decision in the pull request or an ADR.
- Security and privacy concerns can block a change until resolved.
- Changes that alter a public contract (skill name, output path, required
  section, ID semantics) require a major version and migration guidance.

## Change classes

| Class | Examples | Required evidence | Version impact |
|---|---|---|---|
| Editorial | Typos, link repair, clarity without behavior change | Validator and link check | Patch |
| Capability | New check, new optional section, new reference | Tests, eval case, review | Minor |
| Behavior | Changed workflow, new mandatory output, stricter safety rule | Tests, eval cases, threat-model update, two reviewers | Minor or major |
| Contract | Skill rename/removal, output path change, ID semantics | Migration plan, changelog, deprecation period | Major |
| Security fix | Secret exposure, destructive instruction, injection risk | Private report, regression test, advisory if needed | Patch or minor |

## Pull-request requirements

Every pull request must:

- pass the validation workflow;
- state the problem, evidence, and change class;
- update `CHANGELOG.md` for user-visible changes;
- update `metadata.version` and eval version for affected skills;
- add or update a regression case when fixing a defect;
- preserve unrelated user work and permanent IDs;
- avoid secrets, personal data, customer identifiers, and live credentials;
- include links to the standards or sources that justify new claims.

Reviewers check substance, not just formatting:

- Can every factual claim be traced to evidence?
- Is the skill's scope boundary explicit?
- Does it fail safe when evidence is missing?
- Does it avoid destructive actions and secret exposure?
- Are instructions unambiguous for an agent with no prior context?
- Are exclusions and limitations honest?

## Review cadence

| Review | Frequency | Scope |
|---|---|---|
| Skill content review | Quarterly | Frontmatter, standards, links, commands, safety rules |
| Security review | Quarterly and after incidents | Threat model, destructive actions, supply chain, secret handling |
| Dependency and action review | Monthly or automated | GitHub Actions pins, Python dependencies, pre-commit hooks |
| Full collection audit | Annually | Every skill, template, eval, and governance control |
| Post-incident review | After any security or integrity incident | Root cause, regression test, process change |

A review updates `metadata.reviewed` only after the evidence has been checked.
Changing a date without reviewing the content is a governance violation.

## Release process

1. Confirm the validation workflow is green on the release commit.
2. Update `CHANGELOG.md` using Keep a Changelog categories.
3. Bump `metadata.version` for every changed skill and its eval file.
4. Update documentation and migration notes.
5. Create a signed, annotated Git tag (`vMAJOR.MINOR.PATCH`) from the reviewed
   commit.
6. Publish a GitHub release with the changelog entry and any breaking-change
   notice.
7. Verify the published archive contains `SKILL.md` files that start with YAML
   frontmatter.

A release is not valid because a tag exists; it is valid because the tagged
tree passed the gates.

## Deprecation

- Announce the deprecation in `CHANGELOG.md`, the skill's `SKILL.md`, and the
  README.
- Name the replacement and the migration steps.
- Keep the deprecated skill for at least one major release.
- Do not delete historical documentation or recycle IDs.
- Remove the skill only after the deprecation period, with a final changelog
  entry.

## Exceptions and risk acceptance

An exception to this standard requires:

- the rule being waived;
- a documented rationale and compensating control;
- an accountable owner;
- an expiry or review date;
- approval from a maintainer and, for security rules, the security reviewer.

Undocumented exceptions are defects. Do not encode an exception as a silent
special case in a skill.

## Security response

- Report vulnerabilities through the private channel in
  [`SECURITY.md`](../SECURITY.md), not a public issue.
- The maintainer coordinates triage, fix, regression test, release, and
  disclosure.
- Do not include exploit details, secrets, or personal data in a public
  advisory.
- A prompt-injection or destructive-instruction report is a security issue even
  if no code executes, because skills influence agent behavior.

## Repository settings expected by this policy

These settings live in GitHub, not in the tree. Maintainers must keep them
aligned with this document:

- default branch protected against force-push and deletion;
- required status checks from the validation workflow;
- required review from CODEOWNERS;
- secret scanning and Dependabot alerts enabled;
- private vulnerability reporting enabled;
- release tags protected;
- no long-lived credentials stored in repository secrets when OIDC is
  available.

If a setting cannot be enabled, record the gap and compensating control rather
than claiming the control exists.

## Metrics

Track, without inventing targets:

- validator and link-check status on the default branch;
- age of the oldest unreviewed skill;
- number of skills without eval coverage (target: zero);
- open security reports and time to triage;
- deprecated skills past their removal date;
- dependency and action-pin freshness.

## Amending this document

Governance changes follow the same pull-request process. A change that weakens
a safety rule requires explicit maintainer and security-reviewer approval and a
changelog entry.
