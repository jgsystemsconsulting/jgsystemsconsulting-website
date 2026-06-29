# Academic Licence Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a dedicated `docs/academic.html` page announcing the JGSC pro tooling is free for non-commercial academic use, with rationale, eligibility, a courtesy citation request, and a Formspree request form — plus discoverability links across the site.

**Architecture:** Copy `docs/licensing.html`'s single-file structure (inline CSS, masthead, footer, AJAX form script) into a new `docs/academic.html`. Reuse the existing Formspree endpoint `mjgqrjpa`. Add nav/footer/callout links on `index.html` and `licensing.html`. No build step, no new assets.

**Tech Stack:** Static HTML + inline CSS, Formspree AJAX form, GitHub Pages (deploys from `docs/` on `main`).

---

## File structure

- **Create** `docs/academic.html` — the new page (self-contained, mirrors `licensing.html`).
- **Modify** `docs/licensing.html` — masthead nav, footer, top callout linking to academic page.
- **Modify** `docs/index.html` — masthead nav, footer, one line near products pointing academics to the free licence.

There is no test framework on this static site. "Tests" here are concrete verification steps: HTML tag-balance check, local HTTP render check, link-resolution check, and one end-to-end form submission. These replace unit tests appropriately for a static page.

---

## Task 1: Create `docs/academic.html` skeleton (head + masthead + footer)

**Files:**
- Create: `docs/academic.html`

- [ ] **Step 1: Create the file with the full head, masthead, and footer**

Copy the `<style>` block **verbatim** from `docs/licensing.html` (lines 18–70 inclusive, i.e. the entire `<style>…</style>` element). Do not rewrite the CSS — it must match exactly. The file:

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Academic Licence - JG Systems Consulting Labs</title>
<meta name="description" content="JG Systems Consulting Labs pro tooling is free for non-commercial academic use. Who qualifies, why we offer it, how to request access, and an optional citation.">
<link rel="canonical" href="https://labs.jgsystemsconsulting.com/academic.html">
<meta property="og:title" content="Academic Licence - JG Systems Consulting Labs">
<meta property="og:description" content="JGSC Labs pro tooling is free for non-commercial academic use. Who qualifies, why, and how to request access.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://labs.jgsystemsconsulting.com/academic.html">
<meta property="og:image" content="https://labs.jgsystemsconsulting.com/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<style>
/* PASTE THE ENTIRE <style> BLOCK FROM docs/licensing.html HERE, VERBATIM */
</style>
</head>
<body>
<div class="wrap">

  <header class="masthead">
    <span>CLASSIFICATION: PUBLIC</span>
    <span>LICENCE: &copy; JG SYSTEMS CONSULTING LTD</span>
    <span>DOC-ID: JGSC-WEB-003</span>
    <span>REV 0.1.0</span>
    <nav><a href="index.html#products">Products</a><a href="licensing.html">Licensing</a><a href="academic.html">Academic</a><a href="index.html#about">About</a><a href="https://www.jgsystemsconsulting.com">Consulting</a></nav>
  </header>

  <!-- SECTIONS ADDED IN LATER TASKS -->

  <footer>
    <span>&copy; JG Systems Consulting Ltd</span>
    <span><a href="index.html">Labs home</a></span>
    <span><a href="licensing.html">Licensing</a></span>
    <span><a href="academic.html">Academic</a></span>
    <span><a href="https://www.jgsystemsconsulting.com">Main site</a></span>
    <span><a href="https://github.com/jgsystemsconsulting">GitHub</a></span>
    <span><a href="mailto:support@jgsystemsconsulting.com">Contact</a></span>
  </footer>

