# Future-Agent Index

Last reviewed: 2026-07-09

Tags: #agent/orientation #repo/index #aetheris/local-only

This file is the human-readable start workflow for future agents working in this repository.

## Start Workflow

1. Read [../00_Index.md](../00_Index.md).
2. Read [../AGENTS.md](../AGENTS.md).
3. Read [INDEX.md](INDEX.md).
4. Read [current-state.md](current-state.md).
5. Check `git status --short --branch`.
6. Check `git ls-files`.
7. Inspect manifests, source, tests, and CI if they now exist.
8. Treat [../DOCUMENTATION/deep-research-report.md](../DOCUMENTATION/deep-research-report.md) as planning input, not implementation proof.

## What Can Be Inferred Quickly

- The repo is currently documentation/planning-only.
- Aetheris UI is planned as a local-only ChatGPT UI browser extension.
- The recommended stack is WXT, TypeScript, npm, Node 24 LTS, and MV3, but it is not implemented.
- The privacy boundary forbids telemetry, cloud sync, remote code, automatic message sending, and account/session manipulation.
- The repo has documentation, reports, and indexes, but no runnable app scaffold.

## What Cannot Be Inferred Yet

- Exact implementation stack from source files.
- Exact package scripts.
- Exact browser permissions.
- Exact storage schema.
- Exact test runner configuration.
- Exact CI workflow.
- Exact release packaging process.

## Update Obligations

After every meaningful repo change, update the relevant docs:

- source or manifests: [SOURCE-MAP.md](SOURCE-MAP.md), [CONNECTIONS.md](CONNECTIONS.md), [current-state.md](current-state.md)
- package scripts: [commands.md](commands.md), [agent-index.json](agent-index.json)
- tests: [testing.md](testing.md), [SOURCE-MAP.md](SOURCE-MAP.md)
- security or permissions: [security-model.md](security-model.md), [SECURITY.md](SECURITY.md)
- reports: [../reports/INDEX.md](../reports/INDEX.md)
- handoffs: [../handoffs/INDEX.md](../handoffs/INDEX.md)
- roadmap or decisions: [ROADMAP.md](ROADMAP.md), [decisions.md](decisions.md)

## Safety Rules

- Preserve runtime/product behavior unless the user asks for implementation work.
- Do not invent commands when no manifest declares them.
- Do not commit, push, deploy, release, or publish unless explicitly asked.
- Do not track `.obsidian/` or private local workspace state.
- Do not add real prompts, private workflow notes, keys, tokens, credentials, private URLs, or account IDs.

