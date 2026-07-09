# Security And Privacy

Last reviewed: 2026-07-09

Tags: #repo/security #aetheris/privacy #aetheris/local-only

This document is the high-level security and privacy hub. The current implementation-state details remain in [security-model.md](security-model.md).

## Current State

No application source code or extension manifest exists yet. There are no implemented permissions, content scripts, storage schemas, background scripts, release artifacts, or network behaviors to inspect.

## Required Guardrails

Aetheris UI must remain:

- local-only
- least-privilege
- transparent about what it changes
- free of telemetry, analytics, hidden export, cloud sync, and remote code
- limited to `https://chatgpt.com/*` unless a future feature justifies and documents a narrower or changed scope

## Forbidden Behavior

Do not implement:

- automatic ChatGPT message sending
- account, session, authentication, or cookie manipulation
- hidden scraping or background conversation collection
- broad host permissions without a documented feature need
- remote scripts, CDNs, runtime-fetched code, eval, or obfuscation
- committed personal prompts, private workflow notes, credentials, keys, or tokens

## Documentation Duties

When source is added, document:

- extension permissions and rationale
- data storage schema
- import/export behavior
- no-data privacy statement
- local-only processing boundary
- release package review checklist

