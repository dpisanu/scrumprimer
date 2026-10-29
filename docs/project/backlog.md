# Scrum Primer — Product Backlog

**Date:** 2026-10-29  
**Specification:** [Scrum Primer Migration Specification](SPEC.md)<br>
**Open decisions:** [opendecisions.md](opendecisions.md)

This file tracks **implementable work**, not legal permissions, enduring architectural constraints, or acceptance conditions. Those remain in the [specification](SPEC.md), particularly §§1–2, 6–9. The former specification's Phase 1 checklist is split into delivery stories and a standing release gate (§9.3). Later-phase work is tracked in the same table; its non-negotiable design boundaries remain in §2.

**Story identifiers:** `sp-1`, `sp-2`, … are unique and never reused, even if a story is removed.  
**State values:** `To Do`, `In Progress`, `In Review`, `Blocked`, `Done`, `Cancelled`.  
**PR Link:** `—` means no pull request exists yet; replace it with the actual PR URL when available.  
**Phase:** identifies the delivery phase of each story; phase scope and readiness notes follow the backlog table.

## Backlog stories

| Story Number | Phase | description | State | PR Link |
|---|---|---|---|---|
| sp-1 | Phase 0 | Create the independently owned `scrumprimer` GitHub repository and initialize a clean project skeleton without copying the upstream application. | Done | — |
| sp-2 | Phase 0 | Configure a pinned Hugo version, `hugo.toml`, English Markdown content root, and correct `/scrumprimer/` project-path URLs. | Done | — |
| sp-3 | Phase 0 | Implement PR validation for Hugo builds, front-matter schema, expected routes, and project-path links. | Done | — |
| sp-4 | Phase 0 | Configure GitHub Pages deployment from protected `main` via GitHub Actions, with least-privilege workflow permissions. | Done | — |
| sp-5 | Phase 0 | Write `README.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `CODE_OF_CONDUCT.md`, `COPYRIGHT.md`, `CONTENT_LICENSE.md`, `ATTRIBUTION.md`, and the new-code `LICENSE` with appropriately scoped rights statements. | Done | — |
| sp-6 | Phase 0 | Add issue and PR templates, `CODEOWNERS`, reviewer responsibilities, and contributor rights-confirmation instructions. | Done | — |
| sp-7 | Phase 0 | Build the content-and-asset provenance inventory (`data/rights.yaml`) and define the rights-status/front-matter validation policy. | Done | — |
| sp-8 | Phase 1 | Build original responsive Hugo layouts, navigation and reusable components for the resource-oriented structure agreed in sp-35, supporting Guide chapter layouts without assuming five upstream-style routes. | To Do | — |
| sp-9 | Phase 1 | Publish an original English landing page introducing the Guide, illustration resources, available languages and project status, with verified rights metadata. | To Do | — |
| sp-10 | Phase 1 | Publish the standard overview resource view using the sp-36 catalog, approved sp-14 variants, language selection, labeled English fallback and attribution. | To Do | — |
| sp-11 | Phase 1 | Publish the anime overview resource view using the sp-36 catalog, approved sp-14 variants, language selection, labeled English fallback and attribution. | To Do | — |
| sp-12 | Phase 1 | Publish project information with accurate original-author credits, independence, contribution/contact links and public-use rights status. | To Do | — |
| sp-13 | Phase 1 | Standalone Contact page retired: contribution/contact links are covered by sp-12; no requirement to clone the upstream page. | Cancelled | — |
| sp-14 | Phase 1 | Verify each qualifying illustration language variant's source, author, CC BY-ND 3.0 coverage, attribution and checksum; inventory and import only approved unchanged files. | To Do | — |
| sp-15 | Phase 1 | Inventory and verify external original Guide editions by language and actual PDF/EPUB availability, integrate with sp-36, and render outbound links clearly distinguished from generated exports; host no original binaries. | To Do | — |
| sp-16 | Phase 1 | Publish visible independent-project and upstream-credit notices; display an attribution/rights page without suggesting a blanket license. | To Do | — |
| sp-17 | Phase 1 | Enforce the rights policy for pages, Guide chapters/editions, localized assets and generated exports; reject unauthorized upstream binaries, incomplete provenance and placeholder publication URLs. | To Do | — |
| sp-18 | Phase 1 | Implement actual-HTML route, desktop/responsive smoke, internal/external link and baseline semantic/accessibility checks for the agreed resource/Guide structure. | To Do | — |
| sp-19 | Phase 1 | Record deployed English resource-baseline acceptance and, separately, full rights-cleared Guide-track acceptance under specification §9.3; do not claim Guide completion while rights/content/exports remain outstanding. | To Do | — |
| sp-20 | Phase 2 | Implement responsive page layout, navigation, and grids for narrow/mobile and tablet viewports. | To Do | — |
| sp-21 | Phase 2 | Improve responsive typography, spacing, touch targets, and keyboard navigation without weakening baseline accessibility. | To Do | — |
| sp-22 | Phase 2 | Make illustrations and other media display effectively on small screens without editing the original CC BY-ND assets. | To Do | — |
| sp-23 | Phase 2 | Run mobile/tablet device or emulator QA, screen-reader checks, and performance/accessibility regression checks. | To Do | — |
| sp-24 | Phase 1 | Establish locale-ready page, chapter and resource identities and Hugo content conventions while preserving English URLs; document how later language roots are enabled without requiring translated interfaces now. | To Do | — |
| sp-25 | Phase 3 | Enable localized menus/metadata and language switching using sp-24 foundations; implement explicit missing-page/chapter UX under OD-7, separately from sp-36 asset fallback. | To Do | — |
| sp-26 | Phase 3 | Implement translation contribution, review, provenance, status tracking, reviewer identity, and translator credit workflow. | To Do | — |
| sp-27 | Phase 3 | Publish correct `hreflang`/canonical metadata and test cross-language navigation and locale routing. | To Do | — |
| sp-28 | Phase 3 | Pilot an authorized website/Guide translation using locale-specific Markdown, source revision tracking and verified rights; validate completeness under sp-41 and preserve author/translator credits. | To Do | — |
| sp-29 | Phase 1 | Generate individual chapter and complete-Guide PDFs in GitHub Actions from the sp-38 ordered manifest and export-authorized Markdown; validate reading order, links and layout using safe test content until Guide rights are cleared. | To Do | — |
| sp-30 | Phase 1 | Generate chapter and complete-Guide EPUBs from the same manifest and authorized Markdown as sp-29; validate structure, navigation and reading experience. | To Do | — |
| sp-31 | Phase 1 | Add export credits, rights checks, edition/source-revision naming and QA; rebuild on chapter/order/asset/metadata/template changes and deploy matching pages and PDF/EPUB outputs together as uncommitted build artifacts. | To Do | — |
| sp-32 | Phase 4 | If a documented use case is approved, implement and test a legacy MOBI or Kindle-compatible output strategy. | To Do | — |
| sp-33 | Phase 5 | Prepare the upstream proposal package: demo, repository, architecture, editorial process, migration map, validation evidence, rights matrix, risks, and adoption options. | To Do | — |
| sp-34 | Phase 5 | Offer the independent proof of concept to the original maintainers for voluntary review and record feedback and any mutually agreed follow-up. | To Do | — |
| sp-35 | Phase 1 | Define resource-oriented information architecture, routes, stable page/chapter/asset identities, locale behavior and revised release scope; synchronize the specification and backlog before layout implementation. | To Do | — |
| sp-36 | Phase 1 | Implement a localized resource catalog with independent language/format/revision variants, verified destinations, requested-language then labeled English selection, honest unavailable states and all-language discovery regardless of interface locales. | To Do | — |
| sp-37 | Phase 1 | Investigate and document Guide reproduction, Markdown conversion, translation and export rights by edition; record evidence, permitted uses and unresolved restrictions without assuming permission. | To Do | — |
| sp-38 | Phase 1 | Define and validate a Guide manifest with edition metadata, ordered stable chapter IDs, credits, rights and PDF/EPUB targets; test missing/duplicate references and locale consistency using safe fixtures. | To Do | — |
| sp-39 | Phase 1 | Implement Guide contents, independent chapter routes, previous/next navigation and complete reading view from sp-38 and sp-8, using independently authored test content until original Guide publication is authorized. | To Do | — |
| sp-40 | Phase 1 | Convert and review the authorized English Guide into Markdown chapters, preserving source structure, original credits/notices and rights records; blocked until sp-37 documents sufficient rights and sp-38 defines composition. | Blocked | — |
| sp-41 | Phase 3 | Validate Guide translation source revisions, review freshness and edition completeness; prevent incomplete or silently mixed-language whole-Guide exports while flagging stale translations for review. | To Do | — |
| sp-42 | Phase 0 | Limit automatic GitHub Pages builds/deployments to changes in site inputs, build checks or the Pages workflow; preserve manual deployment and unfiltered required PR validation. | Done | — |

## Phase descriptions and readiness notes

The **Phase** field is a planning marker, not a separate backlog. Stories remain in one numbered table, and their IDs do not change when priorities or phase assignments change.

| Phase | Focus | Scope and readiness notes |
|---|---|---|
| Phase 0 | Independent repository foundation | Establish an independent repository, contributor policies, and working CI/CD. This work does **not** grant rights to third-party material. |
| Phase 1 | English resources and early Guide track | Deliver a locale-ready resource site, followed by authorized chapter reading and chapter/full PDF/EPUB downloads. A permission-safe resource baseline may ship while Guide rights remain unresolved, but does not complete the Guide track. Apply [specification §8](SPEC.md#8-original-english-prose-explicit-publication-gate) and record both acceptance milestones through sp-19 under [§9.3](SPEC.md#93-release-invariants-requirements-not-backlog-tasks). |
| Phase 2 | Mobile refinement | Deepen device, touch, performance and accessibility QA; responsive layouts and baseline accessibility already belong to Phase 1. |
| Phase 3 | Multilingual contribution system | Add language support and a translation contribution process. Do **not** import or modify upstream translated publications by default; translations require appropriate adaptation and publication rights. |
| Phase 4 | Optional distribution extensions | Core PDF/EPUB work is in Phase 1. Only consider sp-32 after an explicit use-case decision; never mirror upstream binaries. |
| Phase 5 | Proposal to upstream maintainers | Offer the independent proof of concept for voluntary consideration. This is **not** a transfer of the original domain, brand, content, or copyright. |

See [opendecisions.md](opendecisions.md) for choices that affect story implementation and release.

## Recommended sequence and dependencies

1. Agree information architecture and routes in sp-35; start sp-37 rights investigation in parallel. This planning revision does not mark either implementation story complete.
2. Deliver sp-24 locale foundations and sp-8/sp-9 English layouts/landing page; implement sp-36 catalog and verify source records through sp-14/sp-15.
3. Use the catalog and approved records in sp-10/sp-11; deliver sp-12/sp-16 disclosures and sp-17/sp-18 checks before baseline acceptance in sp-19.
4. Define sp-38 before sp-39 reading views and sp-29/sp-30 exports. Technical prototypes use independent test content; they do not depend on permission to copy the Guide.
5. Unblock sp-40 only with sufficient rights evidence from sp-37 and the sp-38 composition contract. Integrate actual authorized chapters with sp-39, sp-29/sp-30 and sp-31 before full Guide acceptance in sp-19.
6. Activate additional interfaces and the sp-26 translation workflow before the sp-28 pilot; use sp-41 completeness/freshness checks for translated Guide editions.

Keep sp-1–sp-7 completion history intact. Added capabilities extend, rather than retroactively redefine, completed foundation work. The initial language lists in [specification §5.6](SPEC.md#56-initial-resource-discovery-checklist) are verification inputs, not verified permissions or download URLs.
