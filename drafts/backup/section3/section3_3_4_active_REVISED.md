# 3.3.4 Active Learning

Active learning identifies new physics simulations that provide the highest expected improvement in surrogate accuracy, stability, or uncertainty reduction. These approaches are simple, interpretable, and well aligned with DOE's operational context, where transparency and governance are essential.

## Sampling Strategies

Mature approaches include:

| Strategy | Description | Citation |
|----------|-------------|----------|
| **Uncertainty sampling** | Selects simulations at locations with high predictive variance | (Settles, 2009) |
| **Error-based sampling** | Targets regions where model–observation residuals are large or persistent | (Cohn et al., 1996) |
| **Diversity constraints** | Ensures spatial dispersion, stratigraphic coverage, and forcing variability to prevent sampling redundancy | (Wen et al., 2021) |

These strategies have been widely used in groundwater inversion, contaminant transport modeling, and CO₂ storage forecasting, where simulation costs are high and surrogate models must be continually refined (Wang et al., 2023). Recent hydrologic literature emphasizes the value of selecting simulations near the "vicinity of the solution manifold," where small corrections yield substantial improvements in predictive fidelity.

## Selection Process

Active learning is invoked only when a quarterly update is justified by monitoring diagnostics. Once activated, the process progresses through structured steps:

### Step 1: Generate Candidate Pool

Generate a candidate pool of operationally relevant simulation scenarios representing the current regime and near-term management options (e.g., pumping schedules, well reconfigurations).

### Step 2: Score Candidates

Score candidates using uncertainty and error metrics, including:
- Predictive variance
- Credible interval width
- Residual patterns relative to recent field observations

These scoring methods are consistent with approaches applied in hydrologic surrogate refinement (Wang et al., 2023).

### Step 3: Apply Diversity Constraints

Apply diversity constraints to ensure selected scenarios span:
- Hydraulic gradients
- Hydrostratigraphic units
- Forcing conditions

This prevents clustering in redundant areas and enhances surrogate generalization.

### Step 4: Select High-Value Simulations

Select **6–10 high-value simulations** that collectively maximize expected information gain, consistent with batch active learning recommendations in environmental modeling (Vesselinov et al., 2017).

### Step 5: Document Rationale

Document simulation rationale, including expected uncertainty reduction and operational relevance.

### Step 6: Execute and Integrate

Execute selected simulations and incorporate results directly into the fine-tuning batch described in Section 3.3.3, ensuring integration with continual learning and drift mitigation mechanisms.
