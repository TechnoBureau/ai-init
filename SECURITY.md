# Security Policy

## Supported state

Security fixes are applied to the default branch. There is no maintained
release line or backport policy while the collection is at its initial state.

If you maintain a fork, you are responsible for applying updates from upstream.

## Reporting a vulnerability

Report vulnerabilities privately through GitHub Security Advisories:

<https://github.com/TechnoBureau/ai-init/security/advisories/new>

Do not open a public issue, discussion, or pull request for a vulnerability.

Include:

- affected skill, file, and version;
- a minimal reproduction or a clear description of the behavior;
- the impact you believe is possible;
- any suggested fix or mitigation;
- whether the issue is already public.

Never include live credentials, private keys, customer records, or personal
data in a report. Redact secrets and rotate any credential that may have been
exposed.

## What counts as a security issue

- Instructions that can cause secret exposure, data exfiltration, or
  destructive file/Git operations.
- Prompt-injection paths that let untrusted repository content change the
  skill's scope or safety behavior.
- Weak or misleading security guidance that could cause a user to believe a
  control exists when it does not.
- Validator or CI bypasses that allow malformed frontmatter, unsafe links, or
  secret-bearing content to ship.
- Supply-chain issues in the repository's actions, hooks, or dependencies.
- A published skill that fails to load because of corrupted machine-readable
  metadata.

General documentation errors, style issues, and feature requests are not
security issues; use a public issue for those.

## Response targets

These are project targets, measured in business days from a complete private
report. They are not a contractual service-level agreement.

| Stage | Target |
|---|---|
| Acknowledgement | 5 business days |
| Initial triage and severity | 10 business days |
| Critical fix or mitigation | 30 days |
| High severity fix | 60 days |
| Moderate/low fix | Next scheduled release |

Complex issues may take longer. The maintainer will communicate status and any
change to the timeline through the private advisory.

## Disclosure

- We follow coordinated disclosure.
- We will credit reporters who want attribution and respect requests for
  anonymity.
- We aim to publish an advisory after a fix is available, or after 90 days,
  whichever comes first, unless a longer embargo is justified.
- Do not publish exploit details before coordination is complete.

## Safe harbor

We will not pursue action against researchers who:

- act in good faith and avoid privacy violations, data destruction, and service
  disruption;
- test only against their own repositories, forks, or local installations;
- report findings privately and give reasonable time to remediate;
- do not access, modify, or exfiltrate data that does not belong to them.

This statement does not authorize testing against third-party systems or
violating any law.

## Security expectations for users

- Install skills from the official repository or a trusted fork.
- Review generated changes before committing or deploying them.
- Treat skills as instructions, not as a sandbox. Enforce tool and network
  permissions in your agent host.
- Verify YAML frontmatter after installing; a skill that does not start with
  `---` will not load.
- Do not place secrets in a repository that an agent can read unless the host
  isolates them.
- Report suspicious skill behavior rather than editing around it silently.

## Repository security controls

The repository ships these controls:

- validation workflow configuration for pull requests and pushes;
- pre-commit secret scanning with gitleaks and private-key detection;
- pinned GitHub Actions, pre-commit hooks, and Python dependencies;
- Dependabot configuration for actions and Python packages;
- CODEOWNERS ownership rules;
- documentation for private vulnerability reporting.

Some controls depend on GitHub repository settings that are not stored in the
tree: required status checks, CODEOWNERS enforcement, private vulnerability
reporting, secret scanning, and tag protection. A maintainer must verify those
settings; see [governance](./docs/governance.md#repository-settings-expected-by-this-policy).
This document does not assert that they are enabled.

These controls reduce risk; they do not make the collection certified or
compliant with any framework.

## Related documents

- [Threat model](./docs/threat-model.md)
- [Governance](./docs/governance.md)
- [Skill authoring standard](./docs/skill-standard.md)
