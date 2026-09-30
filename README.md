# Aetheris UI

Tags: #repo/index #aetheris/browser-extension #aetheris/chatgpt-ui #aetheris/local-only

Aetheris UI is a public planning and documentation repository for a future local-only browser extension that enhances the ChatGPT web UI at `https://chatgpt.com/*`.

## Status

The repository is not a runnable extension yet. The current branch contains documentation, research, reports, work-management metadata, and agent orientation only.

Implemented repository capabilities:

- canonical documentation and project-memory indexes
- architecture, development, testing, deployment, security, and roadmap planning
- GitHub Issues as the persistent work ledger
- contribution, support, changelog, Issue-form, and pull-request workflow metadata
- local-only Obsidian guidance with `.obsidian/` excluded from version control

Not implemented yet:

- package or dependency manifest
- extension manifest or source scaffold
- browser-extension runtime behavior
- automated tests or CI
- build, package, deployment, or release automation
- versioned software releases

Planning references to WXT, TypeScript, npm, Node 24 LTS, Manifest V3, browser permissions, or release artifacts are recommendations until source/configuration files establish them.

## Intended Audience

This repository is for the project owner, maintainers, contributors, and automated agents preparing or reviewing Aetheris UI. Users cannot install Aetheris UI from this repository yet because no runnable extension exists.

## Product Boundaries

Aetheris UI is intended to remain local-only and least-privilege. Do not add telemetry, analytics, cloud sync, remote code, hidden data export, automatic message sending, account/session/authentication manipulation, or broad host permissions without an explicit documented product decision.

Do not commit real personal prompts, private workflow notes, credentials, keys, tokens, browser-profile data, or other private local state.

## Documentation

- [Documentation hub](docs/INDEX.md)
- [Current state](docs/current-state.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Development](docs/DEVELOPMENT.md)
- [Testing](docs/testing.md)
- [Deployment and release](docs/DEPLOYMENT.md)
- [Security policy](docs/SECURITY.md)
- [Security model](docs/security-model.md)
- [Decisions](docs/decisions.md)
- [Roadmap](docs/ROADMAP.md)
- [Commands](docs/commands.md)
- [Agent orientation](AGENTS.md)
- [Deep research report](DOCUMENTATION/deep-research-report.md)

## Setup And Usage

There is currently no application installation, build, run, test, or package command. Do not invent one. Safe repository inspection commands are documented in [docs/commands.md](docs/commands.md).

## Contributing, Support, And Security

- See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.
- Use [SUPPORT.md](SUPPORT.md) to choose between Issues, Discussions, and security reporting.
- Read [docs/SECURITY.md](docs/SECURITY.md) before reporting security-sensitive information.
- Notable accepted changes are tracked in [CHANGELOG.md](CHANGELOG.md).

## License

No project license has been adopted. `MPL-2.0` is a research recommendation only; it is not the repository license until the owner explicitly adopts a license and a canonical license file is added.

## Deployment And Release

No deployment target or release automation exists. Merging repository changes does not deploy or publish an extension. Release and publication require separate implementation, verification, and explicit authorization.
