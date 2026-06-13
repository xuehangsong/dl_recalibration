# 3.3 Recalibration Mechanism Methods

The recalibration component operates as a single, governed loop designed for stability, transparency, and regulatory credibility. The sequence is **monitor → decide → update (if warranted) → verify**. During routine operations, the surrogate remains unchanged; the team conducts monthly monitoring to track accuracy relative to the most recent stable baseline and calibration of stated uncertainty.

On a fixed decision window (e.g., quarterly), the program determines whether an update is justified. Action is taken only when evidence of drift has persisted for **60–90 days** or when a documented regime change has occurred. When action is justified, the framework executes a small, targeted update supported by a limited number of physics simulations and the most recent field observations. The revised surrogate is then evaluated against pre-registered acceptance criteria, including accuracy, uncertainty coverage, and performance at priority wells or zones. Throughout, the high-fidelity physics model remains the authoritative reference used to inform and validate changes.

## 3.3.1 Uncertainty Quantification

Uncertainty quantification (UQ) within the hybrid modeling framework reconciles the rapid execution of ML surrogates with the rigorous physical consistency of data assimilation (DA). By formalizing UQ across both domains, the framework provides reliable confidence intervals, identifies when a system is operating outside its known regime, and ensures that surrogate models remain physically bounded while assimilation cycles are informed by high-fidelity error characterizations.

### Surrogate Model UQ

For surrogate-based UQ, several approaches partition aleatoric and epistemic uncertainties:

| Method | Citation | Application |
|--------|----------|-------------|
| **Monte Carlo dropout** | (Gal and Ghahramani, 2016) | Estimates epistemic uncertainty by measuring model disagreement across stochastic forward passes |
| **Deep ensembles** | (Lakshminarayanan et al., 2017) | Estimates epistemic uncertainty through disagreement among independently trained models |
| **Conformal prediction** | (Shafer and Vovk, 2008) | Provides statistically valid uncertainty bounds with guaranteed coverage, without requiring strong distributional assumptions |

These methods enable the surrogate to provide not just point predictions but also uncertainty estimates that inform downstream decision-making and trigger logic.

### Physical Model UQ via Data Assimilation

Physical model UQ is handled via data assimilation techniques that reconcile model states with noisy observations:

