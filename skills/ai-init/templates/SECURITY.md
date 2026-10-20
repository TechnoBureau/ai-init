# Security Policy

## Supported state

{{CONFIRMED_SUPPORTED_VERSIONS_OR_CURRENT_DEFAULT_BRANCH}}

State plainly which versions or branches receive security fixes. If there is
no maintained release line, say so instead of implying long-term support.

## Reporting a vulnerability

Report vulnerabilities privately through {{CONFIRMED_PRIVATE_CHANNEL}}.

Do not open a public issue, discussion, or pull request for a vulnerability.

Include:

- affected component, file, and version or commit;
- a minimal reproduction or a clear description of the behavior;
- the impact you believe is possible;
- any suggested fix or mitigation;
- whether the issue is already public.

Never include live credentials, private keys, customer records, or personal
data in a report. Redact secrets and rotate any credential that may have been
exposed.

If no private channel is confirmed, do not publish this file claiming one.
Use the host's private vulnerability reporting feature when available, or ask
the owner to establish a channel and report the gap.

## Scope

In scope: {{CONFIRMED_IN_SCOPE_COMPONENTS}}

Out of scope: {{CONFIRMED_OUT_OF_SCOPE_ITEMS_OR_NOT_DOCUMENTED}}

Typical out-of-scope items include third-party services, social engineering,
and physical security unless the project owner states otherwise. Do not assert
an out-of-scope list that the owner has not confirmed.

## Response targets

These are project targets, not a contractual service-level agreement. Replace
them only with confirmed values.

| Stage | Target |
|---|---|
| Acknowledgement | {{CONFIRMED_OR_NOT_DOCUMENTED}} |
| Initial triage and severity | {{CONFIRMED_OR_NOT_DOCUMENTED}} |
| Fix or mitigation | {{CONFIRMED_OR_NOT_DOCUMENTED}} |
| Disclosure | {{CONFIRMED_OR_NOT_DOCUMENTED}} |

## Disclosure

- Coordinate disclosure with the maintainers.
- Credit reporters who want attribution and respect requests for anonymity.
- Publish an advisory after a fix is available, or after an agreed embargo
  period.
- Do not publish exploit details before coordination is complete.

## Safe harbor

Describe the project's position on good-faith security research only when the
owner has confirmed it. A typical statement covers researchers who avoid
privacy violations, data destruction, and service disruption; test only
against their own systems; report privately; and allow reasonable remediation
time.

Do not imply authorization to test third-party systems or to violate law.

## Security expectations for users

- Install and deploy from official sources.
- Keep dependencies current and monitor advisories.
- Review generated or automated changes before merging or deploying them.
- Enforce least privilege for tokens, CI jobs, and runtime identities.
- Do not place secrets in a repository that contributors or agents can read.
- Report suspicious behavior privately rather than working around it silently.

## Related documents

- [Threat model](./docs/threat-model.md)
- [Security posture](./docs/security.md)
- [Contributing](./CONTRIBUTING.md)
