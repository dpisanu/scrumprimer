# Project Governance

This repository is an independently maintained community proof of concept. It is not affiliated with or endorsed by the original Scrum Primer authors or maintainers. The project does not control the original website, its domain, or its content.

## Roles and responsibilities

- **Repository owner/administrators** manage repository settings, access, and releases. Administrative access does not confer copyright ownership over contributors' or third parties' work.
- **Maintainers** review issues and pull requests for scope, quality, accessibility, licensing, attribution, and provenance. They may request changes or decline contributions that do not meet project requirements.
- **Contributors** remain responsible for having the rights to submit their work and for providing required license confirmations, source information, and attribution.

The repository owner may invite additional maintainers as the project grows. No person is a maintainer solely by virtue of contributing.

## Decisions and changes

Use the [product backlog](docs/project/backlog.md) to track implementation work by story ID (`sp-N`). Record unresolved product or governance choices in [open decisions](docs/project/opendecisions.md). When a decision changes an enduring requirement, update the [project specification](docs/project/SPEC.md) and the related policy documents in the same reviewed change.

Changes to project-wide licensing, contribution terms, or governance must be explained in a pull request and reviewed before adoption. Do not treat an implementation change or repository setting as silently changing those policies.

## Contribution review

Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md) and the repository's pull request template. Maintainers review rights and provenance as well as technical quality. Unclear or disputed material must not be published while the concern is unresolved; maintainers may temporarily remove affected material while investigating.

For each pull request, the assigned reviewer should check that:

- The change identifies a backlog story or explains why no story applies, and stays within the stated scope.
- Relevant tests or validation are reported and are appropriate for the change.
- Required licensing and attribution confirmations are complete; sources, permissions, and content metadata are adequate for any new material.
- The change does not introduce unlicensed upstream text, publications, translations, or assets, or imply official affiliation.

Do not merge while required rights confirmations are missing or a material provenance concern remains unresolved. The repository's [CODEOWNERS](.github/CODEOWNERS) file identifies the current default reviewer; maintainers can update it when review ownership changes.

## Releases and future collaboration

The project may publish an independent GitHub Pages site after the specification's release requirements are met. Any proposal to collaborate with or transfer the project to the original maintainers is voluntary and requires a separate agreement. It does not by itself transfer contributors' copyrights or change previously granted licenses.
