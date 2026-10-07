# Authorization

## Owner-adopted standing grant

The repository owner explicitly adopted this contract in the Repository Agent Toolkit
Bootstrap request. For `jikovec/*`, `mind-seed-systems/*`, and other repositories proven
to be owned and controlled by the user, ordinary repository workflow necessary for a
requested task is standing-authorized: branches/worktrees, scoped edits, commits,
fetch/pull, ordinary rebase/merge, push, PR creation/update, task-related CI/review
remediation, ordinary Issue/Project work-state maintenance, merge after applicable
requirements pass, and cleanup of completed task branches.

This repository is user-owned based on its `jikovec/Aetheris-UI` remote and owner
metadata. Ownership labels are evidence of classification, not independent authority.
Dropie and VaultGuard use their repository/organization rules instead. Unknown ownership
requires establishing the applicable policy; never guess or copy this grant into an
unrelated repository as though that adopted it.

## Limits

A narrower task (for example local-only or review-only) narrows effects. Scope does not
create authority. Standing delivery covers only work necessary for the accepted task.
It does not authorize unrelated PR merges, service settings, collaborators/billing,
credentials, data migration, system activation or destructive operations outside the
granted domain. Release, deployment and force publication require task or separately
established standing authority for the target and effect; read [deployment](deployment.md).
Inspect indirect deployment triggers before source delivery.

Memory, session state, identity labels, credentials and tool availability cannot grant
or enlarge authority. Respect platform restrictions, organization governance and all
externally enforced protection. Never bypass branch protections, rulesets, required
checks/reviews, environment approvals, IAM or hosting protections, even as administrator.

Revalidate grants before consequential effects and when changed/revoked. Governance
changes require explicit policy-authoring authority and valid adoption before or together
with affected work. Proposed rules cannot authorize themselves retrospectively. Reuse
valid scoped permission without repeatedly asking. If a required effect is outside the
grant, prepare the concrete result first, then request only the missing authority.
