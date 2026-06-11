# 3. Methods

This section defines how physics runs are transformed into training data, how surrogates are designed and trained, and how the framework determines that surrogates are accurate enough for decision support. The methods are organized around the three pillars: Governance (Pillar A), Modeling Engines (Pillar B), and Recalibration Mechanisms (Pillar C).

---

# 3.1 Governance Methods

This section defines the governance framework controlling how deep-learning surrogate models are developed, evaluated, monitored, and updated for long-term groundwater remediation at DOE-EM sites. The framework ensures surrogate modeling is scientifically defensible, operationally stable, and aligned with regulatory requirements.

## 3.1.1 Regulatory Framework

Governance is anchored in federal environmental modeling and quality-assurance guidance. Under CERCLA, remedial decisions must remain protective of human health and the environment over long operational horizons (EPA 540-R-01-007). The framework adopts principles from EPA's environmental modeling guidance (EPA/100/K-09/003), which emphasizes clear documentation of model purpose, assumptions, uncertainty, validation, and limitations before models are relied upon for decision support.

Surrogate modeling activities align with DOE O 414.1D Chg 2, which establishes a management system requiring defined acceptance criteria, performance monitoring, corrective action, and continuous improvement for analytical tools used in mission-critical applications. The framework is further governed under DOE EM-QA-001, which incorporates ASME NQA-1 standards (Subpart 2.7) and applies them to environmental management activities, including software and modeling systems.

Together, these regulatory and quality standards establish that surrogate models must be managed as controlled analytical software, with formal verification, validation, documentation, and configuration management processes that support regulatory confidence and long-term stewardship.

## 3.1.2 Model Usage Scope

A central governance principle is the explicit definition of how surrogate models may be used within DOE-EM decision workflows. Surrogate models are intended primarily to support **screening-level analyses**, including:

- Rapid evaluation of alternative remediation scenarios
- Sensitivity analyses and uncertainty exploration
- Preliminary planning studies

In these contexts, surrogates provide substantial value by enabling fast exploration of large scenario spaces that would be impractical using high-fidelity numerical models alone.

For formal regulatory or final remedy decisions, surrogate model outputs are **not used as stand-alone evidence**. Instead, surrogate results may inform and prioritize analyses, guide scenario selection for further evaluation, or support interpretation of system behavior, while final decisions remain grounded in high-fidelity physics-based modeling and empirical data. This distinction aligns with EPA remedial investigation and feasibility study guidance (EPA 540-G-89-004), which emphasizes that models must be used in a manner consistent with their purpose and limitations.

Governance ensures that surrogate models function as **advisory, efficiency-enhancing tools**, rather than replacements for established numerical simulators. Any application of surrogate outputs beyond screening-level support requires explicit documentation of assumptions, uncertainty, and corroboration with physics-based results, consistent with EPA modeling guidance and DOE quality expectations.

## 3.1.3 Acceptance Criteria and Triggers

The governance framework establishes predefined acceptance criteria and recalibration triggers that determine when surrogate models are considered reliable and when updates are warranted. These criteria are defined prior to deployment and are based on project-specific data quality objectives and decision needs, consistent with EPA quality assurance guidance for modeling applications (EPA QA/G-5M).

**Acceptance criteria** typically include:

- Quantitative performance metrics (e.g., error statistics at priority monitoring locations)
- Calibration of uncertainty estimates (e.g., empirical coverage of prediction intervals)
- Spatial and temporal consistency with observed plume behavior
- Stability of performance over time under routine operational conditions

**Recalibration triggers** are defined to detect meaningful degradation in surrogate performance or applicability:

- Sustained increases in prediction residuals
- Inflation or miscalibration of uncertainty estimates
- Documented changes in boundary conditions or operational regimes that move the system outside the surrogate's original training domain

These triggers are evaluated using objective, documented thresholds rather than ad hoc judgment, consistent with DOE quality assurance requirements for corrective action when performance expectations are not met (DOE O 414.1D Chg 2).

