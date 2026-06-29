# Academic / Non-Commercial Free Licence Page — Design

**Date:** 2026-06-29
**Site:** JG Systems Consulting Labs (`labs.jgsystemsconsulting.com`, served from `docs/`)
**Status:** Approved design, pending implementation plan

## Goal

Give academics a clear, dedicated page that tells them the JGSC pro tooling is
**free for non-commercial academic use**, explains *why* we offer it, *who*
qualifies, *how* to request it, and politely *asks* (does not require) that they
cite the work. Today this possibility is only buried in licensing copy; many
eligible users won't know they can ask. This page makes it explicit and
shareable with universities.

## Non-goals

- No change to the commercial licensing model or pricing.
- No new build tooling, CSS files, or frameworks — stay single-file like the rest of the site.
- No legal contract drafting; this is marketing/request copy, not the licence text itself.
- Citation is **requested, not enforced** — no gating mechanism.

## Architecture

A new standalone page `docs/academic.html`, created by copying the structure,
inline `<style>` block, masthead, and footer from `docs/licensing.html`. Same
single-file static pattern, same design tokens (`--ink`, `--line`, `--mono`,
etc.), same "classified document" aesthetic and `§ NN` section numbering. No
shared assets beyond the already-shared `fonts/`, `favicon.svg`, `og.png`.

Plus light discoverability edits to `docs/index.html` and `docs/licensing.html`.

### Why this approach

The site has no templating layer — each page inlines its own CSS. Copying
`licensing.html` is the established pattern and guarantees visual consistency
with zero new infrastructure. The academic request reuses the **proven Formspree
endpoint** (`mjgqrjpa`) that already delivers to `support@jgsystemsconsulting.com`,
so no new form setup or delivery risk.

## Page content — `academic.html`

Metadata: `<title>Academic Licence — JG Systems Consulting Labs</title>`,
canonical `https://labs.jgsystemsconsulting.com/academic.html`, matching OG/Twitter
tags, `DOC-ID: JGSC-WEB-003`, `REV 0.1.0`.

Sections (following the existing `§ NN` pattern):

- **§ 00 — ACADEMIC / NON-COMMERCIAL** (hero)
  Headline: "Free for academia." One paragraph: the JGSC pro tooling — the
  write-tier pro JARs and pro skills — is free for non-commercial academic use.
  Buttons: `Request access →` (anchor to `#request`) and `Back to licensing →`
  (`licensing.html`).

- **§ 01 — WHY WE DO THIS** (rationale)
  Warm, honest framing with no commercial subtext: we want to support the
  academic community, grow the use of AI in MBSE, and get these capabilities into
  the hands of students and researchers. States plainly that academics often
  don't realise they can simply ask — so: just ask.

- **§ 02 — WHO QUALIFIES** (eligibility)
  3-cell `.grid.grid-3`:
  - *Students* — undergrad, master's, PhD; coursework, dissertations, theses.
  - *Faculty & staff* — professors, lecturers, postdocs, research staff; teaching and non-funded research.
  - *Researchers & classrooms* — non-profit / independent researchers, and instructors running the tools cohort-wide in a course.
  Plus one clarifying line: "non-commercial" means not for paid client or
  commercial delivery work — if it's funding revenue, that's a commercial licence.

- **§ 03 — A SMALL ASK: CITE THE WORK** (citation, courtesy)
  Phrased as a request, **not a condition**. "If the tooling helped your work,
  we'd appreciate a citation or acknowledgement — it helps others find it and
  keeps the project going." Provide a ready-to-paste citation and a BibTeX block.

  Citation (plain):
  > JG Systems Consulting Ltd. *jgs-magic-sysmlv1-pro* (MBSE AI tooling). https://labs.jgsystemsconsulting.com

  BibTeX (in a `<pre>`):
  ```bibtex
  @misc{jgsc-mbse-tooling,
    author       = {{JG Systems Consulting Ltd}},
    title        = {jgs-magic-sysmlv1-pro (MBSE AI tooling)},
    howpublished = {\url{https://labs.jgsystemsconsulting.com}},
    note         = {Non-commercial academic licence}
  }
  ```

- **§ 04 — REQUEST ACCESS** (form)
  Formspree form, `action="https://formspree.io/f/mjgqrjpa"`, same AJAX submit
  script and honeypot as `licensing.html`. Fields:
  - Name *(required)*
  - Academic email *(required)* — hint: "Use your university/institution address where possible."
  - Institution *(required)*
  - Role *(required, select)* — Student / Faculty or staff / Researcher / Instructor / Other
  - Product *(required, select)* — same product list as licensing.html
  - Intended use / research area *(textarea)* — what they're building, course or thesis, timeline.
  - `_subject` hidden field: "Academic licence request (labs site)" — so these are distinguishable from commercial enquiries in the shared inbox.
  - Fallback mailto line to `support@jgsystemsconsulting.com`.

## Discoverability edits

- **`academic.html`** — itself gets the nav + footer (built into the copied template).
- **`index.html`** — add `Academic` to masthead nav, `Academic licence` to footer, and one brief line near the products/licensing area pointing academics to the free licence.
- **`licensing.html`** — add `Academic` to masthead nav and footer, plus a short callout near the top (e.g. just after `§ 00`): "Academic or non-commercial? The pro tooling is free for you → Academic licence." linking to `academic.html`.

Nav link text: `Academic` → `academic.html` (consistent across all three pages).

## Error handling

Inherited from the existing form script: AJAX submit with disabled button +
status message; on non-OK response, surface Formspree error messages and
re-enable; on network error, fall back to the support email. Plain POST still
works with JS disabled. Honeypot `_gotcha` field for spam.

## Testing / verification

- Validate HTML structure (matched tags, valid form markup).
- Serve `docs/` locally over HTTP and visually verify `academic.html` renders
  correctly desktop + mobile, matching the site aesthetic.
- Verify all new internal links resolve (per the project's Link Verification
  Protocol): academic.html ↔ licensing.html ↔ index.html nav/footer/callout links.
- Submit the academic form once end-to-end to confirm delivery to
  `support@jgsystemsconsulting.com` with the academic `_subject`, then delete the
  test submission from Formspree (as done previously).

## Open items

None blocking. Citation values confirmed generic (JGSC Ltd / jgs-magic-sysmlv1-pro / labs URL).
