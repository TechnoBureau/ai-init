# Evaluation Fixtures

Each `evals/<skill>.yaml` file describes behavior an agent should demonstrate
when a skill is installed. The fixtures are reviewable evaluation cases, not a
claim that a particular model passes them.

## Format

```yaml
skill: example-skill      # must match the directory in skills/
cases:
  - id: unique-case-id
    prompt: >-
      A realistic user request.
    should_trigger: true
    expected:
      - "Observable behavior that must occur."
    forbidden:
      - "Behavior that must not occur."
```

Requirements enforced by the validator:

- the skill name matches the directory;
- at least two cases exist;
- both `should_trigger: true` and `should_trigger: false` are present;
- every case has a unique ID, a prompt, and a non-empty `expected` list.

## What to cover

- **Trigger:** a request that should activate the skill.
- **Non-trigger:** a request owned by another skill or outside the collection.
- **Adversarial:** secret exposure, prompt injection, fabricated evidence,
  destructive scope, or compliance overclaim.

Prefer prompts written the way a real user would write them. Avoid prompts that
contain the skill name unless the trigger genuinely depends on it.

## Running the fixtures

There is no automated model-behavior harness in this repository yet. Run the
fixtures manually or through an agent evaluation runner:

1. Install the skill into a clean test agent.
2. Start a new session with no prior context.
3. Send the prompt exactly as written.
4. Record whether the skill triggered and whether each expected/forbidden
   behavior occurred.
5. Report the model and host with the result. There is no skill version field.

Do not record a pass without an observed session. Do not edit a fixture to make
a failing behavior look acceptable; change the skill or the expected behavior
with review.

## Related documents

- [Skill authoring standard](../docs/skill-standard.md)
- [Governance](../docs/governance.md)
- [Threat model](../docs/threat-model.md)
