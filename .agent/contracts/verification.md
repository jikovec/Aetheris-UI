# Verification

Use the strongest relevant repository-native evidence reasonably available. Select
checks by changed behavior and risks, not by running every possible command. Read
[project checks](../../docs/testing.md) and [commands](../../docs/commands.md).
Compare against the baseline to distinguish pre-existing failures from task regressions.
Fix causal task defects and rerun affected checks after repairs.

Assign each relevant check exactly one state:

| State | Meaning |
| --- | --- |
| passed | Executed against the reported state and met criteria. |
| failed | Executed and did not meet criteria. |
| blocked/unavailable | Could not execute; name the missing prerequisite or access. |
| intentionally bypassed | Eligible gate consciously skipped under recorded authority. |
| not required | Outside the change's relevant validation scope; state why if material. |

Record command/method, checked ref or artifact, result and meaningful limitations.
An unexecuted check never passed. Do not weaken acceptance criteria to manufacture
success. Local checks, hosted checks, release identity and live acceptance are separate.
Structural skill checks do not prove agent behavior; routing review and native discovery
are separate evidence. Missing app infrastructure is not a successful app build.