</div>
</body>
</html>
```

- [ ] **Step 2: Verify the style block was copied, not omitted**

Run: `grep -c "JetBrainsMono-Bold" docs/academic.html`
Expected: `1` (the Bold @font-face `src` url appears exactly once in the copied style block — confirms CSS was pasted, not left as a comment). Note: do not grep `font-family:'JetBrains Mono'` for this check — that string appears twice (Regular + Bold @font-face declarations).

- [ ] **Step 3: Verify tag balance**

Run: `grep -c "<section" docs/academic.html`
Expected: `0` (no sections yet — they come in Task 2). This is a baseline before adding content.

- [ ] **Step 4: Commit**

```bash
git add docs/academic.html
git commit -m "feat(academic): scaffold academic.html with head, masthead, footer"
```

---

## Task 2: Add §00–§02 content (hero, why, eligibility)

**Files:**
- Modify: `docs/academic.html`

- [ ] **Step 1: Insert the three sections** in place of the `<!-- SECTIONS ADDED IN LATER TASKS -->` comment

```html
  <section id="academic-intro">
    <div class="sec-num">&sect; 00 - ACADEMIC / NON-COMMERCIAL</div>
    <h1>Free for academia.</h1>
    <p>The JG Systems Consulting Labs pro tooling &mdash; the write-tier pro JARs and pro
    skills that let AI agents author and edit live models in CATIA Magic and Sparx Enterprise
    Architect &mdash; is free for non-commercial academic use. No fee, no trial period, no seat
    count. The flagship licence, jgs-magic-sysmlv1-pro, is included.</p>
    <p><a class="btn" href="#request">Request access &rarr;</a> <a class="btn ghost" href="licensing.html">Back to licensing &rarr;</a></p>
  </section>

  <section id="why">
    <div class="sec-num">&sect; 01 - WHY WE DO THIS</div>
    <h2>Putting the tools in your hands</h2>
    <p>We want to support the academic community and see AI-assisted MBSE used more widely, and
    the fastest way to do that is to get these capabilities to the people doing the teaching,
    learning and research. Students and researchers are where the interesting work happens, and a
    licence cost should not stand between you and it. We would rather you used the tooling than
    worried about whether you could. Most people who qualify never realise they can simply ask
    &mdash; so ask.</p>
  </section>

  <section id="who">
    <div class="sec-num">&sect; 02 - WHO QUALIFIES</div>
    <h2>Who qualifies</h2>
    <div class="grid grid-3">
      <div class="cell"><h3>Students</h3><p>Undergraduate, master's and PhD. Coursework, dissertations and theses.</p></div>
      <div class="cell"><h3>Faculty &amp; staff</h3><p>Professors, lecturers, postdocs and research staff, for teaching and non-funded research.</p></div>
      <div class="cell"><h3>Researchers &amp; classrooms</h3><p>Non-profit and independent researchers, and instructors running the tools cohort-wide across a course.</p></div>
    </div>
    <p style="margin-top:1.5rem;color:var(--mute)">"Non-commercial" means not for paid client or commercial delivery work. If the work funds revenue, that is a commercial licence &mdash; see <a href="licensing.html">licensing</a>.</p>
  </section>
```

- [ ] **Step 2: Verify the three sections exist**

Run: `grep -c "<section" docs/academic.html`
Expected: `3`

- [ ] **Step 3: Verify grid cell count**

Run: `grep -c 'class="cell"' docs/academic.html`
Expected: `3`

- [ ] **Step 4: Commit**

```bash
git add docs/academic.html
git commit -m "feat(academic): add hero, rationale, and eligibility sections"
```

---

## Task 3: Add §03 citation section

**Files:**
- Modify: `docs/academic.html`

- [ ] **Step 1: Insert the citation section** immediately after the `#who` section's closing `</section>`

```html
  <section id="cite">
    <div class="sec-num">&sect; 03 - A SMALL ASK: CITE THE WORK</div>
    <h2>A small ask: cite the work</h2>
    <p>If the tooling helped your work, we would appreciate &mdash; but do not require &mdash; a
    citation or acknowledgement in your thesis, paper or report. It helps others find the tooling
    and keeps the project going. This is a courtesy request, not a condition of the licence.</p>
    <p>A paste-ready citation:</p>
    <div class="cell" style="border:1px solid var(--line)">
      <p style="margin:0">JG Systems Consulting Ltd. <em>jgs-magic-sysmlv1-pro</em> (MBSE AI tooling). https://labs.jgsystemsconsulting.com</p>
    </div>
    <p style="margin-top:1.5rem">Or BibTeX:</p>
    <pre style="font-family:var(--mono);font-size:0.8125rem;background:var(--ink-2);border:1px solid var(--line);padding:1rem;overflow-x:auto;color:var(--text)">@misc{jgsc-mbse-tooling,
  author       = {{JG Systems Consulting Ltd}},
  title        = {jgs-magic-sysmlv1-pro (MBSE AI tooling)},
  howpublished = {\url{https://labs.jgsystemsconsulting.com}},
  note         = {Non-commercial academic licence}
}</pre>
  </section>
```

