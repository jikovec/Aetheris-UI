# 2026-09-12 Local Project Orientation Handoff

Tags: #agent/handoff #agent/orientation #aetheris/local-only

## Historical scope and evidence

The September 12 orientation pass verified the documentation/planning foundation for
a future local-only browser extension for `https://chatgpt.com/*`. At that audit,
local `HEAD`, `origin/main` and live remote `main` matched
`73d99948dc218a43dea2d30a86cd40872a96416c`. No application scaffold, package or extension
manifest, application tests, CI workflow, build output or release artifact existed.
These are dated observations, not claims about a later checkout or remote state.

The pass connected the project indexes, source/connection maps, commands and workflow
guide. It kept local source, remote Git, CI, deployment and live acceptance separate.
No commit, push, merge, release or deployment was performed during that pass.
Machine-local paths and session connector details are omitted from this public record.

The outstanding decision was whether the workflow guide, project skill and manual
environment actions should become coherent tracked repository configuration.

## Reconciliation — 2026-10-15

The [October toolkit adoption](../docs/decisions.md#agent-toolkit-adoption--2026-10-07)
established the canonical [toolkit](../.agent/README.md),
[project skill](../skills/project/aetheris-ui-workflow/SKILL.md) and
[workflow compatibility entrypoint](../docs/agent-workflow.md).
Those files supersede the September copies of workflow and authorization prose.

The remaining portable assets are the project skill's
[Codex metadata](../.agents/skills/aetheris-ui-workflow/agents/openai.yaml) and
[manual environment actions](../.codex/environments/environment.toml).
The actions inspect Git state and patch whitespace; setup and cleanup scripts are empty.
Tracking these assets completes the orientation bundle's configuration decision.
The [Obsidian guide](../docs/OBSIDIAN.md) retains graph recommendations while local
`.obsidian/` state stays ignored.

## Next implementation boundary

Use [current state](../docs/current-state.md), [commands](../docs/commands.md) and
[testing](../docs/testing.md) before further work. The extension remains unimplemented.
An implementation task must establish real manifests, source, permissions and checks;
source delivery of this orientation configuration does not establish release,
deployment or live acceptance.
