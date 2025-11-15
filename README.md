# Blueprint Takeoff Training Manual

This repository contains a complete Markdown-based training manual that teaches Ritter Lumber (and similar lumberyard) salespeople how to perform blueprint takeoffs for residential projects. Each chapter lives under `docs/` and walks through blueprint orientation, framing, roofing, siding, foundation, schedules, conversions, a full worked example, and printable worksheets. The content is designed for PDF export so it can be handed to new hires on day one.

## Documentation Layout
```
docs/
├── 01-introduction.md
├── 02-blueprint-orientation.md
├── 03-floor-plan-reading.md
├── 04-wall-framing-takeoff.md
├── 05-roof-takeoff.md
├── 06-elevations-and-siding.md
├── 07-foundation-and-concrete.md
├── 08-window-and-door-schedules.md
├── 09-material-conversion-tables.md
├── 10-full-example-house-takeoff.md
├── 11-master-worksheets.md
├── Blueprint-Takeoff-Manual.md   # combined, print-ready manual
└── img/
    └── README.md                 # diagram production notes
```

## Generate the PDF Locally
Install Pandoc plus a LaTeX engine (e.g., `sudo apt-get install pandoc texlive texlive-xetex`). Then run:

```bash
pandoc docs/Blueprint-Takeoff-Manual.md \
  -o Blueprint-Takeoff-Training-Manual.pdf \
  --from=markdown \
  --pdf-engine=xelatex \
  --toc
```

The resulting `Blueprint-Takeoff-Training-Manual.pdf` will appear in the repository root (or whichever output path you choose).

## GitHub Actions Build
A workflow at `.github/workflows/build-manual.yml` installs Pandoc/LaTeX, renders the PDF, and uploads it as an artifact whenever documentation files change (push, pull request, or manual dispatch). Trigger it from the Actions tab to obtain a fresh PDF without setting up a local toolchain.
