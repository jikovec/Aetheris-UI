# Security And Privacy

Last reviewed: 2026-09-30

Tags: #repo/security #aetheris/privacy #aetheris/local-only

This file is the repository security policy and high-level security/privacy hub. The planned product threat boundaries are documented in [security-model.md](security-model.md).

## Supported State

Aetheris UI has no released or runnable software version yet. Security maintenance currently applies to the current repository documentation/planning baseline, not to a deployed extension.

Do not infer support for a version, browser, package, permission set, or release channel until implementation/release artifacts establish it.

## Reporting A Security Issue

For non-sensitive hardening defects that are safe to discuss publicly, open a GitHub Issue with the minimum reproducible information.

For a vulnerability, secret exposure, exploit path, private prompt/data exposure, or other matter that should not be public:

1. Do not put sensitive details, exploit steps, secrets, private prompts, user data, or credentials in a public Issue or Discussion.
2. If GitHub presents a private `Report a vulnerability` route for this repository, use that route.
3. If no private reporting route is available, open only a minimal public Issue stating that a private security contact is needed. Include no vulnerability details. The maintainer must establish a private channel before details are shared.

No dedicated security email, bounty program, guaranteed response time, or coordinated-disclosure deadline is currently declared.

## Useful Report Information

When a private route exists, include only what is needed to reproduce and assess the problem:

- affected revision/version and browser/environment
- affected path/component
- impact
- minimal reproduction steps
- whether secrets or user data may be exposed
- any safe mitigation already identified

Never include real credentials or unnecessary personal data.

## Required Product Guardrails

Aetheris UI must remain:

- local-only
- least-privilege
- transparent about what it changes
- free of telemetry, analytics, hidden export, cloud sync, and remote code
- limited to `https://chatgpt.com/*` unless a future explicit product decision changes the scope

Forbidden behavior includes automatic ChatGPT message sending, account/session/authentication/cookie manipulation, hidden conversation collection, broad host permissions without a documented need, runtime-fetched executable code, obfuscation, and committed private workflow material/secrets.

## Credential And Secret Handling

Do not commit or paste keys, tokens, cookies, credentials, private URLs, browser-profile data, or other secrets into Issues, Discussions, pull requests, reports, examples, fixtures, or documentation.

If a secret is exposed, remove it from active use and rotate/revoke it at the owning service; repository cleanup alone is not sufficient.

## Security Updates

When implementation begins, security fixes must update affected permission/data/storage documentation and receive proportional verification. Do not promise release timelines before a release process exists.
