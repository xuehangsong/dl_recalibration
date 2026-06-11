# 3. Methods

This section presents the technical methods underlying the DL Recalibration Framework, organized according to the three-pillar architecture introduced in Section 2. Section 3.1 addresses governance methods that establish the operational rules and constraints for the framework. Section 3.2 describes the modeling engine methods, including physics-based numerical models and deep learning surrogates. Section 3.3 details the recalibration mechanism methods that enable adaptive model maintenance. For readers interested in the detailed literature context for surrogate model architectures, Appendix A provides an extended review of the surrogate model landscape, including methodology for literature selection and comprehensive coverage of each model family.

## 3.1 Governance Methods (Pillar A)

Governance methods establish the operational rules, constraints, and decision criteria that guide all framework activities. These methods ensure that recalibration decisions align with site-specific requirements, regulatory constraints, and organizational policies.

### 3.1.1 Site-Specific Constraints

Site-specific constraints define the physical and operational boundaries within which the framework must operate. These constraints include aquifer properties such as hydraulic conductivity ranges, porosity values, and boundary conditions that reflect the hydrogeological setting. Contaminant characteristics including species types, concentration ranges, and regulatory limits establish the scope of predictions the surrogate must support. Infrastructure constraints encompass well locations, pumping capacities, and treatment system specifications that define the operational envelope. Temporal constraints specify the prediction horizons required for operational decisions, typically ranging from days for immediate operations to years for long-term planning.

### 3.1.2 Regulatory Requirements

Regulatory requirements establish the compliance framework within which all modeling and recalibration activities must occur. These requirements include maximum contaminant levels (MCLs) that define acceptable concentration thresholds, monitoring frequencies mandated by permits, and reporting requirements that specify the format and timing of model predictions. The framework must maintain audit trails documenting all model updates, the data used for recalibration, and the governance decisions that authorized changes. Regulatory requirements also influence uncertainty quantification standards, as predictions used for compliance decisions may require specific confidence levels or uncertainty bounds.

### 3.1.3 Operational Policies

Operational policies translate site constraints and regulatory requirements into actionable decision rules. These policies define the thresholds that trigger recalibration activities, specifying acceptable ranges for performance metrics, uncertainty bounds, and drift indicators. Policies establish the approval workflows for model updates, identifying which stakeholders must review and authorize changes before deployment. Resource allocation policies determine how computational resources are distributed between monitoring activities and recalibration tasks. Communication policies specify how model updates and their implications are communicated to operators, regulators, and other stakeholders.

### 3.1.4 Performance Standards

Performance standards establish quantitative criteria for evaluating surrogate model adequacy. These standards include accuracy metrics such as root mean square error (RMSE), mean absolute error (MAE), and coefficient of determination (R²) that must be maintained within specified bounds. Uncertainty standards define acceptable calibration levels, requiring that predicted confidence intervals contain the true values at specified frequencies. Computational standards establish maximum acceptable inference times to ensure predictions can support real-time operational decisions. Stability standards specify acceptable rates of performance degradation, triggering recalibration when metrics decline beyond defined thresholds.

### 3.1.5 Decision Authority Matrix

The decision authority matrix defines who can authorize different types of framework actions. Routine monitoring activities may proceed automatically without human intervention. Minor recalibration actions, such as uncertainty recalibration using conformal prediction, may require notification but not approval. Significant model updates, such as continual learning weight adjustments, require review by technical staff. Major changes, such as full model retraining or architecture modifications, require approval from project leadership and potentially regulatory notification. The matrix ensures appropriate oversight while enabling timely responses to detected issues.

## 3.2 Modeling Engine Methods (Pillar B)

Modeling engine methods encompass both the physics-based numerical models that provide high-fidelity simulations and the deep learning surrogates that enable rapid predictions. This section describes the modeling challenges, numerical model foundations, surrogate model landscape, and training approaches.

### 3.2.1 Site Challenges and Modeling Needs

