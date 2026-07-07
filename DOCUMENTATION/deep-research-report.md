# Aetheris UI Deep Research Analysis

## 1. Executive Summary

Aetheris UI should be built as a cross-browser WebExtension with one shared TypeScript codebase, shipped first as local/unpacked builds for Chrome/Chromium and Firefox, and designed for future store publication without taking on store-risky behavior now. The strongest current technical fit is **WXT as the extension framework**, **Manifest V3 as the target model**, **npm as the package manager**, and a **minimal-permission architecture** centered on static content-script injection into `https://chatgpt.com/*`, `storage.local`, a full options page, and a very small background layer only where commands or cross-context messaging actually require it. Chrome requires MV3 and service-worker-oriented background logic; Firefox’s cross-browser guidance still highlights important differences, especially that Firefox retains background pages in its MV3 implementation model and has its own store/signing requirements. WXT is the clearest current fit because its official docs explicitly cover browser targeting, MV2/MV3 targeting, manifest generation, content scripts, testing, and browser-store packaging. citeturn12view2turn31view1turn6view1turn22view1turn6view3

For v0.0.1, the realistic MVP is not “every imaginable ChatGPT enhancement.” It is a **stable local interface layer**: dark mythic theme system, typography and spacing improvements, width/density/focus controls, refined code-block treatment, local settings, local prompt snippets/templates, user-initiated copy helpers, a few keyboard shortcuts, a popup for quick toggles, and strong documentation/testing/CI/build artifacts. Features that depend on fragile message identity, deep DOM scraping, or browser-specific side-panel behavior should be postponed. The extension should explicitly avoid automation that sends messages, network interception, remote code, telemetry, cloud sync, or unnecessary conversation harvesting, both because they violate the product brief and because they sharply increase policy and maintenance risk. citeturn13view1turn13view2turn21search0turn21search2turn30view0

The best long-term license fit is **MPL-2.0** rather than MIT by default. It preserves openness for modified source files through file-level copyleft, still allows larger works to use different terms, and includes patent protections. That balance fits a personal-first open-source extension better than MIT’s fully permissive stance or GPL’s broader reciprocal scope. citeturn28search1turn29search2turn29search0turn29search1turn29search3

## 2. Product Goal

Aetheris UI should be treated as a **personal-first, public, local-only enhancement layer** for ChatGPT on `https://chatgpt.com/*`. The goal is not to automate ChatGPT or to “extend the internet.” The goal is to make a single target experience more readable, more efficient for technical work, and more aligned with Aetheris’ own development workflow, while remaining maintainable as a public codebase.

Technically, that means the product should improve only what a browser extension can improve safely on a third-party SPA: presentation, local interaction affordances, user-initiated copying/export helpers, local prompt/snippet composition, and local settings. It should not depend on any server, backend account, analytics pipeline, or remote policy service.

## 3. Personal Branding and Open-Source Positioning

The repository should be openly branded as a personal extension owned by Aetheris, on a public entity["company","GitHub","code hosting platform"] repository. That is compatible with clean public maintenance as long as the codebase is explicit about what is public and what is intentionally excluded. Public branding is not a technical problem; undisclosed private workflow content in the repo would be. Future releases can remain clearly personal in tone, defaults, naming, and visuals without pretending to be an “official” ChatGPT extension. That separation also aligns with store policies that prohibit misleading or deceptive representation. citeturn13view1turn14view0turn27search2

The design direction should therefore be implemented as a **tokenized, original visual system** rather than as direct fandom mimicry. “Dark mythic, refined, technical” is viable if it is expressed through spacing, contrast, surfaces, borders, motion restraint, typography, and iconography, not copyrighted symbols, names, or lookalike UI. This is also the maintainable route: design tokens survive longer than hand-painted decorative CSS.

## 4. Hard Scope Boundaries

The supported site should remain exactly `https://chatgpt.com/*`. Chrome’s and Firefox’s content-script models both let extensions target narrowly scoped match patterns, and Chrome’s permission model treats `content_scripts.matches` and `host_permissions` as separate permission surfaces. For this project, broad host access is unnecessary and should be avoided. citeturn12view1turn12view3turn11view2

The privacy boundary is non-negotiable: no cloud backend, no analytics, no telemetry, no remote sync, no external scripts, no hidden data export, and no non-user-initiated conversation collection. Both Chrome Web Store policy and Firefox add-on policy increasingly focus on narrow permissions, single-purpose behavior, and strict limits on data collection/transmission. Firefox’s current add-on policies also prohibit ancillary data transmission and require explicit disclosure/consent for data collection, while Chrome’s policies prohibit collection or use of browsing activity except where required for a user-facing feature and prominently disclosed. citeturn13view1turn13view2turn14view0

The repository boundary is equally strict: ship only the **local template/snippet system**, generic examples, and documentation. Do not include real personal prompts, project prompts, internal notes, keys, or credentials. This is partly product discipline and partly open-source hygiene.

