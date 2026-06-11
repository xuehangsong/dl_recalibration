# 3.3.3 Continual Learning

Continual learning for scientific surrogate models focuses on updating a model in response to gradual system change while preserving valid historical behavior. The framework employs a conservative, stability-focused approach that fits DOE operational requirements.

## Approach Categories

Mature approaches fall into two widely adopted categories:

| Category | Description | Key Citation |
|----------|-------------|--------------|
| **Regularization-based** | Constrain parameter updates to avoid overwriting previously important knowledge | Elastic Weight Consolidation (Kirkpatrick et al., 2017) |
| **Replay-based** | Maintain stability by including a curated set of historical samples during updating | (De Lange et al., 2021) |

Within the environmental modeling literature, sequential fine-tuning has repeatedly been shown to outperform static surrogates in non-stationary systems such as energy load forecasting (Hurtado et al., 2023) and long-horizon operational forecasting (Sayed et al., 2025). These studies emphasize that **frequent retraining is unnecessary—and often destabilizing—when well-designed continual learning mechanisms are in place**.

This aligns with findings in hydrologic surrogate modeling, where modest periodic updates informed by new hydrologic states and compact replay buffers maintain performance while avoiding the computational cost of full retraining (Asher et al., 2015; Wang et al., 2023).

## Fine-tuning Process

Fine-tuning is initiated only after documented indicators of drift demonstrate meaningful degradation—such as sustained increases in predictive error, divergence between modeled and observed temporal trends, or reduced empirical coverage of uncertainty intervals. Once triggered, the update process proceeds through structured steps:

### Step 1: Assemble Update Dataset

Assemble a compact update dataset consisting of:
- Targeted physics simulations representing the changed regime
- Recent validated field observations
- **Replay sample of historical cases: 70–75% of the batch**, consistent with replay ratios shown effective in continual learning applications (De Lange et al., 2021)

### Step 2: Selective Layer Updates

- **Freeze early encoder layers** to preserve structural representations learned from the original physics-informed domain
- **Update later layers** using a small learning rate and a regularization penalty such as EWC or L2 anchoring, following recommendations from continual learning studies in dynamic engineering systems (Hurtado et al., 2023)

### Step 3: Validation and Early Stopping

Monitor validation performance and stop early once improvements plateau, following best practices for stability in sequential fine-tuning.

### Step 4: Uncertainty Recalibration

Recalibrate predictive uncertainty using held-out data or ensemble-based UQ methods to ensure that nominal intervals align with empirical coverage, consistent with uncertainty calibration practices in hydrology and geosciences (Zhu et al., 2019; Wen et al., 2021).

### Step 5: Governance Package

Prepare a governance package including:
- Pre-/post-update performance metrics
- Drift indicators
- Updated uncertainty diagnostics

The surrogate is promoted to operational status only if acceptance criteria are met; otherwise, the system reverts to the prior model.
