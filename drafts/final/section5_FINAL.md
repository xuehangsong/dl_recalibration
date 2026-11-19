# 5. Prototype Demonstration and Pump-and-Treat Lifecycle Case Study

This section uses the pump-and-treat U-Net as the quantitative case study for the recalibration framework. The case study follows one decision path: baseline evaluation reveals a reliability problem, a response-based drift measure identifies the high-change cases, the old/new performance tradeoff determines whether updating is justified, replay and adaptive controllers attempt the update, and the surviving candidates are held for uncertainty calibration and final validation before deployment. The adaptive-replay experiments provide quantitative evidence for the UPDATE decision and a controlled stress-test form of DETECT. CALIBRATE and DEPLOY remain explicit lifecycle gates because the study does not report prediction intervals, calibration data, or an untouched final-test promotion record.

## 5.1 Prototype context and case-study purpose

The U-Net prototype represents a two-dimensional pump-and-treat system on a 128 by 100 grid with 1-meter spacing. The synthetic aquifer has uniform porosity and hydraulic conductivity, one to five extraction wells, varied pumping rates, and plume snapshots at days 0 through 4 from 10,000 nominal physics-based simulation runs. The network receives plume and pumping information together with a Thiem-equation drawdown field and predicts the subsequent concentration field. The experiment description does not document an independent trajectory-level split, so final-test conclusions require verification of the split and its provenance.

The purpose of the case study is to test the management question that matters for remediation support: can an update recover accuracy for rare plume redistribution while retaining reliability for the historical plume behavior that supported the original surrogate? A rare-regime gain by itself is insufficient. The candidate must also preserve historical performance, maintain physically meaningful plume quantities, pass uncertainty-quantification (UQ) and calibration checks, and clear the final validation gate.

## 5.2 MONITOR: the baseline reliability problem

The lifecycle begins with the baseline U-Net operating on the historical and high-change response regimes. The historical regime is defined from the lower tail of a sequential Mass90 footprint-change score, while the rare regime is drawn from the upper tail. The manuscript reports baseline RMSE of **0.58 µg/L** for the historical regime and **10.04 µg/L** for the rare regime. The rare-regime baseline also has a plume-mass error of **32.30%**, peak-concentration error of **14.20%**, and Mass90 error of **7.11%** in the embedded Figure 4 labels.

These values establish the first lifecycle finding. The reliability problem is not limited to average concentration error: the same high-change cases produce large errors in plume quantities that affect capture and remediation interpretation. The displayed rare RMSE is 17.3 times the historical RMSE, and the 32.30% rare plume-mass error makes plume-mass accounting a material concern in this stress test. The spatial examples in Figures 2 and 4 show errors concentrated near high-gradient plume regions and plume boundaries, which is consistent with an error in plume geometry and redistribution rather than a uniform concentration bias.

The baseline evidence is therefore sufficient to justify a detection review. It is still a retrospective aggregate result: the study does not provide the per-trajectory error distribution, seeds, or a verified independent test manifest needed to estimate uncertainty around these averages.

## 5.3 DETECT: identifying the high-change stress condition

The Mass90 score is defined as the relative change in the number of grid cells required to contain 90% of plume mass between consecutive reference states. Figure 1 labels the historical cutoff at the 40th percentile, **0.133**, and the rare cutoff at the 97th percentile, **0.329**. The rare cutoff is therefore 2.47 times the historical cutoff. The resulting partition identifies a small response tail in which the static surrogate is unreliable.

This is the DETECT evidence provided by the adaptive-replay study. It identifies a controlled high-change stress condition that can be sent to the decision step. It does not measure an operational detector's sensitivity, specificity, false-alarm rate, or warning lead time because the score uses the reference plume at time (t+1). It is a retrospective response label, not a prospective trigger based on incoming pumping data, monitoring observations, or a surrogate-only uncertainty signal.

The framework also defines tipping-point-inspired diagnostics for the DETECT step: rolling residual variance, lag-1 autocorrelation, skewness, kurtosis, threshold exceedance, predictive variance, distributional distances, and latent-space drift. These indicators are intended to identify declining predictive resilience before a deployment error becomes unacceptable; they do not imply a physical aquifer tipping point. The current four-day sequence has only four transitions, and the study does not report ordered residual or latent-output records. These detector statistics and the 60–90-day persistence rule therefore cannot be estimated from the reported results. The quantitative conclusion is that Mass90 supplies a reproducible stress label; detector operating characteristics remain an unmeasured lifecycle requirement.

## 5.4 DECIDE: defining the update decision