## 5. Development Environment Priority

The environment should be optimized in this order: Windows 11 first, Arch Linux second, other Linux and older supported Windows third, macOS last. The baseline runtime should be **Node.js 24 LTS**, not “whatever happens to be installed,” because Node 24 is the current LTS line and is supported through the end of April 2028. The official Node download archive currently lists Node `v24.15.0` installers for Windows, and Mozilla’s AMO reviewer default environment currently uses Node `24.14.0` and npm `11.9.0`, which makes Node 24 plus npm an especially pragmatic common denominator. citeturn24search15turn24search4turn15view0

On Windows 11, the simplest initial setup is the official Node 24 LTS installer plus npm, Chrome or another Chromium browser, and Firefox Developer Edition or Firefox Stable. WXT’s dev startup documentation also matters here: it can auto-open the target browser, it discovers browser binaries automatically when possible, and on Windows its persistent Chromium profile path must be absolute. That is directly relevant to a practical Windows-first workflow. citeturn22view0turn17search0turn17search8

On Arch Linux, the repository should not assume that the default repo Node package matches the project’s pinned LTS version. Arch’s official packages currently expose a current Node 25 package and a Node 22 LTS package, while Node upstream’s current LTS is 24. That mismatch means setup docs should require version verification after install instead of assuming repo parity. Arch’s official packages do provide current Firefox, Firefox Developer Edition, and Chromium, so browser installation is straightforward. citeturn25search0turn25search4turn24search1turn25search2turn25search3turn25search6

## 6. Core Assumptions

**Verified facts.** Chrome’s extension platform requires Manifest V3 for current Chrome Web Store submissions, and MV3 replaces persistent background pages with extension service workers. Firefox supports WebExtensions cross-browser work, but current Mozilla guidance still documents meaningful incompatibilities, including browser namespace differences, promise-vs-callback history, and the background-page versus service-worker distinction. WXT currently documents explicit browser targeting, manifest-version targeting, cross-browser API access, and store packaging support. citeturn8search9turn12view2turn31view0turn31view1turn6view1turn6view4turn6view3

**Engineering assumptions.** There is no official, stable DOM integration contract for ChatGPT as a browser-extension target in the source set reviewed for this analysis. Therefore, all ChatGPT page integration should be treated as **best-effort progressive enhancement** on top of an uncontrolled SPA, not as a stable DOM API. This assumption materially affects MVP scope: any feature that depends on stable per-message IDs, internal React internals, or brittle class chains is riskier than theme/layout enhancements and clearly user-initiated copy helpers.

**Planning assumption.** Because the project is local-only and browser-store publication is not a v0.0.1 deliverable, the first milestone should optimize for reproducible local builds, unpacked installs, smoke-check documentation, and future store-readiness notes rather than store submission polish.

## 7. Current Browser Extension Landscape

The browser-extension ecosystem is now firmly MV3-oriented on the Chromium side. Chrome documents MV3 support generally from Chrome 88 onward, and the Chrome Web Store no longer accepts MV2 extensions. MV3’s architecture centers on declarative permissions, package-contained code, and event-driven background logic via service workers instead of always-live background pages. citeturn12view2turn8search9turn21search4

At the same time, the broader WebExtensions landscape is still not perfectly uniform. Mozilla’s documentation is explicit that the API family is an emerging cross-browser standard with real differences across namespace usage, async handling, API coverage, and manifest keys. That means “one codebase” is realistic, but “zero browser-specific thinking” is not. citeturn31view2turn31view0

For Aetheris UI, this is good news overall: the project’s required surface area is relatively small. It mainly needs content scripts, storage, an options page, a popup or action surface, a few commands, and a lightweight background coordinator. That is well inside the intersection of Chrome and Firefox extension capability.

## 8. Chrome vs Firefox Compatibility

The most important compatibility difference is background execution. Chrome MV3 uses extension service workers; Mozilla’s cross-browser guidance notes that Firefox retains background pages in its MV3 model. That means background code must be written as short-lived, event-driven logic with no dependence on DOM access or long-lived in-memory state. The safest architectural response is to keep background responsibilities thin: command routing, cross-context messaging, and maybe version migration logic, but not heavy UI state or DOM processing. citeturn12view2turn31view1turn16search2

The second major difference is API surface and async style. Mozilla documents `browser.*` as the standard promise-based namespace, while Chrome historically used `chrome.*`, with MV3 promise support now covering most appropriate methods. WXT’s own browser wrapper exists specifically to flatten this boundary by exposing a unified `browser` object that maps to the runtime global. That is a strong reason to build on WXT instead of hand-rolling polyfills. citeturn31view0turn31view2turn6view4

The third major difference relevant here is UI surface divergence. Firefox offers `sidebar_action`/`sidebarAction`; Chrome offers `side_panel`/`sidePanel`, and Mozilla explicitly documents these as incompatible. A cross-browser personal productivity extension could use side panels eventually, but not in v0.0.1 if cross-browser parity matters from day one. citeturn9search12turn9search0turn9search1turn9search3

