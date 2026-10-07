# Decisions

Last validated: 2026-10-07

Tags: #repo/decision #aetheris/browser-extension

## Confirmed By Repo Contents

- This checkout contains planning documentation and the agent toolkit; no application implementation.
- No app source, manifests, tests, CI workflows, or release artifacts are present.
- No package manager is confirmed by a manifest.
- No license is confirmed by a `LICENSE` file.
- Obsidian workspace state must remain untracked through `.gitignore`.
- `docs/agent-index.json` is the canonical machine-readable future-agent index.
- Existing lowercase docs such as `docs/testing.md` and `docs/decisions.md` remain canonical to avoid unnecessary case-only path churn on Windows.

## Planning Decisions From Research

These are accepted planning inputs for future work unless the user changes direction. They are not yet implemented.

| Topic | Current planning decision | Status |
| --- | --- | --- |
| Product type | Browser extension enhancing ChatGPT UI locally | Planned |
| Target site | `https://chatgpt.com/*` only | Planned |
| Extension framework | WXT | Recommended |
| Language | TypeScript | Recommended |
| Package manager | npm | Recommended |
| Runtime baseline | Node 24 LTS | Recommended, re-verify before implementation |
| Browser model | Manifest V3 for Chrome/Chromium and Firefox | Recommended |
| UI surfaces | Content script, popup, options page, minimal background logic | Planned |
| Data model | Local settings/snippets, generic examples only | Planned |
| License | MPL-2.0 | Recommended, not adopted until `LICENSE` exists |
| Obsidian integration | Local-first Markdown docs, ignored `.obsidian/` | Implemented for docs only |
| Agent index | `docs/agent-index.json` plus `docs/AGENT-INDEX.md` | Implemented for docs only |

## Hard Product Non-Goals

- No remote code.
- No telemetry or analytics.
- No cloud sync.
- No hidden data export.
- No automatic message sending.
- No session, auth, or account manipulation.
- No broad host permissions without a documented feature requirement.
- No real personal prompts, credentials, private workflow notes, or secrets in the repo.

## Decision Maintenance

When implementation files are added, update this file if source truth differs from these planning decisions. Do not preserve recommendations that have been superseded by manifests, configs, or code.

## Agent toolkit adoption — 2026-10-07

The owner requested and adopted the portable toolkit and standing ordinary repository
delivery policy in [authorization](../.agent/contracts/authorization.md). This supersedes
older agent-setup statements that granted no standing commit/push/merge authority, while
preserving narrower task limits and separate release/deploy/publication requirements.
The adoption is part of the owner-requested bootstrap, not a self-issued agent grant.

Canonical workflow reasoning lives in `skills/`; policy lives in `.agent/contracts/`.
Provider adapters remain thin. The pre-existing project-workflow vocabulary is retained
as a router; `docs/agent-workflow.md` becomes a compatibility pointer. Product design,
privacy boundaries and the lack of an app scaffold remain unchanged.

No verified registry identity or project memory binding was found during reconciliation.
Use the stable repository-qualified project ID and leave Mind-Seed disabled. A later
verified registry binding must reconcile identity instead of silently creating a duplicate.
See the [bootstrap report](../reports/agent-toolkit-bootstrap-2026-10-07.md) for dated evidence.