The DECIDE step asks whether the detected high-change behavior warrants an update and what evidence an updated candidate must satisfy. The decision must balance two outcomes: improvement on the rare regime that triggered review and retention on the historical regime that remains in use. The manuscript shows several illustrative acceptance contracts, including 25% and 30% historical-degradation limits, an 85% rare-improvement target, and a 1.05-times/0.80-times RMSE example. These values are not one frozen preregistered contract.

For a clear numerical decision screen, Figure 5 uses a historical-degradation limit of 30% and a rare-regime improvement requirement of 85%. Under that illustrative rule, the controller outcomes are:

**Table 5.1. Controller outcomes under the illustrative Figure 5 acceptance screen.**

| Controller | Historical degradation | Rare improvement | Result under Figure 5 rule |
|---|---:|---:|---|
| Fixed replay | 80.4% | 88.9% | Fails historical retention |
| Threshold adaptive forgetting | 26.5% | 85.8% | Passes the two plotted checks |
| Loss-balanced | 21.1% | 85.5% | Passes the two plotted checks |
| Loss-balanced with floor | 38.1% | 87.3% | Fails historical retention |

The margins make the decision tradeoff visible. Threshold adaptive forgetting clears the historical boundary by 3.5 percentage points and the rare boundary by 0.8 points. Loss-balanced replay clears the historical boundary by 8.9 points and the rare boundary by 0.5 points. Fixed replay misses historical retention by 50.4 points despite clearing the rare-improvement boundary, while loss-balanced replay with a floor misses historical retention by 8.1 points. The decision under this illustrative screen is therefore to retain the threshold-adaptive and loss-balanced candidates for further evaluation and to reject the two failing controller outcomes under this illustrative screen.

This screening result is controller-specific. It does not support a blanket statement that adaptive replay passes. The reported percentages also do not exactly reproduce from the rounded RMSE values, so the denominator, split, and matched data exposure must be resolved before the rule is treated as an approved deployment contract.

## 5.5 PREPARE: assembling the update data

The update preparation uses the top 3% response regime as the rare-case source and the bottom 40% regime as the historical replay source. This creates a controlled stability–plasticity experiment: rare cases supply the new behavior, while historical cases constrain forgetting. The preparation is therefore sufficient for testing replay and continual-learning methods.

The framework's design guidance is approximately 70–75% historical replay. The study does not report batch counts or sample exposure needed to verify that proportion, so the replay composition cannot be treated as a measured result.

The evidence does not show the framework's active-learning procedure. There is no candidate-pool score, uncertainty ranking, diversity constraint, information-gain calculation, or record of selecting 6–10 new physics simulations. The preparation is therefore a **regime-selected sample**, rather than an active-learning selection. The framework's 6–10 targeted-simulation criterion remains a design requirement for a subsequent simulation-driven update, rather than a measured result from this study.

## 5.6 UPDATE: quantitative comparison of candidate updates

The update experiments quantify the tradeoff that motivated the DECIDE step. Figure 4 provides the following displayed values:

**Table 5.2. Values printed in Figure 4 for the update comparison.**

| Configuration | Historical RMSE (µg/L) | Rare RMSE (µg/L) | Rare mass error (%) | Rare peak error (%) | Historical plotted peak error | Rare Mass90 error (%) |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 0.58 | 10.04 | 32.30 | 14.20 | 0.23 | 7.11 |
| Simple fine-tuning | 1.11 | 3.92 | 9.86 | 7.70 | 0.54 | 3.59 |
| Fixed replay | 1.03 | 1.21 | 1.82 | 3.43 | 0.40 | 1.89 |
| EWC | 5.45 | 1.22 | 1.88 | 3.40 | 2.02 | 1.64 |

The displayed labels show that simple fine-tuning reduces rare RMSE by **61.0%**, rare plume-mass error by **69.5%**, rare peak error by **45.8%**, and rare Mass90 error by **49.5%**, while historical RMSE increases **91.4%**. Fixed replay reduces the four rare metrics by **87.9%**, **94.4%**, **75.8%**, and **73.4%**, respectively, while historical RMSE increases **77.6%**. EWC gives comparable rare-regime reductions but raises historical RMSE by **839.7%** and the plotted historical peak-error metric by **778.3%**. These calculations use the rounded values printed in Figure 4 and are provided in the supporting calculation record.

The update result is thus physically interpretable. Replay recovers the rare plume shape and mass distribution while retaining more historical behavior than simple fine-tuning or EWC in the displayed Figure 4 comparison. It does not eliminate the stability–plasticity tradeoff. The full-network panel in Figure 3 reports an additional historical/rare RMSE pair of **0.64/0.99 µg/L**, compared with **1.11/3.92 µg/L** for decoder-only fine-tuning. That pair would change the ranking if it used the same split and evaluation protocol, but its configuration is unresolved because the manuscript uses conflicting Model C labels across experiments while the framework describes Model C as a different training paradigm.

