# Commands

Last validated: 2026-10-07

## Application commands

None. No application package/extension manifest, lockfile, WXT config, test configuration
or CI workflow exists. Do not run `npm ci`, `npm run dev`, `npm run build`, `npm test`,
`npm run lint` or `npm run typecheck` until source declares them or product scaffolding
is requested. Do not start a dev server for documentation/toolkit work.

## Toolkit validation

The toolkit uses Python 3.9+ with PyYAML. This is tooling, not an adopted application stack.
Use an available environment that supplies both; report a missing dependency rather
than claiming a pass or silently modifying system packages. No environment setup runs
automatically, and the toolkit does not prescribe an installation method.

```bash
python3 .agent/hooks/toolkit/validate.py
```

The [manual hook contract](../.agent/hooks/README.md) defines inputs, effects and exit
codes. `--root <path>` permits validation of an isolated fixture. Use current Git metadata
to verify the configured remote/owner/default branch in addition to static validation.

```bash
git status --short --branch
git diff --check
git diff --cached --check
git ls-files
```

Diff checks cover tracked/staged changes; the toolkit validator also checks newly added
files. Review the final explicit path list before staging or delivery.

## Discovery checks

See [provider discovery](../.agent/workflows/provider-discovery.md) for model-free native
checks. Claude import syntax, native skill discovery and agent routing are separate from
application tests. [Routing cases](../.agent/evals/skill-routing.md) need semantic review.