Groundwater remediation sites present complex modeling challenges that motivate the need for efficient surrogate models. Heterogeneous subsurface properties create spatially variable flow and transport behavior that requires high-resolution discretization to capture accurately. Contaminant plumes exhibit complex geometries influenced by source locations, hydrogeological features, and remediation system operations. Transient conditions arising from seasonal variations, pumping schedules, and changing boundary conditions require models capable of capturing temporal dynamics. The combination of spatial complexity and temporal variability results in physics-based models that require substantial computational resources, often making real-time predictions infeasible for operational decision support.

### 3.2.2 Physics-Based Numerical Models

Physics-based numerical models provide the foundation for surrogate model development by generating training data and serving as the reference standard for accuracy evaluation. These models solve the governing equations for groundwater flow and contaminant transport using numerical methods such as finite differences, finite elements, or finite volumes. Flow models based on Darcy's law and the continuity equation simulate hydraulic head distributions and groundwater velocities. Transport models incorporating advection, dispersion, and reaction processes simulate contaminant concentration evolution. Coupled flow-transport models capture the interactions between these processes, including density-dependent flow effects when relevant. Model calibration using field observations establishes parameter values that reproduce observed behavior, while uncertainty analysis characterizes the range of plausible model predictions given parameter and structural uncertainties.

### 3.2.3 Surrogate Model Landscape

Deep learning surrogate models offer the potential to approximate physics-based model behavior at dramatically reduced computational cost, enabling real-time predictions for operational decision support. The surrogate model landscape encompasses several architectural families, each with distinct characteristics suited to different aspects of groundwater modeling.

Convolutional encoder-decoder architectures, including U-Net and its variants, excel at learning spatial mappings between input fields (such as hydraulic conductivity or boundary conditions) and output fields (such as hydraulic head or concentration distributions). These architectures leverage the spatial structure inherent in gridded subsurface data and have demonstrated success in predicting steady-state and transient groundwater behavior.

Operator-learning architectures, including Fourier Neural Operators (FNO) and Deep Operator Networks (DeepONet), learn mappings between function spaces rather than fixed discretizations. This approach offers potential advantages for problems requiring predictions at varying resolutions or for transfer learning across different site configurations.

Sequence models, including Long Short-Term Memory (LSTM) networks and Transformers, capture temporal dependencies in time-series predictions. These architectures are particularly relevant for forecasting contaminant concentrations at monitoring wells or predicting system responses to changing operational conditions.

Physics-informed approaches incorporate governing equations as soft constraints during training, potentially improving generalization and reducing data requirements. These methods can be combined with any of the above architectures to leverage physical knowledge alongside data-driven learning.

A comprehensive review of the surrogate model literature, including detailed discussion of each architecture family and their applications to subsurface modeling, is provided in Appendix A.

### 3.2.4 General Surrogate Model Training Setup

Surrogate model training follows established deep learning practices adapted for the groundwater modeling context. Training data generation involves running the physics-based numerical model across a range of input conditions that span the expected operational envelope. Input variations may include different hydraulic conductivity fields, boundary condition scenarios, pumping schedules, and initial conditions. The training dataset should capture the variability expected during operational deployment while remaining computationally tractable to generate.

Data preprocessing includes normalization of inputs and outputs to facilitate training, spatial interpolation if the surrogate operates at different resolution than the numerical model, and temporal alignment for time-series predictions. Train-validation-test splits ensure unbiased evaluation of model performance, with care taken to avoid data leakage when temporal or spatial correlations exist.

Training procedures employ standard optimization algorithms such as Adam with learning rate scheduling. Loss functions typically combine prediction accuracy terms with regularization to prevent overfitting. Early stopping based on validation performance prevents overtraining. Hyperparameter optimization, including architecture choices, learning rates, and regularization strengths, may employ grid search, random search, or Bayesian optimization approaches.

## 3.3 Recalibration Mechanism Methods (Pillar C)

