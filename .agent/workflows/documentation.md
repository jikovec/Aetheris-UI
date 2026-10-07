# Aetheris documentation maintenance

Use [AGENTS.md](../../AGENTS.md), the [documentation index](../../docs/INDEX.md) and
[current state](../../docs/current-state.md). Inspect current files before promoting
planning recommendations into implemented facts. The extension remains unimplemented;
toolkit validation does not establish browser functionality.

For a documentation change, preserve canonical paths and relative Markdown navigation.
Update the human and [machine index](../../docs/agent-index.json) together. Source/tooling
changes also update [SOURCE-MAP](../../docs/SOURCE-MAP.md),
[CONNECTIONS](../../docs/CONNECTIONS.md), current-state, commands and testing.
Meaningful reports enter `reports/INDEX.md`; real unresolved follow-up enters
`handoffs/INDEX.md`. Historical reports retain their dated claims.

Run [declared checks](../../docs/commands.md), review links and factual alignment, and
inspect the explicit task diff. No application build, browser install, dev server,
dependency installation or CI workflow is needed for documentation-only work.
Use [Git delivery](../contracts/git-github.md) when the accepted endpoint includes it.
