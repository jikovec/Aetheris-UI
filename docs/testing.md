# Testing

Last validated: 2026-09-30

Tags: #repo/testing

## Current Test Status

No automated application tests are present. There is no package manifest, test runner, source tree, fixture tree, browser automation configuration, or CI workflow.

Application unit/integration/e2e/build checks are therefore not applicable to the current baseline.

## Documentation And Governance Validation

For repository documentation/metadata changes, verify:

1. local Git state with `git status --short --branch` when a local checkout is available;
2. whitespace/patch correctness with `git diff --check` when Git diff state is available;
3. relative Markdown links and referenced files;
4. JSON syntax for `docs/agent-index.json`;
5. YAML syntax/schema shape for Issue forms and other edited YAML;
6. that current-state, command, security, deployment, and navigation claims agree with the actual tree.

Never treat an unavailable local check as passing.

## Evidence States

Use explicit result language:

- `passed` - the check ran and succeeded
- `failed` - the check ran and failed
- `blocked` - a prerequisite prevented execution
- `unavailable` - the required tool/environment was not accessible
- `not applicable` - the check does not apply to the current repository state
- `not run` - applicable but intentionally not executed

## Future Testing Direction

The research report recommends future linting, typechecking, unit tests, DOM fixture/contract tests, build checks, and manual smoke checks on `chatgpt.com`.

Authenticated live ChatGPT automation should not become a required CI gate merely because manual smoke testing is useful.

When the source scaffold is added, replace planning language here with exact scripts/configuration from the repository and document how to add tests, required fixtures/services, browser targets, and CI relationships.
