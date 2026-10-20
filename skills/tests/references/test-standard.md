# Enterprise Test and Verification Standard

Use this reference to select test levels, evidence, and quality gates. The
repository's configured tooling always takes precedence. These are criteria for
judgment, not a mandate to add every tool to every project.

## Test levels

| Level | Purpose | Proves | Does not prove |
|---|---|---|---|
| Static analysis | Detect defects before execution | Type, lint, schema, and policy conformance | Runtime behavior |
| Unit | Isolate logic and error paths | Deterministic component behavior | Integration wiring |
| Integration | Exercise real boundaries | Adapter, transaction, and contract behavior | Full user journeys |
| Contract | Protect producer/consumer compatibility | Schema and semantic compatibility | End-to-end availability |
| End-to-end | Validate critical journeys | A user-visible path works in a composed system | Exhaustive input coverage |
| Exploratory | Find unknown risks | Human-discovered defects and usability issues | Repeatable regression coverage |
| Operational | Validate deploy, backup, restore, failover | Recovery and operability | Application correctness |

Apply the smallest level that can prove the behavior. Prefer many fast unit and
integration tests, fewer end-to-end tests, and explicit manual evidence for
accessibility and exploratory risk.

## Requirement traceability

For each `FR-`/`NFR-` ID, record:

| Requirement | Acceptance criterion | Test or evidence | Level | Status |
|---|---|---|---|---|
| FR-1 | Observable behavior | `tests/path::case` or manual procedure | Unit/Integration/E2E | Covered / Partial / Gap |

Rules:

- `Covered` requires an executed or clearly runnable artifact.
- `Partial` names the uncovered branch or environment.
- `Gap` names the risk and owner where known; do not invent a test result.
- A test title alone is not evidence that the test is meaningful. Confirm it
  fails when the behavior is broken where practical.

## Coverage policy

- Use configured line/branch coverage as a diagnostic, not a target to game.
- Do not set a percentage threshold without an approved policy; coverage does
  not measure assertion quality.
- Mutation testing (for example PIT, Stryker, mutmut) is optional and should be
  scoped to critical modules when runtime permits.
- Record excluded paths and the reason (generated code, vendored code,
  platform-specific branches).
- Never delete assertions or skip tests to raise a metric.

## Security testing

| Control area | Evidence to look for |
|---|---|
| Authentication | Invalid, expired, revoked, and replayed credentials are rejected |
| Authorization | Horizontal and vertical privilege boundaries are enforced server-side |
| Input handling | Validation, encoding, size limits, and injection cases at trust boundaries |
| Session and token handling | Expiry, rotation, revocation, storage, audience, and scope |
| Secrets | No secrets in code, logs, fixtures, build output, or test reports |
| Dependencies | SCA and lockfile integrity; known-exploited vulnerabilities triaged |
| Infrastructure as code | Policy-as-code and drift checks where configured |
| Error handling | Fail closed; no stack traces, secrets, or internal paths exposed to users |
| Rate limiting and abuse | Quotas and lockouts behave under load and attack |
| Logging | Security events are recorded without sensitive values |

Map results to OWASP ASVS 5.0 only when a version and verification level are
confirmed. A passing scanner is not proof of application security.

## Accessibility testing

- Confirm the target, for example WCAG 2.2 Level AA. Do not claim conformance
  from automated checks alone.
- Automated: axe-core or the project's configured tool, with zero new critical
  violations.
- Manual: keyboard-only navigation, visible focus, focus order, screen-reader
  smoke test, zoom/reflow at 400%, reduced motion, target size, and color
  contrast.
- Cover error identification, labels, instructions, status messages, and
  authentication where the UI provides them.
- Record tool versions, browser/assistive-technology versions, and exceptions.

## Performance and resilience testing

- Define workload, data volume, environment, and thresholds before running.
  Do not invent service-level objectives.
- Report percentiles (p50/p95/p99), error rate, throughput, and resource
  saturation; averages alone hide tail latency.
- Compare against a recorded baseline in the same environment class.
- For resilience, test timeouts, bounded retries with jitter, idempotency,
  circuit breaking, partial failure, and recovery. Verify that retries do not
  duplicate side effects.
- For backups, perform a restore test. A backup job that runs is not a restore
  capability.

## Test data and privacy

- Prefer generated synthetic data with deterministic seeds.
- If production-derived data is unavoidable, require documented masking,
  access control, retention limits, and removal after the test.
- Never place personal, financial, health, or credential data in fixtures,
  snapshots, screenshots, or CI logs.
- Ensure deletion and retention paths are tested, including backups where the
  policy requires it.

## Quality gates and exit criteria

A gate is real only when CI or a documented release process enforces it.

| Gate | Evidence | Blocking? |
|---|---|---|
| Build and type checks | CI job or exact local command | Confirm from configuration |
| Unit/integration suite | Passing result on the target commit | Confirm from configuration |
| Security scans | SAST/SCA/secret/IaC results and triage | Confirm from configuration |
| Accessibility | Automated plus manual checklist for UI changes | Confirm from policy |
| Performance | Baseline comparison for hot paths | Confirm from policy |
| Migration | Forward and rollback test on representative data | Confirm from policy |

Do not infer a gate from a dependency, script name, or badge. Read the workflow
triggers and required checks.

## Flaky tests and quarantine

- A flaky test is a defect in the test or the system under test.
- Quarantine requires a linked issue, owner, reason, start date, and removal
  condition. Quarantined tests do not count as coverage.
- Retries may reduce noise but must not hide deterministic failures. Record
  retry counts.
- Fix root causes: shared state, time dependence, port collisions, unordered
  assertions, external network, or insufficient synchronisation.

## Evidence format

Record test evidence as:

```text
Command: <exact command>
Environment: <OS/runtime/framework versions>
Commit: <SHA>
Result: Passed | Failed | Blocked | Not run
Duration: <time>
Artifacts: <paths or links, if any>
Failures: <test IDs and short diagnostics>
Not covered: <explicit gaps>
```

This format prevents the most common documentation failure: claiming a suite
passed without saying what ran, where, and against which commit.
