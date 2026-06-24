# AI from scratch — site

A static site (no build step, no framework) that hosts the "Learning AI from scratch"
curriculum. Plain HTML + one CSS file, so it loads fast and
you can edit it by hand.

## Files
- `index.html` — landing page + curriculum route (shows progress through 8 modules)
- `module-1.html`, `module-2.html` — the lessons
- `styles.css` — shared design system

## Before you deploy — fill in 2 placeholders
In `index.html`, replace:
- `@yourhandle` and the `https://x.com` link → your real X profile

## Deploy to GitHub Pages (~10 min)
1. Create a new **public** repo on GitHub, e.g. `ai-from-scratch`.
2. Upload these files to the repo root (drag-and-drop in the GitHub web UI works).
3. Repo → **Settings → Pages** → Source: **Deploy from a branch**, branch `main`, folder `/root`. Save.
4. Tick **Enforce HTTPS** once it becomes available (can take an hour or so).

Your site will be available at `https://<github-username>.github.io/<repo-name>/`.

## Adding a new module later
Copy `module-2.html` to `module-3.html`, swap in the new content, then in `index.html`
change that module's `<span class="stop soon">` to `<a class="stop live" href="module-3.html">`
and update the node from a number to `✓`. Commit. Done.
