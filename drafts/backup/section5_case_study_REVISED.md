# 5. Prototype and Case Study

This section presents the validation framework, prototype implementations, and case study design that demonstrate the recalibration framework in practice. The prototypes serve as proof-of-concept implementations that validate the seven-step workflow described in Section 2.2 and the methods detailed in Section 3. By demonstrating complete recalibration cycles on representative groundwater modeling problems, these prototypes establish the feasibility of adaptive surrogate management for DOE environmental management applications.

## 5.1 Validation Framework

The validation framework establishes the metrics and acceptance criteria used to evaluate surrogate model performance throughout the recalibration cycle. These metrics align with the governance requirements defined in Section 3.1 and support the trigger logic described in Section 3.3.2.

### 5.1.1 Performance Metrics

Performance metrics quantify the accuracy of surrogate predictions relative to physics-based model outputs and field observations. Root mean square error (RMSE) provides an overall measure of prediction accuracy, with lower values indicating better performance. Mean absolute error (MAE) offers a robust alternative less sensitive to outliers. Bias quantifies systematic over- or under-prediction that may indicate model drift.

For groundwater remediation applications, domain-specific metrics include contaminant mass reduction accuracy (comparing predicted versus simulated mass removal over time), plume extent prediction accuracy (measuring spatial agreement between predicted and simulated plume boundaries), and drawdown head error (quantifying accuracy of hydraulic head predictions near pumping wells). These metrics directly relate to operational decision-making and regulatory compliance.

### 5.1.2 Uncertainty Metrics

Uncertainty metrics evaluate the quality of surrogate uncertainty estimates, which are essential for reliable decision support. Predictive interval coverage measures the fraction of true values falling within stated prediction intervals, with well-calibrated models achieving coverage close to the nominal level (for example, 90% intervals containing true values approximately 90% of the time). Calibration error quantifies the difference between nominal and observed coverage across different confidence levels.

For remediation applications, uncertainty in capture zone delineation is particularly important, as it directly affects compliance with regulatory requirements. Metrics include the probability that predicted capture zones contain actual capture zones and the uncertainty in time-to-cleanup estimates.

### 5.1.3 Drift Detection Metrics

Drift detection metrics support the trigger logic (Section 3.3.2) by quantifying changes in surrogate performance over time. Residual thresholds track whether prediction errors exceed acceptable bounds, with sustained exceedances indicating potential drift. Distributional drift indicators such as the Kolmogorov-Smirnov statistic compare recent residual distributions against baseline distributions. The composite drift index aggregates multiple indicators into a single metric that triggers recalibration when overall evidence of degradation exceeds a threshold.

### 5.1.4 Governance Compliance Metrics

Governance compliance metrics ensure that surrogate operations meet DOE quality assurance requirements. Acceptance criteria alignment verifies that surrogate performance meets the thresholds defined in Section 3.1.3. Audit trail completeness confirms that all model updates, data sources, and decisions are fully documented. Regulatory documentation metrics track the availability and currency of required compliance documentation.

### 5.1.5 Acceptance Thresholds

Acceptance thresholds define the quantitative criteria that surrogates must meet for operational deployment. Example thresholds for groundwater remediation applications include achieving at least 90% accuracy in predicting contaminant mass removed within 10 years, maintaining 95% prediction interval coverage at or above 90%, and demonstrating monitoring network cost reduction of at least 30% compared to physics-only approaches. These thresholds are site-specific and should be established in consultation with site operators and regulators during framework deployment.

## 5.2 Prototype Implementations

Two prototype implementations demonstrate the framework's applicability to representative groundwater modeling problems. These prototypes validate the surrogate architectures discussed in Section 3.2 and provide test cases for the recalibration workflow.

### 5.2.1 U-FNO Surrogate for 2D Cross-Section Transport

The first prototype applies a U-shaped Fourier Neural Operator (U-FNO) architecture to predict contaminant transport in a 2D cross-section domain. This prototype demonstrates the framework's capability for variably saturated flow and transport problems with heterogeneous subsurface properties.

