# Agent Instructions

## Read Order

Before material work, read:

1. `00_Index.md`
2. `docs/INDEX.md`
3. `docs/current-state.md`
4. `docs/decisions.md`
5. `docs/commands.md`
6. `docs/testing.md`
7. `docs/security-model.md`
8. `CONTRIBUTING.md`
9. `docs/AGENT-INDEX.md`
10. `docs/agent-index.json`
11. `DOCUMENTATION/deep-research-report.md` when planning or scaffolding product work

## Repository Authority

- Treat current repository source, manifests, configuration, tests, workflows, and current documentation as higher-priority truth than planning notes or prior chat memory.
- The canonical repository is `jikovec/Aetheris-UI`; the default branch is `main`.
- A local working tree may contain uncommitted or untracked user work. Inspect `git status --short --branch` before local edits and preserve unrelated changes.
- Search for an existing canonical document before adding a new one. Prefer improving the existing file over creating a duplicate.
- Do not rewrite historical reports merely because current terminology changed; add a supersession note when needed.

## Current Baseline

As of the 2026-09-30 repository baseline, no package manifest, extension manifest, application source, automated test suite, CI workflow, build output, or release artifact is present.

- Do not invent runnable application commands.
- Do not claim a planned feature, dependency, browser permission, deployment, or release is implemented without source evidence.
- Documentation-only tasks must not silently become product implementation tasks.

## Work And Delivery Workflow

- Reuse the existing GitHub Issue or other persistent work object when one already covers the task; do not create duplicates.
- For material repository changes, use a focused branch and pull request when authorized.
- Keep Issue/PR state distinct from repository source truth.
- Do not bypass branch protections or repository rules if they are introduced later.
- Do not merge, release, publish, or deploy unless the current request explicitly authorizes that effect.
- A successful merge is not evidence of deployment. This repository currently has no deployment automation.

## Product Guardrails

Aetheris UI is planned as a local-only browser extension for `https://chatgpt.com/*`.

Preserve these boundaries unless the owner explicitly changes product direction:

- no analytics or telemetry
- no cloud sync
- no remote code
- no hidden data export
- no automatic message sending
- no account, session, authentication, or cookie manipulation
- no broad host permissions without a specific documented feature need
- no real personal prompts, private workflow notes, keys, tokens, credentials, private URLs, or browser-profile data in the public repository

## Documentation And Indexing

- Keep GitHub-compatible relative Markdown links as the canonical navigation format.
- Keep `.obsidian/` and private Obsidian state untracked.
- Keep `docs/agent-index.json` aligned with human-readable orientation docs.
- When adding source later, update `docs/SOURCE-MAP.md`, `docs/CONNECTIONS.md`, `docs/current-state.md`, `docs/commands.md`, and `docs/testing.md` in the same change.
- When security, permissions, storage, or data behavior changes, update `docs/SECURITY.md` and `docs/security-model.md`.
- Add meaningful durable reports to `reports/INDEX.md`.
- Use `handoffs/INDEX.md` only for real delegated or blocked follow-up work.

## Validation

For documentation/governance changes, verify at least:

- `git status --short --branch`
- `git diff --check`
- relative Markdown links and referenced files
- JSON/YAML syntax for edited structured files
- that documentation claims match current repository state

Do not report an unavailable or unrun check as passing.
