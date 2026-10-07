# Deployment And Release

Last reviewed: 2026-07-09

Tags: #repo/deployment #aetheris/release

No deployment, package, publishing, or release automation exists in this repository yet.

## Current State

The checkout has no:

- package manifest
- build command
- extension build output
- CI workflow
- release workflow
- browser-store assets
- release zip artifacts

No deploy command should be invented or run.

## Planned Release Direction

The research report recommends local/unpacked release readiness first:

- Chrome/Chromium unpacked local install instructions
- Firefox temporary add-on instructions
- source/rebuild package guidance
- smoke-test checklist
- privacy and permission rationale
- future store-readiness notes

The proposed asset names from research are planning inputs only until build scripts exist:

- `aetheris-ui v0.0.1.zip`
- `aetheris-ui v0.0.1 delta.zip`

## Future Release Documentation

After source and scripts exist, update this file with:

- exact build commands from `package.json`
- artifact output paths
- checksum process if used
- release checklist
- CI workflow references
- manual smoke checklist links
- browser-store readiness notes


## Agent release and deployment routing

The [deployment contract](../.agent/contracts/deployment.md) distinguishes release,
normal deploy and explicitly requested force publication. These workflows discover real
mechanics; their presence does not create artifacts or a runnable deployment path.
Externally enforced protections cannot be bypassed. Ordinary source delivery follows
[authorization](../.agent/contracts/authorization.md) and is not live acceptance.
