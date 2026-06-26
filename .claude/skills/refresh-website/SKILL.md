---
name: refresh-website
description: Refresh the JG Systems Consulting website's products and services sections. Use when new public repos have been added, a product blurb/tier changed, or services.md was edited, and docs/index.html needs regenerating. Discovers public repos, merges them into data/products.yml additively (preserving hand edits), and re-renders the marked sections of docs/index.html.
---

# Refresh website

Regenerates the **products** and **services** sections of `docs/index.html` from their sources,
and syncs `data/products.yml` with the org's current public repos.

## When to use

- A new public repo should appear in the products catalogue.
- A product blurb, tier, featured flag, or ordering changed in `data/products.yml`.
- `pages/services.md` was edited.

## Prerequisites

`sync.py` requires PyYAML (`pip install pyyaml`); it hard-exits without it. `render.py` has a
small built-in fallback parser, so it works even if PyYAML is absent, but installing PyYAML keeps
both consistent. The `gh` CLI must be installed and authenticated.

## Procedure

Run from the repo root (`jgsystemsconsulting-website/`):

1. **Sync products** -- discover public repos and additively merge into `data/products.yml`:
   ```bash
   python .claude/skills/refresh-website/sync.py
   ```
   New repos are appended (blurb seeded from the GitHub description, `tier: free`,
   `featured: false`). Existing entries are preserved. Repos no longer public are flagged, not
   deleted. Review the printed report.

2. **Curate (optional)** -- open `data/products.yml` and adjust `blurb`, `tier`
   (`free`/`pro`/`enterprise`), `featured`, and `order` for any newly added entries. Keep blurbs
   free of em dashes (use commas/colons).

3. **Render** -- regenerate the marked sections of `docs/index.html`:
   ```bash
   python .claude/skills/refresh-website/render.py
   ```
   This rewrites only the content between `<!-- BEGIN:products -->`/`<!-- END:products -->` and
   `<!-- BEGIN:services -->`/`<!-- END:services -->`. The masthead, home, and about sections and
   all CSS are untouched.

4. **Verify**:
   ```bash
   grep -c '—' docs/index.html        # must be 0 (no em dash)
   grep -c 'class="cell"' docs/index.html   # expect 9 (6 products + 3 services); adjust if the catalogue grew
   ```

5. **Review the diff and commit**:
   ```bash
   git add data/products.yml docs/index.html
   git commit -m "chore: refresh website products and services"
   ```

## Invariants

- The renderer writes only between the markers; the rest of `index.html` is hand-authored and
  must never be modified by this skill.
- The sync is additive: never overwrite a human-curated blurb, tier, featured flag, or order.
- Read-only against GitHub (via `gh`); no network writes.
