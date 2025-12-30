# TT-E2 Docs & CI

Goal: practice “engineering hygiene”: documentation that builds, and CI that enforces it.

## Success criteria

- `mkdocs build` succeeds locally
- Navigation includes your new page
- CI “Docs” job is green on your branch/PR

## Local docs workflow

```bash
python3 -m pip install --break-system-packages mkdocs mkdocs-material
mkdocs build
mkdocs serve
```

## What to add
Add one small page that improves student success. Example topics:

* “Common build errors and fixes”
* “How to read sanitizer reports”
* “How to run benchmarks and interpret results”
