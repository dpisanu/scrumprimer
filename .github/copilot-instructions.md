# Project Guidelines

## Architecture
- Treat Markdown as the source of truth for site content. Use Hugo for static-site generation, GitHub Actions for validation and deployment, and GitHub Pages for hosting, as specified in [the project specification](../docs/project/SPEC.md).
- Keep the implementation independent of the original Scrum Primer site. Do not copy its application, templates, prose, or publications; link to original publications unless rights are documented.

## Changes and workflow
- Before implementation, identify the relevant `sp-N` story in the [product backlog](../docs/project/backlog.md). Keep the change within that story, and update the backlog state as work progresses or completes.
- Prefer small, focused, reviewable changes. Follow existing patterns and avoid unnecessary dependencies or architectural complexity.
- Use readable, consistent Markdown, YAML, Hugo templates, and code. Document behavior or workflow changes where appropriate; keep detailed policy in the project documents rather than duplicating it here.

## Licensing and attribution
- Follow the path-based license scope in [README](../README.md), [CONTENT_LICENSE](../CONTENT_LICENSE.md), and [CONTRIBUTING](../CONTRIBUTING.md): project code and general project files are MIT; original project content in designated paths is CC BY-NC-SA 4.0; third-party material retains its own terms.
- Never infer permission from a file's location or an upstream “open source” notice. Verify and record provenance, license or permission, authorship, attribution, and changes as required by [third-party notices](../THIRD_PARTY_NOTICES.md).
- Do not publish upstream prose, translations, or publication files without appropriate rights. Keep qualifying CC BY-ND artwork unmodified and separately attributed.

## Validation
- Run the smallest relevant checks for each change. For site or workflow changes, build with the configured Hugo version and run applicable tests or CI validations; verify project-path URLs and expected routes when affected.
- For content changes, validate front matter, rights status, attribution, links, and rendering. Do not claim checks passed unless they were run.
- Report validation performed and any limitations in the change summary.
