# 5. Prototype Demonstration

This section describes the prototype implementations and case study that will demonstrate the recalibration framework in practice. The prototypes serve as proof-of-concept implementations that validate the seven-step workflow described in Section 2.2 and the methods detailed in Section 3. By demonstrating a complete recalibration cycle on representative groundwater modeling problems, these prototypes establish the feasibility of adaptive surrogate management for DOE environmental management applications.

## 5.1 Demonstration Objectives

The primary objective of the prototype demonstration is to define and evaluate one auditable recalibration cycle, validating how the framework detects surrogate degradation, executes targeted updates, and restores prediction accuracy. This demonstration corresponds to Phase 1 of the development roadmap described in Section 4.3.1, which focuses on proving the concept before building production-quality software. A complete lifecycle claim requires evidence at all seven steps; the current adaptive-replay results provide the update experiment and a controlled rare-regime stress case, while the remaining evidence is specified below.

Success will be evaluated against the acceptance criteria defined in Section 3.1.3, including accuracy metrics at priority monitoring locations, calibration of uncertainty estimates, and spatial-temporal consistency with observed behavior. The demonstration will also document computational efficiency gains relative to physics-only approaches and the number of targeted physics simulations required for recalibration.

Beyond technical validation, the demonstration will exercise the governance procedures embedded in the workflow. The DECIDE step requires human review of detection evidence before authorizing an update, and the DEPLOY step requires validation against acceptance criteria before operational deployment. Documenting these governance interactions will establish procedures for subsequent phases.

## 5.2 Prototype Implementations

Two prototype implementations will demonstrate the framework's applicability to representative groundwater modeling problems. These prototypes validate the surrogate architectures discussed in Section 3.2 and provide test cases for the recalibration workflow.

### 5.2.1 U-FNO Surrogate for 2D Cross-Section Transport

The first prototype applies a U-shaped Fourier Neural Operator architecture to predict contaminant transport in a 2D cross-section domain. This prototype demonstrates the framework's capability for variably saturated flow and transport problems with heterogeneous subsurface properties.

The PFLOTRAN baseline model simulates an 84-meter by 4-meter domain discretized on a 28 by 40 grid. The model solves the variably saturated Richards equation with time-varying boundary conditions representing tidal influence. Heterogeneous permeability and porosity fields are generated using Gaussian random field methods. This configuration is adapted from the GeoFUSE framework developed by Jiang and colleagues (2025).

The U-FNO architecture combines Fourier layers for efficient global operations with U-Net-style skip connections for preserving fine-scale features. The model contains approximately 126 million parameters and is trained using a learning rate of 0.001 with stepwise decay over 200 epochs. Separate networks predict pressure and concentration fields, enabling independent uncertainty quantification for each output type.

This prototype supports the recalibration workflow by enabling fast inference for continuous monitoring during Steps 1 through 3, rapid scenario testing for decision support, and uncertainty quantification via ensemble methods or MC-Dropout. The computational speedup relative to PFLOTRAN enables real-time monitoring and interactive scenario exploration that would be infeasible with physics-only approaches.

### 5.2.2 U-Net Surrogate for 2D Pump-and-Treat Plume Prediction

The second prototype applies a U-Net architecture to predict contaminant plume evolution in a 2D pump-and-treat remediation scenario. This prototype demonstrates the framework's capability for operational decision support in active remediation systems.

Training data generation uses a 128 by 100 mesh with 1-meter cell spacing. The domain includes 1 to 5 extraction wells in a central well field, with well locations and pumping rates varied across 10,000 physics simulation runs. Plume snapshots are captured at 0, 1, 2, 3, and 4 days, providing temporal sequences for training autoregressive prediction. This configuration is based on the work of Song and colleagues (2025).

The U-Net architecture incorporates several physics-inspired modifications. A Thiem equation drawdown map serves as an additional input channel, providing analytical approximation of the flow field that helps the network learn the relationship between pumping and transport. Strided convolutions replace max pooling to preserve spatial information. A leaky tanh bounded activation function ensures physically plausible concentration predictions. Skip connections preserve sharp concentration fronts that would otherwise be smoothed during encoding.

The related original U-Net package describes a 70/15/15 array-level split for training, validation, and test sets. That split is not treated as the split for Yilin's adaptive-replay study until the current study's trajectory manifest and code are verified. Mean squared error loss is minimized using the Adam optimizer with early stopping based on validation performance in the original package. Autoregressive rollout enables multi-step prediction by feeding predicted outputs back as inputs for subsequent time steps.

## 5.3 Case Study Design

