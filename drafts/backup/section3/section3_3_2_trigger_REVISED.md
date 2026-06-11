# 3.3.2 Trigger Logic

As surrogate models operate over time, data distributions and environmental conditions evolve. A trigger logic framework activates model recalibration to maintain trustworthiness and regulatory compliance. The framework combines statistical thresholds with domain-informed criteria to enable adaptive learning while maintaining model interpretability and performance.

## Drift Monitoring Framework

The drift monitoring framework consists of multiple, complementary metrics organized into four categories. By combining signals that capture loss of dynamical stability, increasing model uncertainty, and structural changes in data and learned representations, the framework enables early, interpretable, and statistically robust detection of regime drift.

### Category 1: Tipping Point–Inspired Resilience Metrics

These metrics capture early signs of loss of dynamical stability, motivated by concepts from tipping point science. They are applied to model outputs, residuals, and latent representations without implying physical tipping points in the underlying system.

- **Rolling variance and lag-1 autocorrelation**: Detect increasing fluctuation amplitude and memory, consistent with reduced resilience
- **Skewness and kurtosis**: Monitor asymmetric error growth and heavy-tailed behavior indicative of excursions toward unstable regions

### Category 2: Performance and Uncertainty-Based Metrics

These metrics focus on direct indicators of model reliability under deployment.

- **Prediction residuals**: Monitored using adaptive thresholds derived from rolling statistics (e.g., exceedance of 2× rolling standard deviation)
- **Spatial-temporal clustering**: Persistent threshold violations or clustered error patterns indicate localized or systemic degradation
- **Predictive uncertainty**: For probabilistic models, variance or entropy is tracked; sustained increases relative to historical baselines indicate growing epistemic uncertainty

### Category 3: Distributional and Representation-Level Drift Detection

These diagnostics target statistical and structural changes that may not immediately manifest in errors or uncertainty.

- **Distributional drift**: Assessed by comparing incoming input/output distributions to reference distributions using nonparametric tests (e.g., Kolmogorov–Smirnov test). Statistically significant deviations (e.g., p < 0.01) indicate changes in the data-generating process
- **Latent space drift**: Deviations from the training manifold in learned representation spaces (e.g., bottleneck features, diffusion model embeddings) provide early detection of regime mismatch in high-dimensional settings

### Category 4: Probabilistic Integration and Decision Logic

The final category integrates all diagnostic signals into a robust decision-making layer.

- **Bayesian inference**: Combines evidence from resilience, performance, uncertainty, and distributional indicators with prior knowledge and alternative explanations (e.g., data quality changes)
- **Composite gating mechanisms**: Implemented as Boolean rules (requiring concurrent exceedance across multiple metric families) or score-based aggregation into a unified drift risk index

This integration reduces false positives due to noise or transient anomalies and ensures that interventions are driven by consistent, multi-source evidence.

## Summary of Drift Diagnostics

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

## Implementation Workflow

A three-phase workflow translates generic drift metrics into practical tools for monitoring groundwater model reliability:

### Phase 1: Candidate Identification & Method Selection

Curate a specific subset of indicators from the broader regime drift metrics that are physically and statistically relevant to subsurface flow and transport dynamics.

### Phase 2: Simulation-Based Robustness Testing

Subject candidates to rigorous stress testing using synthetic test cases derived from physics-based model simulations:

- **Scenario generation**: Test cases representing common subsurface regime shifts (aquifer depletion, saltwater intrusion fronts, recharge pattern changes)
- **Reliability analysis**: Quantify sensitivity (true positive rate) and specificity (true negative rate)
- **Bayesian evaluation**: Assess performance in the presence of realistic hydrogeological noise and variable data quality

### Phase 3: Operational Implementation & Recalibration Triggers

Synthesize evaluation results to establish a standardized protocol for model maintenance:

- **Selection of best performers**: Adopt indicators demonstrating high robustness and lead time
- **Defining triggers**: Establish quantitative thresholds as formal recalibration triggers (e.g., rising autocorrelation combined with latent space drift exceeding critical value)
- **Community recommendation**: Distill findings into best practices for the subsurface modeling community
