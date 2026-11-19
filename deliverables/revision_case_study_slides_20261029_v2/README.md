# Revised lifecycle case study — internal meeting, v2

This version replaces the metric-dashboard narrative with the scientific argument of the updated Section 5: what the original lifecycle demonstration intended, what the existing U-Net study now supports, and the evidence required to finish that demonstration.

The seven slides follow one coherent sequence: planned lifecycle and evidence; controlled stress/update design; rare-plume spatial example; joint historical/rare RMSE tradeoff; controller decision screen; validation boundary; and the next known-change-to-validated-update experiment.

There are no bar charts or literature-review slides. Each slide contains one scientific image. The spatial triplet is a faithful crop of manuscript Figure 2(b), preserving its pixels, axes, aspect ratio, and colorbars. It is an example of baseline error, not a reproduced update result. The two scatter plots use separate reported comparisons from manuscript Figures 4 and 5.

Files:

- Updated_case_study_20261029_v2.pptx: native PowerPoint with embedded notes.
- Updated_case_study_20261029_v2.pdf: Microsoft PowerPoint export.
- previews/contact_sheet.png: all seven slides.
- speaker_notes.md: source qualifications and speaking notes.
- FIGURE_AUDIT.md: scientific audit and source treatment.
- figures/: regenerated diagrams/scatter plots and faithful source crop.
- sources/: numerical tables, source hashes, and crop provenance.
- qa/: structural, rendering, source-preservation, and delivery checks.

The previous deck, report, original manuscript, and frozen Section 5 remain unchanged.

Rebuild with python3 scripts/build_deck.py, then render_powerpoint.ps1 and verify_delivery.py. Dependencies are NumPy, Matplotlib, python-pptx, Pillow, lxml, and PyMuPDF.
