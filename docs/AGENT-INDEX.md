# Future-Agent Index

Last reviewed: 2026-09-30

Tags: #agent/orientation #repo/index #aetheris/local-only

## Start Workflow

1. Read [../AGENTS.md](../AGENTS.md).
2. Read [../00_Index.md](../00_Index.md) and [INDEX.md](INDEX.md).
3. Read [current-state.md](current-state.md), [decisions.md](decisions.md), [commands.md](commands.md), and [testing.md](testing.md).
4. Check the relevant GitHub Issue/PR state.
5. In a local checkout, run `git status --short --branch` and `git ls-files`.
6. Inspect manifests, source, tests, workflows, and configuration if they now exist.
7. Treat [../DOCUMENTATION/deep-research-report.md](../DOCUMENTATION/deep-research-report.md) as planning input, not implementation proof.

## Current Facts

- The repository is documentation/planning-only.
- Aetheris UI is planned as a local-only ChatGPT UI browser extension.
- No implementation stack or application commands are source-confirmed.
- Public contribution/support workflow and GitHub Issue/PR templates exist.
- The repository license remains unresolved.
- Privacy boundaries forbid telemetry, cloud sync, remote code, automatic message sending, account/session manipulation, and committed private workflow data.

## Update Obligations

After meaningful repository changes, update the relevant canonical docs:

- source/manifests: [SOURCE-MAP.md](SOURCE-MAP.md), [CONNECTIONS.md](CONNECTIONS.md), [current-state.md](current-state.md)
- package scripts/dependencies: [commands.md](commands.md), [DEVELOPMENT.md](DEVELOPMENT.md), [agent-index.json](agent-index.json)
- tests/CI: [testing.md](testing.md), [SOURCE-MAP.md](SOURCE-MAP.md)
- security/permissions/storage: [SECURITY.md](SECURITY.md), [security-model.md](security-model.md)
- release/deployment: [DEPLOYMENT.md](DEPLOYMENT.md), [../CHANGELOG.md](../CHANGELOG.md)
- reports: [../reports/INDEX.md](../reports/INDEX.md)
- handoffs: [../handoffs/INDEX.md](../handoffs/INDEX.md)

## Safety And Delivery Rules

- Preserve unrelated dirty/untracked user work.
- Do not invent commands, implementation state, tests, or deployment results.
- Reuse existing work objects instead of creating duplicates.
- Do not merge, deploy, publish, tag, or release without explicit authorization.
- Keep `.obsidian/`, generated output, browser-profile data, private prompts, and secrets out of the repository.
