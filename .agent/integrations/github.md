# GitHub

Canonical source: `https://github.com/jikovec/Aetheris-UI`, bound by
[project metadata](../project.yaml) and the checkout's `origin` remote. The owner is
personal namespace `jikovec`; no organization is bound.

Git is required for source operations. Use an available GitHub connector or authenticated
`gh` CLI for operational state. Credentials come from the user's existing credential
helper or authenticated tool session, never tracked files or copied session secrets.
Verify access with a narrow read. No additional plugin installation is required.

Read repository metadata, relevant Issues/PRs/Projects, branches, tags/releases, checks,
workflows and deployment triggers. Mutations follow [authorization](../contracts/authorization.md)
and [Git workflow](../contracts/git-github.md). An enabled integration is not permission
to administer settings, change protections, send unrelated messages or incur charges.

Canonical configuration is live GitHub repository settings and tracked `.github/`
configuration when present. Do not persist mutable checks/PR state as project metadata.
Before source writes inspect workflow triggers, Pages and relevant webhooks; unknown
external integrations remain an explicit limitation. Do not conflate a source push
with release or live acceptance.
