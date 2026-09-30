# Connection Map

Last reviewed: 2026-09-30

Tags: #repo/connection-map #agent/orientation #obsidian/graph

This file explains how documentation, future source/tests, work-management metadata, reports, handoffs, and machine-readable orientation connect.

## Current Connections

- [../README.md](../README.md) is the public entry point.
- [../00_Index.md](../00_Index.md) is the project-memory entry point.
- [INDEX.md](INDEX.md) is the canonical docs hub.
- [current-state.md](current-state.md) records implemented-versus-planned truth.
- [decisions.md](decisions.md) records accepted recommendations and unresolved owner decisions.
- [commands.md](commands.md) records that no application commands exist.
- [testing.md](testing.md) records the current verification model.
- [SECURITY.md](SECURITY.md) routes security reporting; [security-model.md](security-model.md) records the planned product boundary.
- [../CONTRIBUTING.md](../CONTRIBUTING.md) defines contributor workflow.
- [../SUPPORT.md](../SUPPORT.md) routes Issues, Discussions, and security matters.
- [../CHANGELOG.md](../CHANGELOG.md) records notable accepted change history.
- `.github/ISSUE_TEMPLATE/` structures new work intake without replacing repository Issues as the ledger.
- `.github/pull_request_template.md` structures scope, verification, documentation, and security/privacy evidence.
- [agent-index.json](agent-index.json) mirrors durable orientation facts for tools/agents.
- [../reports/INDEX.md](../reports/INDEX.md) lists durable evidence.
- [../handoffs/INDEX.md](../handoffs/INDEX.md) lists real delegated/blocked follow-up work.

## Future Source-To-Docs Links

When source exists, add concrete links such as:

- `entrypoints/*` → [ARCHITECTURE.md](ARCHITECTURE.md), [security-model.md](security-model.md), [SOURCE-MAP.md](SOURCE-MAP.md)
- `src/storage/*` → [SECURITY.md](SECURITY.md), [testing.md](testing.md)
- `src/dom/*` → [ARCHITECTURE.md](ARCHITECTURE.md), DOM fixture tests, [ROADMAP.md](ROADMAP.md)
- `tests/*` → [testing.md](testing.md), [SOURCE-MAP.md](SOURCE-MAP.md)
- `.github/workflows/*` → [DEPLOYMENT.md](DEPLOYMENT.md), [commands.md](commands.md), [testing.md](testing.md)

## Machine-Readable Index

[agent-index.json](agent-index.json) must stay aligned with entry points, source/test areas, commands, safety rules, sensitive paths, work-management surfaces, and known risks.
