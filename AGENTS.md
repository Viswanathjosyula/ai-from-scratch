# AGENTS.md

## Cursor Cloud specific instructions

This repo is primarily a **static website** (plain HTML + CSS) for the "AI from scratch"
curriculum at ai.josyulablog.org, plus a hands-on **FraudWatch** project under `fraudwatch/`.

### Services
- **Static site** — serve from repo root: `python3 -m http.server 8000`
  then open `http://localhost:8000/index.html`.
  Pages: curriculum modules, `roadmap.html`, `interview.html`, `projects.html`.
- **FraudWatch** — finance fraud-detection lab in `fraudwatch/` (scikit-learn).
  Not a long-running service; run scripts on demand (see `fraudwatch/README.md`).
- Companion `.ipynb` files are opened via Colab links in the modules; local Jupyter is optional.

### Lint / test / build
- No site lint/test/build tooling — validate by loading pages in a browser.
- FraudWatch smoke check: `cd fraudwatch && python 01_baseline.py`
  (downloads OpenML `creditcard` on first run into `fraudwatch/data/`, gitignored).

### Non-obvious notes
- GitHub Pages must deploy from branch `main` / root with custom domain `ai.josyulablog.org`.
- Large fraud dataset CSV is gitignored; expect a one-time download on first baseline run.
- Prefer **PR-AUC** (not accuracy) when evaluating FraudWatch models — extreme class imbalance.
