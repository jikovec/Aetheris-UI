---
name: build
description: Implement substantial repository changes and carry them through relevant verification and normal repository completion workflow.
---

# Build

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [git-github](../../.agent/contracts/git-github.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Establish the requested end state, affected files and relevant source/work baseline.
2. Read real manifests, architecture/decisions and task-relevant project procedures.
3. Implement the smallest complete change, preserving unrelated work and existing design.
4. Make ordinary implementation decisions within scope; record necessary tradeoffs.
5. Update affected canonical docs and indexes; verify changed behavior proportionately.
6. Diagnose and repair task-caused failures, rerun affected checks and review the diff.
7. Complete the authorized Git/GitHub endpoint and report evidence by delivery state.

## Decision rules

Use for substantial new work; route a known defect to `fix`. `develop` is an alias.
Do not automatically release, deploy or publish. A local-only task ends locally.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
