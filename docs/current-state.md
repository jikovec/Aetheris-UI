# Current State

Last validated: 2026-09-30

## Canonical Repository Baseline

- Repository: `jikovec/Aetheris-UI`
- Default branch: `main`
- Baseline revision inspected for this pass: `73d99948dc218a43dea2d30a86cd40872a96416c`
- Repository visibility: public
- GitHub Issues and Discussions are enabled.
- The baseline revision contains documentation/planning material only.

This file describes canonical repository state. Local working trees can contain uncommitted or untracked work and must be inspected directly before local edits.

## Implementation Status

Aetheris UI is not a runnable browser extension yet.

Not present at the baseline revision:

- `package.json` or a lockfile
- WXT configuration
- extension manifest
- `entrypoints/`
- `src/`
- `tests/`
- `.github/workflows/`
- build/package output
- release artifacts
- deployment automation

Therefore no repository-declared application install, run, build, test, lint, typecheck, package, deployment, or release command exists.

## Repository And Governance Surface

The repository maintains:

- `README.md` and `00_Index.md` as public/memory entry points
- `AGENTS.md` for automated-agent invariants
- `docs/` as the primary documentation root
- `CONTRIBUTING.md`, `SUPPORT.md`, and `CHANGELOG.md` for public repository workflow
- `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md` for GitHub work intake and review
- `reports/` for durable evidence
- `handoffs/` for real delegated/blocked follow-up work
- `docs/agent-index.json` as the machine-readable agent index

Local `.obsidian/` state and generated/dependency/build/temp artifacts are intentionally excluded by `.gitignore`.

## Product Direction

The research and planning documents describe a future local-only, cross-browser WebExtension for `https://chatgpt.com/*` with local settings, visual enhancements, snippets/templates, and user-initiated helpers.

WXT, TypeScript, npm, Node 24 LTS, Manifest V3, storage design, and browser permission choices remain recommendations until implementation files establish them.

## Source Of Truth

Use this order when facts conflict:

1. Current source, manifests, lockfiles, configuration, tests, workflows, and other executable repository state.
2. Current canonical documentation and indexes.
3. `DOCUMENTATION/deep-research-report.md`.
4. Reports and handoffs.
5. Older chat or memory summaries.

## Known Unresolved Matters

- The implementation stack is not source-confirmed.
- The project license is unresolved; MPL-2.0 is a recommendation only.
- No Code of Conduct has been selected.
- No dedicated private security contact is declared.
- Test/CI strategy is not implemented.
- Release packaging is not implemented.
- Browser-store submission is not a v0.0.1 requirement.
