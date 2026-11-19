# Execution log — seven-step lifecycle evidence package

## 2026-10-07

- Confirmed working repository and preserved unrelated untracked files.
- Used the final Task 1 PDF as the authoritative report source and `Adaptive_Replay_Manuscript_2026_09_09.docx` as Yilin's source manuscript.
- Recorded SHA-256 hashes in `source_manifest_sha256.csv`.
- Frozen report quantitative contract: near-90% interval coverage; site/use-specific error limits; spatial/temporal consistency and no systematic boundary bias; 60–90-day persistence or documented regime change; 6–10 selected physics simulations; 70–75% historical replay guidance; detector sensitivity, specificity, false alarms, and warning lead time; 10^3–10^5 speedup as a framework context/target requiring measurement; tipping-point-inspired variance/autocorrelation/skewness/kurtosis and distributional/latent diagnostics without a universal critical threshold.
- Extracted Yilin's reported setup and results: 128 x 100 mesh, one–five extraction wells, 10,000 nominal physics runs; historical bottom 40% and rare top 3% based on response-derived Mass90 footprint-change score; baseline, fine-tuning, fixed replay, and EWC RMSE values; adaptive-replay percentage claims and cap behavior.
- Calculated ratios and percentage changes only from displayed rounded RMSE values. These calculations are labeled derived and cannot resolve protocol differences in the manuscript's percentage figures.
- Inspected the related original U-Net package under `/home/song884/github/dvz_optimization/unet_ms/` in read-only mode. It documents 10,000 simulation generation and 2D preprocessing, but no evidence here establishes that its scripts are the current adaptive-replay implementation. Source-code lineage is therefore recorded as contextual only.
- Excluded the FY26 data-package contradiction per user instruction.

## Evidence decision

The report may state that Yilin's results exercise the UPDATE step and provide a controlled retrospective stress case for MONITOR/DETECT/DECIDE/PREPARE. It must not state that the complete seven-step lifecycle has been quantitatively executed until the missing UQ calibration, detector metrics, independent split/provenance, and DEPLOY decision artifacts are supplied.

## Next pickup

Obtain the adaptive-replay code/configuration, raw predictions or per-run metric exports, controller logs, split manifest, and model checkpoints. Freeze the acceptance contract before evaluating an untouched final test. Then run the analysis specification in `analysis_specification.md` and update the report from the resulting artifacts.
- Recomputed the rounded-value arithmetic with `derived/recompute_reported_values.awk`; output is archived as `derived/recomputed_values_check.csv`. The checks reproduce the calculations in `derived/reported_value_calculations.csv` and are explicitly not independent experimental results.
- Read the repository's prior adaptive-replay review memory during this execution. It confirms the defensible scope is a controlled offline UPDATE study and requires trajectory-level splits, an untouched final test, matched budgets/exposure, and provenance before stronger lifecycle claims.
- Updated the revision-system Change Log with this evidence-audit task and refreshed its SHA-256 entry in the source manifest.

## 2026-10-07 — embedded-figure quantitative pass

- Extracted all five embedded PNG figures from the authoritative Yilin DOCX and recorded hashes in `source_extracts/embedded_figure_hashes.txt`.
- Read numeric labels from Figures 1, 3, 4, and 5. Added `derived/figure4_metric_values.csv`, `derived/figure4_metric_changes.csv`, `derived/figure5_controller_values.csv`, and `derived/figure_analysis_summary.md`.
- Figure 1 gives Mass90 thresholds of 0.133 at the 40th percentile and 0.329 at the 97th percentile; the rare cutoff is 2.47 times the historical cutoff.
- Figure 4 shows large rare-regime gains in mass/peak/Mass90 metrics for fixed replay and EWC, but severe historical-regime degradation for EWC. The calculations are from displayed rounded labels.
- Figure 5 has four controller outcomes. Under its plotted 30% historical-degradation and 85% rare-improvement gate, threshold adaptive forgetting and loss-balanced pass; fixed replay and loss-balanced-plus-floor fail. The adaptive trajectory reaches replay ratio 0.8 and stays at the cap for most of 100 epochs.
- Figure 3 reports a full-network 0.64/0.99 historical/rare RMSE pair. This result is not merged with Figure 4 because model naming, split, and protocol are unresolved.
- Bounded read-only Deception checks found the original Song U-Net dataset and model-output directories, including multi-gigabyte arrays and H5 models. No adaptive-replay artifacts were located by the completed bounded output inventory. A broad filename search was stopped before completion; no claim is made from that incomplete search.
- Added `results_report.md` as the substantive quantitative lifecycle analysis. It reconstructs the evidence -> criterion -> action trace and records the governed hold at CALIBRATE/DEPLOY caused by missing uncertainty and final-test artifacts.
- Rewrote `drafts/final/section5_FINAL.md` into a single connected case-study story. The new section follows observed baseline failure -> Mass90 stress detection -> old/new decision screen -> regime-selected preparation -> update comparison -> calibration hold -> deployment state.
- Preserved the prior Section 5 version as `section5_before_full_rewrite.md` in the dated package.
- Added Task 10 to the revision change log.
- The final copy-edit supersedes the earlier draft decision to retain U-FNO context: FNO content is removed from the Section 5 case-study text, while the three-mode evaluation context remains.
- Refreshed the revision-instructions source hash after the Task 10 change-log entry.

## 2026-10-08 — final reader-facing copy edit

- Re-read the complete Section 5 as an external report reader and confirmed that the narrative proceeds MONITOR -> DETECT -> DECIDE -> PREPARE -> UPDATE -> CALIBRATE -> DEPLOY.
- Removed FNO and internal-routing language from the case-study draft; the section is centered on the pump-and-treat U-Net evidence.
- Replaced prospective-sounding routine-monitoring wording with baseline-evaluation wording where the offline study cannot support operational monitoring claims.
- Added explicit UQ terminology, the framework's approximately 70–75% historical-replay guidance, and captions for the Figure 5 and Figure 4 quantitative tables.
- Kept Figure 5's 30%/85% screen explicitly illustrative and retained the governed hold at CALIBRATE/DEPLOY.
- Copied the final reader-facing text to `drafts/section5_yilin_results_update_draft.md`; the two Section 5 drafts are byte-for-byte aligned.

## 2026-10-08 — Section 5 version freeze and legacy-content disposition

- Preserved the approved U-Net lifecycle section as `drafts/final/section5_FINAL_20261008_FROZEN.md`.
- Confirmed the frozen snapshot matches `drafts/final/section5_FINAL.md` byte-for-byte; SHA-256: `ea4075935fced71a3abc39954f4de15fde04cbb3803537edaad40ac793aba563`.
- Recorded which earlier Section 5 material should remain archived, remain in framework/governance sections, move to future-work planning, or stay excluded from the current U-Net case study in `section5_legacy_content_disposition.md`.
- Future Section 5 edits must use a new dated file and must not overwrite the frozen snapshot.
- Updated the revision change log and source manifest for the freeze/disposition record.
