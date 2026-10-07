# Release, deploy and publish

[Authorization](authorization.md) determines whether the requested effect is permitted.
Discover actual mechanics in [deployment documentation](../../docs/DEPLOYMENT.md),
source/configuration, workflows and live provider settings. Never infer a target, invent
a release command or treat missing infrastructure as an eligible gate to bypass.

**Release** manages versioning, notes, tags, immutable artifacts and release records.
It does not inherently make anything live. Verify the version, source ref, assets and
published record independently of deployment. Ordinary source delivery is not a release.

**Deploy** follows the normal governed deployment procedure, required checks, provider
policy, migration prerequisites and health/acceptance checks. Establish target/environment,
artifact identity, rollback/recovery path and authorization before effects. Never silently
switch from deployment to force publication when a gate fails.

**Publish** is an explicitly requested force-publication workflow. First identify the
normal blocker and classify who enforces it. Only repository-controlled or
deployment-process-controlled gates may be bypassed under target-specific authority.
Use the minimum necessary force path and retain each failed/skipped check's truthful
status. A gate declared in repository config but externally enforced as required is
an external control, not an eligible local gate.

Never administratively circumvent GitHub branch protection/rulesets, externally required
checks or reviews, protected environment approvals, organization governance, hosting
protections, IAM, cloud policy or equivalent external controls. Administrator credentials
do not change that classification. Ask for a legitimate external resolution when blocked.

For deploy/publish, verify resulting artifact/revision identity, health and observed live
behavior; distinguish machine checks from required human acceptance. Record bypasses,
remaining risk and rollback evidence. A failed or unavailable live check prevents a
claim of live acceptance. This repository has no implemented extension release or
deployment path at the bootstrap baseline; consult current files before future use.
