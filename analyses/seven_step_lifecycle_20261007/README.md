# Seven-step lifecycle evidence package

**Execution date:** 2026-10-07  
**Scope:** evidence-led update of the Task 1 report using Yilin's adaptive-replay U-Net results.  
**Lifecycle:** MONITOR -> DETECT -> DECIDE -> PREPARE -> UPDATE -> CALIBRATE -> DEPLOY.

## Purpose

This package records the quantitative contract in the authoritative Task 1 report, the results that are explicitly reported in Yilin's manuscript, calculations that can be derived from those rounded values, and the evidence still required to claim a completed lifecycle demonstration.

The package is intentionally conservative: manuscript-reported values are not presented as independently reproduced, and framework criteria are not presented as measured results. The withdrawn FY26 data-package discussion is excluded.

## Contents

- `execution_log.md`: dated work log and decisions.
- `source_manifest_sha256.csv`: source hashes and extraction provenance.
- `source_extracts/quantitative_contract.csv`: report-defined quantities with printed page/section anchors.
- `source_extracts/yilin_reported_results.csv`: manuscript-reported values and locations.
- `derived/reported_value_calculations.csv`: arithmetic derived from rounded manuscript values; not new experimental evidence.
- `experiment_inventory.csv`: evidence inventory, status, and blockers for each lifecycle step.
- `lifecycle_evidence_matrix.csv`: claim-level routing to report language.
- `analysis_specification.md`: frozen analysis and data requirements for completing missing steps.
- `inconsistency_register.csv`: unresolved source/configuration conflicts that must not be silently merged.
- `source_extracts/original_unet_lineage.md`: bounded read-only inspection of related original U-Net scripts; lineage is not assumed to be Yilin's implementation.

## Status at package creation

The adaptive-replay manuscript supplies strongest direct evidence for the UPDATE step and a retrospective rare-regime stress condition useful for MONITOR/DETECT. It does not, by itself, provide independently verified uncertainty calibration, detector operating characteristics, active-learning selection records, an untouched final-test promotion record, or a model-version deployment decision. Those gaps are recorded explicitly.

## Actual quantitative analysis completed from available artifacts

The embedded figures in the Yilin DOCX were extracted and analyzed. See `derived/figure_analysis_summary.md` for the numerical interpretation and the CSV files for the calculation inputs and outputs. This adds actual figure-level analysis to the manuscript-reported RMSE table. It still does not substitute for raw-prediction analysis: the figures provide rounded aggregate labels, not trajectory-level samples, seeds, or uncertainty outputs.

The five extracted figures are preserved under `source_extracts/embedded_figures/` with SHA-256 hashes in `source_extracts/embedded_figure_hashes.txt`.
