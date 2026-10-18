# John Baldessari — Exhibition Catalogue

Quarto manuscript project with Python Jupyter notebooks, ready for:

- Publishing from GitHub Pages.
- Interactive notebook execution on MyBinder.

## GitHub Codespaces

Open the project in GitHub Codespaces:

[Launch in GitHub Codespaces](https://codespaces.new/NFDI4Culture/John-Baldessari-Exhibition-Catalogue)

This provides a ready-to-use cloud development environment for the Quarto and notebook workflow without requiring local installation.

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

## Licensing and rights

This project combines different rights regimes:

- Code, Quarto source, and other project software assets are covered by the repository's existing license in [LICENSE](LICENSE), which is the GNU General Public License v3.0.
- Data files in the project, including the OCR-derived catalogue and exhibition dataset, are released under the [Creative Commons CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) dedication and the repository copy of the deed is in [LICENSE-data](LICENSE-data). This means the data may be used, copied, modified, and redistributed without restriction for any purpose, including research and scholarship.
- Where third-party material is included, rights should be checked against the source institution or rights holder. The project is intended primarily for research, teaching, and data work.

The project also notes a text and data mining (TDM) context for research use. Under UK law, the Copyright, Designs and Patents Act 1988 contains research-oriented TDM provisions for lawful access to material; under German law, the copyright exception in § 60d UrhG covers text and data mining for scientific research, subject to the relevant conditions and source rights. These exceptions are jurisdiction-specific and are not legal advice; readers should confirm the applicable terms when using material that is not expressly in the public domain or otherwise clearly licensed.

## Project Layout

- `index.qmd`: manuscript article source.
- `_quarto.yml`: manuscript project configuration.
- `notebooks/`: supporting Jupyter notebooks.
- `requirements.txt` and `runtime.txt`: reproducible Python environment for Binder.

## Publish to GitHub Pages

1. Render locally:

```bash
quarto render
```

1. Commit your changes.
1. In repository Settings, open Pages and set Source to GitHub Actions.
1. Push to `main`.
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
- Publish the rendered manuscript to GitHub Pages on pushes to `main`.


