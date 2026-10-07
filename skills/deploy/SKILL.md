---
name: deploy
description: Deploy the intended repository state through its normal governed deployment process and verify the resulting live state.
---

# Deploy

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

1. Establish target/environment, source/artifact identity and deployment authority.
2. Discover the normal declared procedure, migrations, gates and recovery path.
3. Satisfy required repository/provider checks, reviews and approvals.
4. Execute the governed deployment with only the intended artifact and target.
5. Verify resulting revision, health and actual live behavior against acceptance criteria.
6. Report deployment identity, live evidence and remaining human acceptance or failures.

## Decision rules

Never silently switch to `publish` to get past a blocker. Respect normal process and
external controls. Use `release` for release records without rollout. If this repository
has no actual deployment procedure/artifact, report that prerequisite explicitly.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
