# Scrum Primer — Independent Content as Code Website Proposal

**Status:** Planning draft — independent proof of concept  
**Proposed repository:** `https://github.com/<your-username>/scrumprimer` (not created by this specification)  
**Proposed preview site:** `https://<your-username>.github.io/scrumprimer/` (not deployed yet)  
**Upstream website:** https://scrumprimer.org/  
**Upstream repository:** https://github.com/nerds-odd-e/scrumprimer  
**Supersedes:** n.a.

## 1. Mission and collaboration model

Build an **independent, publicly inspectable, multilingual home for the Scrum Primer Guide and its supporting illustrations**, starting with English. This is a resource-oriented Content as Code project, not a one-to-one clone of the upstream website. Markdown and structured metadata drive the static reading experience, resource discovery, and authorized downloads. The implementation should make it easier to propose a collaborative, transparently licensed workflow to the current Scrum Primer maintainers.

The original [scrumprimer](https://scrumprimer.org/) website, upstream GitHub repository, DNS configuration, and hosting stay **untouched**. There is **no implied endorsement, ownership, permission, or transfer** from the original Scrum Primer maintainers. A proposal for possible adoption comes **after** the proof of concept is complete.

### Non-negotiable boundaries

1. The **new repository** is independently owned and administrated by the initiator until and unless an explicitly agreed handover occurs.
2. **GitHub Pages project site**: host at `https://<your-username>.github.io/scrumprimer/`; do not configure `scrumprimer.org` as a custom domain or make changes to its DNS.
3. **Markdown is the editable source of truth** for website pages and authorized Guide chapters; structured data defines publication composition, language variants, and external links.
4. **Original publication binaries remain externally hosted** and are not mirrored, committed, served, or bundled. Conversion of the Guide into Markdown, translation, and generation of new downloads require documented rights for those specific uses. Until cleared, develop the reading/export architecture using independently authored test content and link to original hosted publications.
5. **Only qualifying illustrations explicitly labeled CC BY-ND 3.0** may be reused, unaltered, with the full required attribution and original source and license links.
6. **Do not copy the existing Ruby/ERB app, CSS, templates, fonts, or unspecified assets** into the new project as a shortcut. Create a fresh site implementation.
7. **Distinguish upstream content from new contributions**. The original website's footer says “This page is open source,” but no clear license for its English prose has been established. This is evidence of an invitation to contribute, **not a transferable license or permission to relicense**. See the publication gate in §8.
8. A visible notice will explain: **independent community migration proposal, not the official Scrum Primer website**.

## 2. Scope and phased roadmap

| Phase | Objective | In scope | Deferred |
|---|---|---|---|
| **0 — Repository foundation** | Set up the clean independent project and governance | Repository structure, Hugo build, Actions, GitHub Pages project URL, contribution and rights policies, provenance inventory | Official-site adoption, original-domain work |
| **1 — English resources and Guide** | Deliver an English resource-oriented site and early Guide reading/export track | Original landing page; illustration resources; project/attribution information; locale-ready identities; verified external editions; chapter reader and ordered manifest; rights-cleared English Guide and chapter/full PDF/EPUB exports | Additional interface languages; uncleared Guide content; optional MOBI |
| **2 — Mobile refinement** | Refine the responsive experience | Device QA, touch usability, artwork display, performance and accessibility regression checks | Does not block starting Guide/export work |
| **3 — Multilingual contribution system** | Add translation governance and locale-aware content | Localized Markdown and UI, language picker, translation status and review, contributor credits, `hreflang`, translation provenance | Assuming rights to reuse upstream translated files |
| **4 — Optional distribution extensions** | Extend distribution where a use case is approved | Optional legacy MOBI/Kindle strategy | Core PDF/EPUB exports belong to Phase 1; unauthorized upstream ingestion remains prohibited |
| **5 — Upstream proposal (after viable demo)** | Invite the original owners to review and optionally adopt the project | Demo, migration report, license/ownership explanation, transfer/fork/integration options | Presuming approval, domain control or forced cutover |

Phase 5 discussions can begin informally earlier, but **adoption is not a prerequisite for developing the independent technical proof of concept**. Public republication of third-party prose remains subject to the separate rights gate in §8.

Phase labels group work rather than impose a waterfall. Publish a permission-safe English resource baseline while Guide rights are investigated; do not claim the Guide delivery is complete until its content and exports are authorized and verified.

### Planning and tracking documents

- **[Backlog](backlog.md)** — implementable work items, grouped by phase, each identified as `sp-N`; holds state and PR references. The backlog includes implementation tasks formerly mixed into the Phase 1 definition of done and later-phase design notes.
- **[Open decisions](opendecisions.md)** — decisions requiring an explicit choice, responsible parties, and a decision record. Factual rights and link verification are work items in the backlog, not decisions.
- **This specification** — durable scope, architecture, constraints, copyright boundaries, and release requirements. A task being marked Done does **not** waive these constraints.

### Cross-phase design constraints

- **Accessibility:** Phase 1 includes responsive layouts, semantic HTML and baseline keyboard/screen-reader accessibility. Phase 2 deepens device testing and refinement rather than postponing basic mobile usability.
- **Localization:** Every website page/section, Guide chapter, interface string, and logical asset must support language variants. Use stable identities across locales. Asset languages are independent of enabled interface languages. New translations require appropriate adaptation/publication rights and translator credits; do not modify CC BY-ND artwork to translate embedded labels.
- **Exports:** PDF and EPUB are the initial formats for authorized chapter and complete-Guide downloads. Build them in GitHub Actions, not on request. A separate export job or reusable workflow is acceptable, but deployment must wait for matching pages and downloads. Legacy MOBI is optional.
- **Upstream adoption:** No adoption outcome is assumed. Continued independent operation, collaboration, upstream integration, or an agreed transfer are possible, but any transfer of repository control, branding, domain operations, or content rights requires separate agreement. Original authors do not lose copyright by adopting the project.

## 3. Phase 0 — Independent repository and hosting

### 3.1 Repository naming and URLs

- **Suggested repository:** `<your-username>/scrumprimer` (subject to availability).
- **GitHub Pages project URL:** `https://<your-username>.github.io/scrumprimer/`.
- **No external/custom domain** is required or expected at this stage.
- The proof of concept must not use ambiguous branding such as “official new Scrum Primer” or imply that the existing owners have approved it.
- All page links, CSS, image URLs, canonical URLs, and sitemap URLs must work under the project path **`/scrumprimer/`**, not assume deployment at `/`.

### 3.2 Technology decision

- **Static site generator:** Hugo (recommended; decision may be revisited without changing the Markdown/content contract).
- **Content format:** Markdown with YAML front matter.
- **Configuration:** Hugo TOML; pin the Hugo version in Actions and document local setup.
- **CI/CD:** GitHub Actions for pull-request validation and deployment from protected `main`.
- **Hosting:** GitHub Pages via GitHub Actions (`configure-pages`, `upload-pages-artifact`, `deploy-pages`).
- **Features:** Default static website with minimal JavaScript, accessible HTML, and portable assets.
- **No runtime backend, database, analytics tracker, translation service, or on-demand document converter.** Pinned build-time export tooling may be introduced for authorized PDF/EPUB generation.

## 4. Proposed repository layout

```text
scrumprimer/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                   # PR/site validation
│   │   └── pages.yml                # Deploy to GitHub Pages
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
├── content/
│   └── en/                           # Future-ready English content root
│       ├── _index.md
│       ├── overview.md
│       ├── anime.md
│       ├── about.md
│       └── guide/
│           ├── _index.md            # Guide contents / reading entry
│           └── chapter-id.md        # Stable chapter identity, not ordering
├── layouts/                         # Original Hugo layouts/partials
├── assets/                          # New CSS and optional JavaScript
├── static/
│   └── third-party/                 # Approved unchanged imported artwork
├── data/
│   ├── publications.yaml            # Links to *external* originals
│   ├── resources.yaml               # Resource families and language/format variants
│   ├── guide.yaml                   # Ordered chapters and edition/export metadata
│   └── rights.yaml                  # Asset and content provenance
├── docs/
│   └── project/
│       └── SPEC.md                           # The living specification when adopted
│       └── backlog.md                        # Phase-grouped stories (sp-N)
│       └── opendecisions.md                  # Outstanding governance/product
├── tests/
│   ├── expected-pages.txt
│   └── check-rights.*
├── hugo.toml
├── README.md
├── MIGRATION.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── GOVERNANCE.md
├── COPYRIGHT.md
├── CONTENT_LICENSE.md
├── ATTRIBUTION.md
├── LICENSE                           # License for NEW software code only
├── THIRD_PARTY_NOTICES.md
└── .gitignore
```

**Note:** These are proposed responsibilities, not files that already exist; exact metadata filenames are settled during implementation. Configure `content/en` while retaining English routes at `/scrumprimer/...` without a premature `/en/` prefix. Additional language roots can be enabled later without moving English content. Generated downloads are build artifacts, not committed original publication binaries.

## 5. Phase 1 — English website content

### 5.1 Resource-oriented navigation

The site must make the Guide, standard overview illustration, and anime overview illustration discoverable, rather than reproduce upstream page boundaries.

| Area | Purpose |
|---|---|
| Home | Original introduction and access to reading, illustrations, languages, and downloads. |
| Guide | Contents, independently addressable chapters, complete reading view, and authorized downloads. |
| Illustration resources | Standard and anime views, verified variants, language selection, source and attribution. |
| Project information | Original author credits, independence, governance, and contribution/contact links. A separate Contact page is not required. |
| Attribution/rights | Per-work license and credit information without a blanket license claim. |

Final routes are agreed in `sp-35` and added to route tests as implemented. English remains under `/scrumprimer/`; upstream paths do not constrain the new information architecture.

The **new site is not responsible for compatibility redirects from upstream routes**. Since both sites coexist, upstream paths remain owned and served by `scrumprimer.org`.

### 5.2 Content contract

Example `content/en/overview.md`:

```yaml
---
title: "Scrum Overview"
page_id: "overview"
lang: "en"
description: "The Scrum Overview illustrations and explanatory text."
upstream_source: "https://scrumprimer.org/overview"
origin: "upstream-website"
rights_status: "permission-unverified"
last_reviewed: "2026-10-29"
---

<!-- English page prose goes here only when its public use is authorized. -->
```

- `page_id` is stable across locales.
- Guide chapters also have stable chapter identities and translation relationships; resource families have stable IDs independent of language, format, and revision.
- Record each translation's source edition/revision, actual translator credits, and review status so later source changes can flag stale translations. Follow the [rights policy](rights-policy.md); do not infer approval from a status or directory.
- `origin` distinguishes `upstream-website`, `original-project`, and `third-party`, as defined in the rights policy. Contributor authorship is recorded separately.
- `rights_status` is internal tracking information, **not** a license grant; `permission-unverified` cannot be treated as open-license metadata.
- Store document download metadata in `data/publications.yaml` so that links can be checked and updated independently from page layout.
- Use Markdown for editor-authored prose; use Hugo templates/shortcodes for images, navigation and metadata, never inline Ruby or ERB.
- The new site's footer must make the independent/experimental status explicit, and must **not** imply every asset is licensed under the same terms.

### 5.3 External publication references

The original domain remains live under the upstream maintainers' control. Therefore, unlike a domain cutover project, **the new site may link directly to current working URLs on `https://scrumprimer.org/`**, without hosting the files or changing their destination.

Example `data/publications.yaml`:

```yaml
publications:
  - id: primer-original-en
    title: "Scrum Primer — original English edition"
    format: "pdf"
    language: "en"
    url: "https://scrumprimer.org/..."    # placeholder; verify exact live path
    source_site: "https://scrumprimer.org/"
    hosted_by_this_project: false
    status: "pending-link-verification"
```

Publication links must be verified before release. If the upstream files are relocated or removed, the new project should update or retire links; it must **not silently mirror the files** as a workaround. Avoid presenting linked original documents as newly authored exports.

Track a resource family separately from its variants. A variant identifies its language, format, edition/revision, source, hosting type (external original or generated export), rights record, and actual destination. Website locale availability does not limit resource-language availability.

### 5.4 Language selection and fallback

- For each requested asset/format, select an approved variant in the current website language; otherwise select its approved English variant.
- Label fallback language visibly. If neither exists, show an unavailable state; never invent a URL or select an unapproved variant.
- Provide access to all available resource languages, including languages without a translated website interface.
- Website-page and chapter fallback are separate from asset fallback. The exact missing-page/chapter UX remains an explicit open decision; never silently present English as a translated page.
- Whole-Guide exports require a complete reviewed edition in the advertised language. Do not silently combine English and translated chapters into a mixed-language download.

### 5.5 Guide composition and build-time exports

Treat **A Lightweight Guide to the Theory and Practice of Scrum** as a publication with language-specific editions, not a set of unrelated website pages. Preserve the original credits to Pete Deemer, Gabrielle Benefield, Craig Larman, and Bas Vodde and supplied copyright notices; verify edition-specific credits before publication.

An explicit manifest defines publication/edition IDs, language, title, source revision, authors and translators, rights, ordered chapter IDs, and enabled export formats. Order comes from this manifest, not filenames, directory enumeration, or navigation labels. Validate unique chapter references, existing files, locale consistency, and edition completeness.

The same authorized Markdown chapters drive the contents page, chapter URLs, previous/next navigation, complete reading view, individual chapter exports, and complete-Guide exports. Avoid duplicate editorial sources for web and downloads.

Approved changes to chapters, order, relevant assets, publication metadata, or export templates regenerate affected PDF/EPUB outputs in GitHub Actions. PRs validate the relevant export builds; production deployment waits for pages and corresponding downloads from the same source revision. Download links serve pre-generated files. Begin with a simple correct build; incremental optimization is optional.

### 5.6 Initial resource discovery checklist

The following availability is reported for planning and must be verified per file, URL, edition, credit, and rights record before publication. It is not proof of permission or a complete verified catalog.

| Resource | Reported languages |
|---|---|
| Original Guide PDF/EPUB editions | English, Simplified Chinese, Traditional Chinese, German, French, Spanish, Italian, Bulgarian, Korean, Vietnamese, Russian |
| Standard overview illustration | English, Chinese, Vietnamese, Japanese, Korean, Thai, French, German, Spanish, Bulgarian, Russian |
| Anime overview illustration | English |
| Upstream website interface | Thai, Russian, Vietnamese, Japanese, English, Chinese |

Do not assume both PDF and EPUB exist for every listed edition. Distinguish Chinese language/script variants where verified instead of guessing their mapping.

## 6. Illustration rights and attribution

Reuse only the specific original images for which a source-page notice **actually confirms** CC BY-ND 3.0 coverage. This does **not** imply blanket coverage of logos, templates, fonts, supplementary artwork, book contents, or translations.

Per image, record:

- Resource family, variant language, format and revision;
- Upstream page URL and original asset URL;
- Creator/attribution party and copyright notice, where supplied;
- Exact Creative Commons version and canonical license link;
- Original filename, checksum, date reviewed, and no-modification status;
- Attribution rendered on the published page or linked attribution page.

Images must remain unaltered: no translated labels, cropping that creates an adaptation, redrawing, recoloring or repackaging as a derivative. Responsive **display sizing** is permitted; avoid modifications of the source asset. Preserve any creator and copyright notices and do not suggest endorsement.

Selecting an existing translated illustration is distinct from creating a translation: verify that exact variant's provenance and license before reuse. Coverage of the English file does not automatically clear every translated file.

Suggested rights record:

```yaml
assets:
  - id: overview-image
    path: "static/third-party/overview-original.png"
    source_page: "https://scrumprimer.org/overview"
    asset_url: "PENDING_VERIFICATION"
    license: "CC-BY-ND-3.0"
    license_url: "https://creativecommons.org/licenses/by-nd/3.0/"
    attribution: "PENDING_AUTHOR_VERIFICATION"
    unchanged: true
    checksum_sha256: "PENDING"
    approved_for_publication: false
```

## 7. Transparent licensing, ownership and governance

The project must distinguish **repository administration**, **copyright ownership**, **license grants**, and **editorial review**. Owning the GitHub repository does not make the maintainer the copyright owner of upstream or contributor materials.

### 7.1 Project licensing model

| Material | Project license/policy | Who has authority? |
|---|---|---|
| Newly written Hugo templates, CSS, JS, build scripts, configuration, and project documentation | **MIT** in `LICENSE` | Authors of that code and documentation |
| Newly authored website prose, UI translations, authorized translations, and editorial artwork in their designated paths | **CC BY-NC-SA 4.0** in `CONTENT_LICENSE.md` | The respective contributors; only material they can legally license |
| Reused original Scrum Primer overview and anime illustrations | **CC BY-ND 3.0**, unmodified, separately attributed | Existing creators/licensors; cannot be relicensed by this project |
| Original English upstream website prose | **Unverified / not sublicensable by this project** until permission/license is established | Upstream copyright holders |
| Guide prose, Markdown conversions and generated editions | **Rights-gated** reproduction, adaptation and export; retain original ownership, notices and applicable terms | Original rights holders; conversion does not grant relicensing authority |
| Original PDFs / EPUBs / MOBI files | **External links only**; not present in repository | Upstream rights holders |
| Future translations | Rights to translation and to publication must be confirmed; record individual translator credits and license | Original prose rights holders + translators as applicable |

Project licensing follows the path-based scope in [README.md](../../README.md), [CONTENT_LICENSE.md](../../CONTENT_LICENSE.md), and [CONTRIBUTING.md](../../CONTRIBUTING.md). These licenses apply only to contributions the project contributors have the right to license; they do not cover upstream material or third-party assets. **Do not** use a blanket license statement that could be read as licensing upstream content or CC BY-ND artwork. CC BY-ND images are not freely adaptable and should not be described as open source software assets.

### 7.2 Copyright and contribution ownership

- The original creators retain copyright in the original Scrum Primer material.
- Contributors retain copyright in their own independently authored contributions; the project receives the rights granted by the applicable contribution/license terms.
- The repository administrator controls merging, releases and settings, but does not automatically own the copyright in external contributions.
- `COPYRIGHT.md` describes ownership by content category, without suggesting assignment.
- `GOVERNANCE.md` defines maintainers, review decisions, release management, conflict handling, and a process for adopting or changing project-wide licenses.
- For contributions, require explicit confirmation that the contributor has the rights to submit the work under the published code/content licensing model. A **DCO-style sign-off** can document provenance if selected; it is not a copyright assignment or a substitute for permission to use third-party material.
- Do not impose a Contributor License Agreement or automatic copyright transfer by default. Any future CLA should be evaluated and disclosed separately.

### 7.3 Minimum contribution workflow

1. Contributor opens an issue or discussion (content correction, accessibility, design, translation, license question).
2. Contributor forks/branches, updates Markdown or independently authored code, and opens a pull request using the template.
3. PR template requests: purpose, page/language affected, source/provenance, third-party asset details, rights confirmation, and testing notes.
4. CI validates front matter, links, rendering, image-rights metadata, forbidden publication binaries, and build output.
5. An authorized maintainer reviews technical/content quality and rights status; language changes later also require language review.
6. Accepted contributions merge to the default branch and deploy automatically, with attribution retained in Git history and/or explicit content credits.
7. Rights disputes are flagged and affected material is unpublished pending review.

A contributor guide must distinguish **issues and suggestions** from **publishing copyrighted text, images, or translations**.

## 8. Original English prose: explicit publication gate

This gate also covers the Guide, chapter conversion, translated editions, and generated exports. Investigate rights in `sp-37`; conversion/publication in `sp-40` is blocked until sufficient authorization is documented. Clear authorship or a copyright notice identifies rights holders but does not itself grant reproduction, adaptation, translation, or redistribution rights.

The upstream footer's **“This page is open source”** message and invitation to contribute do not identify a legally definite license for the page text or Guide. The goal of making the Guide readable in Markdown is not a claim of legal permission. Do not attach the project's CC BY-NC-SA 4.0 content license to inherited prose without authority.

**Practical two-stage policy:**

1. **Development/prototyping:** build page/chapter structure, front matter, manifests, navigation, templates, exports, illustration attribution and link inventories using independently authored test content. Do not copy uncleared Guide or website prose into the public repository, including draft files.
2. **Public Pages publication:** only include upstream paragraphs if their reproduction/publication is authorized, or replace them with independently authored text that does not merely paraphrase protected expression. Link and cite the original site rather than reproducing text where permission remains unclear.

A GitHub repository being public is **not** evidence that all its contents can be republished or re-licensed. The **public-release acceptance criteria** require a rights decision for each page. A demo with an original layout and permission-safe placeholder or newly created text can still prove the architecture while authorization is pending.

This is a risk control rather than a claim that the original site is inaccessible or that the migration must cease. Resolve prose rights with the original maintainers before publishing substantial copied content, especially because the new proof of concept is separately operated.

## 9. CI/CD, quality gates and deployment

### 9.1 Pull-request checks

- Markdown style and front-matter schema validation (`title`, `page_id`, `lang`, `origin`, `rights_status`).
- Build Hugo with an explicitly pinned version and English config.
- Validate actual HTML for the agreed resource/Guide routes under `/scrumprimer/`, not just sitemap entries. Update the expected-route inventory as stories deliver pages.
- Check navigation links, canonical URLs, assets, and sitemap for the **GitHub Pages project-path prefix**.
- Check external URLs when feasible, with handling for occasional upstream outages; no fake “verified” results.
- Reject original upstream publication binaries and unauthorized generated downloads. Allow only rights-cleared newly generated exports from the configured build pipeline, with source revision and rights provenance; do not commit generated publication binaries.
- Validate Guide manifest order/references, chapter metadata, edition completeness, translation freshness and language consistency.
- Test resource locale selection, English fallback, missing variants, and all-language discovery independently of enabled interface languages.
- Validate chapter and whole-Guide PDF/EPUB structure, credits, reading order, links and output availability before deploying matching pages/downloads.
- Check that all included third-party images have approved, complete provenance and attribution data.
- Reject placeholder publication URLs in a release build.
- Ensure there is no blanket declaration that all content or assets share a single license.
- Run basic responsive, HTML accessibility, semantics and desktop smoke checks; expanded device QA is Phase 2.

### 9.2 Pages deployment

- Configure repository **Settings → Pages → Source: GitHub Actions**.
- Build with a base URL such as `https://<your-username>.github.io/scrumprimer/`.
- Deploy via GitHub's maintained Pages actions with minimal permissions (`contents: read`, `pages: write`, `id-token: write` for deployment).
- Deploy production only from `main` to a `github-pages` environment; review branch protection and repository access.
- Do **not** create a `CNAME` pointing to `scrumprimer.org` or change the original site's DNS.
- Confirm the independent-site disclaimer, attribution page, external publication links, and license scope on the live project URL.

### 9.3 Release invariants (requirements, not backlog tasks)

The Phase 1 release is acceptable only if the following remain true, regardless of how the backlog is divided into pull requests:

- The repository and Pages site are independent of the original owners and domain; the deployed site includes a clear non-official-project notice.
- The English landing page, illustration resources, project information and attribution render as actual HTML under the project-site path, using Markdown and structured data rather than a server-side application. No upstream five-page clone is required.
- The rights status of **every published page** is resolved for public use, without presenting unlicensed upstream prose as newly CC-licensed work. Source attribution and ownership information remain visible and accurate.
- Every redistributed third-party image has recorded permission/provenance and required attribution, and its source artwork is unchanged.
- No original publication binary is committed or deployed. External originals and generated exports are clearly distinguished; all links resolve to verified destinations.
- The English resource baseline can ship while Guide rights remain unresolved, explicitly documenting the unavailable reading/export features. It must not be presented as completion of the full Guide track.
- Full Guide-track acceptance requires authorized English Markdown chapters, manifest-driven contents/order/navigation and complete reading view, plus verified chapter and whole-Guide PDF/EPUB downloads generated from the same source revision.
- Assets resolve to the requested language or visibly labeled English fallback; unavailable variants are handled honestly, and all available resource languages remain discoverable.
- Documentation identifies license scope, contribution rules, and governance, and the required CI checks, Pages deployment, desktop smoke checks, and baseline accessibility checks pass.
- Responsive baseline behavior is required. Expanded device QA and additional interface languages can follow; PDF/EPUB exports are part of the early rights-gated Guide track rather than postponed until after multilingual rollout.

## 10. Reference links

- Original website: https://scrumprimer.org/
- Original repository: https://github.com/nerds-odd-e/scrumprimer
- Original overview license information: https://scrumprimer.org/overview
- Original anime license information: https://scrumprimer.org/anime
- Creative Commons BY-ND 3.0 Unported: https://creativecommons.org/licenses/by-nd/3.0/
- Creative Commons BY-NC-SA 4.0 International: https://creativecommons.org/licenses/by-nc-sa/4.0/
- GitHub — deploying a website automatically: https://docs.github.com/en/get-started/start-your-journey/deploying-your-website-automatically
- GitHub — licensing a repository: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- GitHub / Choose a License — no license: https://choosealicense.com/no-permission/
