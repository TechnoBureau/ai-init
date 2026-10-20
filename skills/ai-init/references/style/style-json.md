# JSON Style Baseline

Follow the repository's existing schema and consumer conventions. Do not
reformat generated or lock files by hand. The tooling below is optional unless
present in the repository's scripts or CI configuration.

## Tooling

- Validate against a JSON Schema when the repository defines a schema and
  provides a validation path.
- Formatter: `prettier --parser json` or language-native equivalent.

## Rules

- 2-space indentation.
- Double quotes only; no trailing commas; no comments (plain JSON has no
  comment syntax — use `.jsonc`/`.json5` explicitly if comments are
  required, and say so in the filename/tooling config).
- Key casing: follow the existing API/configuration contract. Do not change
  key names based only on the implementation language; document verified
  cross-service contracts in `docs/architecture.md`.
- Sort keys alphabetically for generated/lock-style files where tooling
  supports it (improves diffs).
- UTF-8 encoding, LF line endings, file ends with newline.
- Large/generated JSON (lockfiles, snapshots) should not be hand-edited —
  note this in a comment in the adjacent `.md` doc since JSON itself can't
  carry comments.
