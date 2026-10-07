# Deterministic hooks

The shared [toolkit validator](toolkit/validate.py) checks real metadata/discovery
invariants. It is manually invoked and is not installed as an automatic Git, provider
or CI hook. No reasoning or task-completion decisions belong in hooks.

| Property | Contract |
| --- | --- |
| Trigger | Manual, after toolkit or orientation changes and before delivery |
| Purpose | Validate identity shape, required files, skill/adaptor parity, links and index alignment |
| Inputs | Current repository files; optional `--root` for an isolated fixture |
| Side effects | None; reads files and prints results, no network or Git mutation |
| Runtime | Usually under one second for this documentation repository |
| Dependencies | Python 3.9+ and PyYAML; listed in project metadata |
| Exit | 0 pass; 1 invalid repository; 2 unavailable dependency or bad invocation |
| Failure | Fail closed on missing files, invalid syntax or inconsistent metadata; never repair automatically |
| Manual use | `python3 .agent/hooks/toolkit/validate.py` from repository root |

Future provider hook configs may call this shared implementation after explicit adoption.
Keep hooks deterministic, idempotent and independently testable; architecture, root cause,
severity, review and completion judgments remain skills.
