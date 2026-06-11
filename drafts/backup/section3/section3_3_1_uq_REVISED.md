# 3.3.1 Uncertainty Quantification

Uncertainty quantification (UQ) within the hybrid modeling framework reconciles the rapid execution of ML surrogates with the rigorous physical consistency of data assimilation (DA). By formalizing UQ across both domains, the framework provides reliable confidence intervals, identifies when a system is operating outside its known regime, and ensures that surrogate models remain physically bounded while assimilation cycles are informed by high-fidelity error characterizations.

## Surrogate Model UQ

For surrogate-based UQ, several approaches partition aleatoric and epistemic uncertainties:

| Method | Citation | Application |
|--------|----------|-------------|
| **Monte Carlo dropout** | (Gal and Ghahramani, 2016) | Estimates epistemic uncertainty by measuring model disagreement across stochastic forward passes |
| **Deep ensembles** | (Lakshminarayanan et al., 2017) | Estimates epistemic uncertainty through disagreement among independently trained models |
| **Conformal prediction** | (Shafer and Vovk, 2008) | Provides statistically valid uncertainty bounds with guaranteed coverage, without requiring strong distributional assumptions |

These methods enable the surrogate to provide not just point predictions but also uncertainty estimates that inform downstream decision-making and trigger logic.

## Physical Model UQ via Data Assimilation

Physical model UQ is handled via data assimilation techniques that reconcile model states with noisy observations:

| Method | Citation | Application |
|--------|----------|-------------|
| **Ensemble Kalman Filter (EnKF)** | (Evensen, 2003) | Computationally efficient covariance propagation when Gaussian assumptions hold |
| **Particle filters** | (Särkkä, 2013) | Represents posterior distribution through weighted samples for non-Gaussian or highly nonlinear contexts |
| **Sequential Bayesian inference** | (Kennedy and O'Hagan, 2001) | Iteratively refines posterior distributions as new observations are integrated |

For complex or high-dimensional systems, sequential Bayesian inference ensures that the physical model's state remains aligned with the evolving real-world system through iterative posterior refinement.

## Hybrid Integration Strategy

The framework treats surrogate UQ and physical-model DA as **complementary** rather than competing approaches (Diaa-Eldeen et al., 2025):

- **Surrogates** are utilized for fast, uncertainty-aware forecasting
- **DA framework** handles rigorous state correction and parameter tuning using real-time observations

A formal feedback loop is established where surrogate outputs—specifically the predicted mean and uncertainty—guide the localization and weight of assimilation updates (Cheng et al., 2023). This integration ensures that:

1. Surrogate predictions inform where DA should focus corrections
2. DA results validate and refine surrogate uncertainty estimates
3. The combined system maintains both computational efficiency and physical consistency

This hybrid approach enables autonomous decision-making in complex dynamical systems while maintaining the reliability required for regulatory applications.
