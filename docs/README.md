# Vbrain Constellation — interactive graph

A live, force-directed graph of this vault, built with D3.js. Every
project, note, idea, and person becomes a node; wikilinks between files
become edges. Click a node to read its tags and connections, drag nodes
around, zoom, and search.

## View it
Enable GitHub Pages for this repo (Settings → Pages → Deploy from a
branch → root `/docs` folder on this branch), then open the Pages URL.
Or just open `docs/index.html` directly in a browser.

## Regenerate after editing the vault
The graph data is generated from the real `.md` files (frontmatter +
`[[wikilinks]]`) — it isn't hand-maintained. After adding or editing
vault entries, regenerate it:

```
pip install pyyaml
python3 docs/scripts/generate.py
```

This rewrites `docs/index.html` from `docs/scripts/template.html` plus
the current contents of `ideas/`, `notes/`, `people/`, and `projects/`.
Commit the updated `docs/index.html` along with your vault changes.
