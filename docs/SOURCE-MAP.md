# Source Map

Last reviewed: 2026-09-30

Tags: #repo/source-map #agent/orientation #aetheris/browser-extension

This file maps current and planned repository areas. Current repository truth comes first.

## Current Application Source Areas

No application source areas exist yet.

Absent at this baseline:

- `package.json` and lockfile
- WXT configuration
- extension manifest
- `entrypoints/`
- `src/`
- `tests/`
- `.github/workflows/`
- build/package/release artifacts

## Current Documentation And Governance Areas

- `README.md` - public repository entry point.
- `00_Index.md` - project-memory entry point.
- `AGENTS.md` - agent authority/workflow/safety rules.
- `CONTRIBUTING.md` - contributor workflow.
- `SUPPORT.md` - support and issue-routing policy.
- `CHANGELOG.md` - notable accepted changes.
- `docs/` - primary documentation root.
- `DOCUMENTATION/deep-research-report.md` - research/planning input.
- `.github/ISSUE_TEMPLATE/` - GitHub work-intake configuration.
- `.github/pull_request_template.md` - pull-request evidence/review template.
- `reports/` - durable validation/planning/implementation evidence.
- `handoffs/` - real delegated/blocked follow-up routing.

## Planned Source Areas

When implementation begins, map only source areas that actually exist:

- `entrypoints/` - extension entrypoints and manifest-facing surfaces
- `src/features/` - independently enableable feature modules
- `src/dom/` - ChatGPT DOM anchor/observer contracts
- `src/storage/` - local settings/snippets/migrations/import/export
- `src/theme/` - design tokens and visual modes
- `src/ui/` - extension-owned UI
- `tests/` - unit/fixture/DOM-contract tests
- `public/` - extension static assets

## Maintenance Rule

Do not mark a planned source/test/workflow area as implemented until the corresponding repository path exists.
