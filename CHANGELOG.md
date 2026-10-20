# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/).

## [Unreleased]

### Planned

- Automated model-behavior evaluation harness for `evals/` fixtures.

## [2.0.0] - 2026-10-20

### Added

- Repository validator (`scripts/validate_skills.py`) enforcing the Agent Skills
  specification and the enterprise metadata profile.
- Link checker (`scripts/check_links.py`) for all non-template Markdown.
- Regression tests covering the 1.x frontmatter corruption and validator rules.
- Pre-commit hooks for YAML/JSON/TOML, whitespace, merge markers, large files,
  private keys, gitleaks, and skill validation.
- CI validation workflow with pinned action commits and read-only permissions.
- Dependabot configuration for GitHub Actions and Python dependencies.
- Trigger, non-trigger, and adversarial evaluation fixtures in `evals/`.
- Frontmatter-aware Markdown linting via `markdownlint-cli2` and
  `.markdownlint-cli2.yaml`, wired into pre-commit and CI.
- Pre-commit hook revisions pinned by commit SHA, with Dependabot coverage for
  the pre-commit ecosystem.
- Enterprise metadata in every skill: spec version, SemVer, owner, review date,
  standards, classification, and risk.
- Enterprise documentation standard, including evidence provenance, RFC
  2119/8174 language, Diátaxis, ADR/MADR, C4/ISO 42010, naming, accessibility,
  and change management.
- Enterprise requirements standard in `prd`: requirement quality rules,
  acceptance criteria, traceability, and a non-functional requirement catalog.
- Enterprise security baseline covering governance, control domains, supply
  chain, vulnerability and incident response, privacy, AI/agent security, and
  anti-overclaim rules.
- Test standard covering traceability, security, accessibility, performance,
  resilience, test data, flaky tests, and evidence format.
- Accessibility reference for design documentation covering WCAG 2.2 AA, EN 301
  549, DTCG tokens, component criteria, and conformance reporting.
- Engineering practices reference covering secure coding, compatibility,
  observability, dependencies, and review checklists.
- Governance, threat model, architecture, security policy, contribution guide,
  code of conduct, CODEOWNERS, and pull-request template.
- Root `AGENTS.md` and `CLAUDE.md` symbolic links to the shared README.

### Removed

- Document-control blocks and their `Owner`, `Status`, `Version`,
  `Last reviewed`, and `Classification` fields. Repository documents, generated
  templates, and skill instructions no longer carry per-document metadata;
  ownership stays in `CODEOWNERS` and review cadence in `docs/governance.md`.
- The PRD approval/change-history table. Approval and revision history are
  recorded in the pull request and Git history instead of duplicated in the
  document.
- `metadata.owner`, `metadata.reviewed`, and `metadata.classification` from
  skill frontmatter, and the corresponding validator rules. Required metadata is
  now `spec`, `version`, `standards`, and `risk`.
- Review dates from template evidence lines; the reviewed commit SHA is kept.

Data classification in the security profile is unchanged: it classifies the
system's data, not the document.

### Changed

- Renamed `docs/Architecture.md` to `docs/architecture.md` for consistent
  lowercase kebab-case documentation naming. `ai-init` migrates existing files
  case-safely and reports the change.
- Expanded templates with traceability, threat model, accessibility, evidence,
  and verification sections.
- Expanded `security`, `tests`, `design`, `prd`, `ai-init`, and `code-quality`
  skill instructions with explicit operating constraints and scope boundaries.
- Updated README documentation index, validation instructions, and governance
  links.

### Fixed

- Restored the required YAML frontmatter to all six `SKILL.md` files. Version
  1.x frontmatter was rendered as a horizontal rule and heading, so compliant
  agents and the Skills CLI could not discover or load any skill.
- Added automated gates so the frontmatter regression cannot merge silently.

### Security

- Security policy with private reporting, response targets, coordinated
  disclosure, safe-harbor expectations, and user guidance.
- Threat model covering prompt injection, secret exposure, destructive actions,
  metadata corruption, supply-chain compromise, and compliance overclaim.
- Secret scanning retained and expanded, with explicit prohibition on secrets,
  credentials, and personal data in generated documentation.

### Breaking changes

- `docs/Architecture.md` is now `docs/architecture.md`.
- Every skill now requires the enterprise metadata block and an eval fixture.
- The shared starter pre-commit configuration includes additional hygiene hooks.

### Migration

1. Upgrade the installed skills.
2. Rename `docs/Architecture.md` to `docs/architecture.md` (two-step rename on
   case-insensitive filesystems) and update links.
3. Run `python scripts/validate_skills.py` against a fork if you maintain one.
4. Reinstall pre-commit hooks with `pre-commit install`.

## [1.0.0] - 2026-10-20

### Added

- Initial collection: `ai-init`, `prd`, `security`, `tests`, `design`, and
  `code-quality` skills with templates, style references, and Mermaid standard.

### Known defect

- All six `SKILL.md` files shipped without YAML frontmatter. The skills were not
  discoverable or loadable by compliant Agent Skills hosts. Fixed in 2.0.0.
