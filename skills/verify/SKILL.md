---
name: verify
description: Independently verify claimed repository, branch, PR, release, deployment, or live state using current evidence.
---

# Verify

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [verification](../../.agent/contracts/verification.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. State the exact claim and acceptance criteria independently of previous agent assertions.
2. Identify the current ref, artifact or live target and authoritative evidence sources.
3. Execute relevant checks, including negative/boundary cases when material.
4. Classify each result and disclose missing prerequisites or coverage limitations.
5. Compare evidence with the claim; report supported completion or exact remaining gaps.

## Decision rules

Do not repair implementation or weaken criteria merely to produce a pass. Use `review`
for defect-oriented change review. Load deployment, Git, scope or memory contracts only
when verifying those states. Structural checks alone cannot prove semantic acceptance.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
