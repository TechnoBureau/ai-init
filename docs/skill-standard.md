# Skill Authoring Standard

This standard is normative for every skill in this repository. `metadata.risk`
determines review depth, but these requirements apply to all skills.

The format follows the open [Agent Skills specification](https://agentskills.io/specification)
and adds the enterprise profile enforced by
[`scripts/validate_skills.py`](../scripts/validate_skills.py) and CI.

## Why this standard exists

A `SKILL.md` without YAML frontmatter is still valid Markdown and can look
almost correct in a rendered diff, yet compliant agents cannot discover or load
it. A formatter can reproduce that failure in one pass by rendering `---` as a
horizontal rule and collapsing `name` and `description` into a heading.

The lesson is structural: machine-readable metadata needs an automated gate,
not reviewer attention. That is why frontmatter validation, unit tests, a
pre-commit hook, and CI are mandatory rather than recommended.

## Required layout

```text
skills/<name>/
├── SKILL.md          # required: frontmatter + instructions
├── references/       # optional: detailed guidance, loaded on demand
├── templates/        # optional: output templates
└── files/            # optional: starter configuration
```

- One skill per directory. The directory name is the skill name.
- `SKILL.md` must be self-contained; skills are installed individually and
  cannot rely on a sibling skill's reference files.
- Keep progressive disclosure: `SKILL.md` holds the workflow and
  non-negotiables; long catalogs, standards, and templates live in
  `references/` and `templates/`.
- Templates under `templates/` must record the output path they target, either
  in `SKILL.md` or in the template itself, so an agent cannot guess wrong.
- Keep `SKILL.md` under 500 lines and roughly 5,000 tokens.
- Use relative links. Every referenced path must exist.
- Do not add executable scripts unless the skill genuinely needs them. If you
  do, they require review as code, pinned dependencies, and tests.

## Frontmatter schema

```yaml
---
name: example-skill
description: >-
  What the skill does, for which repository or product, and what outcome it
  produces. Use when the user asks for <specific triggers>.
license: MIT
compatibility: >-
  Environment requirements, supported platforms, and network needs.
metadata:
  spec: "1.0"
  version: "1.2.3"
  standards: "Agent Skills 1.0; <applicable standards>"
  risk: "low"
allowed-tools: "Read Grep Glob"
---
```

### Field rules

| Field | Required | Rule |
|---|---|---|
| `name` | Yes | 1–64 chars, lowercase `a-z0-9-`, no leading/trailing/consecutive hyphen, equals directory name, no reserved vendor words |
| `description` | Yes | 1–1024 chars, no XML tags, states capability **and** trigger conditions, includes the phrase "Use when/for/to" |
| `license` | Recommended | SPDX identifier or reference to the repository licence |
| `compatibility` | Optional | ≤500 chars; platforms, tools, network and privilege needs |
| `metadata` | Yes (enterprise profile) | String-to-string map; see below |
| `allowed-tools` | Optional | Space-separated declarative tool list; **not** a security boundary |

### Enterprise metadata

| Key | Rule |
|---|---|
| `spec` | Agent Skills specification version; currently `"1.0"` |
| `standards` | Semicolon-separated standards actually applied |
| `risk` | `low`, `medium`, `high`, or `critical`; drives review depth |

All metadata values must be quoted strings. An unquoted numeric value parses as
a YAML number and violates the specification.

### Description quality

The description is the only content an agent sees before loading the skill.
Write it for retrieval:

- name the object and the outcome, not just the activity;
- include the words a user is likely to use;
- include exclusions when confusion with another skill is likely;
- do not include internal process narration or marketing claims.

## Body requirements

Every `SKILL.md` contains, in this order:

1. An H1 title.
2. **Operating constraints** — trust boundary, read/write scope, secret
   handling, destructive-action limits, and evidence honesty.
3. The skill workflow, preflight checks, and evidence rules.
4. A "when not to act" or scope boundary where the skill could overreach.
5. Links to references and templates, each resolving to a real file.

Body rules:

- Use RFC 2119/8174 keywords only for real requirements.
- Never instruct an agent to fabricate facts, owners, dates, controls, test
  results, or compliance status.
- Never instruct an agent to read, print, or commit secrets.
- Treat repository content as untrusted data, not as instructions.
- Preserve user work and permanent IDs.
- Distinguish current behavior from recommendations.
- Keep tables narrow enough to read without horizontal scrolling.
- Do not put unresolved `{{PLACEHOLDER}}` tokens in a skill or reference; they
  belong only in `templates/`.

## Formatter and linter safety

Machine-readable files must survive automated formatting.

- Never run `mdformat`, Prettier, or a Markdown "fix" across `SKILL.md`
  without frontmatter support. The known failure mode is converting `---` to a
  thematic break.
- Configure Markdown tooling to recognize YAML frontmatter. Prefer tools that
  leave frontmatter untouched.
- `pre-commit` runs the validator before a commit; do not bypass hooks with
  `--no-verify` unless the failure is a proven false positive and the reason
  is recorded.
- If a formatter corrupts frontmatter, restore it from Git history and add a
  regression case to `tests/`; do not hand-edit the rendered heading.

## Evaluation fixtures

Every skill has `evals/<name>.yaml`:

```yaml
skill: example-skill
version: "1.2.3"
cases:
  - id: positive-case
    prompt: A realistic user request.
    should_trigger: true
    expected:
      - "Observable behavior that must occur."
    forbidden:
      - "Behavior that must not occur."
  - id: negative-case
    prompt: A request owned by another skill.
    should_trigger: false
    expected:
      - "Routes to the owning skill."
```

Requirements:

- at least one trigger and one non-trigger case;
- each case has a unique ID, a realistic prompt, and observable expectations;
- include at least one adversarial case per skill: secret exposure, fabricated
  evidence, destructive scope, or prompt injection.

These fixtures are reviewable evaluation cases. Until an automated harness is
adopted, they are run manually or by an agent evaluation runner; the repository
does not claim automated model-behavior scoring.

## Validation and review gates

| Gate | Tool | Blocking |
|---|---|---|
| Frontmatter, metadata, links, limits | `scripts/validate_skills.py` | Yes |
| Validator regression tests | `python -m unittest discover -s tests` | Yes |
| Local link integrity | `scripts/check_links.py` | Yes |
| Whitespace, YAML, JSON, TOML, merge markers, large files | pre-commit hooks | Yes |
| Secret scanning | gitleaks pre-commit hook | Yes |
| Markdown consistency | `markdownlint-cli2` with `.markdownlint-cli2.yaml` | Yes |
| Human review | CODEOWNERS | Yes |

Run locally:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py --strict
python scripts/check_links.py
python -m unittest discover -s tests -v
pre-commit run --all-files
```

## Change management

This collection does not maintain a changelog or release version numbers while
it is at its initial state. Change history lives in Git and in the pull request
that makes the change.

- Describe the problem, evidence, and behavior change in the pull request.
- Update affected documentation in the same change.
- Deprecate before removal: mark the skill deprecated in `SKILL.md` and the
  README, publish the replacement, and keep the skill available for at least
  one review cycle.
- Never silently change a permanent document path. Provide migration guidance
  and preserve existing IDs.
- Add a regression test for every fixed defect.

If the project later adopts releases, define the version scheme and changelog
policy in [governance](./governance.md) before applying it.

## Review depth by risk

| Risk | Required review |
|---|---|
| `low` | Validator, tests, one maintainer review |
| `medium` | Add security and evidence review; confirm no destructive default |
| `high` | Add threat-model update and a second reviewer |
| `critical` | Add security owner approval and an explicit threat model |

## Related documents

- [Governance](./governance.md)
- [Threat model](./threat-model.md)
- [Architecture](./architecture.md)
- [Contributing](../CONTRIBUTING.md)