Firefox also has current publication-specific requirements that Chrome does not. New AMO submissions after November 3, 2025 must declare data collection permissions, and a no-data extension can explicitly state `required: ["none"]`. Mozilla also requires an extension ID through `browser_specific_settings.gecko.id` for MV3 signing and self-distribution. citeturn30view0turn31view3

## 9. Recommended Technical Stack

**Primary architecture recommendation:** **WXT + TypeScript + a small React UI layer + CSS custom properties/tokens + npm + Vitest + GitHub Actions**. WXT is the key decision. Its official documentation covers browser targeting, manifest-version targeting, manifest generation, content scripts, storage, testing, and publishing in a way that maps almost exactly onto Aetheris UI’s needs. citeturn6view1turn22view1turn6view2turn22view3turn6view3

Use React only where a component tree materially helps: options page, popup, command palette later, and isolated overlay UI. Do **not** turn the whole extension into a framework-first app. ChatGPT page theming and DOM integration should still lean on focused DOM utilities and CSS layers, because the target page is third-party DOM, not an extension-owned application shell.

Use CSS custom properties as the foundation of the theme system. Avoid Tailwind or other utility-heavy CSS frameworks for v0.0.1. They add review noise, build surface, and theming indirection without solving the actual hard problem, which is controlled, maintainable injection into a hostile DOM.

## 10. Package Manager Recommendation

The recommended package manager is **npm**, not pnpm. The decisive reason is not ideology; it is operational fit. Mozilla’s reviewer default build environment currently includes Node `24.14.0` and npm `11.9.0`, and the AMO source-code-review flow expects clear, reproducible local rebuild instructions with matching lockfiles. npm gives the lowest-friction path for contributors, reviewers, Windows-first onboarding, and CI, while still providing frozen installs through `package-lock.json` and `npm ci`. citeturn15view0turn15view2turn5search3turn5search4

pnpm remains a good tool, and its docs clearly support version pinning and reproducibility, but it introduces an additional tool dependency that this project does not currently need. Aetheris UI is a single-package extension repository, not a multi-package workspace. That reduces the practical upside of pnpm’s store model for v0.0.1. citeturn5search2turn4search4

## 11. Why This Stack Is Best for Aetheris UI

This stack is best because it matches the project’s actual constraint set rather than an abstract “modern frontend” checklist. WXT explicitly supports multiple browsers and manifest versions, generates manifests from structured config, provides a unified extension API surface, supports isolated ShadowRoot UI where appropriate, and ships first-class testing and publishing guidance. That removes a large amount of cross-browser scaffolding work that would otherwise become repo-specific maintenance debt. citeturn6view1turn22view1turn6view4turn33search1turn22view3turn6view3

Choosing npm over pnpm keeps onboarding and AMO rebuild instructions simpler. Choosing React only for extension-owned UI surfaces keeps the options page and popup maintainable without pretending the ChatGPT DOM is a React host application. Choosing tokenized CSS over utility-first styling keeps the visual layer original, readable, and easier to review. Overall, this gives the shortest path to a serious public v0.0.1 without painting the project into a framework or policy corner.

## 12. Rejected Alternatives

**Plasmo.** Plasmo is a serious extension framework, but on the official-doc evidence surfaced in this pass, WXT is more explicit about the exact areas Aetheris UI needs most: browser targeting, manifest-version targeting, store packaging, and testing. For this project, explicit Firefox/chrome planning matters more than broader framework polish.

**Vite + CRXJS or other lower-level custom toolchains.** These are viable, but they push more of the cross-browser burden onto the repository: manifest branching, Firefox packaging, AMO source-zip handling, browser-specific APIs, and dev workflow glue. That is unnecessary when WXT already documents those concerns directly. citeturn6view3turn22view1

**Firefox MV2 as a primary target.** WXT can target Firefox with MV2 defaults, but for a new repository in 2026, that is not the right strategic default. Chrome is fully MV3. Store-readiness is cleaner if the codebase is authored around MV3 assumptions from the start, even while acknowledging Firefox’s implementation differences. citeturn6view1turn8search9

## 13. Repository Architecture Recommendation

Use a single-package repository with clear separation between extension entrypoints, ChatGPT integration code, reusable feature modules, styling tokens, and test fixtures. WXT’s model already expects source entrypoints plus generated manifest output, so the repository should reflect that instead of fighting it. citeturn22view1turn21search15

Recommended structure in plain terms:

