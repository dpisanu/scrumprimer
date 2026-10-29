# Contributing to the Independent Scrum Primer Website

Thank you for considering a contribution. This project aims to be collaborative while preserving **clear copyright ownership, a predictable license for each type of contribution, and reliable attribution**.

**Before submitting a pull request, read this document and complete the required licensing and attribution checklist in the [pull request template](.github/PULL_REQUEST_TEMPLATE.md).** Maintainers will not merge a pull request with an incomplete confirmation or unclear ownership, licensing, or provenance.

## 1. License scope: choose the right directory

The repository has a **directory-based license policy**. For work you authored and have the right to license:

| Where the contribution goes | Required license | Typical contribution |
| --- | --- | --- |
| `content/**` | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) | Markdown pages, editorial text |
| `i18n/**` | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) | Interface translations |
| `translations/**` | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) | Authorized translations of project content |
| `assets/editorial/**` | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) | Original editorial diagrams or artwork |
| `static/third-party/**` | **Existing third-party license/permission** | Licensed external illustrations or assets, with verified attribution |
| All other original project files | [MIT](LICENSE) | Hugo templates, scripts, CSS, JavaScript, workflows, development documentation |

The **folder does not change the legal rights in imported material**. Contributors must have authority to provide original contributions under the corresponding project license, and must not add third-party or upstream work without reviewing and documenting its existing rights. Avoid mixing third-party assets or CC content into MIT code files. If unsure, open an issue before submitting.

**MIT allows commercial use of code.** Your CC BY-NC-SA contributions are noncommercial-licensed, but that condition does not extend to MIT code. Details and exceptions are in [README.md](README.md), [CONTENT_LICENSE.md](CONTENT_LICENSE.md), and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## 2. Contributor rights and licensing agreement

By submitting a pull request and completing the required confirmation in its template, you certify that:

1. **You have the right to contribute.** Your work is your own, or you have identified and documented all third-party material and have the rights needed to submit it under the stated terms.
2. **You retain copyright.** You are not assigning your copyright to the project, its owner, or its maintainers.
3. **You grant the appropriate license for your contribution:**
   - For original contributions to MIT-scoped paths (code, templates, scripts, software and project documentation), you license your contribution under the **MIT License** in [LICENSE](LICENSE).
   - For original contributions in `content/`, `i18n/`, `translations/`, and `assets/editorial/`, you license your contribution under **Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International (CC BY-NC-SA 4.0)** as described in [CONTENT_LICENSE.md](CONTENT_LICENSE.md).
4. **You allow redistribution under these licenses.** Accepted contributions can be published and reused under the applicable license, including by future maintainers of this independent project. You understand that these licenses are generally irrevocable for compliant recipients.
5. **You provide accurate provenance and attribution.** You identify authors, translators, sources, changes, and relevant permissions; you do not present third-party material as your own.
6. **You understand this is independent.** Contribution does not imply endorsement by the original Scrum Primer authors or permission to copy material from their website or publications.

**There is no separate copyright assignment or Contributor License Agreement (CLA) in this initial policy.** Instead, contributions are accepted under the project's existing outbound licenses (“inbound = outbound”). The PR confirmation records your affirmative agreement to those terms.

## 3. Required pull-request license confirmation

Every pull request must use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) and complete its **Licensing and attribution confirmation** section. Select every applicable contribution type and check each certification. For a change with no original copyrightable material, select that option and explain why. Maintainers must request completion or clarification before merging a pull request with an incomplete checklist or unclear rights.

The contributor must make the confirmation; it must not be completed on their behalf. The template makes this requirement visible at submission. It is a review requirement and is not currently enforced by an automated check.

## 4. Content attribution requirements

Each original editorial Markdown file should include YAML front matter with at least its author(s), language, and license. For example:

```yaml
---
title: "A Scrum Topic"
lang: "en"
authors:
  - "Your Name or Chosen Attribution Name"
license: "CC-BY-NC-SA-4.0"
source_url: null
based_on: null
changes: "Original work for this project"
---
```

For translations, provide *both* author and translator credits, original source information, and any required change notices:

```yaml
---
title: "Translated Topic Title"
lang: "de"
authors:
  - "Original Contributor"
translators:
  - "Translator Name"
license: "CC-BY-NC-SA-4.0"
translation_of: "content/en/topic.md"
source_url: "https://example.org/permitted-source"
changes: "German translation of an authorized CC BY-NC-SA 4.0 work"
---
```

Replace these examples with real names and genuine sources. Record additional rights or permission details in the PR or file metadata where needed. For additions to existing pages, preserve prior authors and change notices; do not overwrite earlier attribution.

For editorial content or assets, add or update the corresponding record in [data/rights.yaml](data/rights.yaml). Follow the [rights-status and front-matter policy](docs/project/rights-policy.md) and keep the record consistent with page metadata and third-party notices. Leave publication approval false until a maintainer has verified the required rights evidence.

### Important rules for translations and upstream material

- A **translation is normally an adaptation**. The translator's new copyright does not eliminate rights in the source text.
- Translate only source content that is properly licensed or for which the required permissions have been obtained.
- Do not import or translate the original Scrum Primer website prose, Primer PDFs, or existing upstream translations solely because the website says it is “open source.” First document the relevant right to reproduce or adapt that material.
- Do not treat CC BY-ND 3.0 illustrations as available for modification or relicensing. If you want to use an original illustration unchanged, verify and document all applicable conditions in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- If permission or compatibility is uncertain, raise an issue before investing time in the contribution.

## 5. Code conventions and licensing markers

- Favor readable, maintainable code and small, reviewable changes.
- For new source files that support comments, include an SPDX marker when practical, e.g. `SPDX-License-Identifier: MIT`.
- Do not copy code from another project without verifying that its license allows use and documenting any required attribution or notices.
- Add or update tests and documentation when behavior changes.

## 6. Contribution workflow

1. Search existing issues and the backlog before starting; open an issue for substantial or potentially contentious work.
2. Fork the repository or create a branch, and make a focused change.
3. Put files in the license-appropriate directories; add required authorship, SPDX or Markdown license metadata, and third-party notices.
4. Run relevant validation or tests, when available.
5. Open a pull request explaining the change, the associated story or issue (e.g. `sp-12`), and any affected pages.
6. **Complete the licensing and attribution confirmation in the [pull request template](.github/PULL_REQUEST_TEMPLATE.md).**
7. Respond to reviewer questions, especially about rights, source material, accessibility, and documentation.

The project reserves the right to decline changes that cannot be distributed under the stated licenses or that have insufficient rights documentation.

## 7. Copyright, attribution, and governance

Authors retain copyright in their original work. Git commits and GitHub history help preserve contribution provenance, but **they do not replace explicit copyright and attribution metadata** where required. The maintainers may maintain supplementary credits for work that cannot be adequately credited in a page footer.

The project is independently maintained. If the original Scrum Primer maintainers later choose to adopt or collaborate on the project, existing contributions remain licensed under their originally granted terms; no new organization automatically acquires ownership of those contributions.

## 8. Questions or possible license violations

Open an issue before posting material when the rights are unclear. For suspected copyright or attribution problems, identify the specific file, original source, creator, and concern so maintainers can investigate and, when necessary, remove the material pending review.