| Method | Citation | Application |
|--------|----------|-------------|
| **Ensemble Kalman Filter (EnKF)** | (Evensen, 2003) | Computationally efficient covariance propagation when Gaussian assumptions hold |
| **Particle filters** | (Särkkä, 2013) | Represents posterior distribution through weighted samples for non-Gaussian or highly nonlinear contexts |
| **Sequential Bayesian inference** | (Kennedy and O'Hagan, 2001) | Iteratively refines posterior distributions as new observations are integrated |

For complex or high-dimensional systems, sequential Bayesian inference ensures that the physical model's state remains aligned with the evolving real-world system through iterative posterior refinement.

### Hybrid Integration Strategy

The framework treats surrogate UQ and physical-model DA as **complementary** rather than competing approaches (Diaa-Eldeen et al., 2025). Surrogates are utilized for fast, uncertainty-aware forecasting, while the DA framework handles rigorous state correction and parameter tuning using real-time observations.

A formal feedback loop is established where surrogate outputs—specifically the predicted mean and uncertainty—guide the localization and weight of assimilation updates (Cheng et al., 2023). This integration ensures that surrogate predictions inform where DA should focus corrections, DA results validate and refine surrogate uncertainty estimates, and the combined system maintains both computational efficiency and physical consistency.

This hybrid approach enables autonomous decision-making in complex dynamical systems while maintaining the reliability required for regulatory applications.

## 3.3.2 Trigger Logic

As surrogate models operate over time, data distributions and environmental conditions evolve. A trigger logic framework activates model recalibration to maintain trustworthiness and regulatory compliance. The framework combines statistical thresholds with domain-informed criteria to enable adaptive learning while maintaining model interpretability and performance.

### Drift Monitoring Framework

The drift monitoring framework consists of multiple, complementary metrics organized into four categories. By combining signals that capture loss of dynamical stability, increasing model uncertainty, and structural changes in data and learned representations, the framework enables early, interpretable, and statistically robust detection of regime drift.

**Category 1: Tipping Point–Inspired Resilience Metrics**

These metrics capture early signs of loss of dynamical stability, motivated by concepts from tipping point science. They are applied to model outputs, residuals, and latent representations without implying physical tipping points in the underlying system. Rolling variance and lag-1 autocorrelation detect increasing fluctuation amplitude and memory consistent with reduced resilience, while skewness and kurtosis monitor asymmetric error growth and heavy-tailed behavior indicative of excursions toward unstable regions.

**Category 2: Performance and Uncertainty-Based Metrics**

These metrics focus on direct indicators of model reliability under deployment. Prediction residuals are monitored using adaptive thresholds derived from rolling statistics, such as exceedance of 2× rolling standard deviation. Spatial-temporal clustering of persistent threshold violations or clustered error patterns indicates localized or systemic degradation. For probabilistic models, predictive variance or entropy is tracked, with sustained increases relative to historical baselines indicating growing epistemic uncertainty.

**Category 3: Distributional and Representation-Level Drift Detection**

These diagnostics target statistical and structural changes that may not immediately manifest in errors or uncertainty. Distributional drift is assessed by comparing incoming input/output distributions to reference distributions using nonparametric tests such as the Kolmogorov–Smirnov test, where statistically significant deviations (e.g., p < 0.01) indicate changes in the data-generating process. Latent space drift, measured as deviations from the training manifold in learned representation spaces such as bottleneck features or diffusion model embeddings, provides early detection of regime mismatch in high-dimensional settings.

**Category 4: Probabilistic Integration and Decision Logic**

The final category integrates all diagnostic signals into a robust decision-making layer. Bayesian inference combines evidence from resilience, performance, uncertainty, and distributional indicators with prior knowledge and alternative explanations such as data quality changes. Composite gating mechanisms, implemented as Boolean rules requiring concurrent exceedance across multiple metric families or score-based aggregation into a unified drift risk index, reduce false positives due to noise or transient anomalies and ensure that interventions are driven by consistent, multi-source evidence.

### Summary of Drift Diagnostics

| Metric / Indicator | Category | Applied To |
|--------------------|----------|------------|
| Rolling variance | Resilience | Outputs, residuals |
| Lag-1 autocorrelation | Resilience | Residuals, latent |
| Skewness / kurtosis | Resilience | Residuals |
| RMSE / bias | Performance | Outputs |
| Threshold exceedance | Performance | Residuals |
| Predictive variance | Uncertainty | Outputs |
| KS / energy distance | Distributional | Outputs |
| Maximum mean discrepancy | Distributional | Multivariate output fields |
| Latent Mahalanobis | Representation | Latent space |
| Reconstruction error | Representation | Latent space, outputs |
| Composite drift index | Integration | All |

### Implementation Workflow

A three-phase workflow translates generic drift metrics into practical tools for monitoring groundwater model reliability:

**Phase 1: Candidate Identification & Method Selection**

Curate a specific subset of indicators from the broader regime drift metrics that are physically and statistically relevant to subsurface flow and transport dynamics.

**Phase 2: Simulation-Based Robustness Testing**

Subject candidates to rigorous stress testing using synthetic test cases derived from physics-based model simulations. Scenario generation creates test cases representing common subsurface regime shifts including aquifer depletion, saltwater intrusion fronts, and recharge pattern changes. Reliability analysis quantifies sensitivity (true positive rate) and specificity (true negative rate), while Bayesian evaluation assesses performance in the presence of realistic hydrogeological noise and variable data quality.

**Phase 3: Operational Implementation & Recalibration Triggers**

Synthesize evaluation results to establish a standardized protocol for model maintenance. This phase involves selection of best performers by adopting indicators demonstrating high robustness and lead time, defining triggers by establishing quantitative thresholds as formal recalibration triggers (e.g., rising autocorrelation combined with latent space drift exceeding critical value), and distilling findings into community recommendations and best practices for the subsurface modeling community.
