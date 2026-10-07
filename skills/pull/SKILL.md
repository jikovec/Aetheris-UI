---
name: pull
description: Safely synchronize local repository state with upstream while preserving unrelated work and reconciling conflicts according to repository conventions.
---

# Pull

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [git-github](../../.agent/contracts/git-github.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Inspect status, branch, upstream, scoped instructions and unrelated local work.
2. Fetch the canonical remote and compare divergence before choosing integration.
3. Use fast-forward when possible or the repository's authorized rebase/merge strategy.
4. Preserve dirty/untracked/concurrent files; isolate if safe integration is not possible.
5. Resolve scoped conflicts without discarding either side or silently expanding work.
6. Verify resulting local ref/tree and report changes and unresolved conflicts.

## Decision rules

Destructive reset is not the default synchronization mechanism. Use `investigate` when
the user only asks what diverged. A fetch updates remote-tracking refs, not the current
checkout. Do not claim synchronization if only a fetch succeeded.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
