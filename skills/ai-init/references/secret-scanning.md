# Secret Scanning Standard

Use IBM [`detect-secrets`](https://github.com/IBM/detect-secrets) with a
committed baseline when the repository needs an auditable secret gate. The
baseline is both policy and findings: `plugins_used` defines what runs,
`exclude.files` defines what is skipped, and `results` records audited false
positives by hash.

## Version and dependencies

Pin the IBM fork by its version tag, not a commit SHA:

```yaml
- repo: https://github.com/IBM/detect-secrets
  rev: 0.13.1+ibm.64.dss
  hooks:
    - id: detect-secrets
      additional_dependencies:
        - boxsdk<4
        - chardet<7
```

`boxsdk` and `chardet` are already transitive requirements: the fork declares
`boxsdk[jwt]<4.0.0`, and `binaryornot` pulls in `chardet`. Declaring both in
`additional_dependencies` is still worth doing: it bounds each library so a new
major release cannot silently change hook behavior, and it keeps the hook
environment reproducible from this file alone. Both bounds resolve on Python
3.11 and are exercised in CI.

The baseline `version` must equal the hook `rev`. If they differ, the hook
rewrites the baseline and exits with status 3.

## Baseline policy

[`../files/.secrets.baseline`](../files/.secrets.baseline) records:

| Setting | Value | Reason |
|---|---|---|
| Tool version | `0.13.1+ibm.64.dss` | Must match the pinned hook |
| Plugins | All non-keyword plugins recorded | The hook runs `--use-all-plugins` |
| Keyword detector | Disabled | Flags ordinary prose such as `password: example` |
| Entropy limits | Base64 4.5, hex 3.0 | Tool defaults; raise them only with measured false-positive data |
| Findings | None | A real secret is removed and rotated, never recorded as a suppression |

`--use-all-plugins` is safe only because the keyword detector is explicitly
disabled. It adds Box, GitHub Enterprise, GitHub token, npm, Azure storage,
Square OAuth, and the remaining provider detectors beyond the older default set.

The baseline's `GheDetector` entry records `github.ibm.com` as its instance.
Tailor `ghe_instance` to the organization's GitHub Enterprise host, or disable
that plugin when the repository does not use one.

The committed starter omits `generated_at`. The loader does not require it, and
a timestamp is not a review record. The tool adds it whenever it rewrites the
baseline.

## Hook arguments

```yaml
args:
  - --baseline
  - .secrets.baseline
  - --use-all-plugins
  - --no-keyword-scan
  - --fail-on-unaudited
```

- `--baseline` makes audited false positives stable instead of re-reported.
- `--use-all-plugins` runs every available detector, not just the ones the
  baseline recorded.
- `--no-keyword-scan` disables denylisted-variable-name matching.
- `--fail-on-unaudited` fails when the baseline holds an entry nobody has
  labelled. An empty `results` map means nothing is pending.

Disabling keyword scanning has a cost: a hard-coded password with no provider
pattern and no entropy signal is missed. Keep the gitleaks hook as the
complementary regex gate, and add a provider detector or a custom rule when the
repository depends on a credential type the baseline does not cover.

## Excluded files

The hook `exclude` and the baseline `exclude.files` are the same regular
expression. Change both together; `tests/test_secret_scanning.py` fails when
they diverge.

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
| `*.drawio` | Diagram archives embed compressed XML that trips entropy detectors |

Do not exclude `tests/` or `fixtures/` wholesale. A real key pasted into a
fixture is exactly the accident the scanner exists to catch. Allowlist the
specific line with `# pragma: allowlist secret`, or audit the finding into the
baseline after confirming it is fake.

## Commands

Create or update the baseline after a tool upgrade or an audited finding:

```bash
detect-secrets scan --use-all-plugins --no-keyword-scan --update .secrets.baseline
detect-secrets audit .secrets.baseline
```

`--exclude-files` is stored in the baseline, so later scans reuse it. Pass it
again only when changing the exclusion policy; a new value replaces the old
list. `--update` appends the baseline's own path to the exclusion regex; that
is expected and does not change which project files are scanned.

Verify a change before committing:

```bash
detect-secrets-hook --baseline .secrets.baseline --use-all-plugins \
  --no-keyword-scan --fail-on-unaudited <paths>
```

## Rules

- Never add a real secret to `results`. Remove the secret, rotate it, and then
  rescan. A baseline entry is a suppression, not remediation.
- Keep `plugins_used`, `exclude`, and `version` identical between the repository
  baseline and the starter. Findings may differ; policy must not.
- When the tool version changes, update the hook `rev` and the baseline
  `version` together.
- Keep the gitleaks hook. The two scanners have different engines and failure
  modes.
- Copy the baseline only when the project adopts IBM detect-secrets. Do not
  enable a scanner the project will not maintain.