The PFLOTRAN baseline model simulates an 84-meter by 4-meter domain discretized on a 28 by 40 grid. The model solves the variably saturated Richards equation with time-varying boundary conditions representing tidal influence. Heterogeneous permeability and porosity fields are generated using Gaussian random field methods. This configuration is adapted from the GeoFUSE framework developed by Jiang and colleagues.

The U-FNO architecture combines Fourier layers for efficient global operations with U-Net-style skip connections for preserving fine-scale features. The model contains approximately 126 million parameters and is trained using a learning rate of 0.001 with stepwise decay over 200 epochs with batch size 4. Separate networks predict pressure and concentration fields, enabling independent uncertainty quantification for each output type.

This prototype supports the recalibration workflow by enabling fast inference for continuous monitoring (Steps 1-3), rapid scenario testing for decision support, and uncertainty quantification via ensemble methods or MC-Dropout. The computational speedup relative to PFLOTRAN enables real-time monitoring and interactive scenario exploration that would be infeasible with physics-only approaches.

### 5.2.2 U-Net Surrogate for 2D Pump-and-Treat Plume Prediction

The second prototype applies a U-Net architecture to predict contaminant plume evolution in a 2D pump-and-treat remediation scenario. This prototype demonstrates the framework's capability for operational decision support in active remediation systems.

Training data generation uses a 128 by 100 mesh with 1-meter cell spacing. The domain includes 1 to 5 extraction wells in a central well field, with well locations and pumping rates varied across 10,000 physics simulation runs. Plume snapshots are captured at 0, 1, 2, 3, and 4 days, providing temporal sequences for training autoregressive prediction. This configuration is based on the work of Song and colleagues.

The U-Net architecture incorporates several physics-inspired modifications. A Thiem equation drawdown map serves as an additional input channel, providing analytical approximation of the flow field that helps the network learn the relationship between pumping and transport. Strided convolutions replace max pooling to preserve spatial information. A leaky tanh bounded activation function ensures physically plausible concentration predictions. Skip connections preserve sharp concentration fronts that would otherwise be smoothed during encoding.

The training workflow uses a 70/15/15 split for training, validation, and test sets. Mean squared error loss is minimized using the Adam optimizer with early stopping based on validation performance. Autoregressive rollout enables multi-step prediction by feeding predicted outputs back as inputs for subsequent time steps.

This prototype supports pump-and-treat scenario screening by enabling rapid evaluation of alternative well configurations. Integration with the recalibration loop enables long-term operational support as site conditions evolve.

## 5.3 Case Study Design

The case study demonstrates a complete recalibration cycle using one of the prototype implementations. The design establishes a controlled scenario where drift is introduced and the framework's response is evaluated.

### 5.3.1 Hydrological Modeling Scenario

The case study uses a synthetic site based on characteristics typical of DOE environmental management sites. The scenario involves a contaminated groundwater plume requiring pump-and-treat remediation over a multi-year timeframe. Initial conditions establish a contaminant plume with known extent and concentration distribution. The remediation system consists of a pump-and-treat configuration with extraction wells positioned to capture the plume.

The surrogate model is initially trained on physics simulations representing the baseline operating conditions. The case study then introduces a regime change that causes the surrogate to experience drift, demonstrating the framework's ability to detect degradation and execute recalibration.

### 5.3.2 Data Sources and Simulation Setup

The physics model uses PFLOTRAN configured for the synthetic site, with parameters representative of DOE EM site conditions. Training data consists of an ensemble of simulations spanning heterogeneous subsurface realizations and varying operational conditions. Monitoring data is simulated by extracting observations at well locations from physics model outputs, with measurement noise added to represent realistic field conditions.

Drift injection is accomplished by modifying the pumping regime partway through the simulation period. This change represents an operational modification (such as adding or removing wells, or changing pumping rates) that shifts conditions outside the surrogate's original training distribution. The magnitude of the regime change is calibrated to produce detectable but not catastrophic degradation in surrogate performance.

### 5.3.3 Recalibration Demonstration

The recalibration demonstration proceeds through the complete seven-step workflow. Baseline surrogate performance is established during an initial monitoring period under the original operating conditions. Drift injection introduces the regime change, and the framework's monitoring capabilities (Step 1: MONITOR) track the resulting performance degradation.

