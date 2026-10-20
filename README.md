# AI Init Skills

A modular Agent Skills collection for evidence-grounded repository
documentation, product requirements, enterprise security, test work, design,
and code quality. Install the full collection for the complete workflow or a
single skill for focused work.

## Install

Install every skill for all agents supported by the Skills CLI:

```bash
npx skills add technobureau/ai-init --all --agent '*'
```

For a global install, add `-g`:

```bash
npx skills add technobureau/ai-init --all --agent '*' -g
```

To install one skill, replace `--all` with `--skill` and one of: `ai-init`,
`prd`, `security`, `tests`, `design`, or `code-quality`. See the [Skills CLI
documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
for agent support and options.

## Skills

| Skill | Use it for | Entry point |
|---|---|---|
| `ai-init` | Safe bootstrap for new or existing repositories | [SKILL.md](./skills/ai-init/SKILL.md) |
| `prd` | Evidence-grounded PRD creation or refinement | [SKILL.md](./skills/prd/SKILL.md) |
| `security` | Modular security posture, PQC readiness, and platform hardening | [SKILL.md](./skills/security/SKILL.md) |
| `tests` | Test implementation/review or opt-in `docs/tests.md` creation | [SKILL.md](./skills/tests/SKILL.md) |
| `design` | UI design-system documentation | [SKILL.md](./skills/design/SKILL.md) |
| `code-quality` | Safe dead-code cleanup, modularity, and API contracts | [SKILL.md](./skills/code-quality/SKILL.md) |

Invoke a skill by name where supported, such as `$ai-init`, `$security`, or
`$tests`, or describe the task to an agent that has installed it.

## Defaults and safeguards

- `ai-init` creates the root `README.md` and common documentation. It does not
  create `docs/tests.md`; use `$tests` when test work or that document is
  requested.
- On execution, skills create root `AGENTS.md` and `CLAUDE.md` as relative
  symbolic links to `README.md`, after checking for existing files and
  preserving their unique instructions. They do not use copied templates.
- Documentation is grounded in source and configuration. Existing content,
  permanent IDs, and unrelated work are preserved; empty repositories get a
  clearly labeled initial format rather than invented project facts.
- Security profiles are modular. They conditionally map relevant controls to
  NIST, FIPS, OWASP, CIS, and OpenSCAP/SCAP guidance without treating a
  partial repository review as a compliance attestation.
- Code conventions are derived from repository instructions, language
  requirements, and configured tooling, with recommendations distinguished
  from existing project rules.
- Generated documentation uses uppercase root `README.md`; other project
  documents belong under `docs/`.

## Repository layout

```text
skills/
  ai-init/
    references/style/          # Adaptable language guidance
    references/architecture/   # Mermaid standard
    templates/                 # Common docs; README.md is the only root template
  prd/templates/               # PRD
  security/
    references/                # Modular security baseline
    templates/                 # Security posture
  tests/templates/             # Opt-in tests and verification inventory
  design/
    references/                # Design-system catalog
    templates/                 # Project design document
  code-quality/references/     # Repository-fit engineering practices
```
