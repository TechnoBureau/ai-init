# Contributing

Thank you for contributing. This guide describes how to propose a change, run
the project's checks, and get a change reviewed.

## Before you start

- Search existing issues and pull requests to avoid duplicate work.
- Open an issue for a large change so scope and approach can be agreed first.
- Report security issues through {{SECURITY_REPORTING_CHANNEL_OR_NOT_CONFIGURED}},
  not a public issue.
- By participating, you agree to the code of conduct: {{CODE_OF_CONDUCT_REFERENCE_OR_NOT_CONFIGURED}}.

## Development setup

Prerequisites: {{VERIFIED_RUNTIME_AND_VERSION}}. Copy only commands that exist
in the project's manifests, scripts, or documentation.

```bash
{{VERIFIED_CLONE_COMMAND}}
{{VERIFIED_INSTALL_COMMAND}}
{{VERIFIED_LOCAL_DEV_COMMAND}}
```

Configuration and environment variables are documented in
{{LINK_TO_USAGE_OR_NOT_CONFIGURED}}. Do not commit secrets, credentials, or
personal data; reference the secret store instead.

## Validate before opening a pull request

Run the project's exact configured checks:

```bash
{{VERIFIED_TEST_COMMAND_OR_NOT_CONFIGURED}}
{{VERIFIED_LINT_COMMAND_OR_NOT_CONFIGURED}}
{{VERIFIED_BUILD_COMMAND_OR_NOT_CONFIGURED}}
```

If a command is not configured, say so rather than inventing one. Report the
command, environment, and result when a check fails.

## Coding standards

- Follow the repository's configured formatters, linters, and type checks.
- Document conventions and language guidance in {{LINK_TO_STYLE_OR_NOT_CONFIGURED}}.
- Keep changes focused; avoid unrelated reformatting.
- Add or update tests for behavior changes.
- Do not weaken validation, authorization, or error handling to make a check
  pass.
- Treat public APIs, CLIs, events, and configuration keys as contracts. A
  breaking change needs migration guidance and a deprecation path.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(scope): add the capability
fix(scope): correct the behavior
docs(scope): update the guidance
chore(scope): maintain tooling
```

Keep each commit focused and explain the reason for the change in the body.

## Pull request process

1. Branch from the default branch using a descriptive name.
2. Make the change and run the validation commands above.
3. Open a pull request describing the problem, the change, and the evidence.
4. Link related issues and requirement or decision IDs where they exist.
5. Address review comments and keep the branch current.
6. A maintainer merges when required checks and reviews pass.

Pull requests are reviewed for correctness, evidence, safety, and
maintainability, not only for style.

## Review expectations

- Every factual claim should be traceable to code, configuration, tests, or a
  confirmed decision.
- Missing evidence is marked `Not documented` rather than guessed.
- Security, privacy, and destructive-action impact are stated.
- Documentation is updated when behavior or interfaces change.

## Reporting defects

Include the version or commit, environment, exact steps, expected and actual
behavior, and any relevant logs with secrets removed. Do not paste credentials
or personal data.

## License

By contributing, you agree that your contribution is licensed under the
project's {{CONFIRMED_LICENSE_OR_NOT_DOCUMENTED}}.
