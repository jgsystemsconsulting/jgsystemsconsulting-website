# Changelog

All notable changes to this site are recorded here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] - 2026-06-26

### Added
- Initial JG Systems Consulting Labs site: a single styled page in the
  "engineering drafting" theme, self-hosted fonts, served from `docs/` via
  GitHub Pages at labs.jgsystemsconsulting.com.
- Products catalogue auto-generated from `data/products.yml`, with each card
  linking to the product's live page and source repo.
- `refresh-website` skill (`sync.py` + `render.py`) that discovers the org's
  public repos, seeds each product's live page link, and regenerates the
  products section additively.
- JSON-LD Organization metadata, Open Graph / Twitter tags, governance files
  (LICENSE, NOTICE, SECURITY.md), and a `CNAME` for the `labs` subdomain.
