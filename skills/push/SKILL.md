---
name: push
description: Finalize completed local work through the repository's normal commit, push, pull-request, check, and merge workflow.
---

# Push

## Shared contracts

- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [git-github](../../.agent/contracts/git-github.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Inspect worktree, current branch/upstream and completed task-owned changes.
2. Fetch and inspect relevant live PR/check state; preserve unrelated work.
3. Verify proportionately and review explicit staged paths and the entire final diff.
4. Commit coherent changes, push the task branch and create/update the scoped PR.
5. Inspect current-head checks/reviews, fix task-caused failures and rerun affected checks.
6. Merge when authorized and applicable requirements pass; verify remote default state.
7. Report commits, PR/merge identity and the separate state of the original checkout.

## Decision rules

Use for finishing completed local work, not for version/tag/artifact release. Honor a
preparation-only, draft-only or local-only endpoint. Do not force-push or deploy merely
because credentials permit it. Recheck source-delivery triggers before effects.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
