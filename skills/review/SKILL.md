---
name: review
description: Review a change, branch, pull request, or implementation for material correctness, regression, architecture, security, and maintainability issues.
---

# Review

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [verification](../../.agent/contracts/verification.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Establish change/base/head and requested behavior; read affected contracts and callers.
2. Inspect the actual diff and surrounding implementation, not just the prior summary.
3. Prioritize correctness, requested behavior, regressions, contracts, architecture,
   security, tests and maintainability; include relevant performance/accessibility.
4. Substantiate actionable findings with file locations, trigger, impact and evidence.
5. State material coverage gaps; if no findings, say what was reviewed and its limits.

## Decision rules

Do not bury defects under style noise or claim exhaustive assurance. Review is not
implicit repair authority. Use `verify` for a specific claimed state and `fix` for an
authorized repair. Read Git/GitHub when reviewing branches or PRs.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
