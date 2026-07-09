# Roadmap

Last reviewed: 2026-07-09

Tags: #repo/roadmap #aetheris/browser-extension #aetheris/release

This roadmap separates confirmed repository state from planning recommendations.

## Confirmed Current State

- Documentation and project-memory baseline exists.
- Obsidian and future-agent indexing docs now exist.
- No application scaffold exists.
- No package manifest exists.
- No source, tests, CI, build, package, or release workflow exists.

## Near-Term Documentation Work

- Keep docs aligned with repo truth after each meaningful change.
- Add reports to [../reports/INDEX.md](../reports/INDEX.md).
- Add handoffs to [../handoffs/INDEX.md](../handoffs/INDEX.md) when follow-up work is delegated.
- Keep [agent-index.json](agent-index.json) synchronized with human-readable docs.

## Future Implementation Milestones

These are planning milestones, not implemented features:

1. Source scaffold: WXT, TypeScript, npm, package scripts, and lockfile.
2. Extension baseline: content script for `https://chatgpt.com/*`, popup, options page, minimal background coordinator.
3. Local settings: settings schema, defaults, storage, migrations, reset behavior.
4. Visual system: tokenized theme, density, typography, focus mode, wide mode.
5. Local snippets: generic examples, local CRUD, import/export JSON.
6. Copy helpers: visible, user-initiated copy actions only.
7. Tests and CI: lint, typecheck, unit tests, DOM fixture tests, build checks.
8. Local release readiness: install docs, smoke checklist, source/rebuild package guidance.

## Non-Goals

- cloud sync
- telemetry or analytics
- remote code
- automatic message sending
- session or account manipulation
- hidden conversation indexing
- browser-store submission as a v0.0.1 requirement

