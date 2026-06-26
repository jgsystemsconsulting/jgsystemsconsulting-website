#!/usr/bin/env python3
"""Render the products and services sections of docs/index.html from sources.

Sources:
  data/products.yml      -> § PRODUCTS  (between <!-- BEGIN:products --> / <!-- END:products -->)
  pages/services.md      -> § SERVICES  (between <!-- BEGIN:services --> / <!-- END:services -->)

Writes only between the markers; the rest of index.html is untouched.
Run from the repo root: python .claude/skills/refresh-website/render.py
"""
from __future__ import annotations
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INDEX = ROOT / "docs" / "index.html"
PRODUCTS_YML = ROOT / "data" / "products.yml"
SERVICES_MD = ROOT / "pages" / "services.md"


def load_products() -> list[dict]:
    text = PRODUCTS_YML.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text) or {}
        return data.get("products", [])
    except ModuleNotFoundError:
        return _mini_parse_products(text)


def _mini_parse_products(text: str) -> list[dict]:
    """Tiny fallback parser for the flat list-of-dicts shape we control."""
    items: list[dict] = []
    cur: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("#") or not line.strip():
            continue
        m = re.match(r"\s*-\s+(\w+):\s*(.*)$", line)
        if m:
            if cur:
                items.append(cur)
            cur = {}
            cur[m.group(1)] = _coerce(m.group(2))
            continue
        m = re.match(r"\s+(\w+):\s*(.*)$", line)
        if m and cur is not None:
            cur[m.group(1)] = _coerce(m.group(2))
    if cur:
        items.append(cur)
    return items


def _coerce(v: str):
    v = v.strip()
    if v in ("true", "false"):
        return v == "true"
    if v.isdigit():
        return int(v)
    return v


def render_products(products: list[dict]) -> str:
    ordered = sorted(products, key=lambda p: p.get("order", 9999))
    cells = []
    for p in ordered:
        name = html.escape(str(p.get("name", "")))
        url = html.escape(str(p.get("url", "#")))
        blurb = html.escape(str(p.get("blurb", "")))
        tier = p.get("tier")
        tier_html = f'<p class="tier">{html.escape(str(tier))}</p>' if tier else ""
        cells.append(
            f'<div class="cell"><h3>{name}</h3>{tier_html}'
            f'<p>{blurb}</p><p><a class="btn ghost" href="{url}">View on GitHub &rarr;</a></p></div>'
        )
    return '<h2>Products</h2>\n<div class="grid grid-3">\n' + "\n".join(cells) + "\n</div>"


def render_services(md: str) -> str:
    """Parse `### Title` + following paragraph blocks from services.md."""
    blocks = re.findall(r"^###\s+(.+?)\n+(.+?)(?=\n###|\Z)", md, flags=re.S | re.M)
    cells = []
    for title, body in blocks:
        t = html.escape(title.strip())
        para = html.escape(" ".join(body.split()))
        cells.append(f'<div class="cell"><h3>{t}</h3><p>{para}</p></div>')
    return '<h2>Services</h2>\n<div class="grid grid-3">\n' + "\n".join(cells) + "\n</div>"


def splice(index_text: str, key: str, inner: str) -> str:
    begin, end = f"<!-- BEGIN:{key} -->", f"<!-- END:{key} -->"
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if not pattern.search(index_text):
        sys.exit(f"ERROR: markers for '{key}' not found in {INDEX}")
    return pattern.sub(f"{begin}\n{inner}\n{end}", index_text)


def main() -> int:
    index_text = INDEX.read_text(encoding="utf-8")
    products = load_products()
    services_md = SERVICES_MD.read_text(encoding="utf-8")
    index_text = splice(index_text, "products", render_products(products))
    index_text = splice(index_text, "services", render_services(services_md))
    INDEX.write_text(index_text, encoding="utf-8")
    print(f"Rendered {len(products)} products and services into {INDEX.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