The case study will demonstrate a complete recalibration cycle using one of the prototype implementations. The design establishes a controlled scenario where drift is introduced and the framework's response is evaluated through all seven workflow steps.

### 5.3.1 Scenario Description

The case study uses a synthetic site based on characteristics typical of DOE environmental management sites. The scenario involves a contaminated groundwater plume requiring pump-and-treat remediation over a multi-year timeframe. Initial conditions establish a contaminant plume with known extent and concentration distribution. The remediation system consists of a pump-and-treat configuration with extraction wells positioned to capture the plume.

The surrogate model is initially trained on physics simulations representing the baseline operating conditions. The training ensemble spans heterogeneous subsurface realizations and varying operational conditions within the expected operating envelope. Monitoring data is simulated by extracting observations at well locations from physics model outputs, with measurement noise added to represent realistic field conditions.

### 5.3.2 Drift Injection Plan

Drift injection is accomplished by modifying the pumping regime partway through the simulation period. This change represents an operational modification—such as adding or removing wells, or changing pumping rates—that shifts conditions outside the surrogate's original training distribution. The magnitude of the regime change is calibrated to produce detectable but not catastrophic degradation in surrogate performance.

The drift injection approach allows controlled evaluation of the framework's detection capabilities. By knowing exactly when and how drift is introduced, the demonstration can measure detection latency, false positive rates, and the sensitivity of different drift indicators. This controlled setting provides a rigorous test of the trigger logic described in Section 3.3.2.

### 5.3.3 Recalibration Demonstration Plan

The recalibration demonstration will proceed through all seven workflow steps, documenting the framework's operation at each stage.

During Phase 1 (Continuous Monitoring), the MONITOR step will track surrogate predictions against simulated observations, computing residuals and uncertainty metrics. The DETECT step will evaluate drift indicators against predefined thresholds, with the trigger state machine transitioning from OK to WARNING as degradation accumulates. The DECIDE step will present detection evidence for governance review, demonstrating the human decision point that authorizes recalibration. This step is critical for validating that the framework supports informed decision-making rather than automatic triggering.

During Phase 2 (Triggered Response), the PREPARE step will use active learning methods to select high-value scenarios for new physics simulations, targeting conditions in the new operating regime where the surrogate shows highest uncertainty. The UPDATE step will apply continual learning methods—including replay buffers and Elastic Weight Consolidation—to fine-tune the surrogate while preserving performance on the original regime. The CALIBRATE step will adjust prediction intervals to maintain calibration under the new conditions. The DEPLOY step will validate the updated surrogate against acceptance criteria and, if successful, document the complete governance record.

The planned evidence and quantitative criteria for the seven steps are summarized below. The status column distinguishes what is already available from the adaptive-replay study and what must be generated before the lifecycle is presented as executed.

| Workflow step | Prototype evidence and quantitative criterion | Current status |
|---|---|---|
| MONITOR | Ordered trajectory errors, plume and Mass90 diagnostics, residuals, and UQ coverage near 90 percent; site-specific RMSE and boundary-bias limits | Regime-separated RMSE and Mass90 partition are reported; ordered per-run and UQ records are not available |
| DETECT | Predeclared operating/response drift rule; persistence of 60–90 days or documented regime change; sensitivity, specificity, false alarms, and warning lead time | Mass90 provides a retrospective high-change stress label; detector operating characteristics are not reported |
| DECIDE | Versioned governance record that reviews evidence and freezes the old/new acceptance contract before final testing | Illustrative 25/30 percent and 85 percent values appear in the manuscript; no single approved contract is recorded |
| PREPARE | Candidate scoring by uncertainty, residual/error, decision impact, and diversity; 6–10 targeted physics cases plus documented replay manifest | Rare-regime and replay samples are described; active-learning scores and provenance manifest are not available |
| UPDATE | Matched baseline, fine-tuning, fixed replay, EWC, and adaptive replay comparisons with seeds, budgets, and retention metrics; the framework gives approximately 70–75 percent historical replay as design guidance | Strongest current evidence: manuscript-reported RMSE and adaptive-replay comparisons; actual replay exposure is not verified |
| CALIBRATE | Held-out calibration data, declared UQ method, reliability diagram, coverage and interval-width checks | Not demonstrated in the manuscript |
| DEPLOY | Untouched final test, model-version hash, acceptance checklist, promotion or escalation decision | Not demonstrated; no final-test or model-version decision record is available |

