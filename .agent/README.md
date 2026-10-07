# Repository agent toolkit

[AGENTS.md](../AGENTS.md) is the always-on contract; [project.yaml](project.yaml)
holds stable identity. Canonical reasoning workflows live in `skills/`. Shared policy
lives in `contracts/`; project procedures in [workflows](workflows/README.md), service
references in [integrations](integrations/README.md), deterministic checks in
[hooks](hooks/README.md). Provider adapters only route discovery.

| Task | Workflow |
| --- | --- |
| Substantial implementation; develop | [build](../skills/build/SKILL.md) |
| Local state or root cause without edits | [investigate](../skills/investigate/SKILL.md) |
| External technical evidence | [research](../skills/research/SKILL.md) |
| Test a completion/state claim | [verify](../skills/verify/SKILL.md) |
| Find material defects in a change | [review](../skills/review/SKILL.md) |
| Repair a known defect; reconcile states | [fix](../skills/fix/SKILL.md) |
| Version, tag, artifact or release record | [release](../skills/release/SKILL.md) |
| Normal governed live rollout | [deploy](../skills/deploy/SKILL.md) |
| Explicit force publication past eligible local gates | [publish](../skills/publish/SKILL.md) |
| Finish completed work through Git/PR/merge | [push](../skills/push/SKILL.md) |
| Synchronize local state with upstream | [pull](../skills/pull/SKILL.md) |
| Established project request vocabulary | [aetheris-ui-workflow](../skills/project/aetheris-ui-workflow/SKILL.md) |

Codex: `$build <task>`; Claude Code: `/build <task>`; another provider can read the
linked canonical skill directly. `develop` and `reconcile` are semantic aliases, not
duplicate slash-command implementations. See [provider discovery](workflows/provider-discovery.md).

## Shared policy ownership

- [core](contracts/core.md): evidence, scope of work and preservation.
- [authorization](contracts/authorization.md): adopted standing grants and limits.
- [verification](contracts/verification.md): relevant checks and honest categories.
- [git-github](contracts/git-github.md): source/PR lifecycle and synchronization.
- [deployment](contracts/deployment.md): release, deploy and force-publication semantics.
- [handoff](contracts/handoff.md): concise evidence-backed delivery.
- [memory](contracts/memory.md): contextual persistence and mutation authority.
- [scopes](contracts/scopes.md): identity, visibility and explicit promotion.

Memory and scope contracts load only for work involving persistence, registry/relationship
bindings or promotion. Ordinary implementation does not need them. Mind-Seed is disabled;
there is no `.mind-seed/` binding or memory store in this repository. Project identity
can later bind a verified registry entry without assuming one repository equals one project.

Validate changes with the [toolkit hook](hooks/README.md) and exercise
[routing cases](evals/skill-routing.md). The [bootstrap report](../reports/agent-toolkit-bootstrap-2026-10-07.md)
records reconciliation and verification limits. The [compatibility guide](../docs/agent-workflow.md)
is a pointer, not parallel policy.
