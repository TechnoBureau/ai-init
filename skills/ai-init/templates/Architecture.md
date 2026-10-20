# Architecture — {{PROJECT_NAME}}

> Generate this document for repositories with multiple components, data
> flows, deployment topology, or pipeline stages. Derive every component and
> connection from active code or configuration.

## Overview

{{HIGH_LEVEL_SUMMARY}}

## System / Pipeline Diagram

Every generated Architecture document must include at least one compact,
evidence-based high-level overview diagram. Use `flowchart TB` by default and
show only the main actors, components, and relationships verified in active
code or configuration. If no meaningful relationships are evidenced, do not
invent them; omit this document and explain why.

Add separate diagrams only when they clarify verified behavior: a flowchart
for a non-trivial workflow, a sequence diagram for a time-ordered interaction,
or a mind map for a genuine hierarchy. Keep each diagram focused, use short
labels, and aim for about 5–8 nodes. Split by boundary or concern when a view
would be too wide or dense to read at normal GitHub / Markdown preview size;
do not combine the whole system into one diagram. Start each Mermaid diagram
with the exact init block and follow the guidance in
[`references/architecture/mermaid-standard.md`](./references/architecture/mermaid-standard.md).

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#fafaf5','primaryTextColor':'#1a1a1a','primaryBorderColor':'#3553ff','lineColor':'#3553ff','fontFamily':'JetBrains Mono','fontSize':'12px'}}}%%
flowchart TB
  {{VERIFIED_COMPONENTS_AND_CONNECTIONS}}
```

## Components

| Component | Responsibility | Technology | Evidence |
|---|---|---|---|
| {{COMPONENT}} | {{VERIFIED_ROLE}} | {{VERIFIED_TECH}} | `{{CODE_OR_CONFIG_PATH}}` |

## Interfaces and Data Flow

{{DOCUMENT_ONLY_VERIFIED_APIS_EVENTS_STORAGE_AND_EXTERNAL_CONNECTIONS}}

## Deployment and Environments

| Environment / target | Deployment mechanism | Evidence |
|---|---|---|
| {{TARGET}} | {{CONFIGURED_MECHANISM}} | `{{CONFIG_PATH}}` |

## Security Boundaries

Summarize only architecture-level boundaries visible in configuration or
implementation. See [security.md](./security.md) for the repository security
posture.

## Decisions

See [decisions.md](./decisions.md) for permanent D-IDs, rationale, and
alternatives. Do not maintain a second decision register here.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Structure](./structure.md) · [Decisions](./decisions.md) · [Security](./security.md)