Importantly, the presence of a recalibration trigger does not automatically mandate recalibration. Governance requires formal justification that an update is necessary, proportional, and expected to improve performance. This conservative approach aligns with best practices for model lifecycle management and reduces the risk of destabilizing otherwise reliable surrogate model behavior.

## 3.1.4 Monitoring Schedule

The governance framework defines a structured but adaptable monitoring schedule for surrogate model oversight:

| Level | Frequency | Purpose |
|-------|-----------|---------|
| Automated diagnostics | Regular basis | Track surrogate performance, uncertainty behavior, and consistency with incoming monitoring data |
| Summary evaluations | Monthly or quarterly | Synthesize diagnostic results into management-level indicators |
| Formal decision points | Quarterly | Evaluate potential recalibration with auditable governance review |

This schedule may be adjusted to reflect site-specific monitoring frequencies, rates of system change, and regulatory reporting cycles. The guiding principle is that model review frequency should be commensurate with the pace of environmental and operational change, consistent with EPA and DOE expectations for adaptive environmental management (EPA/100/K-09/003).

## 3.1.5 Configuration Control

To support regulatory confidence and long-term stewardship, the governance framework requires full transparency and auditability for surrogate model deployment and updates. All surrogate model versions are subject to formal configuration control, including:

- Version tracking
- Documentation of training data and assumptions
- Preservation of prior approved models

Each recalibration or significant update produces a documented governance record that includes the trigger rationale, data sources used, evaluation against acceptance criteria, and verification results. These records are retained as part of the project's quality assurance documentation and support independent review or audit if required, consistent with ASME NQA-1 software quality requirements (Subpart 2.7).

Data provenance is explicitly governed. Monitoring data, numerical model outputs, and surrogate training datasets are tracked with metadata describing source, validation status, and applicability. This ensures that the influence of any dataset on surrogate behavior can be reconstructed, supporting traceability and corrective action if data quality concerns arise (EPA QA/G-5M).

### Rollback Definition

**Rollback** is defined within this framework as the formal withdrawal of a surrogate model from operational use, rather than reversion to a previously approved surrogate version. Rollback is invoked when an attempted incremental update fails to meet predefined acceptance criteria, indicating that the surrogate's training domain or structure is no longer scientifically valid.

Under a rollback condition:

1. Neither the updated surrogate nor the prior surrogate is permitted for continued screening or planning analyses
2. Surrogate-based decision support is explicitly suspended
3. Analytical support reverts exclusively to the high-fidelity physics-based numerical model
4. Rollback automatically triggers escalation to a governed full retraining process

Full retraining develops a new surrogate baseline from scratch using updated physics-model ensembles, revised assumptions, and refreshed validation datasets. The retrained surrogate is promoted to operational use only after all governance requirements are satisfied.

This definition of rollback reflects DOE expectations for conservative software lifecycle management in high-consequence environmental applications. Incremental updates are preferred when scientifically defensible, but continued use of any surrogate is not permitted once validity is in question.

---

## Governance Summary

The governance framework ensures that deep-learning surrogate models are integrated into DOE Environmental Management groundwater remediation workflows in a controlled, transparent, and regulator-aligned manner. Key principles include:

- Governance grounded in established EPA and DOE quality assurance standards (CERCLA, DOE O 414.1D, DOE EM-QA-001, NQA-1, EPA QA/G-5M, EPA/100/K-09/003)
- Surrogate use limited to screening- and planning-level decision support
- Primacy of high-fidelity physics-based numerical models for final regulatory and remedy decisions
- Objective acceptance criteria and documented recalibration triggers
- Formal configuration control with full auditability
- Explicit withdrawal and retraining procedures when surrogate validity is in question

---

# 3.2 Modeling Engine Methods

This section describes the physics-based numerical models and deep-learning surrogates that form Pillar B of the recalibration framework. Physics models provide high-fidelity reference simulations; surrogates provide fast inference for screening and scenario analysis.

## 3.2.1 Site Challenges and Modeling Needs

