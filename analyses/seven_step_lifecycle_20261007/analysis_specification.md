# Frozen analysis specification for completing the seven-step evidence

This specification defines what must be present before the report can claim that the complete lifecycle was quantitatively executed. It is a design and audit contract, not a claim that these analyses have already run.

## 1. Data and split contract

- Treat a complete physics run/trajectory as the independent unit. Do not randomly split adjacent snapshots from one trajectory across training, calibration, and final test.
- Archive run IDs, input forcing (well count, locations, rates, schedule, boundary conditions), snapshot times, source physics-model version, preprocessing/normalization, and all random seeds.
- Freeze three disjoint roles before looking at final-test predictions: update training data, controller/UQ calibration and threshold-selection data, and untouched final test. If a trajectory is used for threshold selection, it cannot be counted as final-test evidence.
- Store exact model configuration, optimizer, epochs, trainable layers, replay ratio/cap, stopping rule, checkpoints, and hardware for each comparator.

## 2. MONITOR and DETECT

For every ordered test trajectory, compute concentration-field error, MAE/RMSE, bias, peak error, plume area/mass error, Mass90 error, threshold exceedance at decision-relevant locations, and uncertainty outputs if available. Preserve spatial maps and trajectory-level summaries.

Define the detector on calibration data before final testing. Candidate inputs may include operating-envelope distance, input/output KS or energy distance, latent Mahalanobis/reconstruction error, predictive variance, residual variance, lag-1 autocorrelation, skewness, and kurtosis. A composite detector must state normalization, reference period, threshold, persistence/window length, and state transitions.

Use long enough ordered sequences to estimate lead time. The report's 60–90-day rule is an operational governance requirement; it cannot be manufactured by relabeling four-day snapshots. Report sensitivity, specificity, false-alarm rate, warning lead time, and uncertainty intervals over independent trajectories or stress scenarios. Treat Mass90 as a retrospective response-derived stress label unless a prospective detector input is separately defined.

## 3. DECIDE and PREPARE

Before final-test evaluation, freeze one acceptance contract. At minimum include: (a) rare/high-change improvement target; (b) historical-regime maximum degradation; (c) priority-location error and boundary-bias limits; (d) UQ coverage tolerance around the near-90% target; (e) spatial/temporal consistency checks; and (f) required evidence for an operational-envelope change.

Create a versioned decision record containing trigger evidence, data-quality review, selected pathway, expected benefit/cost, reviewer, date, and acceptance-contract ID. For simulation-driven PREPARE, score a candidate pool with uncertainty, residual/error, expected decision impact, and diversity; select the report's 6–10 high-value scenarios (or document a governing revision of the fewer-than-10 wording). Archive the selected-run rationale and replay manifest.

## 4. UPDATE

Run baseline, simple fine-tuning, fixed replay, EWC, and adaptive replay under matched training exposure, seeds, budgets, and held-out trajectory sets. Report mean and uncertainty across seeds, not a single rounded number. Reconcile manuscript percentage figures against raw predictions and define each improvement/degradation denominator.

## 5. CALIBRATE

Declare one UQ method. For deterministic point predictions, conformal calibration can use held-out nonconformity residuals; stochastic predictive samples are required only for ensemble or dropout spread methods. Fit calibration parameters on the calibration role only. Report empirical coverage, interval width, conditional/spatial coverage at priority regions, reliability diagrams, and calibration before/after update. Evaluate once on untouched final test.

## 6. DEPLOY and failure branch

Use the frozen contract and final-test results to produce a pass/fail decision. Archive model hash/checkpoint, preprocessing version, UQ calibration parameters, evidence manifest, and reviewer decision. If any required gate fails, record return to PREPARE or escalation to full retraining according to the selected governance policy. Resolve the report's withdrawal-versus-prior-model-retention inconsistency before calling the branch operational.

## 7. Efficiency

Measure physics and surrogate inference on stated hardware with warm-up, batch size, I/O treatment, and number of scenarios. Report speedup distribution and cost assumptions. The report's 10^3–10^5 range is context until this benchmark is run.
