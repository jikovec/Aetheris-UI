# Decisions

Last validated: 2026-09-30

Tags: #repo/decision #aetheris/browser-extension

## Confirmed By Repository State

- The repository is currently documentation/planning-only; no runnable application is present.
- No package manager, runtime, framework, or browser permission set is confirmed by implementation files.
- No project license is adopted because no canonical license file or equivalent owner decision exists.
- Obsidian workspace state remains local-only and untracked.
- `docs/agent-index.json` is the canonical machine-readable agent index.
- Existing lowercase docs such as `docs/testing.md` and `docs/decisions.md` remain canonical to avoid unnecessary case-only path churn.
- GitHub Issues are the persistent public work ledger; repository source/docs remain technical truth.
- `CONTRIBUTING.md`, `SUPPORT.md`, `CHANGELOG.md`, and `.github/` templates form the current public repository-governance surface.

## Planning Decisions From Research

These are accepted planning inputs, not implementation claims:

| Topic | Current planning decision | Status |
| --- | --- | --- |
| Product type | Browser extension enhancing ChatGPT UI locally | Planned |
| Target site | `https://chatgpt.com/*` only | Planned |
| Extension framework | WXT | Recommended |
| Language | TypeScript | Recommended |
| Package manager | npm | Recommended |
| Runtime baseline | Node 24 LTS | Recommended; re-verify before implementation |
| Browser model | Manifest V3 for Chrome/Chromium and Firefox | Recommended |
| UI surfaces | Content script, popup, options page, minimal background logic | Planned |
| Data model | Local settings/snippets, generic examples only | Planned |
| License | MPL-2.0 | Recommended; not adopted |
| Obsidian integration | Local-first Markdown docs, ignored `.obsidian/` | Implemented for docs only |

## Owner Decisions Still Required

- Adopt a project license, including whether to accept the MPL-2.0 recommendation.
- Select a Code of Conduct if the repository needs one; none is currently adopted.
- Establish a dedicated private security-reporting contact or enable a repository-private reporting route if desired.

These decisions must not be inferred from research recommendations, commit history, or GitHub ownership.

## Hard Product Non-Goals

- No remote code.
- No telemetry or analytics.
- No cloud sync.
- No hidden data export.
- No automatic message sending.
- No session, auth, account, or cookie manipulation.
- No broad host permissions without a documented feature requirement.
- No real personal prompts, credentials, private workflow notes, or secrets in the repository.

## Decision Maintenance

When implementation files are added, update this file if source truth supersedes a recommendation. Do not preserve stale recommendations as though they remain current implementation decisions.
