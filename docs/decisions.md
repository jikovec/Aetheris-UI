# Decisions

Last validated: 2026-07-07

## Confirmed By Repo Contents

- This checkout currently contains planning documentation only.
- No app source, manifests, tests, CI workflows, or release artifacts are present.
- No package manager is confirmed by a manifest.
- No license is confirmed by a `LICENSE` file.

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
