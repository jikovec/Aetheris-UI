# Codex Project Instructions

## Read Order

For future Codex work in this repository, read these files first:

1. `00_Index.md`
2. `docs/INDEX.md`
3. `docs/current-state.md`
4. `docs/decisions.md`
5. `docs/commands.md`
6. `docs/testing.md`
7. `docs/security-model.md`
8. `docs/AGENT-INDEX.md`
9. `docs/agent-index.json`
10. `DOCUMENTATION/deep-research-report.md` when planning or scaffolding product work

## Repository Truth Rules

- Treat current repository files, manifests, tests, and configs as higher priority than planning notes.
- As of the 2026-07-09 indexing pass, this checkout does not contain application source code, package manifests, extension manifests, tests, CI workflows, or release artifacts.
- Do not invent runnable commands. If `package.json` or another manifest is absent, say that no project commands are declared.
- Do not move, delete, or rename files unless the user explicitly asks.
- Do not edit application source code when the request is documentation-only.
- Do not touch secrets, generated dependency folders, build output folders, or browser profile data.

## Product Guardrails

Aetheris UI is currently documented as a planned local-only browser extension for `https://chatgpt.com/*`.

Preserve these guardrails unless the user changes the product direction:

- local-only behavior
- no analytics or telemetry
- no cloud sync
- no remote code
- no automatic message sending
- no account, session, or authentication manipulation
- no broad host permissions without a specific feature need
- no real personal prompts, private workflow notes, keys, tokens, or credentials in the public repository

## Documentation And Indexing Rules

- Keep documentation GitHub-compatible first: use normal relative Markdown links for durable navigation.
- Obsidian usage is local-only. Do not track `.obsidian/`, Obsidian Sync state, workspace state, private notes, plugin state, or local browser profile state.
- Keep `docs/agent-index.json` aligned with the human-readable docs whenever source, commands, reports, handoffs, or safety rules change.
- When adding source files later, update `docs/SOURCE-MAP.md`, `docs/CONNECTIONS.md`, `docs/current-state.md`, `docs/commands.md`, and `docs/testing.md` in the same change.
- When creating a meaningful report, add it to `reports/INDEX.md`.
- When leaving follow-up work for another agent, add or update `handoffs/INDEX.md`.
- Use Obsidian tags only on hub/index docs and durable reports. Avoid tag spam inside ordinary prose.

## Workflow Notes

- Use the memory docs as orientation, then verify against the repo before editing.
- Prefer focused changes that update the memory docs and reports when the repo state changes.
- Do not start a dev server unless the user explicitly asks or the task requires a running app and the repo actually contains a runnable app.
- If implementation is requested before the project is scaffolded, start by creating or validating the source scaffold and package manifests, then update the memory docs to match.
