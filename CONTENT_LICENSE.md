# License for Original Website Content and Authorized Translations

**Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International (CC BY-NC-SA 4.0)**

- License summary: <https://creativecommons.org/licenses/by-nc-sa/4.0/>
- **Full, controlling legal code:** <https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en>
- SPDX identifier: `CC-BY-NC-SA-4.0`

## Scope: directory-based licensing

For **original material contributed to this project by people authorized to license it**, CC BY-NC-SA 4.0 applies to the following paths, unless a file carries a verified, explicit exception:

- `content/**` — editorial Markdown and website prose.
- `i18n/**` — translated interface text.
- `translations/**` — authorized translations of project-licensed content.
- `assets/editorial/**` — original project-created diagrams and editorial artwork.

**Original project-created files outside these paths are MIT-licensed** under [LICENSE](LICENSE), unless their own valid license notice specifies otherwise. This includes templates, source code, tests, scripts, Hugo configuration, GitHub Actions, and software/project documentation. Do not treat this CC license as applying to the site's implementation code.

**Third-party and upstream exceptions override directory defaults.** No file becomes CC BY-NC-SA solely by being stored in one of the folders above. Material that belongs to the original Scrum Primer authors or other third parties must have verified permission for the intended distribution and adaptations, be explicitly identified, and retain its existing rights and license. For externally licensed assets, use `static/third-party/` and record the details in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Material without sufficient authorization must not be copied into this repository.

This project does **not** claim ownership of, or relicense, the upstream Scrum Primer prose, original illustrations, PDFs, EPUBs, or pre-existing translations. Translation is generally an adaptation: a translator cannot license the underlying work on behalf of the original author.

For a quick lookup of all paths and exceptions, see the **License scope** table in [README.md](README.md).

## What CC BY-NC-SA 4.0 permits and requires

For content actually covered by this license, users may:

- **Share** the content in any medium or format for noncommercial purposes.
- **Adapt** the content, including rewriting and translation, for noncommercial purposes.

When sharing such content or adaptations, users must follow the license terms, including:

1. **Attribution (BY):** give appropriate credit, retain supplied copyright and attribution notices, link to the license and source where reasonably practicable, and indicate modifications.
2. **NonCommercial (NC):** uses primarily intended for or directed toward commercial advantage or monetary compensation are outside the license grant. Commercial permission must be obtained from the relevant rights holder(s).
3. **ShareAlike (SA):** if you share adapted material, your contributions to the adaptation must use the same CC BY-NC-SA license elements (subject to the precise license terms and permitted compatible versions/licenses).
4. **No additional restrictions:** do not apply extra legal or technological restrictions that prevent others from using the material as the CC license allows.

These are explanatory notes. If anything here differs from the legal code, **the Creative Commons legal code controls**.

## Attribution and metadata for each content file

New Markdown content should include front matter identifying the actual authors and licensing status. Example:

```yaml
---
title: "Introduction to Scrum"
lang: "en"
authors:
  - "Contributor Name"
license: "CC-BY-NC-SA-4.0"
source_url: null
based_on: null
changes: "Original content created for this project"
---
```

For an authorized translation, also record the language, translator(s), original work and author(s), source URL, underlying-work license or permission, and the nature of any changes. Attribute upstream creators as well as the translator; a translator cannot replace the original author's credit.

Do not fill in invented author names or license assertions. If provenance or permission is unclear, open an issue and do not merge the content until it has been resolved.

## Copyright and contributor consent

Each contributor **keeps copyright** in their original contribution while granting the public the permissions set out in CC BY-NC-SA 4.0. Contributors confirm this license grant in their pull request as described in [CONTRIBUTING.md](CONTRIBUTING.md). There is no automatic transfer of ownership to the project or its maintainers.

The license grant is limited to rights the contributor can lawfully grant. It does not override third-party rights.
