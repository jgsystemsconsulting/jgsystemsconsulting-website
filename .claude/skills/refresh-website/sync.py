#!/usr/bin/env python3
"""Sync data/products.yml with the org's current public repos (additive merge).

- Adds repos not already in products.yml (blurb seeded from GitHub description).
- Preserves existing blurb / tier / featured / order (never clobbered).
- Flags repos in products.yml that are no longer public (prints a warning; does not delete).

Requires the `gh` CLI authenticated. Run from repo root:
  python .claude/skills/refresh-website/sync.py
Then run render.py to regenerate the page.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PRODUCTS_YML = ROOT / "data" / "products.yml"
ORG = "jgsystemsconsulting"

# Repos that are public but are not products to advertise (skip-list).
SKIP = {".github", "jgsystemsconsulting-website"}


def gh_public_repos() -> list[dict]:
    out = subprocess.run(
        ["gh", "repo", "list", ORG, "--visibility", "public",
         "--json", "name,description,url", "--limit", "200"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        sys.exit(f"gh failed: {out.stderr.strip()}")
    return json.loads(out.stdout)


def load_yaml(text: str) -> dict:
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text) or {"products": []}
    except ModuleNotFoundError:
        sys.exit("PyYAML required for sync.py: pip install pyyaml")


HEADER = (
    "# Source of truth for the PRODUCTS section of docs/index.html.\n"
    "# Maintained by the refresh-website skill: new public repos are appended automatically;\n"
    "# hand-edited blurb / tier / featured / order are preserved on re-run.\n"
)


def dump_yaml(data: dict) -> str:
    import yaml  # available because load_yaml required it
    # PyYAML strips comments on round-trip, so re-prepend the header every write.
    return HEADER + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000)


def deslop(text: str) -> str:
    """House style: no em dash in generated blurbs."""
    return (text or "").replace(" — ", ", ").replace("—", ", ")


def main() -> int:
    existing = load_yaml(PRODUCTS_YML.read_text(encoding="utf-8"))
    products = existing.get("products", [])
    by_name = {p["name"]: p for p in products}

    live = {r["name"]: r for r in gh_public_repos() if r["name"] not in SKIP}

    added = []
    next_order = max([p.get("order", 0) for p in products], default=0)
    for name, repo in live.items():
        if name not in by_name:
            next_order += 1
            entry = {
                "name": name,
                "url": repo["url"],
                "blurb": deslop(repo.get("description") or name),
                "tier": "free",
                "featured": False,
                "order": next_order,
            }
            products.append(entry)
            by_name[name] = entry
            added.append(name)

    missing = [n for n in by_name if n not in live]

    # Only rewrite the file when we actually appended something. A no-change run
    # must leave products.yml byte-for-byte untouched (no comment loss, no churn).
    if added:
        existing["products"] = products
        PRODUCTS_YML.write_text(dump_yaml(existing), encoding="utf-8")

    print(f"Added {len(added)}: {', '.join(added) or '(none)'}")
    if missing:
        print(f"WARNING: no longer public (left in place, review): {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
