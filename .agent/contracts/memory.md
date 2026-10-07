# Persistent memory

> Memory is contextual state, not repository truth.

Current source, configuration, tests, schemas, manifests, Git state, GitHub operational
state, runtime/live evidence and accepted repository decisions supersede memory.
Memory may aid discovery, preserve historical/user-approved context and point to accepted
decisions or project relationships. It cannot become undocumented architectural truth.

Before reading, establish the configured backend, readable scope, tool permissions and
freshness relevant to the task. Reconcile any memory-derived current claim with its
authoritative source. Conflicting memory stays stale/contextual; do not silently edit it.

Access does not grant write authority. A write requires a writable destination, explicit
or standing mutation authority, appropriate content and compliance with
[scope promotion](scopes.md). Do not automatically persist observations, hypotheses,
temporary failures or unverified interpretations. Never store credentials, keys, tokens,
transient secrets or unnecessary sensitive runtime data. Do not write merely to record
that ordinary work happened.

Durable technical decisions go to the accepted repository decision surface first,
then accepted/committed repository state, then an authorized memory pointer or summary.
Prefer links to ADRs, specifications, Issues or PRs over copied canonical content.
Repository bindings hold durable identity/authority references; live mutable memory
stays in the configured external backend unless canonical architecture says otherwise.

No project memory backend or writable scope is currently bound in
[project metadata](../project.yaml). Do not infer enrollment or permission from a
host-provided memory connector. If binding verification is unavailable, say so and
preserve valid existing bindings; never manufacture identifiers or mutate the backend.
