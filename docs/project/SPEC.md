# Scrum Primer — Independent Content as Code Website Proposal

**Specification version:** 0.1  
**Status:** Planning draft — independent proof of concept  
**Proposed repository:** `https://github.com/<your-username>/scrumprimer` (not created by this specification)  
**Proposed preview site:** `https://<your-username>.github.io/scrumprimer/` (not deployed yet)  
**Upstream website:** https://scrumprimer.org/  
**Upstream repository:** https://github.com/nerds-odd-e/scrumprimer  
**Supersedes:** n.a.

## 1. Mission and collaboration model

Build an **independent, publicly inspectable static-site proof of concept** for the Scrum Primer English website, maintained in Markdown and automatically published from a new GitHub repository belonging to the project initiator. The implementation should make it easier to propose a collaborative, multilingual, transparently licensed content workflow to the current Scrum Primer maintainers.

The original [scrumprimer](scrumprimer.org) website, upstream GitHub repository, DNS configuration, and hosting stay **untouched**. There is **no implied endorsement, ownership, permission, or transfer** from the original Scrum Primer maintainers. A proposal for possible adoption comes **after** the proof of concept is complete.

### Non-negotiable boundaries

1. The **new repository** is independently owned and administrated by the initiator until and unless an explicitly agreed handover occurs.
2. **GitHub Pages project site**: host at `https://<your-username>.github.io/scrumprimer/`; do not configure `scrumprimer.org` as a custom domain or make changes to its DNS.
3. **Markdown is the editable source of truth** for new site pages, plus structured data for assets and external publication links.
4. **Original PDFs, EPUBs, MOBI files and original translated publications are not copied**, committed, converted, served, or bundled. The proof of concept may link to their **original hosted URLs** while those URLs remain available.
5. **Only qualifying illustrations explicitly labeled CC BY-ND 3.0** may be reused, unaltered, with the full required attribution and original source and license links.
6. **Do not copy the existing Ruby/ERB app, CSS, templates, fonts, or unspecified assets** into the new project as a shortcut. Create a fresh site implementation.
7. **Distinguish upstream content from new contributions**. The original website's footer says “This page is open source,” but no clear license for its English prose has been established. This is evidence of an invitation to contribute, **not a transferable license or permission to relicense**. See the publication gate in §8.
8. A visible notice will explain: **independent community migration proposal, not the official Scrum Primer website**.

## 2. Scope and phased roadmap

| Phase | Objective | In scope | Deferred |
|---|---|---|---|
| **0 — Repository foundation** | Set up the clean independent project and governance | Repository structure, Hugo build, Actions, GitHub Pages project URL, contribution and rights policies, provenance inventory | Official-site adoption, original-domain work |
| **1 — English baseline** | Demonstrate a complete English Markdown-driven static site | English home, overview, anime, about, contact; approved unchanged illustration assets; links to original externally hosted publications; basic navigation; contributor attribution; CI/CD | Translated pages, extensive mobile redesign, generating PDF/EPUB/MOBI |
| **2 — Mobile experience** | Make the new site excellent on mobile and tablet | Responsive layouts, navigation, artwork display, accessibility, performance checks | Translation and exports |
| **3 — Multilingual contribution system** | Add translation governance and locale-aware content | Localized Markdown and UI, language picker, translation status and review, contributor credits, `hreflang`, translation provenance | Assuming rights to reuse upstream translated files |
| **4 — Derived document exports** | Generate distributions from **appropriately licensed project Markdown** | Versioned PDF/EPUB builds and optional Kindle-compatible/MOBI strategy, publication metadata, export QA | Ingesting original Primer publications without explicit rights |
| **5 — Upstream proposal (after viable demo)** | Invite the original owners to review and optionally adopt the project | Demo, migration report, license/ownership explanation, transfer/fork/integration options | Presuming approval, domain control or forced cutover |

Phase 5 discussions can begin informally earlier, but **adoption is not a prerequisite for developing the independent technical proof of concept**. Public republication of third-party prose remains subject to the separate rights gate in §8.

### Planning and tracking documents

- **[Backlog](backlog.md)** — implementable work items, grouped by phase, each identified as `sp-N`; holds state and PR references. The backlog includes implementation tasks formerly mixed into the Phase 1 definition of done and later-phase design notes.
- **[Open decisions](opendecisions.md)** — decisions requiring an explicit choice, responsible parties, and a decision record. Factual rights and link verification are work items in the backlog, not decisions.
- **This specification** — durable scope, architecture, constraints, copyright boundaries, and release requirements. A task being marked Done does **not** waive these constraints.

