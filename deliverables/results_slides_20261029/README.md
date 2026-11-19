# Updated results — internal meeting

Seven slides focused on the U-Net/adaptive-replay results in the October 28 report revision. Each slide has one key image, a short claim, and a brief caption. Explanations and source qualifications are in embedded speaker notes and `speaker_notes.md`.

- `Updated_results_20261029.pptx`: PowerPoint with editable slide text and embedded notes.
- `Updated_results_20261029.pdf`: Microsoft PowerPoint export.
- `previews/`: individual slide previews.
- `figures/`: all seven figures in PNG, SVG, and PDF.
- `FIGURE_AUDIT.md`: numerical checks, replot decisions, and evidence boundaries.
- `sources/`: copied reported-value tables and source hashes.

Suggested presentation time: approximately 7–10 minutes. The sequence is baseline reliability → update comparison → additional plume metrics → controller screen → acceptance margins → comparison provenance → candidate status.

The deck synthesizes reported experiments. It adds no new training results or independently reproduced test estimates. The original report and frozen Section 5 remain unchanged.

Rebuild in WSL with `python3 scripts/build_results_deck.py`, using NumPy, Matplotlib, python-pptx, Pillow, and lxml. The script reuses the local evidence-deck-builder skill. Render with `powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/render_powerpoint.ps1` from this directory. PDF checks additionally use PyMuPDF. Session dependencies were installed under `/tmp/dl_slides_20261029_python`; use a persistent Python environment for later rebuilds.
