## 3.3.3 Continual Learning

Continual learning for scientific surrogate models focuses on updating a model in response to gradual system change while preserving valid historical behavior. The framework employs a conservative, stability-focused approach that fits DOE operational requirements.

### Approach Categories

Mature approaches fall into two widely adopted categories:

| Category | Description | Key Citation |
|----------|-------------|--------------|
| **Regularization-based** | Constrain parameter updates to avoid overwriting previously important knowledge | Elastic Weight Consolidation (Kirkpatrick et al., 2017) |
| **Replay-based** | Maintain stability by including a curated set of historical samples during updating | (De Lange et al., 2021) |

Within the environmental modeling literature, sequential fine-tuning has repeatedly been shown to outperform static surrogates in non-stationary systems such as energy load forecasting (Hurtado et al., 2023) and long-horizon operational forecasting (Sayed et al., 2025). These studies emphasize that **frequent retraining is unnecessary—and often destabilizing—when well-designed continual learning mechanisms are in place**.

This aligns with findings in hydrologic surrogate modeling, where modest periodic updates informed by new hydrologic states and compact replay buffers maintain performance while avoiding the computational cost of full retraining (Asher et al., 2015; Wang et al., 2023).

### Fine-tuning Process

Fine-tuning is initiated only after documented indicators of drift demonstrate meaningful degradation—such as sustained increases in predictive error, divergence between modeled and observed temporal trends, or reduced empirical coverage of uncertainty intervals. Once triggered, the update process proceeds through structured steps:

**Step 1: Assemble Update Dataset**

The first step assembles a compact update dataset consisting of targeted physics simulations representing the changed regime, recent validated field observations, and a replay sample of historical cases comprising **70–75% of the batch**, consistent with replay ratios shown effective in continual learning applications (De Lange et al., 2021).

**Step 2: Selective Layer Updates**

The second step freezes early encoder layers to preserve structural representations learned from the original physics-informed domain, while updating later layers using a small learning rate and a regularization penalty such as EWC or L2 anchoring, following recommendations from continual learning studies in dynamic engineering systems (Hurtado et al., 2023).

**Step 3: Validation and Early Stopping**

Monitor validation performance and stop early once improvements plateau, following best practices for stability in sequential fine-tuning.

**Step 4: Uncertainty Recalibration**

Recalibrate predictive uncertainty using held-out data or ensemble-based UQ methods to ensure that nominal intervals align with empirical coverage, consistent with uncertainty calibration practices in hydrology and geosciences (Zhu et al., 2019; Wen et al., 2021).

**Step 5: Governance Package**

Prepare a governance package including pre-/post-update performance metrics, drift indicators, and updated uncertainty diagnostics. The surrogate is promoted to operational status only if acceptance criteria are met; otherwise, the system reverts to the prior model.

## 3.3.4 Active Learning

Active learning identifies new physics simulations that provide the highest expected improvement in surrogate accuracy, stability, or uncertainty reduction. These approaches are simple, interpretable, and well aligned with DOE's operational context, where transparency and governance are essential.

### Sampling Strategies

Mature approaches include:

| Strategy | Description | Citation |
|----------|-------------|----------|
| **Uncertainty sampling** | Selects simulations at locations with high predictive variance | (Settles, 2009) |
| **Error-based sampling** | Targets regions where model–observation residuals are large or persistent | (Cohn et al., 1996) |
| **Diversity constraints** | Ensures spatial dispersion, stratigraphic coverage, and forcing variability to prevent sampling redundancy | (Wen et al., 2021) |

These strategies have been widely used in groundwater inversion, contaminant transport modeling, and CO₂ storage forecasting, where simulation costs are high and surrogate models must be continually refined (Wang et al., 2023). Recent hydrologic literature emphasizes the value of selecting simulations near the "vicinity of the solution manifold," where small corrections yield substantial improvements in predictive fidelity.

### Selection Process

Active learning is invoked only when a quarterly update is justified by monitoring diagnostics. Once activated, the process progresses through structured steps:

**Step 1: Generate Candidate Pool**

Generate a candidate pool of operationally relevant simulation scenarios representing the current regime and near-term management options (e.g., pumping schedules, well reconfigurations).

**Step 2: Score Candidates**

Score candidates using uncertainty and error metrics, including predictive variance, credible interval width, and residual patterns relative to recent field observations. These scoring methods are consistent with approaches applied in hydrologic surrogate refinement (Wang et al., 2023).

**Step 3: Apply Diversity Constraints**

Apply diversity constraints to ensure selected scenarios span hydraulic gradients, hydrostratigraphic units, and forcing conditions. This prevents clustering in redundant areas and enhances surrogate generalization.

**Step 4: Select High-Value Simulations**

Select **6–10 high-value simulations** that collectively maximize expected information gain, consistent with batch active learning recommendations in environmental modeling (Vesselinov et al., 2017).

**Step 5: Document Rationale**

Document simulation rationale, including expected uncertainty reduction and operational relevance.

**Step 6: Execute and Integrate**

Execute selected simulations and incorporate results directly into the fine-tuning batch described in Section 3.3.3, ensuring integration with continual learning and drift mitigation mechanisms.