The adaptive trajectory in Figure 5 reaches replay ratio \(r=0.8\) and remains at that cap for most of the 100 plotted update epochs. This shows that the displayed controller selected high historical replay under its validation signal. It does not isolate the benefit of adaptive scheduling from the benefit of using a high replay ratio. A fixed-replay-at-0.8 run with matched seed, update budget, and historical exposure is required for that causal comparison.

## 5.7 CALIBRATE: the candidate enters the uncertainty gate

After UPDATE, the candidate cannot move directly to deployment. The framework requires post-update UQ calibration using held-out calibration data, with coverage near **90%**, interval width, reliability diagrams, and spatial checks at decision-relevant regions. The calibration set must remain separate from the data used to select the replay controller and from the untouched final test.

The adaptive-replay study reports point predictions and physical plume metrics but no prediction intervals, ensemble or dropout samples, conformal nonconformity scores, calibration parameters, or reliability diagrams. The RMSE reductions therefore do not establish UQ calibration. The lifecycle action supported by the study is to hold the threshold-adaptive and loss-balanced candidates at the CALIBRATE gate. A deterministic surrogate could use conformal residual calibration if an independent calibration set is available; stochastic predictive samples are needed only for ensemble or dropout-based spread estimates. Neither calibration path can be evaluated from the reported results.

## 5.8 DEPLOY: final validation and lifecycle state

DEPLOY requires an untouched final test and a versioned acceptance record. The candidate must satisfy the selected old/new performance contract, priority-location error limits, spatial and temporal consistency, near-90% uncertainty coverage, and the absence of systematic decision-boundary bias. The record must include the model hash, preprocessing version, calibration parameters, data provenance, reviewer decision, and the failure response if a gate is not met.

The adaptive-replay study does not report those artifacts. The correct lifecycle outcome is therefore a governed hold: the update experiment has produced candidates and a quantitative screening decision, but no candidate is promoted. The workflow remains at the calibration and validation gate, with further preparation or controlled retraining available if a candidate fails the eventual calibration or final-test gate. This is the endpoint supported by the reported case-study evidence, and it closes the decision logic without claiming an unsupported deployment.

## 5.9 Integrated lifecycle result

The case study can be read as one continuous chain. Baseline evaluation shows that the model is reliable on historical behavior but fails on rare high-change behavior. The Mass90 score identifies the response tail that requires review. The DECIDE screen turns the old/new tradeoff into an explicit update requirement. PREPARE assembles rare cases and historical replay, and UPDATE shows which methods recover rare plume quantities while limiting forgetting. Figure 5 retains two controller candidates under its illustrative gate and rejects two others. The surviving candidates then encounter the UQ-calibration gate, where the current evidence stops because no interval or calibration record exists. DEPLOY consequently remains pending, and the lifecycle returns to governed evidence collection rather than silently promoting a point-prediction improvement.

This sequence demonstrates the quantitative core of the seven-step workflow: each step produces evidence that changes the next action. It also defines the remaining work precisely. A completed operational demonstration would add the trajectory-level split and raw predictions, prospective detector metrics and lead time, the active-learning selection record, independent UQ calibration, and an untouched final-test/model-version decision. Until those records exist, the defensible claim is a controlled demonstration of the update decision within the seven-step workflow, with measured update performance and a documented hold at CALIBRATE/DEPLOY.

## 5.10 Expected outcomes and implementation implications

The framework describes a context of 10³–10⁵ surrogate speedup relative to physics simulation and approximately 6–10 targeted high-value simulations for simulation-driven preparation. Those values remain targets until benchmarked on defined hardware and a documented candidate-selection run. The adaptive-replay study's reported point metrics do not measure update cost, physics-run savings, or inference speed for the current controller.

The U-Net update mechanism is sufficiently developed to support a controlled candidate comparison. The next prototype increment should preserve trajectory identity, freeze the detector and acceptance contract before final testing, generate uncertainty outputs or conformal calibration residuals, and archive the final promotion record. These additions would complete a reproducible seven-step demonstration while preserving the report's governance boundary that high-fidelity physics remains authoritative for final remedy decisions.

The evaluation should also retain three operational modes: physics-only analysis, surrogate-only analysis without recalibration, and hybrid analysis using the recalibration workflow. Comparing those modes will quantify the value of the lifecycle itself, alongside the accuracy differences among update algorithms.
