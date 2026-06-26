# JG Systems Consulting Labs

The open-source and products site for **JG Systems Consulting Ltd**, built and served from GitHub.
Consulting lives on the main site at [www.jgsystemsconsulting.com](https://www.jgsystemsconsulting.com);
this Labs site publishes the tooling behind that practice. It is served at
[labs.jgsystemsconsulting.com](https://labs.jgsystemsconsulting.com).

## How it works

This repo is both the **spec** and the **site**:

- `pages/*.md` are human-readable page specs (the source of truth for the home and about
  sections). Browsable here on GitHub; they read like a document.
- `data/products.yml` is the source of truth for the products list, maintained by the
  `refresh-website` skill (see below). Each entry has a `page` (the product's live GitHub Pages
  site) and a `url` (the source repo).
- `docs/index.html` is the actual website: one styled page in the JG Systems "engineering
  drafting" theme. The **products** section is generated between marker comments from
  `products.yml`; everything else is hand-authored.
- `docs/fonts/` holds self-hosted web fonts (no CDN).

GitHub Pages serves `docs/` (Settings, Pages, Branch `main`, folder `/docs`). The `docs/CNAME`
file points the `labs` subdomain at this site.

## Refreshing products

As the offering grows, run the **`refresh-website`** Claude skill (in `.claude/skills/`). It
discovers the org's public repos, merges any new ones into `data/products.yml` (keeping your
hand-edited blurbs and ordering, and seeding each product's live page link from its GitHub Pages
site), then regenerates the products section of `docs/index.html`. Review the diff and commit.
