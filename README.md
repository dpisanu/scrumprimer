# Scrum Primer — Independent Website Project

> **Project status:** Independent, community-driven proof of concept. This repository is not affiliated with, endorsed by, or maintained by the original Scrum Primer authors or the maintainers of [scrumprimer.org](https://scrumprimer.org/).

This project explores a maintainable, contribution-friendly static website for Scrum Primer using **Markdown as content**, **Hugo as the static site generator**, **GitHub Actions for validation and deployment**, and **GitHub Pages for hosting**.

The long-term aim is to demonstrate a working alternative that can be proposed to the original maintainers for voluntary adoption. Nothing here changes or replaces the original website.

## Project goals

- Create an independent English-first static website, with content managed as Markdown.
- Make proposed changes reviewable through issues and pull requests.
- Preserve transparent authorship, contributor attribution, content provenance, and licensing.
- Add responsive design, multilingual content, and document-export workflows in later phases.
- Link to the original PDFs and other publications rather than importing their files.

## Project status and roadmap

This repository begins with its governance and licensing documents. The website and build pipelines will be added incrementally.

1. **Foundation:** repository policies, static-site setup, build and deployment workflows.
2. **English website:** original or expressly authorized Markdown content, navigation, links, attribution, and independent GitHub Pages deployment.
3. **Mobile experience:** responsive layouts and accessible navigation.
4. **Multilingual support:** translation structure, translator credits, and contribution workflows.
5. **Exports:** PDF, EPUB, and other formats only for material we are entitled to reproduce and adapt.
6. **Upstream proposal:** invite the original maintainers to review and potentially adopt the work.

See the [project specification](docs/project/SPEC.md), [product backlog](docs/project/backlog.md), and [open decisions](docs/project/opendecisions.md).

Project policies: [governance](GOVERNANCE.md), [code of conduct](CODE_OF_CONDUCT.md), [copyright](COPYRIGHT.md), [content license](CONTENT_LICENSE.md), [attribution](ATTRIBUTION.md), and [third-party notices](THIRD_PARTY_NOTICES.md).

## Local Hugo validation

Install Hugo Extended at the exact version in [.hugo-version](.hugo-version). From the repository root, run:

```sh
hugo
```

Hugo writes generated files to `public/`, which is ignored by Git. Until the site layouts are added, Hugo warns that HTML templates are missing; the command currently validates the configuration and content setup rather than producing a complete website. The configured base URL targets the independent GitHub Pages project path; do not change it to `scrumprimer.org`.

## License scope — determined by repository path

This is a **multi-license repository**. The rules below identify the intended licenses of **original work contributed to this project**. They do **not** transfer rights in third-party material or upstream Scrum Primer content.

| Repository path | Applies to original, project-contributed work | License |
| --- | --- | --- |
| `content/**` | Editorial Markdown and website prose | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) |
| `i18n/**` | Translated user-interface strings | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) |
| `translations/**` | Authorized translations of project-licensed content | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) |
| `assets/editorial/**` | Original project-created diagrams and editorial artwork | [CC BY-NC-SA 4.0](CONTENT_LICENSE.md) |
| `static/third-party/**` | Separately licensed or permitted third-party material | **Its own license or permission**, recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) |
| **All other original project files** | Hugo templates, CSS, JavaScript, build scripts, GitHub Actions, configuration, README, development documentation, etc. | [MIT](LICENSE) |

**Short rule:** project-owned editorial content and translations = CC BY-NC-SA 4.0; project-owned code and all other project files = MIT; third-party material = its own license. **The repository path is not permission to relicense somebody else's work.**

Files with a verified, more specific license notice are exceptions and must be documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) or their own file. Place new third-party assets in `static/third-party/` rather than in a content or code directory, and preserve their required credits. Do not introduce ambiguous mixed-license files without splitting them or recording explicit per-file licensing and attribution.

**License summary:** CC BY-NC-SA 4.0 allows noncommercial sharing and adaptations with attribution and the required ShareAlike terms. MIT permits commercial reuse of the project's code. These terms are *not* an overall noncommercial restriction on the entire software repository.

**Original Scrum Primer prose, PDFs, pre-existing translations, and artwork are not automatically covered by either project license.** Existing PDFs and publications remain external links. Project-authored content must be original or documented as authorized for the intended license. See [CONTENT_LICENSE.md](CONTENT_LICENSE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

Contributors retain copyright in their own work and confirm the license appropriate to each changed path in their pull requests; no assignment of copyright is required. See [CONTRIBUTING.md](CONTRIBUTING.md).

### Original Scrum Primer and provenance

- Original website: [scrumprimer.org](https://scrumprimer.org/)
- Original source repository: [nerds-odd-e/scrumprimer](https://github.com/nerds-odd-e/scrumprimer)
- Scrum Primer publication authors (as identified by the upstream project): Pete Deemer, Gabrielle Benefield, Craig Larman, and Bas Vodde.

The original site welcomes contributions but does not thereby grant a clearly specified license for all of its prose. **Do not interpret the license declarations in this repository as permission to copy, adapt, or relicense that original prose.** Any inclusion of original third-party text requires an applicable license, permission, or other lawful basis and must be documented.

The original Overview and Anime illustration pages identify CC BY-ND 3.0; those images, if reused, remain under their **own** license and must not be represented as CC BY-NC-SA material. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Contributing

Contributions are welcome, especially:

- Original improvements to the website implementation and accessibility.
- Independently written or expressly authorized educational content.
- Translations of content we have the right to translate.
- License, attribution, and content-provenance corrections.

**Before opening a pull request, read [CONTRIBUTING.md](CONTRIBUTING.md) and include its required contribution-license confirmation in the PR description.**

## Hosting

The website is intended to run on an independent GitHub Pages project URL of the form:

`https://YOUR-GITHUB-USERNAME.github.io/scrumprimer/`

Replace `YOUR-GITHUB-USERNAME` with the repository owner's account name once the project is published. This is **not** the official `scrumprimer.org` domain.

## Governance and ownership

- Original contributors remain owners of the copyrights in their respective contributions.
- Maintainers review submissions for scope, quality, proper attribution, and licensing compatibility.
- No contribution grants the project ownership of the original Scrum Primer publication or website.
- Any proposed collaboration or adoption by upstream maintainers is voluntary and subject to their approval.

## Disclaimer

This project is independently maintained. References to Scrum Primer are for identification, context, and attribution; they do not imply endorsement or official status.
