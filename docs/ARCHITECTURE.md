# Architecture

Last reviewed: 2026-07-09

Tags: #repo/architecture #aetheris/browser-extension #aetheris/wxt #aetheris/mv3

This document records the planned architecture for Aetheris UI. It is not proof that source code exists.

## Current Implementation State

No application architecture is implemented yet. The checkout currently has no `package.json`, extension manifest, WXT config, `entrypoints/`, `src/`, `tests/`, or CI workflow.

## Planned Product Shape

Aetheris UI is planned as a local-only browser extension for `https://chatgpt.com/*`.

Recommended planning direction from [deep-research-report.md](../DOCUMENTATION/deep-research-report.md):

- WXT-based WebExtension project
- TypeScript source
- npm package management
- Manifest V3 for Chrome/Chromium and Firefox
- static content-script matching for `https://chatgpt.com/*`
- small popup for quick toggles
- full options page for detailed settings
- minimal background coordinator
- local settings and snippets stored in extension storage
- CSS custom properties and design tokens for the visual system

## Planned Source Areas

When implementation begins, the source layout should stay modular and easy to disable per feature:

- `entrypoints/` for content script, popup, options page, and minimal background entrypoints.
- `src/features/` for independently enableable feature modules.
- `src/dom/` for selector contracts, anchor discovery, route detection, and observer utilities.
- `src/storage/` for schema, migrations, settings, snippets, import, and export.
- `src/ui/` for extension-owned UI components.
- `src/theme/` for tokens, surfaces, typography, density, and mode definitions.
- `tests/` for unit tests, DOM fixtures, and selector/contract checks.
- `public/` for icons and static extension assets.

## Integration Boundaries

- Treat ChatGPT as an uncontrolled third-party single-page application.
- Prefer progressive enhancement over deep coupling.
- Avoid reliance on undocumented React internals, unstable class chains, or hidden page state.
- Keep feature modules individually disableable when ChatGPT DOM changes.
- Keep extension-owned UI isolated from page UI where practical.

## Privacy And Security Architecture

The architecture must preserve the project guardrails documented in [security-model.md](security-model.md):

- no remote code
- no telemetry or analytics
- no cloud sync
- no automatic message sending
- no account or session manipulation
- no broad host permissions without a specific documented need
- no committed private prompts, credentials, keys, or tokens

## Source Of Truth

This file is planning guidance until source files exist. Once implementation begins, manifests, configs, source, tests, and CI files outrank this document.

