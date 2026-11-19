# Integrated report revision — October 28, 2026

This is a complete review draft built around the seven-step lifecycle and the available offline U-Net/adaptive-replay evidence. It distinguishes demonstrated results from illustrative criteria and future validation requirements.

- `Framework_revised_20261028.docx`: clean reading and editing copy.
- `Framework_revised_20261028.pdf`: 77-page Microsoft Word export.
- `Framework_revised_20261028_tracked.docx`: native Word comparison against the preserved `final report/Framework_revision.docx` source.
- `REVIEW_DECISIONS.md`: three consolidated scientific decisions, with recommended bounded treatments already applied.
- `COMMENT_DISPOSITION.md`: treatment of the source comments and additional consistency corrections.
- `figures/`: nine replacement figures in PNG, SVG, and PDF. Only labels, axes, and legends appear inside the figures; explanations are in report captions.

For one focused review, read the Summary, Section 6.4, and Section 5, then address the three items in `REVIEW_DECISIONS.md` together. Prospective detector evaluation, independent uncertainty calibration, and final deployment validation remain research requirements.

The original reports, manuscript, and frozen Section 5 were preserved and their hashes verified. Both delivered DOCX files open in Microsoft Word. The clean file has no comments or revisions. Rejecting the 581 comparison revisions restores the original text; accepting them and updating the contents restores the revised text exactly. The final PDF was checked for layout, figure presentation, broken fields, and visible placeholders.

## Rebuild and verification

The working sources are `section5_20261028.md`, `sources/`, and `scripts/`. Use `build_report.py`, then run `finalize_word.ps1 -SkipComparison`, `export_pdf.ps1`, `compare_word.ps1`, `verify_word_package.ps1`, and `verify_package.py` in that order. Figure regeneration uses `make_figures.py`. The PowerShell scripts require Microsoft Word on Windows; report assembly and figure generation run in WSL.

Python dependencies include python-docx, lxml, NumPy, Matplotlib, PyMuPDF, and Pillow. The scripts currently include the temporary session dependency directory as a fallback; install these packages in a persistent Python environment for later rebuilds.

Verification records and delivery hashes are in `qa/final_verification.json`, `qa/word_verification.json`, `qa/comparison_verification.json`, and `qa/delivery_sha256.json`.
