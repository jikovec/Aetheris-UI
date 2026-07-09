# Development

Last reviewed: 2026-07-09

Tags: #repo/development #aetheris/wxt #aetheris/local-only

This repository does not currently contain a runnable application scaffold. Development commands are not declared yet.

## Current State

There is no:

- `package.json`
- lockfile
- WXT config
- extension manifest
- source directory
- test directory
- CI workflow

Because no package manifest exists, do not run `npm ci`, `npm run dev`, `npm run build`, `npm test`, lint, typecheck, or package commands for this repo.

## Safe Inspection

Use the read-only commands in [commands.md](commands.md) to inspect the current repository.

## Planned Development Direction

The current research recommends:

- Windows-first setup
- Arch Linux as the second documented environment
- Node 24 LTS, re-verified at implementation time
- npm and `package-lock.json`
- WXT and TypeScript
- Vitest for unit and DOM-fixture tests
- GitHub Actions after source and package scripts exist

These are recommendations only until source and manifests are added.

## Future Scaffold Requirements

The first source implementation pass should:

- add a package manifest and lockfile
- document exact package scripts in [commands.md](commands.md)
- update [current-state.md](current-state.md)
- update [testing.md](testing.md)
- update [SOURCE-MAP.md](SOURCE-MAP.md)
- update [CONNECTIONS.md](CONNECTIONS.md)
- update [agent-index.json](agent-index.json)

## Non-Goals

Do not add generated dependency folders, browser profile data, private prompt libraries, secrets, build outputs, or release artifacts to the repository.

