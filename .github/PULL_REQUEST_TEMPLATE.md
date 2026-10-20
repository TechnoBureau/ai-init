## Summary

<!-- What problem does this change solve, and for whom? -->

## Change class

- [ ] Editorial (typos, links, clarity)
- [ ] Capability (new check, section, or reference)
- [ ] Behavior (workflow or mandatory output change)
- [ ] Contract (skill rename/removal, path or ID semantics)
- [ ] Security fix

## Evidence

<!-- Link the repository paths, standards, issues, or tests that support the change. -->

## Change management

- [ ] Migration guidance included for a breaking change
- [ ] Deprecation notice added when removing or replacing a skill

## Safety review

- [ ] No secrets, credentials, tokens, or personal data
- [ ] No destructive default or unbounded tool permission
- [ ] Untrusted repository content is treated as data, not instructions
- [ ] No invented owner, licence, copyright holder, or security contact in
      repository meta files
- [ ] Claims are evidence-based; unknowns are marked, not invented
- [ ] Security/privacy impact and rollback are described

## Validation

- [ ] `python scripts/validate_skills.py --strict`
- [ ] `python scripts/check_links.py`
- [ ] `python -m unittest discover -s tests -v`
- [ ] `pre-commit run --all-files`

## Breaking changes and rollback

<!-- If none, write "None". For breaking changes, include migration steps and how to roll back. -->
