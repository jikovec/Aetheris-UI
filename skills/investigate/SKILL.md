---
name: investigate
description: Inspect repository, runtime, or work state to establish current behaviour, root cause, or required work without changing implementation by default.
---

# Investigate

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml), applicable `AGENTS.md` and
[workflow index](../../.agent/workflows/README.md). Load only the procedures/integrations
relevant to the task. Discover real commands from [commands](../../docs/commands.md).

## Workflow

1. Identify the question, current behavior and evidence needed to answer it.
2. Inspect bounded repository, runtime or work state without changing implementation.
3. Trace the causal path and test hypotheses with permitted read-only diagnostics.
4. Separate observed facts, supported conclusions, inferences and unknowns.
5. Report root cause or required work with source pointers and unresolved uncertainty.

## Decision rules

Default to read-only. Do not silently implement a discovered fix. Use `research` for
external technical evidence, `pull` for requested synchronization, and `verify` to test
a completion claim. Load Git, scope or memory contracts only if those states matter.

## Completion and handoff

Report the achieved endpoint, meaningful evidence and exact unresolved action using the
handoff contract. Keep local/source, hosted checks and live evidence separate. Unexecuted
checks are never passes; do not turn a blocked step into a broader unrequested task.
