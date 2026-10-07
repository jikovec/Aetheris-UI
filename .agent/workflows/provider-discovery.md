# Provider discovery

Canonical skills live under `skills/`, including the established project entrypoint
under `skills/project/aetheris-ui-workflow/`. Each native adapter contains only matching
frontmatter and a relative link to that canonical file. Regular files avoid Windows
symlink privileges; the validator catches adapter drift. Add or change each provider
adapter atomically with its canonical skill.

## Codex

Current [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
designates `.agents/skills/`, scanning from working directory to repository root.
Use `$build <task>` or another skill name after repository discovery refresh.
The installed Codex also scans `.codex/skills/`. To avoid duplicate selectable names,
that path contains only a compatibility index; executable adapters live once in
`.agents/skills/`. `.codex/` configuration must not define separate policy.

For model-free runtime inspection, use the installed
[app-server skills API](https://learn.chatgpt.com/docs/app-server): initialize the
stdio server, send `initialized`, then `skills/list` with `cwds` set to this repository
and `forceReload: true`. Inspect repository-scoped skills and errors; do not start a
model turn. Static adapter validation alone is not native discovery proof.

## Claude Code

[Claude skills](https://code.claude.com/docs/en/skills) load from
`.claude/skills/<name>/SKILL.md`; invoke `/build <task>` or the relevant name.
[CLAUDE.md imports](https://code.claude.com/docs/en/memory) support the literal
`@AGENTS.md` line, keeping repository policy canonical.

The installed CLI's stream-json initialization control response can enumerate commands
without a user/model prompt. Isolate the probe: disable hooks, MCP and tools, use only
project settings and disable session persistence. Report only matching skill names;
raw initialization responses may contain private account metadata. This probe is
version-sensitive, so check CLI support before reuse. Import syntax verification and
skill discovery do not prove every model follows the instructions.

## Other providers

Read `AGENTS.md`, choose a canonical workflow and follow its linked shared contracts.
Add native adapters only for providers actually supported by this repository. Native
settings or subagents cannot expand authorization or duplicate workflow policy.