The Mass90 partition is retained as a controlled stress-test variable. It is calculated from consecutive reference plume states and therefore cannot serve alone as a prospective detector. Similarly, the four-day sequence cannot establish the report's 60–90-day persistence requirement or robust rolling early-warning statistics. Those limitations are part of the evidence record, rather than assumptions used to complete the lifecycle claim.

### 5.3.4 Evaluation Approach

The evaluation will compare surrogate performance before and after recalibration across multiple dimensions. Accuracy metrics including root mean square error and mean absolute error will quantify prediction improvement. Uncertainty calibration metrics will verify that prediction intervals maintain appropriate coverage. Computational efficiency metrics will document the speedup relative to physics-only approaches and the number of targeted physics runs required for recalibration.

The evaluation will also compare three operational modes: physics-only analysis using numerical models for all predictions, surrogate-only analysis using the trained surrogate without recalibration, and hybrid analysis using the surrogate with the recalibration framework. This comparison will quantify the value added by the recalibration framework relative to both alternatives.

### 5.3.5 Evidence status of the adaptive-replay results

Yilin's adaptive-replay study supplies the strongest current quantitative evidence for the UPDATE step and a controlled stress condition for MONITOR and DETECT. The synthetic prototype is reported as a 128 × 100 grid with one to five extraction wells, varied pumping rates, and 10,000 nominal physics-based runs. The response-derived Mass90 footprint-change score partitions the historical regime as the bottom 40 percent and the rare high-change regime as the top 3 percent. This partition requires the reference plume at consecutive times, so it is a retrospective stress label rather than a prospective operating trigger.

The manuscript reports the following denormalized RMSE values:

| Configuration | Historical regime (µg/L) | Rare regime (µg/L) | Evidence label |
|---|---:|---:|---|
| Baseline U-Net | 0.58 | 10.04 | Manuscript-reported |
| Simple fine-tuning | 1.11 | 3.92 | Manuscript-reported |
| Fixed replay | 1.03 | 1.21 | Manuscript-reported |
| EWC | 5.45 | 1.22 | Manuscript-reported |

Arithmetic from these displayed rounded values gives a 77.6 percent historical-regime increase for fixed replay relative to the baseline and an 87.9 percent rare-regime reduction. The manuscript separately reports 80.4 percent, 26.5 percent, and 88.9 percent comparisons for fixed and adaptive replay. Those percentages are retained as manuscript-reported claims until the figure-generation data establish their denominator, split, and matched comparator. They must not be silently substituted with the rounded-value calculations.

The embedded Figure 4 labels provide additional physical metrics for the same four named configurations. Relative to the displayed baseline, fixed replay reduces rare-regime plume-mass error from 32.30 to 1.82 percent (94.4 percent), rare peak error from 14.20 to 3.43 percent (75.8 percent), and rare Mass90 error from 7.11 to 1.89 percent (73.4 percent). EWC produces similar rare-regime reductions, but its historical RMSE increases from 0.58 to 5.45 µg/L (839.7 percent) and the plotted historical peak-error metric increases from 0.23 to 2.02 (778.3 percent). Simple fine-tuning reduces rare-regime RMSE by 61.0 percent but increases historical RMSE by 91.4 percent. These percentages are calculated from the labels printed in Figure 4 and are archived in the evidence package; they are not recomputed from raw predictions.

Figure 5 reports four controller outcomes under its illustrative acceptance region of historical degradation no greater than 30 percent and rare-regime improvement at least 85 percent. Threshold adaptive forgetting (26.5 percent, 85.8 percent) and loss-balanced replay (21.1 percent, 85.5 percent) fall inside that region. Fixed replay (80.4 percent, 88.9 percent) and loss-balanced replay with a denominator floor (38.1 percent, 87.3 percent) fall outside it. Thus the figure does not support a blanket statement that adaptive replay passes: one adaptive controller variant fails the plotted gate. The trajectory reaches replay ratio (r=0.8) and remains there for most of the 100 plotted update epochs, so a fixed-replay-at-0.8 comparator is needed to isolate scheduling from high replay exposure.

The layer-freezing panel in Figure 3 reports a full-network result of 0.64 µg/L historical RMSE and 0.99 µg/L rare RMSE, compared with 1.11 and 3.92 µg/L for decoder-only fine-tuning. Because the manuscript also uses “Model C” for replay in another comparison, and the Task 1 report uses Model C for retraining from scratch, this result cannot be ranked with Figure 4 until its configuration, split, and test protocol are reconciled.

