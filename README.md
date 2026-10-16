# John Baldessari — Exhibition Catalogue

Quarto manuscript project with Python Jupyter notebooks, ready for:

- Publishing from GitHub Pages.
- Interactive notebook execution on MyBinder.

## Quick Start

1. Install Quarto (1.8+ recommended).
1. Create and activate a Python 3.11 environment.
1. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Render the manuscript:

```bash
quarto render
```

## Project Layout

- `index.qmd`: manuscript article source.
- `_quarto.yml`: manuscript project configuration.
- `notebooks/`: supporting Jupyter notebooks.
- `requirements.txt` and `runtime.txt`: reproducible Python environment for Binder.

## Publish to GitHub Pages

1. Push this repository to GitHub.
1. In repository Settings, open Pages and set Source to GitHub Actions.
1. Run the `github-pages-publish.yml` workflow (or push to `main`).
1. Future pushes to `main` auto-redeploy.

Notes:

- The publish workflow renders with Quarto and deploys the `_manuscript/` output to GitHub Pages.
- Never commit account tokens or credentials.

## MyBinder

Launch Binder (after pushing to GitHub):

https://mybinder.org/v2/gh/NFDI4Culture/John-Baldessari-Exhibition-Catalogue/main?urlpath=lab/tree/notebooks

If you fork this repository, update the Binder URL above to use your own GitHub owner/repository path.

Binder uses:

- `requirements.txt` for Python package installation.
- `runtime.txt` for Python version pinning.

Binder is intended for interactive notebook execution. Quarto rendering is
validated by CI and local development setup.

## CI

This project includes GitHub Actions workflows to:

- Execute notebooks and render-check Quarto content on pushes and PRs.
- Publish the rendered manuscript to GitHub Pages on pushes to `main` or via manual workflow dispatch.
