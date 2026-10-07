---
name: aetheris-ui-workflow
description: Route Aetheris UI inspect, implement, verify, prepare-delivery and finish requests through its documentation and index maintenance workflow.
---

# Aetheris UI workflow

Use this compatibility entrypoint for established project workflow requests.
Read [AGENTS.md](../../../AGENTS.md) and
[documentation maintenance](../../../.agent/workflows/documentation.md).

Choose the canonical task workflow rather than implementing another policy:

| Request | Canonical workflow |
| --- | --- |
| inspect | [investigate](../../investigate/SKILL.md) |
| implement | [build](../../build/SKILL.md) |
| verify | [verify](../../verify/SKILL.md) |
| prepare delivery | [push](../../push/SKILL.md), preparation only until the requested endpoint permits delivery |
| finish | The unfinished accepted task's workflow and current authority |

Preserve source/plan distinctions and synchronize affected indexes. Complete proportional
checks using declared commands. Report implementation, remote delivery and live evidence
separately. This router does not turn an inspection into edits or delivery into deployment.