The manuscript also reports that the adaptive controller reached its imposed replay cap and reduced historical degradation relative to fixed replay. These claims support adaptive replay as a candidate UPDATE method. They do not demonstrate uncertainty calibration, detector sensitivity or specificity, active-learning selection, or final deployment. The four-day sequence and four transitions cannot establish the report's 60–90-day persistence rule or robust rolling early-warning statistics. The complete lifecycle evidence package therefore still requires the independent trajectory split, a frozen DECIDE acceptance contract, a prospective detector record, the PREPARE provenance manifest, UQ calibration outputs, and an untouched final-test and model-version decision record.

### 5.3.6 Reconstructed lifecycle decision trace

The available results support a quantitative reconstruction of the lifecycle decision path. This trace uses the manuscript’s displayed results and Figure 5’s 30 percent historical-degradation and 85 percent rare-improvement rule as an illustrative decision contract. It identifies the action supported by the evidence at each transition; it does not convert missing artifacts into completed operational records.

| Transition | Measured evidence | Criterion applied | Resulting action |
|---|---|---|---|
| MONITOR → DETECT | Baseline historical/rare RMSE is 0.58/10.04 µg/L; rare plume-mass, peak, and Mass90 errors are 32.30%, 14.20%, and 7.11% | Compare rare-regime behavior with historical reference and inspect decision-relevant plume metrics | Flag the high-change regime for detection review |
| DETECT → DECIDE | Mass90 score cutoffs are 0.133 at the 40th percentile and 0.329 at the 97th percentile | Treat the top-3% response regime as a controlled stress condition | Reconstruct a warning condition; sensitivity, specificity, false alarms, and lead time remain unmeasured |
| DECIDE → PREPARE | Simple fine-tuning improves rare RMSE but raises historical RMSE by 91.4%; fixed replay raises it by 77.6% | Update is justified only if rare improvement is paired with bounded historical degradation | Select replay-based preparation for a controlled update comparison |
| PREPARE → UPDATE | Update data combine top-3% rare cases with bottom-40% historical replay cases | Preserve historical exposure while adapting to the rare regime | Run simple fine-tuning, fixed replay, EWC, and adaptive-controller variants; active-learning selection is not demonstrated |
| UPDATE → CALIBRATE | Threshold adaptive and loss-balanced controllers meet the illustrative 30%/85% region; fixed replay and loss-balanced-plus-floor do not | Historical degradation ≤30% and rare improvement ≥85% | Retain the passing controller variants as calibration candidates; reject failing variants under this illustrative rule |
| CALIBRATE → DEPLOY | No prediction intervals, calibration set, coverage, or reliability diagram are reported | Coverage near 90% and held-out calibration checks are required | Hold the candidate; no deployment decision can be supported |
| DEPLOY → MONITOR | No untouched final-test result or model-version record is available | Final-test accuracy, UQ, consistency, provenance, and approval record are required | Remain in governed evaluation and monitoring; do not promote the candidate |

This trace gives the report a complete lifecycle logic: the measured rare-regime failure creates the detection case, the old/new tradeoff determines update eligibility, the controller comparison screens candidates, and the absence of UQ and final-test evidence blocks promotion. The available data therefore exercise the loop through a governed hold at CALIBRATE/DEPLOY rather than through a completed deployment.

## 5.4 Expected Outcomes

The framework identifies surrogate inference speedups on the order of 10³ to 10⁵ relative to physics-based models and a targeted simulation workload of approximately 6 to 10 cases (with the separate planning text stating fewer than 10). These are framework targets until measured on stated hardware and a documented active-learning run. The prototype must report post-update accuracy, uncertainty coverage near the 90 percent criterion, spatial and temporal consistency, and the frozen acceptance contract from Section 3.1.3 before a deployment claim is made.

The demonstration will produce documented deliverables including a complete recalibration cycle with all seven workflow steps executed and recorded, governance documentation meeting the audit trail requirements of Section 3.1.5, and reproducible code capturing each step for subsequent development phases.

The demonstration will also generate lessons for Phase 2 development as described in Section 4.3.2. These lessons will inform decisions about automation priorities, user interface requirements, and integration with site data systems. Experience with the prototype will reveal which aspects of the workflow benefit most from automation and which require continued human oversight.

## 5.5 Summary

This section has described the prototype implementations and case study design that will demonstrate the recalibration framework. Two prototypes—U-FNO for cross-section transport and U-Net for pump-and-treat plume prediction—provide test cases for the seven-step workflow. The case study design establishes a controlled scenario for demonstrating complete recalibration cycles, with drift injection and systematic evaluation of framework response. Expected outcomes include quantitative validation of speedup and accuracy, documented governance procedures, and lessons for subsequent development phases.
