---
name: publish
description: Force-publish the intended state by bypassing only eligible repository or deployment-process gates while preserving external platform protections.
---

# Publish

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [deployment](../../.agent/contracts/deployment.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Establish an explicit force-publication request, target and applicable authority.
2. Identify the normal deployment blocker and which authority enforces it.
3. Classify local repository/process gates versus external platform protections.
4. Bypass only eligible local gates using the minimum necessary force path.
5. Preserve failed/bypassed/unavailable results truthfully and record exact bypasses.
6. Verify resulting live artifact identity, health and observed acceptance; report limits.

## Decision rules

Never circumvent branch protections, rulesets, externally required checks/reviews,
environment approvals, organization governance, provider protections, IAM or cloud policy.
Administrator access does not permit bypass. Unknown gate ownership stops bypass work.
Absent artifacts/configuration are missing prerequisites, not gates. Ordinary website
publication without force intent routes to `deploy`, not this force workflow.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
