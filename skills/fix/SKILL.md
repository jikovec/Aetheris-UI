---
name: fix
description: Diagnose and repair a known defect, failed check, incomplete prior change, review finding, or inconsistency between authoritative project states.
---

# Fix

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

1. Establish the known defect, failed check, incomplete change or reconciliation target.
2. Reproduce or gather sufficient causal evidence; identify baseline versus task failures.
3. Trace the cause and repair the smallest complete affected path, preserving other work.
4. Add a meaningful regression check where the behavior and risk warrant it.
5. Rerun affected checks; update canonical docs/indexes when facts change.
6. Review the final repair and complete the authorized Git/GitHub endpoint.

## Decision rules

Repair causes rather than hiding symptoms with retries, sleeps or relaxed thresholds.
`reconcile` means this skill with reconciliation intent. Distinguish repository truth,
docs, Git, GitHub, runtime/deployment, registry, memory and handoffs; do not duplicate
work objects. Load scope/memory contracts only when persistent state is involved.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
