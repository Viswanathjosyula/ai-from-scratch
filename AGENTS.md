# AGENTS.md

## Cursor Cloud specific instructions

This repo is a **static website** (plain HTML + one CSS file) for the "AI from scratch"
curriculum, deployed via GitHub Pages. There is no build step, framework, package
manager, or dependency install — see `README.md` for the deploy/authoring flow.

### Services
- **Static site** — `index.html` (landing + curriculum), `module-1.html`, `module-2.html`
  (lessons), `styles.css` (shared styles), `CNAME` (GitHub Pages domain).
- `overfitting.ipynb` / `algorithms.ipynb` are **not** run locally. They are only opened
  remotely via the "Open in Colab" links in the module pages, so serving/editing the site
  does not require Python or Jupyter.

### Run in development
Serve the files from the repo root with any static file server, e.g.:

```
python3 -m http.server 8000
```

Then open `http://localhost:8000/index.html`. Editing an HTML/CSS file and refreshing the
browser shows changes immediately (no hot-reload, just a manual refresh).

### Lint / test / build
There is no lint, test, or build tooling in this repo — changes are validated by opening
the pages in a browser and checking they render and navigate correctly.
