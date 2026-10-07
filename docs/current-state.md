# Current State

Last validated: 2026-10-07

## Implemented repository infrastructure

The repository contains product planning, documentation indexes and a portable agent
toolkit. [Project metadata](../.agent/project.yaml) binds Aetheris UI to
`jikovec/Aetheris-UI`; its repository-derived identity is stable across checkout paths.
Organization is unbound for this personal-account repository. Mind-Seed is disabled.

The [toolkit](../.agent/README.md) provides eight shared contracts, eleven canonical
workflows, the existing Aetheris project-workflow vocabulary, Codex/Claude discovery
adapters and a manually invoked structural validator. These are development tools;
they do not implement browser-extension behavior.

## Application state

No `package.json`, package lockfile, WXT config, extension manifest, `entrypoints/`,
`src/`, application `tests/`, CI workflow, app build output or release artifact exists.
There are no declared application build/test/lint/package/release commands.
Use [commands](commands.md) and [testing](testing.md) for actual toolkit validation.

## Product direction

[Product research](../DOCUMENTATION/deep-research-report.md) recommends a local-only
ChatGPT WebExtension using WXT, TypeScript, npm, Node 24 LTS and Manifest V3.
These remain planning recommendations until current manifests adopt them. License,
browser permissions, storage schemas, test runner and release mechanics are not
implemented. Preserve [privacy/security boundaries](security-model.md).

## Evidence and history

Current source/configuration/tests establish technical truth, current GitHub state
establishes work status, and accepted decisions establish policy. Planning research,
historical reports and memory cannot override current authoritative evidence.

The July 2026 documentation passes are retained as dated historical reports.
The [October toolkit report](../reports/agent-toolkit-bootstrap-2026-10-07.md) records
reconciliation with the pre-existing local orientation bundle and the separate open
baseline PR. Neither historical reports nor this page substitute for current Git state.
