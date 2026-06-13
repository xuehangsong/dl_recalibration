# 5. Prototype Demonstration

This section describes the prototype implementations and case study that will demonstrate the recalibration framework in practice. The prototypes serve as proof-of-concept implementations that validate the seven-step workflow described in Section 2.2 and the methods detailed in Section 3. By demonstrating a complete recalibration cycle on representative groundwater modeling problems, these prototypes establish the feasibility of adaptive surrogate management for DOE environmental management applications.

## 5.1 Demonstration Objectives

The primary objective of the prototype demonstration is to complete one full recalibration cycle, validating that the framework can detect surrogate degradation, execute targeted updates, and restore prediction accuracy. This demonstration corresponds to Phase 1 of the development roadmap described in Section 4.3.1, which focuses on proving the concept before building production-quality software.

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

The training workflow uses a 70/15/15 split for training, validation, and test sets. Mean squared error loss is minimized using the Adam optimizer with early stopping based on validation performance. Autoregressive rollout enables multi-step prediction by feeding predicted outputs back as inputs for subsequent time steps.

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

### 5.3.4 Evaluation Approach

The evaluation will compare surrogate performance before and after recalibration across multiple dimensions. Accuracy metrics including root mean square error and mean absolute error will quantify prediction improvement. Uncertainty calibration metrics will verify that prediction intervals maintain appropriate coverage. Computational efficiency metrics will document the speedup relative to physics-only approaches and the number of targeted physics runs required for recalibration.

The evaluation will also compare three operational modes: physics-only analysis using numerical models for all predictions, surrogate-only analysis using the trained surrogate without recalibration, and hybrid analysis using the surrogate with the recalibration framework. This comparison will quantify the value added by the recalibration framework relative to both alternatives.

## 5.4 Expected Outcomes

The prototype demonstration is expected to produce several quantitative outcomes. Surrogate inference speedups of 10³ to 10⁴ times relative to physics-based models will enable real-time decision support. Recalibration will require fewer than 10 targeted physics simulations selected by active learning, demonstrating efficient use of computational resources. Post-recalibration accuracy will recover to within acceptance criteria defined in Section 3.1.3.

The demonstration will produce documented deliverables including a complete recalibration cycle with all seven workflow steps executed and recorded, governance documentation meeting the audit trail requirements of Section 3.1.5, and reproducible code capturing each step for subsequent development phases.

The demonstration will also generate lessons for Phase 2 development as described in Section 4.3.2. These lessons will inform decisions about automation priorities, user interface requirements, and integration with site data systems. Experience with the prototype will reveal which aspects of the workflow benefit most from automation and which require continued human oversight.

## 5.5 Summary

This section has described the prototype implementations and case study design that will demonstrate the recalibration framework. Two prototypes—U-FNO for cross-section transport and U-Net for pump-and-treat plume prediction—provide test cases for the seven-step workflow. The case study design establishes a controlled scenario for demonstrating complete recalibration cycles, with drift injection and systematic evaluation of framework response. Expected outcomes include quantitative validation of speedup and accuracy, documented governance procedures, and lessons for subsequent development phases.
