# Testing

Last validated: 2026-10-07

## Toolkit checks

Run the [declared validator](commands.md) after toolkit/orientation edits. It parses YAML
and JSON, checks baseline files and identity shape, matches frontmatter and canonical
adapters, resolves local Markdown links, checks index paths and rejects conflict markers
or text hygiene errors. It is read-only and does not verify live remotes or model behavior.
Exercise negative cases in an isolated copy: missing canonical skill, adapter drift,
invalid metadata and a broken reference must fail. Missing PyYAML must be reported as
unavailable, not a successful check.

Review [routing cases](../.agent/evals/skill-routing.md) for neighboring workflow boundaries,
authorization and deployment semantics. Verify native provider discovery where the actual
CLI environment permits. Report static validation, semantic routing and native discovery
independently. Do not claim a model inference test when only discovery was inspected.

## Application checks

No application tests, runner, browser fixtures, package manifest or CI workflow exists.
The toolkit validator does not prove extension privacy behavior or browser functionality.
Future product testing should cover lint/typecheck, pure logic, DOM contract fixtures,
builds and manual cross-browser smoke checks. Authenticated live ChatGPT automation is
not a required CI gate in the planning direction. Adopt exact commands from manifests
when implementation exists and update this document with them.