- [ ] **Step 2: Verify section count and BibTeX presence**

Run: `grep -c "<section" docs/academic.html` → Expected: `4`
Run: `grep -c "jgsc-mbse-tooling" docs/academic.html` → Expected: `1`

- [ ] **Step 3: Commit**

```bash
git add docs/academic.html
git commit -m "feat(academic): add courtesy citation section with paste-ready + BibTeX"
```

---

## Task 4: Add §04 request form + AJAX script

**Files:**
- Modify: `docs/academic.html`

- [ ] **Step 1: Insert the form section** after the `#cite` section's closing `</section>`

```html
  <section id="request">
    <div class="sec-num">&sect; 04 - REQUEST ACCESS</div>
    <h2>Request access</h2>
    <p>Fill in the form and we will set you up. Using a university or institution email address
    helps us verify eligibility quickly.</p>

    <form class="form" id="academic-form" action="https://formspree.io/f/mjgqrjpa" method="POST">
      <div class="field">
        <label for="name">Name <span class="req">*</span></label>
        <input type="text" id="name" name="name" autocomplete="name" required>
      </div>
      <div class="field">
        <label for="email">Academic email <span class="req">*</span></label>
        <input type="email" id="email" name="email" autocomplete="email" required>
        <span class="hint">Use your university/institution address where possible &mdash; it speeds up verification.</span>
      </div>
      <div class="field">
        <label for="institution">Institution <span class="req">*</span></label>
        <input type="text" id="institution" name="institution" autocomplete="organization" required>
      </div>
      <div class="field">
        <label for="role">Role <span class="req">*</span></label>
        <select id="role" name="role" required>
          <option value="" selected disabled>Select your role&hellip;</option>
          <option value="Student">Student (undergrad / master's / PhD)</option>
          <option value="Faculty or staff">Faculty or staff</option>
          <option value="Researcher">Researcher (non-profit / independent)</option>
          <option value="Instructor">Instructor (classroom / cohort use)</option>
          <option value="Other">Other</option>
        </select>
      </div>
      <div class="field">
        <label for="product">Product <span class="req">*</span></label>
        <select id="product" name="product" required>
          <option value="" selected disabled>Select a product&hellip;</option>
          <option value="jgs-magic-sysmlv1-pro">jgs-magic-sysmlv1-pro</option>
          <option value="jgs-magic-sysmlv2-pro (coming soon)">jgs-magic-sysmlv2-pro (coming soon)</option>
          <option value="jgs-magic-sysmlv2-pro-skills (coming soon)">jgs-magic-sysmlv2-pro-skills (coming soon)</option>
          <option value="jgs-sparx-mcp-sysmlv1 (coming soon)">jgs-sparx-mcp-sysmlv1 (coming soon)</option>
          <option value="jgs-sparx-mcp-archimate (coming soon)">jgs-sparx-mcp-archimate (coming soon)</option>
          <option value="jgs-sparx-mcp-naf4 (coming soon)">jgs-sparx-mcp-naf4 (coming soon)</option>
          <option value="jgs-sparx-mcp-uaf (coming soon)">jgs-sparx-mcp-uaf (coming soon)</option>
          <option value="Other / not sure">Other / not sure</option>
        </select>
      </div>
      <div class="field">
        <label for="message">Intended use &amp; research area</label>
        <textarea id="message" name="message" placeholder="What you are building, the course or thesis, which tool/version, timeline."></textarea>
      </div>
      <!-- honeypot: bots fill this, humans don't -->
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="hidden" aria-hidden="true">
      <input type="hidden" name="_subject" value="Academic licence request (labs site)">
      <div>
        <button type="submit" class="btn" id="submit-btn">Send request &rarr;</button>
      </div>
      <p class="form-status hidden" id="form-status" role="status" aria-live="polite"></p>
    </form>

    <p style="margin-top:2rem;color:var(--mute)">Prefer email? Write to
    <a href="mailto:support@jgsystemsconsulting.com?subject=Academic%20licence%20request">support@jgsystemsconsulting.com</a>.</p>
  </section>
```

- [ ] **Step 2: Insert the AJAX script** immediately before `</body>` (after the closing `</div>` of `.wrap`). The script references `academic-form` (not `license-form`):

