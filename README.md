# Aetheris UI

Tags: #repo/index #aetheris/browser-extension #aetheris/chatgpt-ui #aetheris/local-only

Aetheris UI is currently a planning and documentation repository for a future local-only browser extension that enhances the ChatGPT web UI at `https://chatgpt.com/*`.

No runnable extension is implemented in this checkout yet. The repository currently contains project memory, documentation, research, reports, and future-agent orientation files.

## Current Status

- No `package.json` is present.
- No extension manifest is present.
- No `entrypoints/`, `src/`, or `tests/` directories are present.
- No application build, test, lint, package, CI, deploy, or release command is declared.
- Existing WXT, TypeScript, npm, Node 24 LTS, and MV3 references are planning recommendations until source files are created.

## Documentation

- [Project memory index](00_Index.md)
- [Documentation hub](docs/INDEX.md)
- [Current state](docs/current-state.md)
- [Architecture plan](docs/ARCHITECTURE.md)
- [Development workflow](docs/DEVELOPMENT.md)
- [Testing status](docs/testing.md)
- [Security and privacy model](docs/security-model.md)
- [Obsidian guide](docs/OBSIDIAN.md)
- [Future-agent index](docs/AGENT-INDEX.md)
- [Machine-readable agent index](docs/agent-index.json)
- [Deep research report](DOCUMENTATION/deep-research-report.md)

## Privacy And Security Boundaries

Aetheris UI is planned as a local-only extension. Preserve these boundaries unless the product direction is explicitly changed:

- no analytics or telemetry
- no cloud sync
- no remote code
- no hidden data export
- no automatic ChatGPT message sending
- no account, authentication, or session manipulation
- no broad host permissions without a documented feature need
- no real personal prompts, credentials, private workflow notes, keys, or tokens in the public repository

## Setup

There is currently no application setup command. Do not run `npm`, build, test, or browser-extension commands until a package manifest and source scaffold exist.

Safe repository inspection commands are documented in [docs/commands.md](docs/commands.md).


## Repository agent workflows

Use the [portable toolkit](.agent/README.md) for build, investigate, research, verify,
review, fix, release, deploy, publish, push and pull workflows. Codex and Claude load
thin adapters to the same canonical skills. [Toolkit checks](docs/commands.md) validate
the agent infrastructure; the browser extension remains unimplemented.
