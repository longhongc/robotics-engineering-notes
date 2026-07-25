# Repository profile

Reinspect this repository on every curation run. This is the setup-time baseline.

## Authoring and rendering

- Canonical source notes are Markdown under `raws/<subject>/`.
- Generated MkDocs-compatible notes are under `docs/notes/`.
- Run `python format_raw_to_docs.py --clean` after source changes; do not edit generated note files manually.
- Notes use descriptive stable filenames, heading-first Markdown, lists, fenced code, and LaTeX. No front matter convention was found.
- Subject indexes such as `raws/<subject>/index.md` are hand-maintained and copied into generated docs.

## Site and CI

- `mkdocs.yml` uses the ReadTheDocs theme, MathJax-compatible arithmatex, superfences, details, and a permalinked TOC. It has no explicit `nav` or `site_url`.
- `.github/workflows/docs.yml` installs `requirements.txt`, regenerates docs, and runs `mkdocs build --strict --site-dir site` before GitHub Pages deployment on `main`.
- Non-Markdown assets such as images are canonical under `raws/` beside the source note, commonly `raws/<subject>/assets/`. The formatter copies them to the identical relative path under `docs/notes/`; CI uses `--clean` and runs `verify_generated_assets.py` to prevent stale or missing generated assets.
- No repository test directory, `AGENTS.md`, contributor guide, or existing Codex skill was present during setup.

## Validation

Run:

```bash
python format_raw_to_docs.py --clean
python verify_generated_assets.py
mkdocs build --strict --site-dir site
git diff --check
```

Use the existing repository `.venv` when available. Add or run other checks discovered on a future run.

## Remote

The local checkout uses `git@github.com:longhongc/robotics-engineering-notes.git` for fetch and push. Verify the remote and default branch before creating a branch or PR.
