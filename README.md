# loe-posit

Quarto manuscript project with Python Jupyter notebooks, ready for:

- Publishing from GitHub to Posit Connect Cloud.
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

## Publish to Posit Connect Cloud (GitHub Source)

1. Push this repository to GitHub.
1. In Posit Connect Cloud, create new content from GitHub.
1. Select repository `mrchristian/loe-posit`, branch `main`, and configure as Quarto content.
1. Trigger initial deployment.
1. Future pushes to `main` auto-redeploy.

Notes:

- `_publish.yml` is generated when using `quarto publish` CLI flow. If used later, commit `_publish.yml` so destination metadata is shared across collaborators.
- Never commit account tokens or credentials.

## MyBinder

Launch Binder (after pushing to GitHub):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mrchristian/loe-posit/main?urlpath=lab/tree/notebooks)

Binder uses:

- `requirements.txt` for Python package installation.
- `runtime.txt` for Python version pinning.

Binder is intended for interactive notebook execution. Quarto rendering is
validated by CI and local development setup.

## CI

This project includes GitHub Actions workflows to:

- Execute notebooks and render-check Quarto content on pushes and PRs.
- Optionally publish to Posit Connect Cloud via a manual workflow dispatch.
