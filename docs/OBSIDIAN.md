# Obsidian Guide

Last reviewed: 2026-07-09

Tags: #obsidian/local #obsidian/graph #repo/index #agent/orientation

Aetheris UI can be opened as a local Obsidian vault for documentation navigation. Obsidian integration is local-first and plaintext by default.

## Local Vault Rules

- Keep `.obsidian/` ignored.
- Do not track workspace state, Sync settings, plugin state, private notes, or browser profile data.
- Do not add Obsidian cloud, sharing, encryption, account coupling, or company integrations.
- Keep repository docs readable on GitHub without Obsidian.

## Link Convention

Use normal relative Markdown links for durable documentation:

- good: `[Architecture](ARCHITECTURE.md)`
- good: `[Research](../DOCUMENTATION/deep-research-report.md)`
- avoid as canonical links: `[[Architecture]]`

Wiki links may be useful in private local notes, but they should not be the main repo navigation format.

## Graph Hubs

Use these files as graph hubs:

- [../00_Index.md](../00_Index.md)
- [INDEX.md](INDEX.md)
- [AGENT-INDEX.md](AGENT-INDEX.md)
- [SOURCE-MAP.md](SOURCE-MAP.md)
- [CONNECTIONS.md](CONNECTIONS.md)
- [ROADMAP.md](ROADMAP.md)
- [../reports/INDEX.md](../reports/INDEX.md)
- [../handoffs/INDEX.md](../handoffs/INDEX.md)

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

Repo tags:

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

Do not use tags that imply unsupported behavior or false guarantees:

- #cloud-sync
- #telemetry
- #auto-send
- #official-chatgpt
- #account-automation
- #production-ready

## Tagging Rules

- Tag hub docs, indexes, durable reports, and handoffs.
- Do not tag every paragraph or every ordinary doc page.
- Use tags to support graph navigation, not as a replacement for links.
- Keep GitHub Markdown compatibility as the primary format.