- `entrypoints/` for content script, popup, options page, and minimal background entrypoint.
- `src/features/` for independent feature modules such as theme, density, copy helpers, snippets, and collapse controls.
- `src/dom/` for selector contracts, anchor discovery, route detection, and observer utilities.
- `src/storage/` for schema, migrations, import/export logic, and settings access.
- `src/ui/` for extension-owned React components.
- `src/theme/` for tokens, scales, surfaces, and mode definitions.
- `tests/` for pure logic tests, DOM-fixture tests, and contract tests against sampled markup.
- `docs/` for install instructions, smoke checklist, store-readiness notes, privacy statement template, and release process.
- `public/` for icons and static assets.

The important architectural rule is **feature modularity**. Every page enhancement should be individually enableable, individually testable, and individually disableable if ChatGPT UI changes break it.

## 14. Manifest and Permission Strategy

Use **Manifest V3 for both Chrome and Firefox builds**. Keep the manifest intentionally small. For v0.0.1, the likely required permission set is just `"storage"` plus declarative content-script matching for `https://chatgpt.com/*`. Chrome’s permission model and Firefox’s host-permissions documentation both support a narrow approach here: `content_scripts.matches` is sufficient for static injection, while `host_permissions` grant extra privileges like tab metadata access and programmatic injection and therefore should be omitted unless a real feature needs them. citeturn12view1turn12view3turn11view2turn11view0

Avoid `"tabs"`, `"activeTab"`, `"downloads"`, `"scripting"`, and broad host patterns in the MVP unless a feature truly requires them. Chrome explicitly warns that some permissions trigger install/runtime warnings, and narrow permissions are a store-policy expectation. Export/import can be implemented from extension-owned UI using standard Blob/object-URL download patterns instead of the `downloads` API, which avoids an additional permission and warning surface. citeturn12view5turn35search2turn35search5turn35search0turn35search4turn35search17

For Firefox store readiness, plan `browser_specific_settings.gecko.id` and `browser_specific_settings.gecko.data_collection_permissions.required = ["none"]` into the future publication manifest profile. That is not optional for a new AMO submission in the current policy environment. citeturn31view3turn30view0

## 15. ChatGPT UI Integration Strategy

Treat ChatGPT integration as **progressive enhancement on a third-party SPA**. Chrome’s content-script model allows reading and mutating the page DOM from an isolated world, while keeping the extension’s JS environment separate from the page’s own scripts. That isolation is exactly what Aetheris UI wants: page shaping without page-code entanglement. citeturn12view0turn12view3

The integration should have three layers. First, a **page-level visual layer** that adjusts typography, widths, spacing, sidebar density, code blocks, and noise reduction using scoped selectors and CSS variables. Second, an **extension-owned UI layer** for controls such as quick toggles, snippet insertion UI, and later command-palette UI; those should use Shadow DOM isolation. Third, a **local state layer** that keeps settings and local feature state in extension storage, not in page globals. WXT’s `createShadowRootUi` support and the platform’s Shadow DOM model are useful here, but only for extension-owned widgets; Shadow DOM cannot replace page-level CSS when the goal is to restyle host-page content. citeturn33search1turn33search0turn33search3

Bootstrapping should happen at `document_idle`, followed by narrow observer-based reattachment or reconciliation as ChatGPT’s route or content changes. Do not inject into every frame. Do not programmatically inject on broad tab events. Declarative, static injection against the one supported origin is the safer and simpler route. citeturn12view3

## 16. DOM Fragility and Update-Resilience Strategy

The extension should assume DOM breakage will happen. The correct response is not “avoid DOM work entirely”; it is to constrain DOM coupling. Use **semantic anchors first**: roles, labels, stable layout landmarks, `code`/`pre` structures, button text or accessible names where defensible, and broad section relationships. Avoid deep chains of obfuscated classes, positional selectors, and assumptions about React component order. This is an engineering recommendation rather than a vendor-guaranteed contract.

For dynamic re-detection, use `MutationObserver`, but narrowly. MDN documents it as the modern platform mechanism for DOM change observation. Observe only the smallest container that matters, prefer `childList` and `subtree` over broad attribute tracking unless a feature absolutely needs attributes, and aggressively debounce reconciliation. Observers should be disconnectable per feature, not global forever-observers over the entire document. citeturn20search3turn20search0turn20search6

Every feature module should have three states: **available**, **degraded**, and **disabled**. If the intended anchor is missing, the module should fail quietly and stop. The extension’s core — theme settings, options page, popup, snippet storage — must remain functional even if page-level integration regresses.

## 17. Visual Improvement System

The visual system should be built as a layered CSS architecture using **design tokens first**, feature CSS second, and emergency fallback guards third. Chrome documents that declarative content-script CSS is injected before DOM construction/display for matching pages, which is useful for low-flicker base theming. Use that for static baseline variables and calm visual normalization; use runtime JS only where stateful classes must change. citeturn12view3

The token model should include at minimum: base surfaces, elevated surfaces, borders, accent levels, text tiers, code surfaces, spacing scales, corner radii, focus rings, and motion timing. Theme intensity should not mean “more decoration.” It should mean stronger or softer contrast, border glow, surface separation, and accent saturation. This keeps the design personal and mythic without turning into unreadable fantasy chrome.

