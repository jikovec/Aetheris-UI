# Security Model

Last validated: 2026-07-09

Tags: #repo/security #aetheris/privacy #aetheris/local-only

## Current Implementation State

No application source code or extension manifest exists yet, so there are no implemented permissions, storage schemas, content scripts, or background behaviors to inspect.

This file records the intended security and privacy model for future implementation.

The broader security hub is [SECURITY.md](SECURITY.md).

## Intended Security Boundaries

Aetheris UI should remain local-only and least-privilege.

Required guardrails:

- no remote code
- no external scripts or CDNs
- no telemetry
- no analytics
- no cloud sync
- no hidden data export
- no automatic ChatGPT message sending
- no account, auth, or session manipulation
- no broad host permissions without a documented feature need
- no private prompts, keys, credentials, or workflow notes committed to the repo

## Intended Browser Permission Posture

Planned minimum posture:

- target only `https://chatgpt.com/*`
- use extension storage for local settings and snippets
- prefer static content-script matching over broad host permissions where possible
- keep background logic minimal and event-driven
- avoid permissions such as `tabs`, `downloads`, `scripting`, and broad host access unless a specific feature requires them and the reason is documented

## Data Handling

Planned data handling:

- settings and snippets stay local to the browser profile
- example snippets in the repo must be generic
- import/export should be user-initiated and file-based
- any processing of visible ChatGPT page content must be local and user-initiated

## Unknowns

- Actual extension permissions are unknown until a manifest exists.
- Actual storage schema is unknown until source exists.
- Actual CSP and web-accessible resources are unknown until source exists.
- Actual release packaging controls are unknown until build scripts exist.
- Actual source-package review controls are unknown until release automation exists.