Recalibration mechanism methods provide the adaptive capabilities that maintain surrogate model performance as conditions evolve. These methods span uncertainty quantification, trigger logic for detecting when recalibration is needed, and multiple update strategies ranging from lightweight adjustments to full retraining.

### 3.3.1 Uncertainty Quantification

Uncertainty quantification (UQ) methods enable the surrogate model to provide not just point predictions but also measures of prediction confidence. Reliable uncertainty estimates are essential for operational decision-making, as they indicate when predictions can be trusted and when additional caution is warranted.

Monte Carlo Dropout provides a computationally efficient approach to uncertainty estimation by applying dropout during inference and aggregating predictions across multiple stochastic forward passes. The variance across passes provides an estimate of model uncertainty, with higher variance indicating regions of input space where the model is less confident. This approach requires minimal architectural changes and can be applied to existing trained models.

Deep Ensembles train multiple models with different random initializations and aggregate their predictions. The spread across ensemble members captures both aleatoric uncertainty (inherent data variability) and epistemic uncertainty (model uncertainty due to limited training data). Ensembles typically provide well-calibrated uncertainty estimates but require training and maintaining multiple models.

Conformal Prediction provides distribution-free prediction intervals with guaranteed coverage properties. Given a calibration dataset, conformal prediction constructs prediction intervals that contain the true value with a specified probability, regardless of the underlying data distribution. This approach is particularly valuable for recalibration, as prediction intervals can be updated using new observations without retraining the underlying model.

Calibration assessment evaluates whether predicted uncertainties match observed error frequencies. A well-calibrated model should have 90% prediction intervals that contain the true value approximately 90% of the time. Calibration metrics such as the expected calibration error (ECE) and reliability diagrams quantify calibration quality and identify systematic over- or under-confidence.

### 3.3.2 Trigger Logic

Trigger logic methods detect when surrogate model performance has degraded sufficiently to warrant recalibration. Effective triggers balance sensitivity (detecting genuine degradation) against specificity (avoiding unnecessary recalibration due to normal variability).

Performance-based triggers monitor prediction accuracy metrics computed on incoming observations. When metrics such as RMSE or MAE exceed predefined thresholds, or when rolling averages show sustained degradation trends, recalibration is triggered. Threshold selection balances responsiveness against stability, with tighter thresholds enabling faster response but potentially triggering on transient fluctuations.

Uncertainty-based triggers monitor the calibration of uncertainty estimates. When prediction intervals consistently fail to achieve their nominal coverage (e.g., 90% intervals contain true values less than 85% of the time), the uncertainty quantification requires recalibration. Conversely, overly conservative intervals (coverage exceeding nominal levels) may indicate opportunities to tighten predictions.

Drift detection methods identify changes in the statistical properties of input data or model residuals that may indicate distribution shift. The Kolmogorov-Smirnov (KS) test compares the distribution of recent observations against a reference distribution, flagging significant differences. The Page-Hinkley test detects changes in the mean of a sequence, suitable for identifying gradual drift. Composite drift indices combine multiple indicators into a single metric that triggers when overall evidence of drift exceeds a threshold.

Governance-based triggers incorporate domain knowledge and operational context. Scheduled reviews ensure periodic assessment regardless of automated metrics. Event-based triggers respond to known changes such as new well installations, pumping schedule modifications, or seasonal transitions. Regulatory triggers ensure recalibration before compliance reporting deadlines.

### 3.3.3 Continual Learning

Continual learning methods update model weights to incorporate new information while preserving previously learned knowledge. The central challenge is catastrophic forgetting, where training on new data causes the model to lose performance on earlier data distributions.

Elastic Weight Consolidation (EWC) addresses catastrophic forgetting by adding a regularization term that penalizes changes to weights that were important for previous tasks. Importance is estimated using the Fisher information matrix, which measures how sensitive the loss is to each weight. Weights with high Fisher information are constrained to remain close to their previous values, while less important weights can adapt freely to new data.

