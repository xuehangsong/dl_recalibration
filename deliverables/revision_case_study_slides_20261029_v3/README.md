# Updated case study — internal meeting, v3

Nine slides connect the planned lifecycle to the updated U-Net results: controlled stress selection, spatial baseline error, adaptation–retention tradeoff, physical plume metrics, replay feedback, controller screening, and remaining validation.

The five flowcharts (slides 1, 2, 6, 8, 9) are native editable PowerPoint objects. Each diagram is grouped for moving/resizing; enter the group or ungroup it to edit individual boxes, labels, and attached connectors. The four scientific-figure slides retain high-resolution images. Editable flowcharts do not depend on SVG conversion or screenshots.

## Delivery

- `Updated_case_study_20261029_v3.pptx`: presentation with editable diagrams and embedded notes.
- `Updated_case_study_20261029_v3.pdf`: Microsoft PowerPoint export.
- `previews/contact_sheet.png`: slide overview.
- `speaker_notes.md`: source qualifications and speaking notes.
- `sources/evidence_audit.md`: fresh audit of the original manuscript, including equations, tables, and captions.
- `FIGURE_AUDIT.md`: figure treatments and evidence boundaries.
- `qa/`: structural, native-rendering, and delivery verification.

## What changed from v2

The flowcharts now have native boxes, text, and connectors that stay attached when nodes move. The new physical-metrics slide replots the reported mass, peak, and Mass90 errors as aligned scientific dot plots. The new replay loop explains how historical and rare validation signals inform the next training mix. Direct manuscript anchors and limitations are included in notes.

The manuscript audit also identified changes in trainable layers across configurations, inconsistent acceptance thresholds, and an incomplete controller equation. The deck keeps claims configuration-specific, retains the Figure 5 screen as illustrative, and represents feedback conceptually. Figure 4 and Figure 5 remain separate comparisons. No unreported uncertainty, test result, deployment, detector trajectory, or causal scheduling gain is added.

## Rebuild

Run `python3 scripts/build_deck.py`, render using `powershell.exe` with `scripts/render_powerpoint.ps1`, and run `python3 scripts/verify_delivery.py`. Dependencies: NumPy, Matplotlib, Pillow, python-pptx, lxml, PyMuPDF, and Microsoft PowerPoint for native rendering. Scripts use the installed fallback at `/tmp/dl_slides_20261029_python` and the established evidence-deck-builder helper.

The v2 deck, source manuscript, report, and frozen Section 5 are preserved and checked by SHA-256.
