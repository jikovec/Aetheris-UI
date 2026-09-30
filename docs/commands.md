# Commands

Last validated: 2026-09-30

## Repository-Declared Application Commands

None.

No package manifest, lockfile, WXT configuration, test configuration, CI workflow, build script, or release workflow exists, so the repository declares no application install, run, build, test, lint, typecheck, package, deployment, or release command.

## Safe Git Inspection

These commands are valid in any local checkout with Git installed:

~~~text
git status --short --branch
git ls-files
git log --oneline --decorate -n 20
git diff --check
~~~

Use `git status --short --branch` before editing a local checkout so unrelated dirty/untracked work is preserved.

## File Inspection

POSIX shell examples, when those utilities are available:

~~~sh
find . -maxdepth 2 -type f -print
find docs reports handoffs DOCUMENTATION -type f -print
~~~

PowerShell examples:

~~~powershell
Get-ChildItem -Force
Get-ChildItem -Recurse -File docs, reports, handoffs, DOCUMENTATION
~~~

These are environment helpers, not application commands.

## Structured Documentation Validation

After editing repository metadata:

- parse `docs/agent-index.json` as JSON
- parse edited `.yml`/`.yaml` Issue forms as YAML
- verify relative Markdown links and referenced files
- run `git diff --check`

Use a parser available in the current environment; the repository does not currently declare a language runtime solely for documentation validation.

## Future Commands

The research report recommends an npm/WXT project, but the following are not current repository commands and must not be treated as executable requirements until a manifest declares them:

- `npm ci`
- `npm run dev`
- `npm run build`
- `npm test`
- `npm run lint`
- `npm run typecheck`

Do not start a development server unless source exists and the task requires it.