Trigger activation occurs when drift detection metrics (Step 2: DETECT) exceed thresholds and governance review (Step 3: DECIDE) authorizes recalibration. The demonstration documents the time required to detect drift and the evidence presented for governance decision-making.

Targeted physics runs (Step 4: PREPARE) are selected using active learning methods to efficiently sample the new operating regime. The number of additional simulations required is tracked as a key efficiency metric. Fine-tuning execution (Step 5: UPDATE) applies continual learning methods to update the surrogate while preserving performance on the original regime.

Uncertainty recalibration (Step 6: CALIBRATE) adjusts prediction intervals to maintain calibration under the new conditions. Performance comparison documents the improvement in accuracy and uncertainty calibration before and after recalibration, demonstrating the framework's effectiveness.

## 5.4 Evaluation Plan

The evaluation plan defines the analyses that will be performed to assess framework performance and demonstrate value relative to alternative approaches.

### 5.4.1 Baseline Comparison

Baseline comparison evaluates three operational modes: physics-only (all predictions from numerical models), surrogate-only (all predictions from the trained surrogate without recalibration), and hybrid (surrogate with recalibration framework). Computational cost comparison quantifies the simulation time and resources required for each mode. Accuracy comparison assesses prediction quality across a range of scenarios, including conditions within and outside the original training distribution.

### 5.4.2 Recalibration Effectiveness

Recalibration effectiveness metrics quantify the framework's ability to maintain surrogate performance over time. Error reduction after update measures the improvement in accuracy metrics following recalibration. Uncertainty calibration improvement tracks changes in prediction interval coverage. Time to detect drift measures the latency between regime change and trigger activation. Number of physics runs required quantifies the computational cost of recalibration relative to full retraining.

### 5.4.3 Computational Efficiency

Computational efficiency metrics demonstrate the practical value of the surrogate approach. Speedup factors compare surrogate inference time to physics model simulation time, with target speedups of 10³ to 10⁴ times faster. Cost of targeted physics runs quantifies the computational investment required for recalibration. Total computational budget tracks cumulative resources over the operational period. Comparison to full retraining demonstrates the efficiency gains from continual learning relative to training new models from scratch.

## 5.5 Development Timeline

Implementation proceeds through three phases that progressively build capability and confidence, aligning with the development phases described in Section 4.5.

### 5.5.1 Phase 1: Prototype Demonstration

Phase 1 demonstrates one complete recalibration cycle using a single surrogate architecture (U-Net or U-FNO). Basic drift detection uses threshold-based triggers with manual governance decisions. Success is defined as completing the full MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY cycle with documented performance improvement.

### 5.5.2 Phase 2: Integrated Framework

Phase 2 integrates all framework components with realistic site data. Multiple surrogate options are available, with automated trigger logic implementing the composite drift index from Section 3.3.2. Continual learning with replay buffers and EWC enables efficient updates. A governance dashboard supports human-in-the-loop decision-making. Success is defined as framework operation on representative site data with governance-compliant documentation.

### 5.5.3 Phase 3: Operational System

Phase 3 deploys the framework for operational use at DOE EM sites. Production-quality implementation integrates with site monitoring systems and meets full regulatory documentation requirements. Training materials support site operators, and maintenance procedures ensure long-term sustainability. Success is defined as framework acceptance for operational use under DOE quality assurance requirements.

## 5.6 Summary

This section has presented the validation framework, prototype implementations, and case study design that demonstrate the recalibration framework in practice. The validation framework establishes metrics for performance, uncertainty, drift detection, and governance compliance that align with the methods described in Section 3. Two prototype implementations—U-FNO for cross-section transport and U-Net for pump-and-treat plume prediction—demonstrate the framework's applicability to representative groundwater modeling problems.

The case study design establishes a controlled scenario for demonstrating complete recalibration cycles, with drift injection and systematic evaluation of framework response. The evaluation plan defines baseline comparisons and effectiveness metrics that will quantify the framework's value relative to physics-only and surrogate-only approaches. The phased development timeline provides a path from prototype demonstration through operational deployment at DOE EM sites.
