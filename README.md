# JG Systems Consulting — website

The company website for **JG Systems Consulting Ltd**, built and served from GitHub.

## How it works

This repo is both the **spec** and the **site**:

- `pages/*.md` — human-readable page specs (the source of truth for the home, services, and
  about sections). Browsable here on GitHub; they read like a document.
- `data/products.yml` — the source of truth for the products list, maintained by the
  `refresh-website` skill (see below).
- `docs/index.html` — the actual website: one styled page in the JG Systems "engineering
  drafting" theme. The **products** and **services** sections are generated between marker
  comments from the sources above; everything else is hand-authored.
- `docs/fonts/` — self-hosted web fonts (no CDN).

GitHub Pages serves `docs/` once the repo is public (Settings → Pages → Branch `main`, folder
`/docs`).

## Refreshing products and services

As the offering grows, run the **`refresh-website`** Claude skill (in `.claude/skills/`). It
discovers the org's public repos, merges any new ones into `data/products.yml` (keeping your
hand-edited blurbs and ordering), and regenerates the products and services sections of
`docs/index.html`. Review the diff and commit.
