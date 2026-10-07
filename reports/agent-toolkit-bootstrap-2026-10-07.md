# Repository agent toolkit bootstrap — 2026-10-07

Tags: #agent/report #repo/decision

## Scope and identity

The owner requested implementation of a portable repository agent toolkit and explicitly
authorized the ordinary branch → checks → commit → PR → merge workflow for this user-owned
repository. [The adopted authorization contract](../.agent/contracts/authorization.md)
records that grant and preserves separate release/deployment/publication boundaries.

Identity is `github:jikovec/Aetheris-UI`, display name Aetheris UI. Live GitHub metadata
confirmed a public repository in the personal `jikovec` namespace with default branch
`main`. Organization is null; no organization ID was invented. The portable
[project metadata](../.agent/project.yaml) contains stable discovery facts, no current
commit, branch status, session identifier, credentials or test result.

## Reconciliation

Canonical remote `main` and the starting local HEAD were
`73d99948dc218a43dea2d30a86cd40872a96416c`. The original checkout contained a dirty local
orientation bundle, an untracked Aetheris workflow skill/guide, and manual Codex
environment actions. Implementation used an isolated worktree from fetched `origin/main`;
the original bundle was preserved rather than broadly staged or published.

The established `aetheris-ui-workflow` vocabulary is retained under `skills/project/`.
Its generic behavior now routes to canonical skills; the reusable documentation/index
process is factored into a shared workflow. `docs/agent-workflow.md` is a compatibility
pointer. The original machine-local project card and environment file were not copied
into public source. No tracked monolithic development prompt existed to retire.

[PR #12](https://github.com/jikovec/Aetheris-UI/pull/12) is a separate unmerged documentation
baseline and overlaps orientation paths. It was inspected but not adopted, merged,
closed or modified by this bootstrap. Reconcile those paths before a future merge of
that PR; do not reintroduce superseded authority/discovery statements.

The local project relocation catalogue supplies a display name/path, not a canonical
project ID or enrollment authority. A read-only query of the available Mind-Seed project
registry found no matching project, repository or workspace record. No repo-local
Mind-Seed metadata, persistent project memory binding or enrollment instruction existed.
The host's MemPalace connector returned an unavailable transport error; its memory
contents and scope bindings could not be verified. Therefore Mind-Seed remains disabled,
no `.mind-seed/` tree or speculative scope IDs were created, and no registry/memory
mutation occurred. This is not a claim that all external registries were accessible.

## Resulting architecture

- [AGENTS.md](../AGENTS.md) is the concise always-on contract; `CLAUDE.md` imports it.
- Eight [shared contracts](../.agent/README.md) own execution, authority, verification,
  Git/GitHub, deployment, handoff, memory and scopes.
- Eleven canonical workflows live under `skills/`; `develop` and `reconcile` are semantic aliases.
- One established project skill routes reusable Aetheris documentation work.
- Shared workflows cover documentation maintenance and provider discovery.
- GitHub is the sole documented repository integration; credentials stay external.
- The [manual deterministic validator](../.agent/hooks/README.md) has no automatic
  hook/CI installation or mutation side effects.
- [Routing fixtures](../.agent/evals/skill-routing.md) cover 3 positive and 2 negative
  cases for each skill, plus authorization and external-control boundaries.

Initial native discovery exposed duplicate Codex names when both `.agents/skills/` and
`.codex/skills/` contained adapters. Executable Codex adapters now live only in the
currently documented `.agents/skills/`; `.codex/skills/` is a compatibility index.
Claude uses `.claude/skills/`. All executable adapters point to canonical skills and
share identical discovery metadata. No separate provider policy or global configuration
was created. See [provider evidence sources](../.agent/workflows/provider-discovery.md).

## Validation and delivery evidence

Passed on the candidate:

- Read-only toolkit validator: 12 canonical skills, 24 native adapters, 87 text files and
  383 relative links; YAML/JSON, identity/index alignment and routing structure checked.
- All 12 canonical skills passed the skill-creator frontmatter validator.
- Six isolated negative fixtures were correctly rejected: missing canonical skill,
  adapter policy drift, wrong repository owner, broken reference, duplicate YAML key
  and duplicate Codex discovery surface. Missing PyYAML returned unavailable (exit 2).
- Codex CLI 0.159.2 and Claude Code 2.1.284 each discovered all 12 expected names exactly
  once, with no missing names or reported discovery errors. No model prompt was sent.
- Independent read-only semantic review covered all 36 positive examples, 24
  counterexamples and 8 authority probes with no remaining actionable findings.
  This was source review, not model-inference execution.
- Candidate tracked-diff whitespace check passed. Staged/final checks run before delivery.

Validation used existing Python 3.12.14 and host-provided PyYAML 6.0.3 exposed through
`PYTHONPATH`; no package or system dependency was installed. Bare Python lacked PyYAML,
which was reported as unavailable before using the existing package. The permanent
command requires a Python 3.9+ environment with PyYAML; it does not embed host paths.

Native discovery is separate from model-based workflow execution. Claude import syntax
was checked against official documentation and statically; no inference-level instruction
compliance claim is made. Application builds/tests, CI and live acceptance are not
required for this toolkit change because no application exists. The final PR record
establishes remote delivery state; this report does not claim a future merge in advance.

Live preflight found no Actions workflows, Actions runs, tags, releases, repository
Projects, active repository webhooks, Pages deployment, branch protection or rulesets.
Existing Issues #1–#11 remain separate product/work-management items. No issue was
created or closed for this scoped bootstrap. Account-level external integration absence
cannot be proven from these repository reads.

## Intentionally outside scope

The [integration handoff](../handoffs/2026-10-07-agent-toolkit-integration.md) records
the concrete reconciliation needed before future local-checkout or PR #12 integration.

Application scaffolding, browser installation, dependency adoption for the app, CI,
license/community policy, store/release mechanics, deployment, external registry
enrollment, memory mutation and the separate baseline PR remain outside this change.
Future product work must update source/command/testing maps from real implementation.
