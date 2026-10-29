# Scrum Primer — Product Backlog

**Backlog version:** 0.2  
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
| sp-3 | Phase 0 | Implement PR validation for Hugo builds, front-matter schema, expected routes, and project-path links. | To Do | — |
| sp-4 | Phase 0 | Configure GitHub Pages deployment from protected `main` via GitHub Actions, with least-privilege workflow permissions. | To Do | — |
| sp-5 | Phase 0 | Write `README.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `CODE_OF_CONDUCT.md`, `COPYRIGHT.md`, `CONTENT_LICENSE.md`, `ATTRIBUTION.md`, and the new-code `LICENSE` with appropriately scoped rights statements. | Done | — |
| sp-6 | Phase 0 | Add issue and PR templates, `CODEOWNERS`, reviewer responsibilities, and contributor rights-confirmation instructions. | Done | — |
| sp-7 | Phase 0 | Build the content-and-asset provenance inventory (`data/rights.yaml`) and define the rights-status/front-matter validation policy. | To Do | — |
| sp-8 | Phase 1 | Build original Hugo layouts, navigation, and reusable page components for the five English routes. | To Do | — |
| sp-9 | Phase 1 | Prepare and publish the English homepage from Markdown, with origin metadata and public-use rights verified before publication. | To Do | — |
| sp-10 | Phase 1 | Prepare and publish the English Overview page from Markdown, with origin metadata and public-use rights verified before publication. | To Do | — |
| sp-11 | Phase 1 | Prepare and publish the English Anime page from Markdown, with origin metadata and public-use rights verified before publication. | To Do | — |
| sp-12 | Phase 1 | Prepare and publish the English About page from Markdown, retaining accurate author credits and public-use rights status. | To Do | — |
| sp-13 | Phase 1 | Prepare and publish the English Contact page from Markdown, directing project contributions to the new repository. | To Do | — |
| sp-14 | Phase 1 | Inventory qualifying upstream illustrations, verify authorship, attribution and CC BY-ND 3.0 coverage, record checksums, and include only approved unchanged artwork. | To Do | — |
| sp-15 | Phase 1 | Add `data/publications.yaml` with verified external PDF/EPUB links and render clearly labeled outbound download links; host no original binaries. | To Do | — |
| sp-16 | Phase 1 | Publish visible independent-project and upstream-credit notices; display an attribution/rights page without suggesting a blanket license. | To Do | — |
| sp-17 | Phase 1 | Implement release checks for content rights and image metadata, forbidden upstream publication binaries, and placeholder publication URLs. | To Do | — |
| sp-18 | Phase 1 | Implement desktop smoke tests, internal/external link checks, and baseline semantic/accessibility checks. | To Do | — |
| sp-19 | Phase 1 | Verify the deployed English site against the Phase 1 release invariants in the specification and record the acceptance result. | To Do | — |
| sp-20 | Phase 2 | Implement responsive page layout, navigation, and grids for narrow/mobile and tablet viewports. | To Do | — |
| sp-21 | Phase 2 | Improve responsive typography, spacing, touch targets, and keyboard navigation without weakening baseline accessibility. | To Do | — |
| sp-22 | Phase 2 | Make illustrations and other media display effectively on small screens without editing the original CC BY-ND assets. | To Do | — |
| sp-23 | Phase 2 | Run mobile/tablet device or emulator QA, screen-reader checks, and performance/accessibility regression checks. | To Do | — |
| sp-24 | Phase 3 | Introduce Hugo locale configuration and additional language content roots while preserving the existing English URLs and stable `page_id` values. | To Do | — |
| sp-25 | Phase 3 | Add localized menus, translated metadata, language switcher, and explicit locale-fallback behavior. | To Do | — |
| sp-26 | Phase 3 | Implement translation contribution, review, provenance, status tracking, reviewer identity, and translator credit workflow. | To Do | — |
| sp-27 | Phase 3 | Publish correct `hreflang`/canonical metadata and test cross-language navigation and locale routing. | To Do | — |
| sp-28 | Phase 3 | Pilot one authorized translation using language-specific Markdown and verified rights; do not import upstream translated documents by default. | To Do | — |
| sp-29 | Phase 4 | Add a separate GitHub Actions PDF-generation workflow using only export-authorized project Markdown. | To Do | — |
| sp-30 | Phase 4 | Generate EPUB from the same authorized Markdown source and validate its structure and reading experience. | To Do | — |
| sp-31 | Phase 4 | Add export metadata, rights validation, release/version naming, and automated quality checks for generated documents. | To Do | — |
| sp-32 | Phase 4 | If a documented use case is approved, implement and test a legacy MOBI or Kindle-compatible output strategy. | To Do | — |
| sp-33 | Phase 5 | Prepare the upstream proposal package: demo, repository, architecture, editorial process, migration map, validation evidence, rights matrix, risks, and adoption options. | To Do | — |
| sp-34 | Phase 5 | Offer the independent proof of concept to the original maintainers for voluntary review and record feedback and any mutually agreed follow-up. | To Do | — |

## Phase descriptions and readiness notes

The **Phase** field is a planning marker, not a separate backlog. Stories remain in one numbered table, and their IDs do not change when priorities or phase assignments change.

| Phase | Focus | Scope and readiness notes |
|---|---|---|
| Phase 0 | Independent repository foundation | Establish an independent repository, contributor policies, and working CI/CD. This work does **not** grant rights to third-party material. |
| Phase 1 | English Markdown website | Deliver an English static website. Independently written or clearly marked demonstration text can be used until appropriate public-use permission for upstream English prose is established. `sp-9`–`sp-13` are **not** complete merely because Markdown files exist: published content must satisfy the rights gate in [specification §8](SPEC.md#8-original-english-prose-explicit-publication-gate). Release criteria live in [specification §9.3](SPEC.md#93-release-invariants-requirements-not-backlog-tasks), and `sp-19` records their verification. |
| Phase 2 | Mobile experience | Improve responsive layouts and mobile usability. Basic HTML semantics and accessibility must already work in Phase 1. |
| Phase 3 | Multilingual contribution system | Add language support and a translation contribution process. Do **not** import or modify upstream translated publications by default; translations require appropriate adaptation and publication rights. |
| Phase 4 | Document exports | Generate new documents only from export-authorized project Markdown; never mirror upstream PDF/EPUB/MOBI binaries. `sp-32` depends on an explicit MOBI decision. |
| Phase 5 | Proposal to upstream maintainers | Offer the independent proof of concept for voluntary consideration. This is **not** a transfer of the original domain, brand, content, or copyright. |

See [opendecisions.md](opendecisions.md) for choices that affect story implementation and release.
