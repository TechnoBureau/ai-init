# Secret Scanning Standard

Use IBM [`detect-secrets`](https://github.com/IBM/detect-secrets) with a
committed baseline when the repository needs an auditable secret gate. The
baseline is both policy and findings: `plugins_used` defines what runs,
`exclude.files` defines what is skipped, and `results` records audited false
positives by hash.

## Baseline policy

[`../files/.secrets.baseline`](../files/.secrets.baseline) pins:

| Setting | Value | Reason |
|---|---|---|
| Tool version | `0.13.1` | Must match the pre-commit `rev`; a mismatch makes the hook rewrite the file and exit 3 |
| Keyword detector | Disabled | Flags ordinary prose such as `password: example`; provider and entropy detectors carry the signal |
| Entropy limits | Base64 4.5, hex 3.0 | Tool defaults; raise them only with measured false-positive data |
| Findings | None | A real secret is removed and rotated, never recorded as a suppression |

Provider detectors stay enabled: AWS, Artifactory, Basic Auth, Cloudant, IBM
Cloud IAM, IBM COS HMAC, JWT, Mailchimp, Private Key, Slack, Softlayer, Stripe,
and Twilio.

Disabling keyword scanning has a cost: a hard-coded password with no provider
pattern and no entropy signal is missed. Keep the gitleaks hook as the
complementary regex gate, and add a provider detector or a custom rule when the
repository depends on a credential type the baseline does not cover.

The committed starter omits `generated_at`. The loader does not require it, and
a timestamp is not a review record. The tool adds it whenever it rewrites the
baseline.

## Excluded files

| Pattern | Why |
|---|---|
| `.secrets.baseline` | Stores hashes, not secrets, and must not scan itself |
| `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, `pnpm-lock.yaml`, `bun.lockb` | Resolved dependency trees are full of high-entropy hashes |
| `go.mod`, `go.sum` | Dependency pins and checksums |
| `Cargo.lock`, `poetry.lock`, `Pipfile.lock`, `Gemfile.lock`, `composer.lock` | Lockfiles |
| `requirements*.txt`, `pom.xml`, `build.gradle`, `build.gradle.kts` | Dependency declarations whose version pins look like secrets |
| `node_modules/`, `vendor/`, `third_party/` | Third-party code cannot be fixed here and is not reviewed here |
| `dist/`, `build/`, `.venv/`, `venv/`, `__pycache__/` | Generated or local output |
| `*.min.js`, `*.min.css`, `*.map`, `*.lock`, `*.sum`, `*.snap` | Minified, source-map, lock, checksum, and snapshot output |

Do not exclude `tests/` or `fixtures/` wholesale. A real key pasted into a
fixture is exactly the accident the scanner exists to catch. Allowlist the
specific line with `# pragma: allowlist secret`, or audit the finding into the
baseline after confirming it is fake.

## Commands

Create or update the baseline after a tool upgrade or an audited finding:

```bash
detect-secrets scan --no-keyword-scan --update .secrets.baseline
detect-secrets audit .secrets.baseline
```

`--exclude-files` is stored in the baseline, so later scans reuse it. Pass it
again only when changing the exclusion policy; a new value replaces the old
list. `--update` appends the baseline's own path to the exclusion regex; that
is expected and does not change which project files are scanned.

Verify a change before committing:

```bash
detect-secrets-hook --baseline .secrets.baseline --no-keyword-scan <paths>
```

## Rules

- Never add a real secret to `results`. Remove the secret, rotate it, and then
  rescan. A baseline entry is a suppression, not remediation.
- Keep `plugins_used` and `exclude` identical between the repository baseline
  and the starter. Findings may differ; policy must not.
- When the tool version changes, update the pre-commit `rev` and the baseline
  `version` together.
- Keep the gitleaks hook. The two scanners have different engines and failure
  modes.
- Copy the baseline only when the project adopts IBM detect-secrets. Do not
  enable a scanner the project will not maintain.
