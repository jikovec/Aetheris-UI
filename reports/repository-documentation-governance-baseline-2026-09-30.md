# Repository Documentation, Governance, Metadata, And Hygiene Baseline — 2026-09-30

Tags: #agent/report #repo/index #repo/development #repo/security

## Baseline

- Canonical repository: `jikovec/Aetheris-UI`
- Default branch: `main`
- Base revision inspected: `73d99948dc218a43dea2d30a86cd40872a96416c`
- Base tree contained documentation/planning material only; no application source, manifests, tests, workflows, build output, or release artifacts.
- GitHub Issues and Discussions were enabled; there were 11 open Issues and no open pull requests at inspection time.
- `main` was the only branch and had no branch protection/ruleset at inspection time.
- Local workstation status could not be inspected during this pass because the authorized device was offline. Remote changes were therefore isolated on a new branch and no local files were mutated.

## Applicability Review

| Requested artifact | Result |
| --- | --- |
| `SECURITY.md` | Represented canonically by `docs/SECURITY.md`; improved there rather than duplicated. |
| `AGENTS.md` | Required; improved. |
| `README.md` | Required; improved. |
| `DEPLOYMENT.md` | Represented by `docs/DEPLOYMENT.md`; improved. |
| `robots.txt` | Not applicable; no deployed/indexable web surface exists. |
| `LICENSE.md` / `LICENSE` | Requires owner/legal decision; MPL-2.0 is recommended but not adopted. |
| `CONTRIBUTING.md` | Required for the public repository; created. |
| `CODE_OF_CONDUCT.md` | Requires owner/community-policy decision; not selected. |
| `SUPPORT.md` | Applicable because Issues and Discussions are enabled; created. |
| `CHANGELOG.md` | Applicable; created with an explicit pre-version convention. |
| `ARCHITECTURE.md` | Represented canonically by `docs/ARCHITECTURE.md`; no duplicate created. |
| `DEVELOPMENT.md` | Represented by `docs/DEVELOPMENT.md`; improved. |
| `TESTING.md` | Represented by `docs/testing.md`; improved, preserving canonical lowercase path. |
| `INSTALLATION.md` | Not applicable until a runnable extension exists. |
| `CONFIGURATION.md` | Not applicable; no runtime configuration exists. |
| `TROUBLESHOOTING.md` | Not applicable; no evidence-backed runtime failure catalogue exists. |
| `GOVERNANCE.md` | Not needed as a separate file; current authority/workflow is sufficiently expressed by repository ownership, `AGENTS.md`, `CONTRIBUTING.md`, and GitHub work objects. |
| `MAINTAINERS.md` | Not needed; no multi-maintainer model requiring a separate canonical file is established. |
| `CODEOWNERS` | Not applicable at this baseline; no distinct ownership/review map is established and no protection/enforcement exists. |
| `THIRD_PARTY_NOTICES.md` | Not applicable; no dependencies, vendored code, models, datasets, or bundled assets exist. |
| `NOTICE.md` | Not applicable for the current repository/license state. |
| `.gitattributes` | Not created; no demonstrated normalization/diff/merge need justifies it before source exists. |
| `.editorconfig` | Applicable to current Markdown/JSON/YAML authoring; created with minimal non-speculative rules. |
| `CITATION.cff` | Not applicable; no research/software release citation boundary is established. |
| `sitemap.xml` | Not applicable; no deployed/indexable site exists. |

## GitHub Metadata

Created a single work-item Issue form rather than separate bug/feature taxonomies, plus a pull-request template. The templates capture outcome, evidence, acceptance criteria, relevant paths, security/privacy sensitivity, verification, documentation impact, and delivery boundaries without inventing priority/type metadata.

## Hygiene

The base tree contained none of the requested generated/cache/archive debris. `.gitignore` was expanded only for relevant local/dependency/build/temp/backup/OS artifacts. Archives, patches/diffs, `/versions/`, and broad language-specific cache patterns were not blindly ignored because they may become legitimate repository inputs or are not currently relevant.

## Material Corrections

- Replaced stale July local-checkout history in `docs/current-state.md` with the current canonical remote baseline.
- Made the license status explicit: MPL-2.0 is recommended, not adopted.
- Clarified that no application commands, tests, CI, deployment, release, or install path exists.
- Added a real security-reporting policy without inventing a security email, bounty, SLA, or private channel.
- Made `merge to main != deployment/publication/release` explicit.
- Added local dirty-work preservation and Issue → branch → verification → PR delivery rules for contributors and agents.

## Validation Plan

After creating the branch changes, validate the remote tree for:

- JSON parsing of `docs/agent-index.json`
- YAML parsing/schema shape of `.github/ISSUE_TEMPLATE/*.yml`
- relative Markdown link targets
- references to existing repository paths
- whitespace/trailing-space issues in changed text
- PR diff against base revision

Local-only `git status --short --branch` and `git diff --check` remain unavailable until an authorized local device is online; they must not be reported as passed.

## Remaining Owner Decisions

- project license
- Code of Conduct selection, if desired
- dedicated private security-reporting route, if desired

No software implementation, merge, deployment, publication, tag, or release is part of this baseline pass.