Safe fallback behavior matters. If a ChatGPT DOM region changes, the system should still be able to apply global tokens and safe body-level layout improvements even if finer-grained treatment of messages or sidebars becomes unavailable.

## 18. Dark Mythic Aetheris Design Direction

The design target should be **ritual atmosphere through structure, not ornament**. That means near-black layered surfaces, controlled metal/ember accents, crisp separators, readable typography, restrained gradients, and minimal motion. The “mythic” part should come from hierarchy and mood, not from copied symbols or over-textured panels.

Accessibility must actively constrain the aesthetic. WAI guidance is clear that keyboard access, visible focus, contrast, and reduced-motion support are not optional usability extras. Contrast targets should stay comfortably above minimal readable thresholds for primary text and interactive focus. Focus indicators should be obvious, not decorative. Motion triggered by interaction should respect reduced-motion preferences. citeturn19search1turn19search9turn19search12turn19search0turn19search5

The practical design rule is simple: if a dark-mythic treatment reduces scanning speed in long technical chats, it is the wrong treatment.

## 19. Developer Workflow Improvement System

The strongest developer-oriented features for v0.0.1 are the ones that are clearly local, clearly user-initiated, and relatively low-fragility:

- Better code block presentation, including spacing, density, and visual contrast.
- One-click code copying improvements where the DOM provides obvious code-block boundaries.
- Copy whole answer and copy prompt actions for visible content only.
- Local prompt/snippet/template manager with placeholder variables and generic example presets.
- Collapse/expand for long answers and long code blocks.
- Quick width and density toggles for long technical threads.

These all improve daily use without requiring hidden automation or invasive data handling.

Features that should **not** be in v0.0.1 include automatic prompt sending, background scraping of all conversations, token estimation based on guessed internals, and broad conversation indexing. Those features either violate the privacy posture, rely on unstable inference, or create store-review risk. Chrome’s and Firefox’s current policy posture both favor narrow, disclosed, user-facing behavior. citeturn13view1turn14view0

## 20. General Usability Improvement System

Keyboard shortcuts are worth including early because both Chrome and Firefox support extension commands. Use a very small command set in v0.0.1: toggle focus mode, open quick controls, maybe open snippets. Do not ship a huge shortcut matrix initially. Both browsers support manifest-defined commands, and Firefox additionally exposes a shortcut-settings UI API that Chrome does not. citeturn34search0turn34search1turn34search2turn34search8

The general usability layer should prioritize friction reduction for long-form technical work: quick toggles, visible settings entry points, better scrolling ergonomics, and clear reset behavior. A full command palette is attractive, but it belongs in post-MVP unless it can be kept genuinely small and robust.

Settings access should be simple: action popup for quick toggles, full options page for detailed settings. Chrome and Firefox both support extension options pages, though they present them differently. That is fine; `runtime.openOptionsPage()` normalizes the entry behavior well enough for this project. citeturn8search6turn8search7turn8search12turn8search2

## 21. Personalized Local-Only Features

Local-only personalization is a natural strength of the extension model. `storage.local` is available across extension contexts, persists beyond cache/history clearing, and is explicitly local to the machine in Firefox’s documentation. This makes it the right default home for settings, theme mode, snippet libraries, and other personal preference data. citeturn11view0turn11view1

For import/export, keep the pipeline local and file-based. Standard browser APIs allow a user to select a file through normal file inputs and let an extension-generated page create downloadable JSON using Blob/object URLs and the anchor `download` attribute, which means the MVP does not need the `downloads` permission. citeturn35search22turn35search4turn35search16turn35search0

Local presets and UI profiles are good candidates, but multi-profile behavior should be simple in v0.0.1: one active profile plus export/import is enough. More advanced profile switching can come later.

## 22. Private Template and Personal Data Boundary

The snippet/template subsystem should be designed as a **public engine with private content excluded by default**. That means the repository contains schema, storage, CRUD UI, import/export behavior, placeholder support, and generic example templates only. It must not ship with any private prompts or real workflow artifacts.

Technically, the cleanest boundary is to treat example templates as demo content and anything real as user-imported local JSON. That makes the privacy boundary obvious in the codebase and prevents accidental leakage through commits, screenshots, test fixtures, or release zips.

## 23. Storage Strategy

For v0.0.1, use `storage.local` as the primary store. Chrome’s current docs set the `storage.local` quota at 10 MB unless `unlimitedStorage` is requested, and Firefox documents local storage as machine-local while subjecting large volumes to broader browser/IndexedDB-style quota behavior. For the MVP feature set, that is enough if stored data is kept compact. citeturn11view0turn11view1

Do **not** use `window.localStorage` for extension state. Chrome explicitly discourages it because service workers cannot use it, content scripts share it with the host page, and data can be lost when browsing history is cleared. Firefox similarly recommends `storage.local` instead. citeturn11view0turn11view1