Numerical groundwater and reactive transport models provide the high-fidelity representation of site-specific subsurface processes that underpin Pillar B. At EM sites, these models describe how contaminants move and transform in complex hydrogeologic settings, and how engineered controls (e.g., pump-and-treat systems) influence plume evolution.

The physical phenomena represented typically include:

- **Advection and dispersion** of dissolved species (Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016)
- **Sorption** onto solid phases and associated reaction processes
- **Non-Fickian plume spreading** from heterogeneity and diffusion-controlled mass exchange between transmissive and low-permeability zones (Guo et al., 2021)
- **Back diffusion** from fine-grained units, recognized as a major control on plume persistence after source removal (Yang et al., 2016, 2017)
- **Density-driven flow** in systems impacted by DNAPL, LNAPL (Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017), or seawater intrusion (Werner et al., 2013; Xu et al., 2019)
- **Engineered operations** including pump-and-treat wells, injection/extraction networks, and time-varying boundary conditions (Ko et al., 2005)

These mechanisms explain why plumes can remain above regulatory thresholds long after active remediation has ceased, and must be explicitly represented in numerical models.

## 3.2.2 Physics-Based Numerical Models

Several well-established simulators serve as workhorses for groundwater flow and transport modeling:

| Model | Application | Citation |
|-------|-------------|----------|
| **MODFLOW** | Regional groundwater flow, multi-layer systems | (Harbaugh, 2005) |
| **MT3DMS** | Conservative and reactive solute transport | (Zheng and Wang, 1999) |
| **PFLOTRAN** | Reactive transport, multiphase flow, variable density | (Hammond et al., 2014) |
| **eSTOMP** | Variably saturated flow with geochemical reactions | (White and Oostrom, 2003) |
| **TOUGH2** | Non-isothermal processes, variable fluid density | (Pruess et al., 1999) |
| **PARFLOW** | Integrated surface-subsurface flow at high resolution | (Maxwell et al., 2015) |
| **HYDRUS** | Vadose zone and near-surface transport | (Šimůnek et al., 2016) |

Within Pillar B, these codes collectively form the high-fidelity modeling layer that defines the governing equations, numerical schemes, and parameterizations treated as authoritative reference.

### Computational Constraints

Despite their fidelity, these simulators impose significant computational constraints:

- Individual forward runs can take **hours to days** on standard computing resources (Hammond et al., 2014; Maxwell et al., 2015)
- Planning tasks often require **hundreds to thousands** of model evaluations for Monte Carlo realizations, scenario sweeps, or sensitivity analyses (Rubin, 2003)
- Interactive exploration of design space becomes impractical using only high-fidelity models

These limitations motivate the data-driven surrogate modeling engines that sit on top of the numerical model.

## 3.2.3 Surrogate Model Landscape

Recent work in hydrogeology and subsurface reactive transport has demonstrated that deep-learning surrogates can emulate high-fidelity simulators with **orders-of-magnitude speedup** while retaining accuracy (Li et al., 2020). We organize existing surrogate approaches into five families based on input-output structure and typical EM use-cases (Luo et al., 2023):

### Family 1: Convolutional Encoder-Decoder Models

**Architecture:** U-Net, ResNet variants  
**Use case:** High-resolution spatial fields (heads, salinity, plume extent)

These networks treat spatial fields as images and learn direct mappings from input fields (hydraulic conductivity, boundary conditions, pumping patterns) to output fields. Convolutions preserve interfaces, sharp fronts, and channelized structures.

Key citations:
- Attention U-Net for steady-state hydraulic head fields (Taccari et al., 2022)
- Image-to-image regression for multiphase flow (Mo et al., 2019)
- AR-ResUNet for dynamic multiphase flow and solute transport (Jiang et al., 2021)
- U-Net surrogate for transient groundwater flow inverse problems (Lauzon, 2024)

### Family 2: Operator-Learning Models

**Architecture:** FNO, U-FNO, DeepONet  
**Use case:** Learning PDE solution operators across many boundary/parameter configurations

