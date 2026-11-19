# Yilin results mapped to the seven-step prototype workflow

## Purpose

This note routes the existing adaptive-replay results into the report update for the pump-and-treat U-Net prototype. It separates measured results in Yilin's manuscript from workflow evidence that still needs to be generated or documented.

Primary source:

- `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx`

Report destinations:

- `drafts/final/section5_FINAL.md`
- `drafts/final/section2_2_FINAL.md`
- `drafts/final/section3_FINAL.md`

## Existing measured results

The manuscript describes a 128 x 100 two-dimensional pump-and-treat plume prototype with one to five extraction wells, varied pumping rates, and plume snapshots at days 0 through 4 from 10,000 physics-based simulation runs.

The regime partition is based on the sequential Mass90 footprint-change score. The historical regime is the bottom 40 percent of the score distribution, and the rare high-change regime is the top 3 percent. This is a response-based offline partition; it is not yet an operational detector based directly on incoming pumping or monitoring data.

Reported model-update results are:

| Configuration | Historical-regime result | Rare-regime result | Interpretation |
|---|---:|---:|---|
| Baseline U-Net | RMSE 0.58 micrograms/L | RMSE 10.04 micrograms/L | Static model degrades on rare high-change cases |
| Simple fine-tuning | RMSE 1.11 micrograms/L | RMSE 3.92 micrograms/L | Rare-regime improvement with substantial historical loss |
| Fixed replay | RMSE 1.03 micrograms/L | RMSE 1.21 micrograms/L | Stronger old/new tradeoff than simple fine-tuning |
| EWC | RMSE 5.45 micrograms/L | RMSE 1.22 micrograms/L | Rare-regime improvement with unacceptable historical degradation in this configuration |
| Adaptive replay | Historical degradation reduced from 80.4% to 26.5% in the reported comparison | Rare-regime improvement reported as greater than 85% | Promising controller result, but the matched fixed-replay comparison and exact test provenance must be confirmed |

The manuscript also reports that the adaptive replay ratio reached its imposed upper cap. That result supports a high-replay update under the tested controller and does not, by itself, isolate the benefit of adaptive scheduling.

## Quantitative values already defined in the early report

The early report supplies the quantitative contract that the updated Section 5 should use:

- Prediction interval coverage probability near **90%**.
- Drift persistence of approximately **60–90 days**, or earlier action when a documented regime change occurs.
- **6–10** high-value physics simulations for a simulation-driven active-learning update.
- Historical replay of approximately **70–75%** of the update batch.
- Drift-detection evaluation using sensitivity/true-positive rate, specificity/true-negative rate, false alarms, and warning lead time.
- Surrogate inference speedup on the order of **10^3–10^5** relative to physics simulation as a framework target/context.
- RMSE and related error thresholds at priority monitoring locations, with the actual limit set by intended use.
- Spatial and temporal consistency with the physics reference and absence of systematic bias at decision-relevant boundaries.

These are not all measured Yilin results. The report update must label them as acceptance criteria, operating rules, or expected targets until the U-Net evidence package evaluates them.

## Workflow evidence map

| Workflow step | What the existing results support | Evidence status | Work needed for the report |
|---|---|---|---|
| **MONITOR** | Historical and rare-regime RMSE, plume error maps, Mass90 behavior, and regime-separated performance comparisons provide diagnostic measures. | Partial | Recast the evaluations as monitoring windows and provide the metric definitions, counts, seeds, and trajectory-level summaries. |
| **DETECT** | The Mass90 score identifies high-change cases and shows that the static surrogate performs poorly in that regime. | Partial | Document the trigger rule before evaluation, persistence/window logic, and whether the trigger is based on operational inputs, observations, or the response-derived Mass90 score. |
| **DECIDE** | The acceptance-region analysis provides an old-regime degradation limit and a rare-regime improvement requirement. | Partial | Freeze one acceptance contract and create a decision record stating why the update was approved. Resolve the manuscript's 25%, 30%, 85%, and 1.05x/0.80x criteria. |
| **PREPARE** | The selected rare-regime samples plus historical replay samples form a controlled update dataset. | Partial | Add a split/provenance manifest and label this as regime-selected preparation. Do not call it active learning unless candidate scoring and selection were actually run. |
| **UPDATE** | Fine-tuning, fixed replay, EWC, and adaptive replay directly exercise the update step. | Strongest evidence | Reconcile model labels, exact trainable layers, replay ratios/caps, epochs, seeds, update budget, and matched exposure across comparators. |
| **CALIBRATE** | The manuscript reports point-prediction and plume metrics, but no uncertainty coverage or reliability results. | Not demonstrated | Use existing raw predictions to perform post-hoc uncertainty calibration if available, or mark this step as a planned prototype extension. Do not infer UQ calibration from RMSE. |
| **DEPLOY** | The acceptance-region figure gives a proposed promotion rule and the manuscript discusses continued use. | Partial | Evaluate the chosen candidate on an untouched final test set, record pass/fail, create a model-version record, and document the deployment or escalation decision. |

## Recommended report framing

Use the existing results as a **controlled seven-step prototype case study**, with the evidence level stated for each step. The report can claim that the Yilin results provide the technical core for the PREPARE and UPDATE portions and a preliminary basis for DETECT, DECIDE, and DEPLOY acceptance logic. It should claim full lifecycle execution only after the missing trigger record, uncertainty-calibration evidence, final-test record, and model-version decision are added.

The report should not copy the manuscript's illustrative thresholds as if they were already approved. Select one acceptance contract before the final test. If the values remain exploratory, label them as sensitivity scenarios and remove the word “redeploy” from the associated result claim.

## Minimum additions needed to complete the lifecycle demonstration

1. Preserve complete trajectories and create a manifest for training, controller validation/calibration, and untouched final-test partitions.
2. Define one controlled drift event or high-change evaluation window and record when the detector changes state.
3. Create a DECIDE record that selects the update pathway and acceptance contract.
4. Archive the PREPARE dataset manifest, including the rare cases and replay samples used for the update.
5. Re-run or verify the adaptive and fixed-replay comparisons with matched update budgets and seeds.
6. Add uncertainty calibration using stored predictive samples, ensembles, dropout outputs, or another declared UQ source.
7. Evaluate the selected candidate once on the untouched final test and record promotion, rejection, or escalation.

Until items 1, 3, 6, and 7 are complete, the report should describe the work as a strong controlled update demonstration with a lifecycle-oriented protocol, rather than as completed evidence for every operational step.