Replay buffers maintain a subset of historical training examples that are interleaved with new data during updates. By continuing to train on representative historical examples, the model maintains performance on earlier distributions while adapting to new conditions. Buffer management strategies determine which examples to retain, with approaches including random sampling, reservoir sampling, and importance-based selection. Empirical studies suggest replay buffers containing 70-75% historical data and 25-30% new data provide effective balance.

Layer freezing selectively updates only certain layers while keeping others fixed. Early layers that learn general features may be frozen to preserve foundational representations, while later layers that learn task-specific mappings are updated to adapt to new conditions. This approach reduces computational cost and can improve stability when new data is limited.

Progressive networks add new capacity for new tasks while preserving existing weights entirely. Lateral connections allow new components to leverage features learned by previous components. This approach eliminates forgetting but increases model size with each update.

### 3.3.4 Active Learning

Active learning methods strategically select which new data points would be most valuable for improving model performance, enabling efficient use of limited labeling budgets (in this context, expensive physics-based model runs).

Uncertainty sampling selects points where the current model is most uncertain, as measured by prediction variance, entropy, or other uncertainty metrics. By focusing on high-uncertainty regions, active learning efficiently reduces epistemic uncertainty and improves model coverage of the input space.

Query-by-committee uses an ensemble of models and selects points where ensemble members disagree most strongly. Disagreement indicates regions where additional training data would help resolve model uncertainty.

Expected model change selects points that would cause the largest update to model parameters if labeled. This approach directly targets points that would be most informative for learning.

Diversity sampling ensures selected points cover the input space broadly rather than clustering in a single high-uncertainty region. Combining uncertainty and diversity criteria often outperforms either alone.

Batch selection strategies determine how to select multiple points simultaneously when parallel labeling is possible. Batch sizes of 6-10 points have been found effective in related applications, balancing computational efficiency against the diminishing returns of larger batches.

### 3.3.5 Multi-Fidelity Data Fusion

Multi-fidelity data fusion methods combine information from sources of varying accuracy and cost. In the groundwater modeling context, high-fidelity sources include detailed physics-based simulations and laboratory measurements, while lower-fidelity sources include simplified models, remote sensing data, and operational measurements with higher uncertainty.

Transfer learning leverages models trained on abundant low-fidelity data as starting points for training on limited high-fidelity data. The low-fidelity model learns general patterns that transfer to the high-fidelity task, reducing the amount of expensive high-fidelity data required.

Co-kriging and related geostatistical methods model the correlation structure between fidelity levels, enabling optimal combination of multi-fidelity observations for spatial prediction.

Multi-fidelity neural networks incorporate fidelity level as an input, learning a single model that can predict at any fidelity level. This approach enables efficient training on mixed-fidelity datasets and can extrapolate to predict high-fidelity outputs from low-fidelity inputs.

Bayesian approaches place prior distributions over the relationship between fidelity levels, enabling principled uncertainty quantification that accounts for fidelity-dependent errors.

### 3.3.6 Full Retraining

Full retraining involves training a new surrogate model from scratch using an updated training dataset. While computationally expensive, full retraining may be necessary when cumulative drift has moved conditions far from the original training distribution, when model architecture changes are required, or when continual learning approaches have accumulated sufficient approximation errors.

The decision to fully retrain versus continue with incremental updates involves tradeoffs between computational cost, model performance, and operational continuity. Governance policies should specify conditions under which full retraining is required, such as after major site changes or when performance metrics fall below minimum acceptable thresholds despite incremental updates.

Full retraining provides an opportunity to incorporate architectural improvements, expand the training distribution to cover newly observed conditions, and reset any accumulated errors from incremental updates. The new model should be validated against both historical and recent observations before deployment, with parallel operation of old and new models during a transition period when feasible.

Training dataset curation for full retraining should include representative examples from the full operational history, with emphasis on conditions that caused previous model failures. Active learning insights from the operational period can guide selection of additional physics-based simulations to fill coverage gaps identified during deployment.