Operator-learning models generalize beyond pointwise mappings to learn the entire solution operator of the PDE. The Fourier Neural Operator (FNO) learns this operator in Fourier space, enabling resolution-invariant surrogates (Li et al., 2020).

Key citations:
- U-FNO for CO₂-water multiphase systems (Wen et al., 2022)
- DeepONet for confined aquifer flow (Taccari et al., 2024)
- **GeoFUSE framework** for seawater intrusion: U-FNO achieves ~10⁵ speedup per inference relative to PFLOTRAN (Jiang et al., 2025)
- Physics-informed U-FNO for climate stress testing at Savannah River Site (Wang et al., 2022)

### Family 3: Sequence Models

**Architecture:** LSTM, GRU, Transformer variants  
**Use case:** Low-dimensional time series (breakthrough curves, well responses)

Sequence models focus on time series outputs monitored at high frequency. LSTM and GRU networks capture long-range temporal dependencies.

Key citations:
- GRU-based surrogates for groundwater levels and water quality (Chen et al., 2021)
- Encoder-decoder LSTM for contaminant source identification (Anshuman and Eldho, 2023)
- DSCNN-GRU surrogate for transient groundwater head fields (Li et al., 2025)

### Family 4: Generative Models

**Architecture:** VAE, GAN, diffusion models  
**Use case:** Sampling full state ensembles, probabilistic inversion

Generative surrogates sample entire ensembles of plausible states and parameter fields consistent with physics and observations.

Key citations:
- VAE/GAN for facies realizations and Bayesian inversion (Graham and Chen, 2020)
- Diffusion models for multivariate subsurface property fields (Miele and Linde, 2025)
- Pretrained diffusion model for porous-media flow (Wang et al., 2025c)
- Conditional diffusion for CO₂ storage plume forecasting (Wang et al., 2025b)

### Family 5: Regression Surrogates

**Architecture:** Gaussian processes, Kriging, shallow ANNs  
**Use case:** Low-dimensional mappings (design variables → scalar metrics)

For decision-support tasks where quantities of interest are scalar metrics (total cost, cleanup time, risk index), simpler regression surrogates remain powerful tools, especially when data are limited and interpretability matters.

Key citations:
- Review of surrogate models in groundwater (Asher et al., 2015)
- Reduced-dimensional GP regression for groundwater allocation (Siade et al., 2020)
- GP surrogate for surfactant-enhanced aquifer remediation (Shams et al., 2021)
- Advances in GP surrogate construction and validation (Marrel and Iooss, 2024)

## 3.2.4 Training Setup

Standard practices for surrogate model training include:

| Element | Approach |
|---------|----------|
| **Data splits** | Hold out realizations across time and parameter ranges; separate training and test ensembles (Jiang et al., 2025) |
| **Normalization** | Standardize each channel; record scaling in metadata for consistent inference |
| **Early stopping** | Track validation metric on decision outputs, not only global averages; save best checkpoint |
| **Runtime reporting** | Record forward runtime and surrogate inference time to report speedups alongside accuracy |

The numerical models described in this section provide training data, physical grounding, and validation targets for surrogates, while surrogates aim to reproduce key numerical results at a fraction of the computational cost.

**Note:** Detailed paper-by-paper analysis of surrogate modeling literature is provided in Appendix A (Tables A1, A2).

---

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

The framework treats surrogate UQ and physical-model DA as **complementary** rather than competing approaches (Diaa-Eldeen et al., 2025):

- **Surrogates** are utilized for fast, uncertainty-aware forecasting
- **DA framework** handles rigorous state correction and parameter tuning using real-time observations

A formal feedback loop is established where surrogate outputs—specifically the predicted mean and uncertainty—guide the localization and weight of assimilation updates (Cheng et al., 2023). This integration ensures that:

1. Surrogate predictions inform where DA should focus corrections
2. DA results validate and refine surrogate uncertainty estimates
3. The combined system maintains both computational efficiency and physical consistency

