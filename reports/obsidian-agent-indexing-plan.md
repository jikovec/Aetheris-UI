# Obsidian And Agent Indexing Planning Report

Date: 2026-07-09

Tags: #agent/report #repo/index #obsidian/graph #aetheris/browser-extension

## Repository Summary

Aetheris UI is currently a documentation and planning repository for a future local-only browser extension targeting `https://chatgpt.com/*`.

Current repo truth:

- documentation and project-memory files exist
- no runnable app scaffold exists
- no package manifest exists
- no extension manifest exists
- no source, tests, CI, build, deploy, or release artifacts exist

The deep research report recommends WXT, TypeScript, npm, Node 24 LTS, Manifest V3, local extension storage, a narrow ChatGPT host scope, and local-only privacy boundaries. Those remain planning recommendations until source files exist.

## Source-Of-Truth Hierarchy

Use this order when facts conflict:

1. source code, manifests, lockfiles, configs, tests, and CI files when present
2. current root docs, `docs/`, and machine-readable indexes
3. `DOCUMENTATION/deep-research-report.md`
4. reports and handoffs
5. inferred notes or older memory summaries

## Current Documentation Map

Existing docs before this implementation pass:

- `00_Index.md`
- `AGENTS.md`
- `docs/current-state.md`
- `docs/decisions.md`
- `docs/commands.md`
- `docs/testing.md`
- `docs/security-model.md`
- `docs/releases/2026-07-07-local-documentation-release.md`
- `DOCUMENTATION/deep-research-report.md`
- `reports/project-memory-validation-2026-07-07.md`
- `reports/next-version-local-changes-report.md`

Missing or weak areas:

- public `README.md`
- canonical `docs/INDEX.md`
- architecture/development/deployment/roadmap hubs
- Obsidian guide and tag taxonomy
- human-readable source and connection maps
- machine-readable future-agent index
- report and handoff indexes
- `.gitignore` protection for `.obsidian/`

## Obsidian Readiness

The repo can be opened as a local Obsidian vault for documentation navigation. `.obsidian/` must remain ignored because it can contain local workspace state, Sync settings, plugin state, and other private machine state.

Recommended conventions:

- use normal relative Markdown links as canonical links
- use tags only on hubs, indexes, reports, and handoffs
- keep GitHub Markdown compatibility
- avoid private local notes inside the public repo
- do not add Obsidian cloud/sync/account/encryption setup

## Tag Taxonomy

Global tags:

- #repo/index
- #repo/architecture
- #repo/development
- #repo/testing
- #repo/security
- #repo/deployment
- #repo/roadmap
- #repo/decision
- #repo/source-map
- #repo/connection-map
- #agent/orientation
- #agent/handoff
- #agent/report
- #obsidian/local
- #obsidian/graph

Repo-specific tags:

- #aetheris/browser-extension
- #aetheris/chatgpt-ui
- #aetheris/wxt
- #aetheris/mv3
- #aetheris/local-only
- #aetheris/privacy
- #aetheris/theme
- #aetheris/snippets
- #aetheris/dom-contracts
- #aetheris/release

Do not use tags implying unsupported behavior:

- #cloud-sync
- #telemetry
- #auto-send
- #official-chatgpt
- #account-automation
- #production-ready

## Proposed Complete System

Implement:

- `README.md`
- `.gitignore`
- updated `00_Index.md`
- updated `AGENTS.md`
- `docs/INDEX.md`
- `docs/ARCHITECTURE.md`
- `docs/DEVELOPMENT.md`
- `docs/SECURITY.md`
- `docs/DEPLOYMENT.md`
- `docs/OBSIDIAN.md`
- `docs/AGENT-INDEX.md`
- `docs/SOURCE-MAP.md`
- `docs/CONNECTIONS.md`
- `docs/ROADMAP.md`
- updated lowercase `docs/decisions.md`, `docs/testing.md`, and `docs/security-model.md`
- `docs/agent-index.json`
- `reports/INDEX.md`
- `handoffs/INDEX.md`
- implementation report

Omit `.agents/index.json` because the repo has no `.agents/` convention and `docs/agent-index.json` is sufficient.

Use the existing lowercase docs instead of case-only replacements for `docs/decisions.md` and `docs/testing.md` to avoid Windows path ambiguity and duplicate navigation.

## Verification Plan

Safe verification:

- `git status --short --branch`
- `git ls-files`
- PowerShell file inventory
- `Get-Content -Raw docs\agent-index.json | ConvertFrom-Json`
- `git diff --check`

Do not run package, build, test, lint, or dev-server commands until a package manifest exists.

## Risks And Non-Goals

Do not change runtime behavior, source code, build logic, deployment, release state, browser profile data, cloud/account integrations, Obsidian Sync setup, encryption setup, or generated dependency folders.

Do not invent project history, implemented architecture, commands, tests, CI, browser permissions, release artifacts, or security guarantees.

## Ready-To-Run Implementation Prompt

Inside this repository, re-check current repo state before editing. Implement the approved complete documentation, Obsidian, repo-indexing, and future-agent orientation system from this report. Prefer complete docs/indexing when valid, but omit or merge artifacts only with explicit reasoning. Preserve runtime behavior. Add `.gitignore` protection for `.obsidian/`. Add or update human-readable docs and `docs/agent-index.json`. Keep Obsidian local-first and plaintext. Avoid secrets, private local state, and private prompts. Run safe docs, JSON, and whitespace verification. Produce a final implementation report. Do not commit, push, deploy, publish, tag, release, or perform cloud/account/encryption setup.

