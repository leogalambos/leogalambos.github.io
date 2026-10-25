# Leo Galambos — personal GitHub Pages

A responsive, compact personal research and engineering portfolio based on **MkDocs Material**, with a photographic hero inspired by the supplied reference and a seven-card project grid.

## Quick start

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m mkdocs build --strict
python -m mkdocs serve
```

Deployment: GitHub repository `leogalambos.github.io`, branch `main`; `Settings → Pages → GitHub Actions`. On each push the workflow builds with `--strict` and deploys `site/`.

Projects: JAI, EGOTHOR v4, J7M, Radixor, ZeroEcho, conflux and MethodAtlas; publications are collocated under project pages. MethodAtlas is described as work originating in Egothor and later adapted for commercial use. No employer affiliation or endorsement is claimed.

External photography is not loaded at runtime. Assets and SVG are bundled in the repository. Contact and project navigation require no JavaScript beyond what MkDocs Material provides.

## Conservative header (v6)

The design uses an actual MkDocs Material header partial in `overrides/partials/header.html`, **not** a static screenshot or imitation. The desktop header is one row with Leo Galambos, Home / Projects / Profile / Contact, native Material search, palette switch, and a compact GitHub icon. The mobile drawer is the native Material drawer. Academic credentials appear only on the profile page, not in the topbar, homepage hero, or footer.

No `navigation.tabs` is enabled. Header-specific styles reside in `docs/assets/css/header.css`. To verify actual deployment, run `python -m mkdocs build --strict`; `tests/test_structure.py` includes header invariants.

## Patch 6.1 — MkDocs 404 rendering

The header is now safe when MkDocs Material builds `404.html` with `page=None`, or when a template renders without `page` in the context. `overrides/partials/header.html` computes `current_url` and `is_home` before navigation and does not directly dereference a missing page. A regression test renders the real header partial under strict Jinja undefined-variable behavior for 404, missing page, homepage, project, profile and contact routes.
