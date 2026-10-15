# Obsidian Guide

Last reviewed: 2026-10-15

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

<!-- local-graph-scope-2026-07-21:start -->
## Default Local Graph View

For a knowledge-only Global Graph view, use this filter in the ignored local `.obsidian/graph.json`:

```text
path:docs OR path:DOCUMENTATION OR path:reports OR path:handoffs OR file:00_Index OR file:AGENTS
```

| Control | Suggested setting | Purpose |
| --- | --- | --- |
| Attachments | off | Removes source, media, generated, dependency, and evidence-file noise. |
| Tags | off | Keeps normal Markdown links as the visible relationship model. |
| Existing files only | on | Hides unresolved targets until a real note exists. |
| Orphans | on | Keeps genuine degree-zero Markdown notes visible for maintenance. |

The filter keeps maintained documentation, evidence, handoffs, and stable root hubs visible while source, dependencies, generated output, and attachments stay outside the normal knowledge view.

A large outer ring of isolated colored nodes usually means attachments were enabled with an empty or overly broad filter; it does not by itself prove missing documentation backlinks. Keep Orphans enabled, classify each remaining Markdown orphan, and connect it through the narrowest real owner, archive, report, handoff, release, or specification index. Do not create decorative backlinks only to improve the metric.

The graph JSON is local UI state, not repository truth. If an old force layout remains visible after this setting changes, close and reopen Global Graph once so Obsidian reloads the filter. Re-run the Markdown link/component audit after adding or moving documentation.
<!-- local-graph-scope-2026-07-21:end -->
