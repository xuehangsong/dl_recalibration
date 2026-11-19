# Source passages used in the audit

Page numbers below are **printed PDF page numbers** in PNNL-39195, not the zero-based PDF file index.

## Task 1 report (authoritative PDF)

- **Printed p. 8, §2.2.1, MONITOR:** monitoring compares predictions to observations, computes residuals and UQ metrics, and tracks interval coverage/calibration statistics.
- **Printed p. 9, §2.2.1, DETECT/DECIDE:** DETECT evaluates uncertainty, residual bias, uncertainty inflation, distributional drift, and extrapolation; persistence example is 60–90 days. DECIDE is a human governance review and selects observation- or simulation-driven pathway.
- **Printed p. 10, §2.2.2, PREPARE–CALIBRATE:** simulation-driven preparation scores candidates using uncertainty, residuals, and diversity and selects 6–10 scenarios; CALIBRATE evaluates held-out validation coverage and reliability diagrams.
- **Printed p. 11, §2.2.2, DEPLOY:** validation uses held-out data not used for training or calibration and checks error, UQ, spatial/temporal consistency, and the pre-update baseline; failed candidates are not deployed.
- **Printed p. 15, §3.1.3:** typical acceptance criteria include site-specific RMSE limits, prediction interval coverage near 90%, spatial/temporal consistency, and no systematic concentration bias at compliance boundaries.
- **Printed p. 16, §3.1.5:** rollback is defined as formal withdrawal of surrogate use and escalation to full retraining; high-fidelity physics is the sole analytical support during rollback.
- **Printed pp. 25–26, §3.3.2 and Table 6 printed p. 26:** candidate diagnostics include rolling variance, lag-1 autocorrelation, skewness/kurtosis, RMSE/bias, threshold exceedance, predictive variance, KS/energy distance, MMD, latent Mahalanobis/reconstruction error, and a composite index. The report specifies sensitivity/specificity and lead time for stress testing, but no universal critical threshold.
- **Printed p. 27, §3.3.3:** update batch guidance uses approximately 70–75% historical replay.
- **Printed p. 45, §5.4:** expected outcome says fewer than 10 targeted simulations and 10^3–10^5 speedup; these are expectations and conflict slightly with the 6–10 PREPARE range.

## Yilin manuscript

- **§2.1 extracted text lines 170–175:** 128 × 100 mesh, one–five extraction wells, varied pumping rates, 10,000 physics-based simulation runs.
- **Results extracted lines 587–592:** baseline 0.58/10.04 µg/L RMSE and simple fine-tuning 1.11/3.92 µg/L for historical/rare regimes.
- **Results extracted lines 627–644:** fixed replay 1.03/1.21 µg/L and EWC 5.45/1.22 µg/L for historical/rare regimes.
- **Results extracted lines 686–706:** controller reaches an imposed replay cap; manuscript reports fixed-to-adaptive historical degradation 80.4% to 26.5%, adaptive rare improvement >85%, and fixed rare improvement 88.9%.

The manuscript line numbers refer to the Pandoc extraction `/tmp/adaptive_replay.txt` generated during this execution. They are navigation anchors, not replacements for the source DOCX.