This hybrid approach enables autonomous decision-making in complex dynamical systems while maintaining the reliability required for regulatory applications.

## 3.3.2 Trigger Logic

As surrogate models operate over time, data distributions and environmental conditions evolve. A trigger logic framework activates model recalibration to maintain trustworthiness and regulatory compliance. The framework combines statistical thresholds with domain-informed criteria to enable adaptive learning while maintaining model interpretability and performance.

### Drift Monitoring Framework

The drift monitoring framework consists of multiple, complementary metrics organized into four categories. By combining signals that capture loss of dynamical stability, increasing model uncertainty, and structural changes in data and learned representations, the framework enables early, interpretable, and statistically robust detection of regime drift.

**Category 1: Tipping Point–Inspired Resilience Metrics**

These metrics capture early signs of loss of dynamical stability, motivated by concepts from tipping point science. They are applied to model outputs, residuals, and latent representations without implying physical tipping points in the underlying system.

- **Rolling variance and lag-1 autocorrelation**: Detect increasing fluctuation amplitude and memory, consistent with reduced resilience
- **Skewness and kurtosis**: Monitor asymmetric error growth and heavy-tailed behavior indicative of excursions toward unstable regions

**Category 2: Performance and Uncertainty-Based Metrics**

These metrics focus on direct indicators of model reliability under deployment.

- **Prediction residuals**: Monitored using adaptive thresholds derived from rolling statistics (e.g., exceedance of 2× rolling standard deviation)
- **Spatial-temporal clustering**: Persistent threshold violations or clustered error patterns indicate localized or systemic degradation
- **Predictive uncertainty**: For probabilistic models, variance or entropy is tracked; sustained increases relative to historical baselines indicate growing epistemic uncertainty

**Category 3: Distributional and Representation-Level Drift Detection**

These diagnostics target statistical and structural changes that may not immediately manifest in errors or uncertainty.

- **Distributional drift**: Assessed by comparing incoming input/output distributions to reference distributions using nonparametric tests (e.g., Kolmogorov–Smirnov test). Statistically significant deviations (e.g., p < 0.01) indicate changes in the data-generating process
- **Latent space drift**: Deviations from the training manifold in learned representation spaces (e.g., bottleneck features, diffusion model embeddings) provide early detection of regime mismatch in high-dimensional settings

**Category 4: Probabilistic Integration and Decision Logic**

The final category integrates all diagnostic signals into a robust decision-making layer.

- **Bayesian inference**: Combines evidence from resilience, performance, uncertainty, and distributional indicators with prior knowledge and alternative explanations (e.g., data quality changes)
- **Composite gating mechanisms**: Implemented as Boolean rules (requiring concurrent exceedance across multiple metric families) or score-based aggregation into a unified drift risk index

This integration reduces false positives due to noise or transient anomalies and ensures that interventions are driven by consistent, multi-source evidence.

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

Subject candidates to rigorous stress testing using synthetic test cases derived from physics-based model simulations:

- **Scenario generation**: Test cases representing common subsurface regime shifts (aquifer depletion, saltwater intrusion fronts, recharge pattern changes)
- **Reliability analysis**: Quantify sensitivity (true positive rate) and specificity (true negative rate)
- **Bayesian evaluation**: Assess performance in the presence of realistic hydrogeological noise and variable data quality

**Phase 3: Operational Implementation & Recalibration Triggers**

Synthesize evaluation results to establish a standardized protocol for model maintenance:

- **Selection of best performers**: Adopt indicators demonstrating high robustness and lead time
- **Defining triggers**: Establish quantitative thresholds as formal recalibration triggers (e.g., rising autocorrelation combined with latent space drift exceeding critical value)
- **Community recommendation**: Distill findings into best practices for the subsurface modeling community

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

Assemble a compact update dataset consisting of:
- Targeted physics simulations representing the changed regime
- Recent validated field observations
- **Replay sample of historical cases: 70–75% of the batch**, consistent with replay ratios shown effective in continual learning applications (De Lange et al., 2021)

