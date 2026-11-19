# Quantitative lifecycle analysis of Yilin's pump-and-treat U-Net results

**Analysis date:** 2026-10-07  
**Sources:** Task 1 final report and Yilin's adaptive-replay DOCX.  
**Analysis type:** figure-level and manuscript-value quantitative analysis; raw prediction files for the adaptive-replay study were not available in the repository.

## Result

The available evidence supports a controlled lifecycle reconstruction through the update decision. It does not show a completed operational cycle because the study does not provide detector operating characteristics, uncertainty calibration, or an untouched final-test promotion record.

The model failure is concentrated in the response regime selected by the Mass90 footprint-change score. The manuscript labels the 40th-percentile cutoff as **0.133** and the 97th-percentile cutoff as **0.329**. The rare cutoff is therefore **2.47 times** the historical cutoff. This is a retrospective response classification: it uses consecutive reference plume states and does not identify an operational cause or provide a prospective warning time.

## MONITOR: baseline reliability loss

The manuscript reports baseline historical/rare RMSE of **0.58/10.04 µg/L**. Figure 4 additionally labels baseline rare plume-mass error **32.30%**, rare peak error **14.20%**, and rare Mass90 error **7.11%**. These values define the monitoring signal: the rare regime is not only a pixelwise accuracy problem; it also changes plume quantities relevant to pump-and-treat decisions.

Relative to the displayed baseline, fixed replay reduces rare RMSE by **87.9%**, rare plume-mass error by **94.4%**, rare peak error by **75.8%**, and rare Mass90 error by **73.4%**. Its historical RMSE increases **77.6%**. EWC gives similar rare-regime reductions but increases historical RMSE by **839.7%**. Simple fine-tuning reduces rare RMSE by **61.0%** and increases historical RMSE by **91.4%**. The calculation inputs and outputs are in `derived/figure4_metric_values.csv` and `derived/figure4_metric_changes.csv`.

## DETECT: controlled stress condition

The Mass90 score creates a controlled high-change stress condition for the DETECT step. It shows that the static model is unreliable for the top response tail and gives a reproducible retrospective label for evaluating updates. It does not provide sensitivity, specificity, false-alarm rate, or warning lead time. The four-day sequence has only four transitions, so it cannot support the Task 1 report's 60–90-day persistence requirement or robust rolling variance/autocorrelation estimates.

The correct quantitative conclusion is that the response-derived Mass90 partition supports a stress-test detector label. A prospective detector analysis still requires ordered trajectories with known onset times, a threshold frozen on calibration data, and independent trajectories for operating-characteristic estimates.

## DECIDE: old/new tradeoff

The decision question is whether rare-regime improvement justifies historical-regime degradation. Figure 5 provides an illustrative contract: historical degradation no greater than **30%** and rare improvement at least **85%**. Applying that contract to the four plotted controller outcomes gives:

| Controller | Historical degradation | Rare improvement | Decision under Figure 5 rule |
|---|---:|---:|---|
| Fixed replay | 80.4% | 88.9% | Reject: retention fails |
| Threshold adaptive forgetting | 26.5% | 85.8% | Passes two plotted checks |
| Loss-balanced | 21.1% | 85.5% | Passes two plotted checks |
| Loss-balanced + floor | 38.1% | 87.3% | Reject: retention fails |

The margins to the two boundaries are quantified in `derived/figure5_acceptance_margins.csv`. Threshold adaptive forgetting clears the historical boundary by 3.5 percentage points and the rare boundary by 0.8 points. Loss-balanced clears them by 8.9 and 0.5 points. Fixed replay misses historical retention by 50.4 points, and loss-balanced-plus-floor misses it by 8.1 points.

This is a controller-specific screening result. It does not support the general statement that adaptive replay passes. The acceptance values are illustrative in the manuscript and are not a recorded preregistered decision contract.

## PREPARE: regime-selected update data

The study prepares an update set from the top-3% rare response regime and historical replay from the bottom-40% regime. That is sufficient to test stability and plasticity. It is not evidence of the Task 1 active-learning procedure because no candidate-pool scores, diversity constraints, information-gain values, or 6–10-run selection record is provided.

The report should call this **regime-selected preparation**. A future active-learning run can be compared with random selection using the same physics-run budget and an untouched evaluation set.

## UPDATE: method comparison

The update comparison is the strongest completed portion of the lifecycle. Simple fine-tuning, fixed replay, EWC, and adaptive controller variants show the expected stability–plasticity tradeoff. Fixed replay provides the strongest balanced result among the Figure 4 configurations, but Figure 5's fixed-replay controller result fails the illustrative retention boundary because its percentage calculation comes from a different controller comparison. These panels must remain separate until the figure-generation data reconcile their denominators, splits, and exposure.

The replay trajectory reaches **r = 0.8** and remains at that cap for most of the 100 plotted epochs. The result demonstrates high replay exposure in the displayed adaptive run. It does not isolate the value of adaptive scheduling. A fixed-replay-at-0.8 comparison with matched seed, update budget, and historical exposure is required for that causal claim.

Figure 3 adds a full-network pair of **0.64/0.99 µg/L** historical/rare RMSE, compared with decoder-only **1.11/3.92 µg/L**. Relative to its displayed baseline of 0.58/10.04, the full-network pair is a 10.3% historical increase and a 90.1% rare reduction. The pair is not merged into the Figure 4 ranking because the manuscript uses conflicting Model C labels and does not establish protocol equivalence.

## CALIBRATE: missing uncertainty result

The Task 1 contract requires prediction-interval coverage near **90%**, interval-width reporting, reliability analysis, and held-out calibration data. The adaptive-replay manuscript provides point predictions and physical error metrics but no predictive intervals, ensemble/dropout outputs, conformal scores, calibration set, or reliability diagram. Consequently, no numerical CALIBRATE result can be inferred from the RMSE improvements.

The lifecycle state after UPDATE is therefore “candidate awaiting calibration.” The candidate cannot move to DEPLOY based on the reported point metrics alone.

## DEPLOY: promotion is blocked by evidence, not by model accuracy alone

The Task 1 DEPLOY gate requires an untouched final test, comparison against the baseline, uncertainty checks, spatial and temporal consistency, provenance, and a model-version record. None of those final promotion artifacts is present for the adaptive-replay result. The correct reconstructed action is to hold the candidate in governed evaluation and return to calibration or further preparation.

This is a useful lifecycle result: the quantitative update analysis produces a candidate-selection decision, then the workflow stops at the calibration/deployment gate because the required uncertainty and final-test evidence are absent. That is stronger and more defensible than calling the update “deployed.”

## Scope and unresolved comparisons

Figure 3(a) displays a different baseline pair, 0.49/9.20 before and 0.67/1.20 after fine-tuning, than Figure 4's 0.58/10.04 baseline. Figure 3(c) labels a full-network result as Model C, while the manuscript's update table uses Model C for replay and the Task 1 report uses Model C for from-scratch retraining. The percentage claims of 80.4%, 26.5%, and 88.9% also do not exactly reproduce from the rounded RMSE labels. These are protocol-resolution issues, not arithmetic errors to be silently corrected.

The next raw-artifact requirement is specific: obtain the executed adaptive-replay code/configuration, trajectory split manifest, per-run predictions or metric arrays, controller logs, seeds, checkpoints, and any UQ outputs. Those artifacts would permit independent trajectory-level uncertainty estimates, detector operating characteristics, calibration, and a final promotion decision.
