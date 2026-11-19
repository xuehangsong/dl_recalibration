# Updated case study — source-audited v4

The nine-slide presentation preserves v3's simple scientific style and five native editable flowcharts. All 28 numerical result values in the three replots come directly from the labels in Yilin's manuscript Figures 4(a) and 5(b). No experimental value was changed for v4. Source footers and embedded notes now identify the exact source panels and distinguish replotting, faithful cropping, native method diagrams, and planned work.

## Files

- `Updated_case_study_20261029_v4.pptx` / `.pdf`: main presentation.
- `Yilin_original_figures_20261029.pptx` / `.pdf`: five-slide source companion reproducing the original manuscript figures without alteration.
- `previews/contact_sheet.png`: main-deck overview.
- `AUDIT_REPORT.md`: numerical, scientific, and historical findings.
- `qa/numeric_value_ledger.csv`: value-level source trace and classification.
- `sources/original_figures/`: original embedded images and provenance manifest.
- `speaker_notes.md`: detailed interpretation and limits.

## Provenance

Primary empirical source: `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx`, SHA-256 `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`. The filename is a version identifier; it is not used to establish publication or an actual modification date. Word metadata identifies Fang, Yilin as author. The accepted-view text, original embedded images, October 7 transcription tables, revised report, and deck were compared.

Data trace: original manuscript image → manually transcribed displayed labels → archived CSV → Matplotlib replot → slide. The crop comes directly from original Figure 2(b). Native diagrams describe source methods, the report's lifecycle, or proposed validation, not additional experiments. The source companion deliberately preserves the paper's original labels, titles, and plotting conventions for inspection.

This is a verification against the available source record. The underlying adaptive-replay predictions, executed configurations, seeds, trajectory manifests, and metric-generation code are not in the inspected local evidence package, so the source experiments have not been independently reproduced.

The previous slides, original manuscript, revised report, frozen Section 5, and archived analysis CSVs remain unchanged. A separate `analyses/seven_step_lifecycle_20261007/ERRATA_20261029.md` corrects a legacy percentage interpretation.

## Rebuild

Run `python3 scripts/build_deck.py`, use PowerPoint through `scripts/render_powerpoint.ps1`, then run `python3 scripts/verify_delivery.py`. The source companion uses `scripts/build_source_companion.py` and `scripts/render_source_companion.ps1`. Python dependencies and the established evidence-deck-builder helper are the same as v3.