A good split is:

- `storage.local` for settings, toggles, snippets, and compact UI state.
- `storage.session` only for ephemeral runtime state if needed later.
- IndexedDB only if post-MVP features introduce significantly larger local datasets, such as structured per-chat annotations or rich offline indexes. That is not necessary for v0.0.1. citeturn11view0turn10search2turn10search21

## 24. Privacy and Security Model

The security model should start with three hard rules: **no remote code, no unsolicited data transmission, and least privilege**. Chrome’s MV3 migration guidance explicitly disallows remotely hosted code, and Mozilla’s current add-on policy requires add-ons to be self-contained and not load remote code for execution. citeturn21search0turn21search4turn21search5turn21search2turn21search14

The privacy model should be equally blunt: Aetheris UI should not send conversation content anywhere. If a future feature needs to inspect visible conversation text to copy or locally transform it, that processing must remain local and user-initiated. Chrome’s Limited Use policy and Mozilla’s add-on policies both become far more demanding once browsing or content data is collected or transmitted. The easiest compliant posture is simply not to transmit it at all. citeturn13view1turn13view2turn14view0turn30view0

Security-conscious implementation choices follow from that:

- No remote scripts, CDNs, or runtime-fetched code.
- No `eval`, obfuscation, or hidden automation.
- No web-accessible scripts unless there is a compelling need.
- No permission creep.
- No relaxed CSP.
- No hidden network fetches for themes, prompts, or assets.

Mozilla also explicitly disallows obfuscated extension code, and AMO source review expects rebuildable sources with matching output. citeturn15view1turn15view2

## 25. Accessibility Requirements

Aetheris UI should target **WCAG 2.2 AA as a practical baseline**, with selected AAA-inspired choices where they are cheap and beneficial, especially for focus visibility. That means keyboard-operable controls, no mouse-only actions, visible focus indicators, unobscured focused elements, sufficient text contrast, descriptive labels for icon buttons, and reduced-motion support for nonessential animation. citeturn19search1turn19search4turn19search12turn19search3turn19search9turn19search5

For the extension specifically, this has several concrete consequences:

- Popup and options UI must be fully keyboard navigable.
- Content-script overlays must not trap focus accidentally.
- Buttons added into ChatGPT must expose accessible names.
- Visual focus mode must not hide the focused control.
- Compact mode must not shrink hit targets into frustration.

This is especially important because the extension’s visual identity intentionally pushes toward a dense technical interface. Density is acceptable; inaccessible density is not.

## 26. Performance Requirements

The performance budget should be conservative because the extension runs on a site the extension does not control. The content script should add **small, incremental enhancements**, not a second application. Chrome’s MV3 architecture exists partly to reduce background resource cost, and `storage` operations are asynchronous and quota-limited, so state should be cached judiciously and written in batches, not constantly. citeturn12view2turn11view0

Practical requirements for v0.0.1:

- One bootstrap pass at page load.
- Narrow `MutationObserver` usage with debounced reconciliation.
- Style recalculation kept simple and token-driven.
- No polling loops.
- No global re-walk of the full DOM after every change.
- No heavy parsing of offscreen conversation content.
- Blob/object URLs revoked after export to avoid memory leaks. citeturn20search0turn20search3turn35search1turn35search16

If a feature cannot be implemented without frequent full-page scanning, it should probably be postponed.

## 27. Testing and Verification Strategy

Testing should be layered. For unit and logic tests, use WXT’s documented Vitest integration. It already polyfills extension APIs in-memory, carries over WXT config, and is the path of least resistance for this stack. citeturn22view3

For DOM-facing features, prefer **fixture-based contract tests** over live-site browser automation. The repository should include representative HTML fixtures or snapshot fragments for the kinds of page structures the extension targets: message blocks, code areas, sidebar items, composer area, and route-shell changes. Those tests should validate selectors, feature gating, copy transformations, and collapse behavior without requiring an authenticated live ChatGPT session.

For extension-level verification, use build checks, linting, formatting, unit tests, and Firefox-oriented tooling such as `web-ext` for run/build/lint workflows. WXT’s own E2E guidance points to Playwright as the practical choice for Chrome extension E2E, but for this project it should remain optional and should target local fixtures or extension-owned surfaces, not live `chatgpt.com` as a release blocker. citeturn17search2turn17search6turn7search3

Manual smoke tests on `chatgpt.com` should absolutely exist, but they should be documented checklists, not mandatory automated CI gates.

## 28. Build, Packaging, and Release Strategy

The build strategy should produce separate browser artifacts from one codebase. WXT already supports browser-specific builds and zipping, including Firefox-specific source packaging expectations. citeturn6view1turn6view3

For v0.0.1, define two release assets exactly as requested:

**`aetheris-ui v0.0.1.zip`**<br>
This should be the **local-install release bundle**. It should contain:
- Chrome/Chromium unpacked build output.
- Firefox local/temporary-addon build output.
- install instructions,
- smoke-test checklist,
- changelog/release notes,
- checksums if desired.

