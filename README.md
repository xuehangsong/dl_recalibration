# Deep Learning Recalibration

This repository contains the DOE-EM deep-learning recalibration framework, its report revisions, the audited adaptive-replay case study, and the TTP scope extension for the next demonstration.

## Current evidence

The strongest completed technical evidence is the controlled offline pump-and-treat U-Net update study. The audited results support baseline monitoring, a retrospective high-change stress label, old/new candidate screening, regime-selected preparation, and update comparisons. Uncertainty calibration, prospective trigger performance, untouched final testing, and deployment approval remain future evidence requirements.

## Active paths

- `drafts/final/section5_FINAL.md` contains the current reader-facing Section 5.
- `drafts/final/section5_FINAL_20261008_FROZEN.md` preserves the dated Section 5 snapshot used for provenance.
- `plans/yilin_results_seven_step_evidence_map.md` maps reported results to the seven workflow steps and lists the missing records.
- `analyses/seven_step_lifecycle_20261007/` contains source extracts, calculations, evidence matrices, and the execution log.
- `deliverables/report_revision_20261028/` contains the integrated report package and verification records.
- `deliverables/revision_case_study_slides_20261029_v4/` contains the current audited case-study deck and source companion.
- `method_manuscript/` contains the selected manuscript source and the review records.
- `TTP/` contains the revised FY27 scope, tracked comparison, and native Word QA records.
- `reviews/` contains the weekly and Q4 status-review packages.
- `archive/20261118_superseded/` contains intermediate derivatives retained for provenance.

## Verification

The report package and slide package each include their own rebuild and verification instructions. The v4 deck checks source hashes, numeric values, native PowerPoint shape editability, notes, layout bounds, and source-image fidelity. The manuscript lineage audit checks the 22 retained and archived Word derivatives against the selected source figures and captions.

The project currently contains planning and evidence-audit work. The next technical milestone is an executed trigger-and-recalibration demonstration using simulated monitoring observations, before-and-after predictions, an independent calibration set, and a final-test decision record.
