# Threat Model — {{PROJECT_NAME}}

This is a design-level threat model. It records what the system protects, where
trust changes, and which threats and controls exist. It is not a penetration
test, an audit opinion, or proof that a control operates effectively.

## Scope and assumptions

- Assessed components: {{VERIFIED_COMPONENTS}}
- Environments: {{VERIFIED_ENVIRONMENTS}}
- Out of scope: {{EXCLUSIONS_OR_NONE}}

State assumptions explicitly. An unstated assumption cannot be reviewed.

## Assets

| Asset | Why it matters | Evidence |
|---|---|---|
| {{ASSET}} | {{IMPACT_IF_COMPROMISED}} | `{{PATH_OR_NOT_DOCUMENTED}}` |

Typical assets include identities and sessions, credentials and keys, personal
or regulated data, source and build artifacts, availability of the service, and
the integrity of generated documentation.

## Trust boundaries

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#fafaf5','primaryTextColor':'#1a1a1a','primaryBorderColor':'#3553ff','lineColor':'#3553ff','fontFamily':'JetBrains Mono','fontSize':'12px'}}}%%
flowchart TB
  {{VERIFIED_USERS_AND_SYSTEMS}}
```

| Boundary | What changes here | Expected control |
|---|---|---|
| {{BOUNDARY}} | {{TRUST_OR_PRIVILEGE_CHANGE}} | {{AUTHENTICATION_VALIDATION_OR_ISOLATION}} |

Keep the diagram to about 5–8 nodes. Show only relationships verified in code
or configuration; omit the diagram rather than inventing one.

## Threats and controls

Use STRIDE for security threats and LINDDUN for privacy threats. Assign stable
T-IDs and never recycle them.

| ID | Threat | Category | Impact | Controls | Residual risk |
|---|---|---|---|---|---|
| T-01 | {{THREAT_DESCRIPTION}} | {{STRIDE_LINDDUN}} | {{IMPACT}} | {{EXISTING_CONTROL_OR_NONE}} | {{EVIDENCED_OR_NOT_ASSESSED}} |

Consider at minimum, where applicable:

- injection through untrusted input, files, logs, or retrieved content;
- broken authentication or authorization, including horizontal and vertical
  privilege boundaries;
- secret exposure in code, logs, artifacts, errors, or documentation;
- destructive or irreversible operations without confirmation or recovery;
- supply-chain compromise of dependencies, actions, hooks, or images;
- denial of service through unbounded input, recursion, or resource use;
- sensitive-data disclosure through prompts, telemetry, or model providers;
- tampering with machine-readable metadata or generated artifacts;
- overclaim: presenting an assessment as a certification or a control as
  verified when only design evidence exists.

## Data flows and privacy

| Data | Source | Destination | Crosses trust boundary | Retention |
|---|---|---|---|---|
| {{DATA_TYPE}} | {{SOURCE}} | {{DESTINATION}} | {{YES_NO}} | {{CONFIRMED_OR_NOT_DOCUMENTED}} |

Apply data minimization and purpose limitation. Do not infer a legal basis or
retention obligation from the presence of data; record only confirmed policy.

## Controls mapped to threats

| Control | Threat IDs | Type | Status | Evidence |
|---|---|---|---|---|
| {{CONTROL}} | {{T_IDS}} | {{PREVENT_DETECT_RECOVER}} | {{VERIFIED_PARTIAL_NOT_EVIDENCED}} | `{{PATH}}` |

A control listed here reduces risk; it does not prove operating effectiveness.

## Review triggers

Review this model when:

- a new external interface, data store, or identity path is added;
- permissions, tool access, or deployment topology change;
- a new dependency, action, or third-party service is introduced;
- an incident, near miss, or penetration-test finding occurs;
- the threat landscape or applicable framework changes materially.

## Related documents

- [Security posture](./security.md)
- [Architecture](./architecture.md)
- [Decisions](./decisions.md)
- [Governance](./governance.md)