```html
<script>
// ponytail: AJAX submit so users stay on-page; plain POST still works if JS is off
(function(){
  var form = document.getElementById('academic-form');
  var status = document.getElementById('form-status');
  var btn = document.getElementById('submit-btn');
  if(!form) return;
  form.addEventListener('submit', function(e){
    e.preventDefault();
    btn.disabled = true;
    status.className = 'form-status'; status.classList.remove('hidden');
    status.textContent = 'Sending…';
    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: {'Accept': 'application/json'}
    }).then(function(res){
      if(res.ok){
        form.reset();
        status.className = 'form-status ok';
        status.textContent = 'Thanks — your request is in. We’ll reply by email shortly.';
      } else {
        return res.json().then(function(data){
          var msg = (data && data.errors) ? data.errors.map(function(e){return e.message}).join(', ') : 'Something went wrong. Please email support@jgsystemsconsulting.com.';
          status.className = 'form-status err'; status.textContent = msg;
          btn.disabled = false;
        });
      }
    }).catch(function(){
      status.className = 'form-status err';
      status.textContent = 'Network error. Please email support@jgsystemsconsulting.com.';
      btn.disabled = false;
    });
  });
})();
</script>
```

- [ ] **Step 3: Verify form wiring**

Run: `grep -c "academic-form" docs/academic.html` → Expected: `2` (form id + script getElementById)
Run: `grep -c "mjgqrjpa" docs/academic.html` → Expected: `1`
Run: `grep -c "<section" docs/academic.html` → Expected: `5`

- [ ] **Step 4: Commit**

```bash
git add docs/academic.html
git commit -m "feat(academic): add request form and AJAX submit handler"
```

---

## Task 5: Discoverability links on `licensing.html`

**Files:**
- Modify: `docs/licensing.html`

- [ ] **Step 1: Add `Academic` to the masthead nav.** Find this line in `docs/licensing.html`:

```html
    <nav><a href="index.html#products">Products</a><a href="licensing.html">Licensing</a><a href="index.html#about">About</a><a href="https://www.jgsystemsconsulting.com">Consulting</a></nav>
```

Replace with:

```html
    <nav><a href="index.html#products">Products</a><a href="licensing.html">Licensing</a><a href="academic.html">Academic</a><a href="index.html#about">About</a><a href="https://www.jgsystemsconsulting.com">Consulting</a></nav>
```

- [ ] **Step 2: Add the top callout.** Find the closing `</section>` of the `#licensing-intro` section (it ends with the two buttons paragraph). Immediately after that `</section>`, insert:

```html
  <section id="academic-callout">
    <div class="sec-num">&sect; 00.1 - ACADEMIC</div>
    <h2>Academic or non-commercial? It's free.</h2>
    <p>If you're a student, researcher, or faculty member using this for non-commercial academic
    work, you don't need to pay &mdash; the pro tooling is free for you.
    <a href="academic.html">See the academic licence &rarr;</a></p>
  </section>
```

- [ ] **Step 3: Add `Academic` to the footer.** Find in `docs/licensing.html`:

```html
    <span><a href="index.html">Labs home</a></span>
```

Insert immediately after it:

```html
    <span><a href="academic.html">Academic</a></span>
```

- [ ] **Step 4: Verify**

Run: `grep -c "academic.html" docs/licensing.html`
Expected: `3` (nav + callout link + footer)

- [ ] **Step 5: Commit**

```bash
git add docs/licensing.html
git commit -m "feat(academic): link academic page from licensing nav, callout, footer"
```

---

## Task 6: Discoverability links on `index.html`

**Files:**
- Modify: `docs/index.html`

- [ ] **Step 1: Add `Academic` to the masthead nav.** Find in `docs/index.html`:

```html
    <nav><a href="#products">Products</a><a href="licensing.html">Licensing</a><a href="#about">About</a><a href="https://www.jgsystemsconsulting.com">Consulting</a></nav>
```

Replace with:

```html
    <nav><a href="#products">Products</a><a href="licensing.html">Licensing</a><a href="academic.html">Academic</a><a href="#about">About</a><a href="https://www.jgsystemsconsulting.com">Consulting</a></nav>
```

- [ ] **Step 2: Add the academic line in the products section.**

**Important:** the products grid in `docs/index.html` is wrapped in an auto-generated block delimited by `<!-- BEGIN:products -->` and `<!-- END:products -->` (regenerated by the refresh-website automation). Do NOT insert content inside that block — it will be overwritten. The `#products` section currently has **no** intro paragraph; it goes straight from `<div class="sec-num">&sect; 01 - PRODUCTS</div>` to the `<!-- BEGIN:products -->` marker.