**Step 2: Selective Layer Updates**

- **Freeze early encoder layers** to preserve structural representations learned from the original physics-informed domain
- **Update later layers** using a small learning rate and a regularization penalty such as EWC or L2 anchoring, following recommendations from continual learning studies in dynamic engineering systems (Hurtado et al., 2023)

**Step 3: Validation and Early Stopping**

Monitor validation performance and stop early once improvements plateau, following best practices for stability in sequential fine-tuning.

**Step 4: Uncertainty Recalibration**

Recalibrate predictive uncertainty using held-out data or ensemble-based UQ methods to ensure that nominal intervals align with empirical coverage, consistent with uncertainty calibration practices in hydrology and geosciences (Zhu et al., 2019; Wen et al., 2021).

**Step 5: Governance Package**

Prepare a governance package including:
- Pre-/post-update performance metrics
- Drift indicators
- Updated uncertainty diagnostics

The surrogate is promoted to operational status only if acceptance criteria are met; otherwise, the system reverts to the prior model.

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

Score candidates using uncertainty and error metrics, including:
- Predictive variance
- Credible interval width
- Residual patterns relative to recent field observations

These scoring methods are consistent with approaches applied in hydrologic surrogate refinement (Wang et al., 2023).

**Step 3: Apply Diversity Constraints**

Apply diversity constraints to ensure selected scenarios span:
- Hydraulic gradients
- Hydrostratigraphic units
- Forcing conditions

This prevents clustering in redundant areas and enhances surrogate generalization.

**Step 4: Select High-Value Simulations**

Select **6–10 high-value simulations** that collectively maximize expected information gain, consistent with batch active learning recommendations in environmental modeling (Vesselinov et al., 2017).

**Step 5: Document Rationale**

Document simulation rationale, including expected uncertainty reduction and operational relevance.

**Step 6: Execute and Integrate**

Execute selected simulations and incorporate results directly into the fine-tuning batch described in Section 3.3.3, ensuring integration with continual learning and drift mitigation mechanisms.

## 3.3.5 Multi-fidelity Data Fusion

Multi-fidelity modeling enhances surrogate accuracy and computational efficiency by combining inexpensive low-fidelity simulations with high-fidelity simulations and field observations. This approach enables broad coverage of the parameter space while anchoring predictions to high-accuracy data where available.

### Fusion Strategies

Two mature strategies dominate the multi-fidelity literature:

