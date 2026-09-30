# Contributing

Aetheris UI is currently documentation/planning-only. Contributions must reflect the repository state that actually exists rather than assuming the future extension scaffold has already been implemented.

## Before Starting

1. Read `AGENTS.md`, `docs/INDEX.md`, and `docs/current-state.md`.
2. Check the existing GitHub Issues and Discussions before creating a duplicate work item.
3. Inspect the current `main` branch and, for local work, run `git status --short --branch` before editing.
4. Preserve unrelated dirty or untracked work.

Use Issues for actionable repository work and bugs. Use Discussions for design questions or topics that are not yet executable work. Follow `SUPPORT.md` for routing.

## Current Development State

No application package, source scaffold, test runner, CI workflow, build command, or release command exists yet. The only repository-declared commands are safe inspection/validation commands documented in `docs/commands.md`.

Do not add instructions such as `npm ci`, `npm run build`, or `npm test` as required project commands until a committed manifest actually declares them.

## Change Workflow

For material changes:

1. Use the existing Issue/work object when one already covers the work.
2. Create a focused branch from the current `main` branch.
3. Make the smallest coherent change that satisfies the work object.
4. Update affected canonical documentation and indexes in the same change.
5. Run proportional validation.
6. Open a pull request that links the work object and records exact verification results.

Do not merge, deploy, publish, tag, or release unless separately authorized.

## Documentation Responsibilities

When repository truth changes, update the matching documentation:

- source/manifests/configuration: `docs/current-state.md`, `docs/SOURCE-MAP.md`, `docs/CONNECTIONS.md`
- commands/dependencies: `docs/commands.md`, `docs/DEVELOPMENT.md`, `docs/agent-index.json`
- tests/CI: `docs/testing.md`, `docs/SOURCE-MAP.md`, `docs/agent-index.json`
- security/permissions/storage/data handling: `docs/SECURITY.md`, `docs/security-model.md`
- release/deployment behavior: `docs/DEPLOYMENT.md`, `CHANGELOG.md`
- meaningful reports: `reports/INDEX.md`

Historical reports should remain historically accurate. Add supersession notes instead of rewriting history.

## Validation

For the current documentation-only baseline, run:

~~~text
git status --short --branch
git diff --check
git ls-files
~~~

Also validate relative Markdown links and parse any edited JSON/YAML. If a check is unavailable, report it as unavailable rather than passing.

Application build/test checks are not currently applicable because no runnable application exists.

## Security And Privacy

Never include real personal prompts, private workflow notes, browser-profile data, credentials, keys, tokens, secrets, private URLs, or sensitive vulnerability details in a public Issue or pull request.

Read `docs/SECURITY.md` before reporting security-sensitive information. Preserve the local-only, no-telemetry, no-cloud-sync, no-remote-code, no-auto-send product boundaries unless the owner explicitly changes them.

## Licensing

The repository does not currently contain an adopted project license. Do not add license headers, relicense existing material, or copy third-party code/assets on the assumption that the research recommendation of MPL-2.0 has already been accepted.