Insert this standalone paragraph on its own line **immediately before** the `<!-- BEGIN:products -->` comment (i.e. between the `sec-num` div and the BEGIN marker), so it sits inside `#products` but outside the auto-generated region:

```html
    <p style="color:var(--mute)">Pro tooling is free for non-commercial academic use &mdash; <a href="academic.html">see the academic licence &rarr;</a></p>
```

The exact anchor to find (insert the paragraph on the line directly above it):

```html
    <!-- BEGIN:products -->
```

```html
    <p style="color:var(--mute)">Pro tooling is free for non-commercial academic use &mdash; <a href="academic.html">see the academic licence &rarr;</a></p>
```

- [ ] **Step 3: Add `Academic` to the footer.** Find in `docs/index.html`:

```html
    <span><a href="licensing.html">Licensing</a></span>
```

Insert immediately after it:

```html
    <span><a href="academic.html">Academic</a></span>
```

- [ ] **Step 4: Verify**

Run: `grep -c "academic.html" docs/index.html`
Expected: `3` (nav + products line + footer)

- [ ] **Step 5: Commit**

```bash
git add docs/index.html
git commit -m "feat(academic): link academic page from homepage nav, products, footer"
```

---

## Task 7: Verification — render, links, tag balance

**Files:** none modified (verification only)

- [ ] **Step 1: Tag-balance sanity check on academic.html**

Run:
```bash
python -c "import re,sys; h=open('docs/academic.html',encoding='utf-8').read(); print('sections', h.count('<section')==h.count('</section>')); print('divs', h.count('<div')==h.count('</div>')); print('forms', h.count('<form')==h.count('</form>'))"
```
Expected: all three print `True`.

- [ ] **Step 2: Serve docs/ locally and screenshot**

Run (background): `python -m http.server 8765 --directory docs`
Then load `http://localhost:8765/academic.html` and confirm: page renders in the site's dark "classified" style, masthead + 5 sections + footer present, form fields visible, BibTeX block readable. Check at desktop (≥1280px) and mobile (360px) widths. Stop the server when done.

Acceptance: page is visually consistent with licensing.html; no unstyled/broken layout.

- [ ] **Step 3: Internal link resolution check** (per project Link Verification Protocol)

Run:
```bash
cd docs && for f in academic.html licensing.html index.html; do echo "== $f =="; grep -oE 'href="[^"]*"' "$f" | grep -vE 'https?:|mailto:|#'; done; cd ..
```
Confirm every relative `href` points to a file that exists (`academic.html`, `licensing.html`, `index.html`, `favicon.svg`, `fonts/...`). No 404 targets.

- [ ] **Step 4: End-to-end form test**

Load `http://localhost:8765/academic.html`, fill the form with test values (role=Student, product=jgs-magic-sysmlv1-pro), submit. Confirm the on-page success status appears and that an email arrives at `support@jgsystemsconsulting.com` with subject "Academic licence request (labs site)". Then delete the test submission from the Formspree dashboard (form `mjgqrjpa`, at `https://formspree.io/forms/mjgqrjpa/submissions`) to keep the inbox clean.

Acceptance: success message shows; email delivered with correct subject; test submission removed.

- [ ] **Step 5: Final status check (no commit — verification task)**

Run: `git status --short`
Expected: clean working tree (all changes already committed in Tasks 1–6).

---

## Self-review notes

- **Spec coverage:** §00–§04 page sections → Tasks 1–4. Eligibility (3-cell grid covering the 4 eligible groups: students; faculty & staff; and researchers + classroom instructors merged into one cell) → §02 grid + clarifier. Citation as courtesy (not enforced) → §03 wording "appreciate — but do not require". Formspree reuse with academic fields + distinct `_subject` → Task 4. Discoverability (nav, footer, licensing callout, homepage line) → Tasks 5–6. Verification (HTML, render, links, e2e form) → Task 7. All spec sections mapped.
- **Form id consistency:** `academic-form` used in both the `<form>` and the script's `getElementById` (Task 4). Distinct from licensing.html's `license-form` so the two pages' scripts never collide.
- **No placeholders:** every code step shows complete markup. The one conditional is Task 6 Step 2 (intro-paragraph vs standalone line) — both branches give exact code; the executor reads the live file to pick the branch.
