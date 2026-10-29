# Content and Asset Rights Policy

This policy defines the provenance inventory and rights/front-matter checks for `sp-7`. It implements the requirements in [SPEC.md](SPEC.md#6-illustration-rights-and-attribution), [CONTENT_LICENSE.md](../../CONTENT_LICENSE.md), and [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md). It does not grant rights or change the project's licenses.

## Inventory coverage

[data/rights.yaml](../../data/rights.yaml) is the structured inventory of local editorial Markdown and editorial or third-party assets. Use one record per file, including draft or unapproved files. Code, configuration, and project documentation retain the MIT scope described in [README.md](../../README.md); they do not need individual records here.

Keep the inventory synchronized with content front matter and the human-readable third-party notices when adding, modifying, moving, or removing files. Paths are repository-relative, use forward slashes, and must identify an existing file without `..` segments. IDs and paths must be unique across the inventory; content `page_id` values must be unique within each language.

The current inventory contains the original English landing-page copy and the owner's AI-assisted logo, both contributed under CC BY-NC-SA 4.0. Their publication approval and the owner's declarations are documented in the [landing-page permission record](landing-page-permission.md). Original publication binaries and upstream translations remain external; their download links belong in `data/publications.yaml` when `sp-15` is implemented.

## Content records and front matter

Every Markdown page must have YAML front matter containing nonempty strings for `title`, `page_id`, `lang`, `origin`, and `rights_status`. Use stable lowercase, hyphen-separated `page_id` identifiers across locales. English pages use `lang: en` in the initial phase.

Each inventory content record contains:

| Field | Validation policy |
| --- | --- |
| `id`, `path` | Unique inventory identifier and repository-relative Markdown path. |
| `page_id`, `lang`, `origin`, `rights_status` | Must agree with the page's front matter. |
| `authors`, `translators` | Lists of actual attribution names; preserve prior credits. `authors` must be nonempty for approved editorial content. `translators` must be nonempty for an approved translation. |
| `license` | Exact license identifier when verified, otherwise `null`. Never infer a third-party license from its directory. |
| `source_url`, `based_on` | Actual source URL and underlying-work reference when applicable; otherwise `null`. |
| `changes` | Nonempty description of original work or modifications, including translation. |
| `permission_reference` | Reference to documented permission when relying on a specific grant; otherwise `null`. Do not commit private correspondence or personal data as evidence. |
| `reviewed_by`, `last_reviewed` | Actual reviewer and ISO date (`YYYY-MM-DD`) of rights review; `null` until reviewed. |
| `approved_for_publication` | Boolean, initially `false`. Approval requires the evidence below, not merely a status label. |
| `notes` | Unresolved questions or other context; must not substitute for evidence. |

Approved editorial pages also carry `authors`, `license`, `source_url`, `based_on`, and `changes` in front matter, consistent with the inventory. Authorized translations additionally record `translators` and `translation_of`, the underlying work's author(s), and the underlying license or permission. Preserve source credits and modification notices.

## Origins and rights status

`origin` identifies provenance: `original-project` for independently authored contributions, `upstream-website` for material from the original site, and `third-party` for other externally sourced work. A contributor's independently authored work is still `original-project`; authorship is recorded separately.

| `rights_status` | Meaning | Eligible for approval? |
| --- | --- | --- |
| `original-project` | Project-origin work or scaffold; authorship and license still require review. Retains the existing scaffold's status without asserting clearance. | Only with documented authorship and the applicable project license. |
| `permission-unverified` | Reuse rights have not been established. | No. |
| `license-verified` | An applicable third-party license has been verified for the intended use. | Only with complete source, license, attribution, and review evidence. |
| `permission-granted` | A specific permission grant has been verified for the intended use. | Only with a permission reference and its conditions documented. |
| `restricted` | The intended publication or adaptation is not permitted, or a rights dispute is unresolved. | No. |

Unknown origins/statuses, malformed field types, missing required keys, duplicate IDs, nonexistent paths, or metadata disagreements are validation failures. Unreviewed inventory entries may retain `null` evidence fields and empty credit lists only while `approved_for_publication` is `false`; this is not permission to commit unlicensed material.

## Asset records

The `assets` list is empty until files are imported. Future records require `id`, `path`, `origin`, `rights_status`, `title`, `authors`, `source_page`, `asset_url`, `license`, `license_url`, `copyright_notice`, `attribution`, `unchanged`, `checksum_sha256`, `permission_reference`, `reviewed_by`, `last_reviewed`, and `approved_for_publication`.

Use the content-record rules for shared fields. For externally sourced assets, `source_page`, `asset_url`, and `license_url` identify the actual public sources and exact license version; use `null` while unverified. Original project artwork may use `null` source URLs but must identify its creators and applicable license. `copyright_notice` preserves any supplied notice; do not invent one. `attribution` contains the required display credit. `unchanged` is a boolean, and `checksum_sha256` must match the imported file's SHA-256 digest before approval.

Place imported third-party assets in `static/third-party/` and record their credits in [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md). Qualifying upstream illustrations retain CC BY-ND 3.0, require `unchanged: true`, and must not be cropped, translated, redrawn, or relicensed. Original project artwork in `assets/editorial/` retains its applicable project license and actual creator credit.

## Publication gate and review

Approval requires a maintainer to verify actual authorship, source, applicable license or permission, intended use, required credits, modification notices, and review details. Translations also require adaptation rights. Assets require matching checksums and verified attribution; CC BY-ND assets must remain unchanged.

Scaffolds and unresolved records are not release-ready. `permission-unverified` and `restricted` material must not be published, and an approval flag cannot override those restrictions. The project's CC BY-NC-SA 4.0 policy never relicenses upstream prose or third-party artwork.

## Validation responsibility

The existing [site validator](../../scripts/validate_site.py) checks the initial required front-matter fields and page IDs, but does not yet enforce this complete inventory policy or publication approval. For now, maintainers review these requirements with the mandatory [contribution confirmation](../../CONTRIBUTING.md#3-required-pull-request-license-confirmation).

`sp-14` verifies and imports qualifying artwork. `sp-17` implements the release checks against this policy, including content/asset metadata, forbidden publication binaries, and placeholder publication URLs. Do not treat the current CI result as rights clearance.