1. **Autoregressive Gaussian-process and co-Kriging models** treat high-fidelity outputs as corrected versions of low-fidelity predictions (Kennedy & O'Hagan, 2000; Le Gratiet, 2013). These methods provide principled uncertainty propagation and are well-suited for problems with moderate dimensionality.

2. **Neural discrepancy models** learn nonlinear mappings between fidelity levels (Perdikaris et al., 2017). These approaches capture complex relationships that linear correction models cannot represent, enabling more flexible fidelity fusion.

Recent advances include physics-aware multi-fidelity networks that embed physical constraints directly into the learning architecture (Wen et al., 2021) and transfer learning approaches in which surrogates are pre-trained on large low-fidelity ensembles and fine-tuned using a smaller high-fidelity subset (Tang et al., 2022).

### Fidelity Levels

In groundwater flow and reactive transport applications:

- **Low-fidelity (LF)**: Coarse-grid simulations (e.g., coarse PFLOTRAN or MODFLOW models) provide broad characterization of system variability across the parameter and operational space.
- **High-fidelity (HF)**: Fine-grid simulations or field observations anchor localized accuracy where precise predictions are required.

This combination achieves strong performance with orders-of-magnitude reduction in simulation cost compared to using high-fidelity data alone (Asher et al., 2015).

### Fusion Process

The multi-fidelity fusion procedure integrates coarse simulations, fine simulations, and field data through a structured workflow:

1. **Identify fidelity levels and align datasets**, ensuring spatial, temporal, and unit consistency across LF, HF, and observational sources.

2. **Pre-train surrogate models on low-fidelity simulations**, exploiting their broad coverage of the parameter and operational space.

3. **Introduce high-fidelity data**—simulation or observational—and train a discrepancy model or co-Kriging structure so that predictions inherit LF global structure and HF local accuracy (Kennedy & O'Hagan, 2000; Perdikaris et al., 2017).

4. **Quantify fidelity-conditioned uncertainty**, expanding intervals where only LF information is available and narrowing them where HF evidence supports confidence, consistent with UQ strategies in Wen et al. (2021).

5. **Validate fused predictions** against withheld HF runs or independent observational periods to confirm improved performance over single-fidelity surrogates.

6. **Integrate the fused surrogate into the continual learning loop**, enabling more accurate drift detection, better-informed active learning selection, and more stable fine-tuning updates.

### Integration with Recalibration Framework

Multi-fidelity methods integrate naturally with active learning and continual learning, enabling scalable refinement even under evolving operational regimes. When active learning identifies high-uncertainty regions, the framework can strategically deploy either LF or HF simulations based on the expected information gain and computational budget. The fused surrogate provides improved baseline predictions that enhance drift detection sensitivity and reduce false-positive recalibration triggers.

## 3.3.6 Full Retraining

Full retraining is reserved for circumstances in which the existing surrogate is no longer representative of the physical system or operational domain. This approach provides a clean, traceable reset that aligns with DOE's emphasis on lifecycle documentation and reproducibility.

### Trigger Conditions

Concept drift literature emphasizes that full retraining is appropriate when foundational assumptions underlying the surrogate no longer hold (Parisi et al., 2019; Sayed et al., 2025). Specific conditions that warrant full retraining include:

- **Regime shifts or major forcing changes** that fundamentally alter system behavior beyond the original training domain
- **Redefinition of the underlying physics model**, such as revised geologic interpretations or updated reaction networks
- **Recalibration of the numerical model** after incorporation of new hydrogeologic data or conceptual model updates (Laloy et al., 2017)
- **Major reconfiguration of pumping and boundary conditions** that invalidate the original training scenarios
- **Repeated fine-tuning failures** indicating that the training domain has materially shifted

Studies in multi-fidelity and physics-informed ML reinforce that when high-fidelity simulations deviate substantially from prior domains, incremental updates cannot maintain integrity, and a new baseline surrogate is needed (Wen et al., 2021).

### Retraining Process

The retraining process proceeds through a formal set of steps:

1. **Verify retraining triggers**, including major operational changes, substantive updates to the physics model, or repeated fine-tuning failures indicating material domain shift.

2. **Redesign the training domain**, defining updated ranges of hydrofacies, operational scenarios, and boundary forcings consistent with new conceptual understanding.

3. **Generate a new ensemble of high-fidelity simulations**, supplemented where appropriate by low-fidelity runs to maintain broad coverage and accelerate sampling.

4. **Integrate recent field observations**, anchoring the surrogate to empirical system behavior.

5. **Train a new surrogate from scratch**, including UQ calibration, validation against benchmark scenarios, and documentation of performance improvements relative to the previous baseline.

6. **Designate the new model as the operational baseline**, while archiving the prior surrogate, training data, and diagnostic artifacts to preserve full scientific and regulatory traceability.

### Governance Requirements

Full retraining is conducted under configuration control and subject to the same verification, validation, uncertainty calibration, and acceptance criteria as an initial deployment. The retrained surrogate is promoted to operational use only after all governance requirements are satisfied.

Key governance elements include:

- **Complete documentation** of trigger rationale, data sources, and design decisions
- **Archival of prior surrogate** and all associated training artifacts
- **Independent validation** against withheld data and benchmark scenarios
- **Formal acceptance review** before operational deployment

This conservative approach reflects DOE expectations for software lifecycle management in high-consequence environmental applications, ensuring that continued use of any surrogate is not permitted once validity is in question.
