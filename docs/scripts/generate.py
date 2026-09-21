#!/usr/bin/env python3
"""Regenerate docs/index.html from the vault's actual files and wikilinks.

Run from anywhere: python3 docs/scripts/generate.py
Re-run this after adding/editing vault entries to keep the graph current.
"""
import os
import re
import json
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
FOLDERS = ["ideas", "notes", "people", "projects"]
HUB_ID = "self"


def slug_from_path(path):
    return os.path.splitext(os.path.basename(path))[0]


def build_graph_data():
    nodes = {}

    for folder in FOLDERS:
        d = os.path.join(REPO_ROOT, folder)
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(d, fn)
            slug = slug_from_path(fn)
            text = open(path, encoding="utf-8").read()
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
            fm = yaml.safe_load(m.group(1)) or {}
            nodes[slug] = {
                "id": slug,
                "label": fm.get("title") or slug,
                "type": fm.get("type") or folder,
                "group": folder,
                "tags": fm.get("tags") or [],
            }

    links = []
    seen_links = set()
    for folder in FOLDERS:
        d = os.path.join(REPO_ROOT, folder)
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(d, fn)
            slug = slug_from_path(fn)
            text = open(path, encoding="utf-8").read()
            wikilinks = set(re.findall(r"\[\[([a-zA-Z0-9_\-]+)\]\]", text))
            for target in wikilinks:
                if target in nodes and target != slug:
                    key = tuple(sorted([slug, target]))
                    if key not in seen_links:
                        seen_links.add(key)
                        links.append({"source": slug, "target": target, "weight": 2})

    # attach any node with no path to the hub, so nothing floats off the graph
    adj = {slug: set() for slug in nodes}
    for l in links:
        adj[l["source"]].add(l["target"])
        adj[l["target"]].add(l["source"])

    visited = set()
    stack = [HUB_ID]
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        stack.extend(adj.get(cur, set()) - visited)

    for slug in nodes:
        if slug not in visited and slug != HUB_ID:
            links.append({"source": HUB_ID, "target": slug, "weight": 1})
            visited.add(slug)

    return {"nodes": list(nodes.values()), "links": links}


def main():
    data = build_graph_data()
    template_path = os.path.join(DOCS_DIR, "scripts", "template.html")
    template = open(template_path, encoding="utf-8").read()
    payload = json.dumps(data, separators=(",", ":"))
    out = template.replace("__GRAPH_DATA__", payload)
    out_path = os.path.join(DOCS_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {out_path} — {len(data['nodes'])} nodes, {len(data['links'])} links.")


if __name__ == "__main__":
    main()
