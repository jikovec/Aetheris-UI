# Source Map

Last reviewed: 2026-07-09

Tags: #repo/source-map #agent/orientation #aetheris/browser-extension

This file maps current and planned source areas. Current repository truth comes first.

## Current Source Areas

No application source areas exist yet.

Absent as of this review:

- `package.json`
- WXT config
- extension manifest
- `entrypoints/`
- `src/`
- `tests/`
- `.github/workflows/`
- release artifacts

## Current Documentation Areas

- `00_Index.md` - root project-memory index.
- `AGENTS.md` - agent instructions and repo safety rules.
- `README.md` - public repository entry point.
- `docs/` - current docs and future source orientation.
- `DOCUMENTATION/deep-research-report.md` - product and technical research.
- `reports/` - validation, planning, and implementation reports.
- `handoffs/` - future handoff routing.

## Planned Source Areas

When implementation begins, map source areas here:

- `entrypoints/` -> extension entrypoints and manifest-facing surfaces.
- `src/features/` -> independently enableable UI enhancement features.
- `src/dom/` -> ChatGPT DOM anchor discovery and observer utilities.
- `src/storage/` -> local settings, snippets, migrations, import, and export.
- `src/theme/` -> CSS tokens, density, typography, and visual modes.
- `src/ui/` -> popup, options, and extension-owned UI components.
- `tests/` -> unit, fixture, and DOM-contract tests.
- `public/` -> icons and static extension assets.

## Planned Test Areas

No test areas exist yet. Future test mapping should include:

- pure logic tests
- settings and migration tests
- DOM fixture tests
- selector contract tests
- build checks
- manual smoke checklist for local browser installs

## Maintenance Rule

Do not mark a planned source area as implemented until the corresponding file or directory exists in the checkout.

