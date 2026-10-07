# Semantic scopes

Scope containment describes context, not a universal override hierarchy. Authority is
assigned by data type and valid governance. Availability of content does not prove read
permission; visibility below is always restricted by configured tools and access policy.

| Scope | Identity and lifetime | Read visibility | Write authority | Inheritance and promotion | Status |
| --- | --- | --- | --- | --- | --- |
| global | Established user/system identity; durable across projects | Configured global context only | Valid global governing authority | Shared defaults; promotion from organization needs destination authority | Policy only where adopted; memory contextual |
| organization | Canonical organization ID; organization lifetime | Authorized members/projects | Organization's governing process | May constrain projects; promote to global only with global write authority | Organization identity/policy canonical in its designated source |
| project | Stable project ID, possibly multiple repos; project lifetime | Authorized project participants | Project owner or delegated project rights | Inherit applicable organization policy; promote to organization only when appropriate and authorized | Accepted project decisions canonical; memory contextual |
| repository | Remote-qualified repository binding; repository lifetime | Public source or permitted private source | Repository/task grant for affected paths | Refines generic execution; cross-repo promotion requires project authority | Current technical source and accepted repository policy authoritative for their data |
| agent | Configured agent identity; configured agent lifetime | Assigned permitted context | Explicit or standing agent-scope grant | Inherit relevant constraints, never identity/permission expansion; durable promotion needs destination authority | Agent notes contextual, never project identity authority |
| task | Established task/work ID; accepted objective lifetime | Participants and delegated scope | Current task grant | Narrows scope; promote to project only after canonical decisions and destination approval | Findings provisional until validated; intent can grant permitted action authority |
| session | Actual runtime session ID; session lifetime | Current permitted execution context | Session-local state within task grant | Inherits constraints; session to task promotion is explicit | Ephemeral observations/hypotheses; no durable authority |

A lower scope cannot rewrite higher-scope identity: a session cannot rename a project,
a task cannot redefine an organization and an agent cannot mint a competing canonical
project ID for convenience. Registry-owned scope IDs must come from the registry.

Current repository source/configuration/tests are not overridden by project, agent, task
or session memory. Lower scopes may narrow organization policy but cannot widen prohibited
permissions. Repository instructions refine generic execution; task/session instructions
do not silently remove repository safety/governance boundaries. Memory/session state
cannot manufacture authorization. There may be no organization binding for a personal repo.

Promotion (session → task → project → organization → global) is never automatic.
For every move establish a writable destination, appropriate scope/content, mutation
authority and a supporting persistence mechanism. Update canonical repository/registry
truth first where applicable. Durable technical decisions normally reach accepted
repository decisions/commits before or together with authorized memory promotion.
Unpromoted findings remain ephemeral. Read [memory](memory.md) when persistence applies.
