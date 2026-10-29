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

### OD-3 — Publication route for upstream English prose

- **Question:** For which original English website pages is republication permission established? For any remaining pages, use new independently authored text or limit the public site to an architectural demo pending permission?
- **Current position:** The original “This page is open source” notice does not itself identify a license. No copied prose can be relicensed by this project without authority.
- **Needed by:** Publishing each English page (`sp-9`–`sp-13`) and Phase 1 public-release acceptance.
- **Decision:** Open; **publication gate** under specification §8.

### OD-4 — Optional translations information page

- **Question:** Should the English site include a `/translations/` roadmap/information page before Phase 3, without offering translated content?
- **Current position:** Not required for Phase 1.
- **Needed by:** Final Phase 1 navigation and scope (`sp-8`, `sp-19`) if included.
- **Decision:** Open; default is **defer**.

## Phase 4 — Exports

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

## Decision log

No decisions have yet been formally recorded in this document. Once made, move the relevant entry to a `Resolved decisions` section while retaining its identifier, outcome, rationale, date, and reference URL. Keep consequential design constraints synchronized in the specification and implementation work tracked in the backlog.