**`aetheris-ui v0.0.1 delta.zip`**<br>
This should be the **source/rebuild bundle**. It should contain:
- source files required to rebuild identical artifacts,
- lockfile,
- build instructions,
- docs needed for future AMO source review,
- no `node_modules`,
- no secrets,
- no generated dev junk.

That “delta” interpretation is the only technically coherent one for a first public release with no previous version. It becomes the reviewable change-set from the empty baseline to v0.0.1.

GitHub releases can comfortably host these assets within normal release limits. Firefox source review also benefits from this split because AMO expects rebuildable source and matching outputs. citeturn27search2turn15view2turn15view3turn6view3

## 29. Local/Unpacked Installation Strategy

For Chrome/Chromium, the official local path is still the extensions page with Developer Mode and **Load unpacked**. That should be the primary documented install method. Chrome’s own distribution guidance also emphasizes unpacked loading for trusted code during development. citeturn17search0turn17search8

For Firefox, the official local path is **about:debugging → This Firefox → Load Temporary Add-on**, or equivalent `web-ext`-assisted workflows. Mozilla’s docs are explicit that temporary installs last until restart unless otherwise managed by tooling. citeturn17search1turn17search3

One current nuance matters for development tooling: Chrome has removed the old `--load-extension` command-line path in modern versions because it was abused. That makes manual `chrome://extensions` loading and framework-aware dev tooling more important than old CLI habits. citeturn18view0

## 30. GitHub Repository Setup

The public repository should include the minimum serious open-source hygiene from day one:

- `README.md` with scope, privacy model, browser support, local install steps, and non-goals.
- `LICENSE`.
- `CONTRIBUTING.md`.
- `SECURITY.md`.
- `CHANGELOG.md`.
- issue templates and PR template.
- CI workflows for build/test/lint on pull requests.
- release workflow for tagged builds and upload of the two zip assets.

GitHub Actions should use a matrix strategy across at least `windows-latest` and `ubuntu-latest`, with Node 24 pinned. GitHub’s docs explicitly support matrix workflows and dependency caching, and release assets can be attached directly to releases. citeturn27search0turn27search1turn27search3turn27search8

Because Windows 11 is the primary environment, Windows CI should not be optional. Linux CI is still essential because Firefox review defaults are Ubuntu-based and Arch users are a priority audience.

## 31. Browser Store Readiness

v0.0.1 does **not** need final store submission assets, but the repository should be intentionally prepared for them. On the Chrome side, that means narrow permissions, no remote code, clear single-purpose positioning, honest disclosures, and a short privacy statement that explicitly says the extension is local-only and does not transmit user data. Chrome’s policies become much stricter once user data is handled or broader permissions are requested. citeturn13view1turn13view2turn13view3

On the Firefox side, readiness means even more documentation discipline: self-contained source, no obfuscation, rebuild instructions, lockfile, declared extension ID, and data-collection declaration set to `none` for a new no-data add-on. Mozilla’s reviewer documentation is explicit that if they cannot rebuild or evaluate the extension, the submission may be rejected. citeturn15view0turn15view1turn15view2turn30view0turn31view3

Store-readiness documentation for this project should therefore include:
- permission rationale,
- privacy statement,
- reviewer build steps,
- explanation of local-only behavior,
- statement that no analytics/telemetry/remote code are used,
- explanation of why only `chatgpt.com` is matched.

## 32. License Recommendation

The recommended license is **MPL-2.0**. Mozilla’s own FAQ describes MPL as a simple, file-level copyleft license designed to encourage sharing of modifications while still allowing combination with code under other licenses with relatively low friction. GitHub’s Choose a License summary aligns with that: MPL requires source disclosure for licensed files and modifications to those files, while allowing larger works to be distributed under different terms. citeturn28search1turn29search2

Why not MIT? MIT is simpler, but it allows direct proprietary forks of the extension with almost no reciprocity requirement. For a personal-first public project whose value is concentrated in its UI logic, theme system, and workflow affordances, that is a weak fit. Why not GPLv3? GPLv3 is stronger than necessary here and extends reciprocity much further across combined works than is useful for this project’s likely adoption pattern. Apache-2.0 is better than MIT due to patent language, but it is still fully permissive. MPL-2.0 is the best middle ground. citeturn29search0turn29search1turn29search3turn28search0

## 33. v0.0.1 MVP Scope

v0.0.1 should be ambitious, but it should still be a **stability-first productivity layer**, not a speculative power-user suite.

