# Connection Map

Last reviewed: 2026-10-07

Tags: #repo/connection-map #agent/orientation #obsidian/graph

This file explains how docs, source, tests, reports, handoffs, decisions, and the machine-readable index should connect.

## Current Connections

- [../README.md](../README.md) points to the main docs and current repo status.
- [../00_Index.md](../00_Index.md) is the root memory entry point.
- [INDEX.md](INDEX.md) is the docs hub.
- [current-state.md](current-state.md) records implemented-vs-planned truth.
- [decisions.md](decisions.md) records planning decisions and their status.
- [commands.md](commands.md) records application absence and actual toolkit validation commands.
- [testing.md](testing.md) separates toolkit validation from absent application tests.
- [security-model.md](security-model.md) records current and intended security boundaries.
- [agent-index.json](agent-index.json) mirrors the durable orientation facts for tools and agents.
- [../reports/INDEX.md](../reports/INDEX.md) lists reports.
- [../handoffs/INDEX.md](../handoffs/INDEX.md) lists concrete follow-up handoffs.

## Future Source-To-Docs Links

When source exists, add concrete links like:

- `entrypoints/content.*` -> [ARCHITECTURE.md](ARCHITECTURE.md), [security-model.md](security-model.md), [SOURCE-MAP.md](SOURCE-MAP.md)
- `src/storage/*` -> [SECURITY.md](SECURITY.md), [testing.md](testing.md)
- `src/dom/*` -> [ARCHITECTURE.md](ARCHITECTURE.md), DOM fixture tests, [ROADMAP.md](ROADMAP.md)
- `tests/*` -> [testing.md](testing.md), [SOURCE-MAP.md](SOURCE-MAP.md)
- `.github/workflows/*` -> [DEPLOYMENT.md](DEPLOYMENT.md), [commands.md](commands.md)

## Reports And Handoffs

- Reports should link back to docs, source areas, or decisions they validate.
- Handoffs should link to the exact unresolved docs, source areas, or reports.
- Roadmap entries should link to the report or decision that justifies them.

## Machine-Readable Index

[agent-index.json](agent-index.json) should stay aligned with:

- docs entry points
- source areas
- test areas
- commands
- safety rules
- sensitive path rules
- Obsidian conventions
- known risks


## Agent toolkit connections

- [Toolkit index](../.agent/README.md) connects stable metadata, contracts and workflows.
- [Canonical skills](../skills/) own reasoning; [Codex adapters](../.agents/skills/) and
  [Claude adapters](../.claude/skills/) point there. `.codex/skills/` provides compatibility.
- [Project workflow](../skills/project/aetheris-ui-workflow/SKILL.md) routes existing requests.
- [Shared documentation procedure](../.agent/workflows/documentation.md) maintains the indexes.
- [Validator](../.agent/hooks/toolkit/validate.py) checks toolkit structure;
  [routing cases](../.agent/evals/skill-routing.md) exercise semantics.
- [Bootstrap report](../reports/agent-toolkit-bootstrap-2026-10-07.md) records reconciliation.

These are repository tools and documentation; application source/test areas remain planned.
