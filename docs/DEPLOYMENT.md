# Deployment And Release

Last reviewed: 2026-09-30

Tags: #repo/deployment #aetheris/release

## Current State

No deployment, package, publishing, or release automation exists.

The repository has no application manifest, build command, extension build output, CI workflow, release workflow, browser-store package, hosted service, or production environment.

## Repository Merge Boundary

At the current baseline:

~~~text
merge to main != deployment
merge to main != publication
merge to main != software release
~~~

A merge changes repository content only. It is not evidence that an extension was built, installed, uploaded, published, or deployed.

Release, publication, or future store submission requires separate implementation, verification, and explicit authorization.

## Planned Local Release Direction

The research report recommends local/unpacked release readiness before browser-store publication:

- Chrome/Chromium unpacked local-install instructions
- Firefox temporary/local add-on instructions
- source/rebuild package guidance
- smoke-test checklist
- privacy and permission rationale
- future store-readiness notes

Proposed asset names in research remain planning inputs until build/package scripts exist:

- `aetheris-ui v0.0.1.zip`
- `aetheris-ui v0.0.1 delta.zip`

## Future Documentation Requirements

When a release pipeline exists, this file must record exact build/package commands, artifact paths, required checks, secrets/environment handling, manual versus automatic triggers, rollback/recovery procedure, release-versus-deployment distinction, and live/readback verification where applicable.

Do not infer release or deployment success from a merge or CI result.
