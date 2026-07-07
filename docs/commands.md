# Commands

Last validated: 2026-07-07

## Repo-Declared Commands

None.

No `package.json`, lockfile, WXT config, test config, or CI workflow is present in the checkout, so no application, build, test, lint, package, or release commands are currently declared by the repo.

## Safe Inspection Commands

These commands are useful for future validation and do not require a scaffolded app:

```powershell
git status --short --branch
git ls-files
Get-ChildItem -Force
Get-ChildItem -Recurse -File docs, reports, DOCUMENTATION
```

If `rg` is unavailable or blocked in the Windows app runtime, use:

```powershell
Select-String -Path docs\*.md, reports\*.md, DOCUMENTATION\*.md -Pattern "text to find"
```

## Future Commands

The research report recommends an npm-based WXT project. Once `package.json` exists, read it before running commands.

Common commands that may be expected after scaffolding, but are not currently declared:

```powershell
npm ci
npm run dev
npm run build
npm test
npm run lint
npm run typecheck
```

Do not run these until they exist in the repo or the user explicitly asks to scaffold them.

Do not start a dev server unless the task requires it and the repo contains a runnable app.
