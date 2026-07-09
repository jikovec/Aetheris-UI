# Testing

Last validated: 2026-07-09

Tags: #repo/testing

## Current Test Status

No automated tests are present.

The checkout currently has no:

- package manifest
- test runner config
- source files
- test files
- browser fixture files
- CI workflow

Therefore, there is no runnable project test suite at this time.

## Current Validation Scope

For documentation-memory work, validate by checking:

```powershell
git status --short --branch
git ls-files
Get-ChildItem -Force
Get-ChildItem -Recurse -File docs, reports, handoffs, DOCUMENTATION
```

Then compare memory docs against actual files present in the checkout.

For documentation/indexing changes, also validate:

```powershell
Get-Content -Raw docs\agent-index.json | ConvertFrom-Json
git diff --check
```

## Future Testing Direction

The research report recommends layered testing for the eventual extension:

- linting
- typechecking
- unit tests
- fixture-based DOM contract tests
- build checks
- manual smoke checks on `chatgpt.com`

The report also recommends not making authenticated live ChatGPT automation a required CI gate.

When a package manifest is added, update this file with the exact scripts from `package.json` and the expected validation order.

## Unknowns

- Test runner is not implemented.
- Browser automation strategy is not implemented.
- DOM fixtures are not present.
- Manual smoke checklist is not present.
- CI validation is not present.