### Cross-phase design constraints

- **Accessibility:** Phase 1 includes semantic HTML and baseline keyboard/screen-reader accessibility. Phase 2 expands responsive usability, touch targets, performance, and device testing; it does not postpone fundamental accessibility.
- **Localization:** Use stable `page_id` identifiers across language variants. New translations require authorization for adaptations of the source prose, appropriate translation rights, and translator credit. Do not translate labels embedded in CC BY-ND illustrations by modifying the original files.
- **Exports:** Only content with suitable export rights may produce new PDF/EPUB documents. Markdown remains the editorial source of truth, and export builds belong in a separate workflow. The original upstream publications remain external. PDF/EPUB are the initial target formats; legacy MOBI is optional pending a use-case decision.
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
- **No runtime backend, database, analytics tracker, translation service, or document converter** is needed for Phase 1.

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
│       └── contact.md
├── layouts/                         # Original Hugo layouts/partials
├── assets/                          # New CSS and optional JavaScript
├── static/
│   └── images/                      # Only rights-reviewed artwork
├── data/
│   ├── publications.yaml            # Links to *external* originals
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

**Note:** The proposed structure anticipates language-specific content from day one. Configure Hugo's English content directory as `content/en` while retaining English routes at `/scrumprimer/...` without introducing a premature `/en/` prefix. Phase 3 can add additional language content directories without moving the English files.

## 5. Phase 1 — English website content

### 5.1 Page inventory and proposed navigation

| Upstream page | New project-site URL (relative to `/scrumprimer/`) | Source file | Notes |
|---|---|---|---|
| Home (`/`, `/home`) | `/` | `content/en/_index.md` | New English landing page; external original-publication links |
| `/overview` | `/overview/` | `content/en/overview.md` | Unmodified, rights-reviewed overview illustration |
| `/anime` | `/anime/` | `content/en/anime.md` | Unmodified, rights-reviewed anime illustration(s) |
| `/about` | `/about/` | `content/en/about.md` | Upstream credits, independent-project disclosure |
| `/contact` | `/contact/` | `content/en/contact.md` | Contact link points to the new repository for contributions; do not impersonate the upstream owners |
| `/translations` | Not required for Phase 1 | — | Add real translation features in Phase 3; optional future-roadmap notice elsewhere |

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
- `origin` distinguishes `upstream-website`, `original-project`, and future contributor-supplied content.
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

## 6. Illustration rights and attribution

Reuse only the specific original images for which a source-page notice **actually confirms** CC BY-ND 3.0 coverage. This does **not** imply blanket coverage of logos, templates, fonts, supplementary artwork, book contents, or translations.

Per image, record:

- Upstream page URL and original asset URL;
- Creator/attribution party and copyright notice, where supplied;
- Exact Creative Commons version and canonical license link;
- Original filename, checksum, date reviewed, and no-modification status;
- Attribution rendered on the published page or linked attribution page.

Images must remain unaltered: no translated labels, cropping that creates an adaptation, redrawing, recoloring or repackaging as a derivative. Responsive **display sizing** is permitted; avoid modifications of the source asset. Preserve any creator and copyright notices and do not suggest endorsement.

Suggested rights record:

