---
name: refresh-website
description: Refresh the JG Systems Consulting Labs site's products section. Use when new public repos have been added, a repo's GitHub Pages site went live, or a product blurb/tier changed, and docs/index.html needs regenerating. Discovers public repos, merges them into data/products.yml additively (preserving hand edits, seeding each product's live page link), and re-renders the products section of docs/index.html.
---

# Refresh website

Regenerates the **products** section of `docs/index.html` from `data/products.yml`, and syncs
that file with the org's current public repos and their live product pages.

## When to use

- A new public repo should appear in the products catalogue.
- A repo's GitHub Pages site was enabled and its `page` link should be picked up.
- A product blurb, tier, featured flag, or ordering changed in `data/products.yml`.

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
   New repos are appended (blurb seeded from the GitHub description, `page` seeded from the repo's
   GitHub Pages site / homepage, `tier: free`, `featured: false`). Existing entries are preserved,
   except a missing `page` link is backfilled. Repos no longer public are flagged, not deleted.
   Review the printed report.

2. **Curate (optional)** -- open `data/products.yml` and adjust `blurb`, `tier`
   (`free`/`pro`/`enterprise`), `featured`, and `order` for any newly added entries. Keep blurbs
   free of em dashes (use commas/colons).

3. **Render** -- regenerate the products section of `docs/index.html`:
   ```bash
   python .claude/skills/refresh-website/render.py
   ```
   This rewrites only the content between `<!-- BEGIN:products -->` and `<!-- END:products -->`.
   The masthead, home, and about sections and all CSS are untouched. Each card links to the
   product page (`Open`) and the source repo (`Source`).

4. **Verify**:
   ```bash
   grep -c '—' docs/index.html                  # must be 0 (no em dash)
   grep -o 'class="cell"' docs/index.html | wc -l   # one per product; adjust as the catalogue grows
   ```

5. **Review the diff and commit**:
   ```bash
   git add data/products.yml docs/index.html
   git commit -m "chore: refresh website products"
   ```

## Invariants

- The renderer writes only between the products markers; the rest of `index.html` is
  hand-authored and must never be modified by this skill.
- The sync is additive: never overwrite a human-curated blurb, tier, featured flag, or order. The
  only field refreshed on existing entries is a missing `page` link (backfill only).
- Read-only against GitHub (via `gh`); no network writes.
