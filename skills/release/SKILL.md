---
name: release
description: Prepare and complete the repository's normal release workflow, including versioning, notes, tags, artifacts, or release records where applicable.
---

# Release

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [git-github](../../.agent/contracts/git-github.md)
- [deployment](../../.agent/contracts/deployment.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Establish requested version/release target and authority for tags, artifacts and records.
2. Discover actual versioning, changelog, packaging, tagging and release mechanics.
3. Prepare the intended source state, notes and artifacts using declared commands.
4. Complete required verification/review before release mutations.
5. Create only authorized release objects and verify their version/ref/assets/checksums.
6. Report release identity, evidence and any remaining deployment work separately.

## Decision rules

Do not invent release mechanics when absent. Use `push` for ordinary source delivery.
Release does not imply deploy or publish; a live rollout requires separate applicable
authority and procedure. Missing build infrastructure is a blocker, not a bypassable gate.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
