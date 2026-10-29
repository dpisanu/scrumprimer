# Scrum Primer — Open Decisions

**Date:** 2026-10-29  
**Specification:** [Scrum Primer Migration Specification](SPEC.md)<br>
**Backlog:** [backlog.md](backlog.md)

This register contains **choices that need an explicit decision**, not tasks to implement already agreed requirements. Until a decision is recorded, the specification's existing guardrails apply. Record each outcome with the decision, rationale, date, and (when available) issue or PR link; do not silently change policy by editing a story.

## Phase 0 — Foundation and governance

### OD-1 — Repository owner and long-term home

- **Question:** Which GitHub account and repository name will host the proof of concept, and should community-organization ownership be a later goal?
- **Current position:** Independent repository under the initiator's account; suggested name `scrumprimer`.
- **Needed by:** Publication of the first Pages deployment (`sp-1`, `sp-4`).
- **Decision:** Open.

### OD-2 — Licenses for newly authored contributions

- **Question:** How will contributor acknowledgement be captured (e.g., PR confirmation vs. DCO sign-off)?
- **Current position:** Project-authored code and project documentation use MIT; original project content in the designated content paths and authorized translations use CC BY-NC-SA 4.0. These licenses do not apply automatically to upstream website text or CC BY-ND illustrations.
- **Needed by:** Publishing contribution and license policies (`sp-5`, `sp-6`).
- **Decision:** Open.

## Phase 1 — English release

### OD-3 — Publication route while upstream rights are unresolved

- **Question:** If Guide reproduction, conversion, translation or export rights cannot be established, retain external-only Guide links indefinitely or pursue a separately scoped independently authored publication?
- **Current position:** Ship a permission-safe resource baseline and prototype technical Guide features with independent test content. Do not copy or relicense upstream prose without authority. Investigating the actual rights is verification work in `sp-37`, not a policy choice.
- **Needed by:** Actual Guide conversion/publication (`sp-40`) and full Guide-track acceptance (`sp-19`); not required to develop safe technical fixtures.
- **Decision:** Open; **publication gate** under specification §8.

### OD-4 — Optional standalone translations information page

- **Question:** Beyond required all-language resource discovery, is a separate translation-status/contribution page useful?
- **Current position:** An optional information page is not a substitute for accessing existing resource-language variants; that access is required in `sp-36`, even with an English-only interface.
- **Needed by:** Information architecture (`sp-35`) if included.
- **Decision:** Open; default is **defer**.

## Distribution extensions

### OD-5 — Legacy MOBI distribution

- **Question:** Is there sufficient demand or a required distribution target for legacy MOBI generation, as opposed to PDF and EPUB/modern Kindle-compatible approaches?
- **Current position:** Optional; do not implement by default.
- **Needed by:** `sp-32`.
- **Decision:** Open; default is **omit**.

## Phase 5 — Proposal for adoption

### OD-6 — What qualifies as a proposal-ready proof of concept?

- **Question:** What evidence must be complete before formally inviting the upstream maintainers to adopt or collaborate: English baseline only, mobile improvements, translations prototype, export demo, verified rights matrix, or other criteria?
- **Current position:** At minimum, a working English project-site demo, documented editorial workflow, provenance/license status, and known limitations; adoption remains voluntary.
- **Needed by:** `sp-33`, `sp-34`.
- **Decision:** Open.

## Reclassified from the previous specification (verification, not decisions)

The following items were in old §12, but they have discoverable answers rather than being policy choices. They are therefore tracked as actionable stories in [backlog.md](backlog.md):

- **Original illustration coverage and attributions:** Verify specific image files, authors, license notices and hashes in `sp-14`; retain the CC BY-ND limitations from specification §6.
- **Original English publication destinations:** Identify and check actual external PDF/EPUB download URLs in `sp-15`; do not mirror original binaries.
- **Guide reuse rights:** Verify actual reproduction, conversion, adaptation, translation and export permissions per edition in `sp-37`; clear author credits alone are not authorization.
- **Reported language availability:** Verify the initial language checklist in specification §5.6 through `sp-14`/`sp-15`, including Chinese script distinctions and actual format availability.

## Additional locale and publication decisions

### OD-7 — Missing website-page and chapter translations

- **Question:** For a missing translated page/chapter, link explicitly to English, display a labeled English reading fallback, or show an unavailable/translation-needed view?
- **Current position:** Asset selection is already specified as requested language then visibly labeled English, with an unavailable state if neither exists. Do not assume this settles page/chapter navigation, or silently present English as translated content.
- **Needed by:** `sp-25` and the multilingual reading pilot (`sp-28`).
- **Decision:** Open.

## Resolved decisions

### OD-8 — Initial Guide export formats and edition completeness

- **Decision:** PDF and EPUB are the initial chapter and whole-Guide formats. Generate downloads at build time and deploy them with matching pages; no on-demand conversion backend. Publish whole-Guide downloads only for complete reviewed editions in the advertised language, not silent mixtures of English and translated chapters.
- **Rationale:** Reuse one ordered Markdown source, keep downloads predictable and static, and avoid misleading readers about translation completeness.
- **Date:** 2026-10-29.
- **Reference:** Project-owner approval of the specification/backlog alignment in this conversation; no issue or PR reference recorded yet.
- **Implementation:** `sp-29`–`sp-31`, `sp-38`, `sp-41`. Legacy MOBI remains open under OD-5.

## Decision log

Record future outcomes in `Resolved decisions`, retaining the identifier, outcome, rationale, date, and reference URL when available. OD-1 and OD-2 remain open as explicitly requested. Keep consequential design constraints synchronized in the specification and implementation work tracked in the backlog.
