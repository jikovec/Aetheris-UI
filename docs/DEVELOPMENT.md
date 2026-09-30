# Development

Last reviewed: 2026-09-30

Tags: #repo/development #aetheris/wxt #aetheris/local-only

## Current Development Mode

The repository currently supports documentation, research, governance, and work-management changes only. No runnable application scaffold exists.

No package/runtime prerequisite is declared for application development because there is no application manifest yet. Git is sufficient for repository inspection; use the editor/tooling of your choice for Markdown/JSON/YAML changes.

## Orientation

Before editing:

1. Read `../AGENTS.md`.
2. Read `current-state.md`, `decisions.md`, `commands.md`, and `testing.md`.
3. Check the current `main` branch and relevant GitHub work object.
4. In a local checkout, run `git status --short --branch` and preserve unrelated changes.

## Workflow

For material changes, use:

~~~text
Issue / work object
→ focused branch
→ implementation or documentation change
→ proportional verification
→ pull request
~~~

Do not merge, deploy, publish, tag, or release without explicit authorization.

## Current Commands

There are no application install/build/test commands. See `commands.md` for safe inspection and documentation-validation commands.

## Future Scaffold Requirements

When implementation begins, the first scaffold change must source its commands and dependencies from committed manifests/configuration and update:

- `current-state.md`
- `decisions.md` if recommendations are accepted or superseded
- `commands.md`
- `testing.md`
- `SOURCE-MAP.md`
- `CONNECTIONS.md`
- `agent-index.json`

The research recommendation of WXT, TypeScript, npm, Node 24 LTS, Vitest, and GitHub Actions must be re-verified at implementation time.

## Generated And Local Files

Do not commit dependency folders, build/test output, temporary/backup files, browser-profile data, `.obsidian/` state, private prompts, or secrets. `.gitignore` records the current recurrence-prevention rules.

## Environment Variables

No application environment variables are currently declared.

## Debugging

There is no runtime to debug yet. Documentation defects should be reproduced against the current repository files and reported through the normal Issue/PR workflow.