**Include in v0.0.1:**
- WXT-based cross-browser project targeting Chrome MV3 and Firefox MV3.
- npm-based setup pinned to Node 24 LTS.
- Popup for quick toggles and options entry.
- Full options page.
- Local settings schema and migration path.
- Dark mythic theme token system with readable defaults.
- Focus mode, compact mode, and wide mode.
- Typography, spacing, sidebar density, and conversation readability improvements.
- Improved code block and inline-code presentation.
- Copy helpers: copy prompt, copy code, copy visible answer.
- Local prompt/snippet/template manager with generic example templates only.
- Import/export settings and snippets as local JSON.
- Safe reset-to-defaults.
- Minimal keyboard shortcuts.
- Linting, formatting, Vitest tests, fixture-based DOM tests, CI, docs.
- Local/unpacked install instructions and the two final zip assets.

**Do not include in v0.0.1:**
- automatic message sending,
- remote sync,
- analytics/telemetry,
- hidden scraping,
- token-count heuristics presented as authoritative,
- side-panel-only workflows,
- per-chat notes or message pinning that depend on uncertain message identity,
- full conversation search/indexing,
- browser-store submission assets as required deliverables.

This scope is large, but still realistic because most included features are local, user-initiated, and visual/interaction-layer focused rather than structurally invasive.

## 34. Post-MVP Roadmap

The post-MVP roadmap should expand only where the benefit outweighs the fragility.

**High-value next steps:**
- richer command palette,
- local UI profiles and presets,
- better message navigation and anchors,
- optional per-chat annotations if durable conversation identifiers can be verified manually,
- improved export formats,
- more advanced code-block utilities,
- optional DOM-contract snapshot packs for faster regression handling.

**Conditional later work:**
- side-panel experiences, but only with explicit Chrome/Firefox divergence planning,
- per-message pinning, only if stable message identity is found,
- conversation search/indexing, only if implemented on-demand and locally,
- optional Firefox/Chrome store submission pipelines after the repo proves stable in public local use.

**Probably never:**
- automation that bypasses user intent,
- session/authentication manipulation,
- network interception,
- cloud sync,
- data collection.

## 35. Risks and Mitigations

The primary risk is **ChatGPT DOM churn**. Mitigation: progressive enhancement, feature-level kill switches, narrow observers, selector contracts, and fixture-based regression tests.

The second risk is **cross-browser divergence**, especially in background execution and UI surfaces. Mitigation: MV3-first architecture with minimal background responsibilities, no side-panel dependency in MVP, and WXT-based browser targeting. citeturn31view1turn9search12turn6view1

The third risk is **policy drift**. Chrome and Firefox policies continue to evolve around privacy, remote code, and disclosure. Mitigation: stay local-only, keep permissions minimal, document no-data behavior clearly, and keep the extension self-contained and rebuildable. citeturn13view1turn13view2turn14view0turn30view0

The fourth risk is **public-repo leakage of private workflow content**. Mitigation: generic example templates only, `.gitignore` discipline, release-checklist review for source zips, and no screenshots or fixture content containing private prompts.

The fifth risk is **accessibility regression through aesthetic ambition**. Mitigation: WCAG-driven focus/contrast/motion checks and manual keyboard walkthroughs on every release candidate. citeturn19search1turn19search9turn19search12turn19search5

## 36. First Development Prompt Seed

The future v0.0.1 implementation prompt should instruct the implementation agent to create a **public, local-only, cross-browser WXT project** using **npm**, **TypeScript**, **Node 24 LTS**, and a **Windows 11-first workflow** with Arch Linux as the second documented environment. It should require Chrome MV3 and Firefox MV3 targets, a popup, an options page, a minimal background coordinator, one content-script entrypoint for `https://chatgpt.com/*`, a tokenized dark mythic theme system, local settings and snippet storage, copy helpers, import/export JSON, linting, formatting, tests, CI, documentation, and local/unpacked install instructions. citeturn6view1turn22view1turn22view3turn6view3turn15view0

It should also explicitly forbid remote code, analytics, telemetry, cloud sync, auto-send behavior, account/session manipulation, and reliance on fragile undocumented ChatGPT internals as release blockers. The prompt should require the two release assets:
- `aetheris-ui v0.0.1.zip`
- `aetheris-ui v0.0.1 delta.zip`

It should stop at build/test/lint/package/manual-smoke readiness and should **not** require automated live verification on `chatgpt.com`.

## 37. Sources

This analysis was based primarily on official documentation from entity["company","Google","tech company"] Chrome Extensions and Chrome Web Store policy docs, official Mozilla WebExtensions / Extension Workshop / MDN documentation from entity["organization","Mozilla","web nonprofit"], official WXT framework documentation, official Node.js and npm documentation, official GitHub Actions and Releases documentation, and W3C WAI accessibility guidance. The most important source groups are Chrome MV3/content-script/permission/policy docs, Mozilla cross-browser/MV3/AMO policy/source-review docs, WXT browser-target/testing/publishing docs, Node/npm reproducibility docs, and WAI WCAG guidance. citeturn12view2turn12view3turn13view1turn14view0turn15view2turn30view0turn6view1turn6view3turn22view3turn24search1turn5search3turn27search0turn19search17