```yaml
assets:
  - id: overview-image
    path: "/images/overview-original.png"
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

### 7.1 Proposed licensing model (recommendation, not adopted yet)

| Material | Proposed license/policy | Who has authority? |
|---|---|---|
| Newly written Hugo templates, CSS, JS and other project code | **MIT** (or another explicit OSI-approved software license) in `LICENSE` | Authors of that code |
| Newly authored website prose and new project documentation | **CC BY 4.0** recommended in `CONTENT_LICENSE.md` | The respective prose authors; only content they can legally license |
| Reused original Scrum Primer overview and anime illustrations | **CC BY-ND 3.0**, unmodified, separately attributed | Existing creators/licensors; cannot be relicensed by this project |
| Original English upstream website prose | **Unverified / not sublicensable by this project** until permission/license is established | Upstream copyright holders |
| Original PDFs / EPUBs / MOBI files | **External links only**; not present in repository | Upstream rights holders |
| Future translations | Rights to translation and to publication must be confirmed; record individual translator credits and license | Original prose rights holders + translators as applicable |

**CC BY 4.0** for new prose is offered as a permissive, attribution-based option facilitating translations and revisions. Alternatives such as CC BY-SA 4.0 should be chosen consciously. **Do not** place a blanket CC BY statement in the footer or README that could be read as licensing upstream content or CC BY-ND artwork. Note also that **CC BY-ND images are not freely adaptable** and should not be described as open source software assets.

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

The upstream footer's **“This page is open source”** message and invitation to contribute do not identify a legally definite license for the page text. The project initiator has expressed the working assumption that the English website prose can be transferred to Markdown. Record that assumption transparently, but **do not convert it into a claim of legal permission**, nor attach the new CC BY content license to that inherited prose.

**Practical two-stage policy:**

1. **Development/prototyping:** build the page structure, front matter, navigation, templates, illustration attribution and link inventory. Prepare content mappings and Markdown drafts, recognizing that copying upstream text is still a copyright-sensitive act; restrict any unlicensed drafts appropriately.
2. **Public Pages publication:** only include upstream paragraphs if their reproduction/publication is authorized, or replace them with independently authored text that does not merely paraphrase protected expression. Link and cite the original site rather than reproducing text where permission remains unclear.

A GitHub repository being public is **not** evidence that all its contents can be republished or re-licensed. The **public-release acceptance criteria** require a rights decision for each page. A demo with an original layout and permission-safe placeholder or newly created text can still prove the architecture while authorization is pending.

This is a risk control rather than a claim that the original site is inaccessible or that the migration must cease. Resolve prose rights with the original maintainers before publishing substantial copied content, especially because the new proof of concept is separately operated.

## 9. CI/CD, quality gates and deployment

### 9.1 Pull-request checks

- Markdown style and front-matter schema validation (`title`, `page_id`, `lang`, `origin`, `rights_status`).
- Build Hugo with an explicitly pinned version and English config.
- Validate expected pages at `/scrumprimer/`, `/scrumprimer/overview/`, `/scrumprimer/anime/`, `/scrumprimer/about/`, `/scrumprimer/contact/`.
- Check navigation links, canonical URLs, assets, and sitemap for the **GitHub Pages project-path prefix**.
- Check external URLs when feasible, with handling for occasional upstream outages; no fake “verified” results.
- In Phases 0–3, reject `.pdf`, `.epub`, `.mobi` publication binaries in the repository/site output. In Phase 4, explicitly allow only rights-cleared **newly generated exports** in a separate configured pipeline; never copy or redistribute original upstream binaries.
- Check that all included third-party images have approved, complete provenance and attribution data.
- Reject placeholder publication URLs in a release build.
- Ensure there is no blanket declaration that all content or assets share a single license.
- Run basic HTML accessibility, semantics and desktop smoke checks; expanded mobile work is Phase 2.

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
- The English home, overview, anime, about, and contact pages render at the project-site paths and are maintained through Markdown rather than a server-side application.
- The rights status of **every published page** is resolved for public use, without presenting unlicensed upstream prose as newly CC-licensed work. Source attribution and ownership information remain visible and accurate.
- Every redistributed third-party image has recorded permission/provenance and required attribution, and its source artwork is unchanged.
- No original PDF, EPUB, MOBI, or translated-publication binary is committed or deployed. Publication links point only to checked external destinations, with no invented replacements.
- Documentation identifies license scope, contribution rules, and governance, and the required CI checks, Pages deployment, desktop smoke checks, and baseline accessibility checks pass.
- Mobile enhancement, multilingual release, and new document exports are **not** Phase 1 release blockers. They are recorded under later phases in [backlog.md](backlog.md).

## 10. Reference links

- Original website: https://scrumprimer.org/
- Original repository: https://github.com/nerds-odd-e/scrumprimer
- Original overview license information: https://scrumprimer.org/overview
- Original anime license information: https://scrumprimer.org/anime
- Creative Commons BY-ND 3.0 Unported: https://creativecommons.org/licenses/by-nd/3.0/
- Creative Commons BY 4.0 International: https://creativecommons.org/licenses/by/4.0/
- GitHub — deploying a website automatically: https://docs.github.com/en/get-started/start-your-journey/deploying-your-website-automatically
- GitHub — licensing a repository: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- GitHub / Choose a License — no license: https://choosealicense.com/no-permission/

---

**Version 0.5 change summary:** Extracts the former §10 definition of done into implementation stories plus release invariants; extracts actionable Phase 2–5 work from former §11 while retaining cross-phase requirements in §2; moves former §12 choices to [opendecisions.md](opendecisions.md), with factual verification tracked in [backlog.md](backlog.md). Story IDs are stable and follow `sp-N`. The independently hosted proof-of-concept and rights model are unchanged.
