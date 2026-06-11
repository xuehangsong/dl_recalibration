# 2.1 Three-Pillar Architecture

The proposed recalibration framework is organized around three core pillars that together provide the foundation for maintaining deep-learning surrogate accuracy over operational timescales. Rather than representing sequential workflow stages or software layers, these pillars function as management domains—organizational containers that hold and maintain specific concerns essential to the framework's operation. Each pillar serves a distinct role: Pillar A establishes the rules and policies that govern operations, Pillar B manages the computational models that generate predictions and ground truth, and Pillar C provides the adaptive methods that monitor performance and orchestrate corrections.

The three pillars define what the framework manages, while the recalibration workflow described in Section 2.2 defines how these elements interact during operations. Each workflow step draws resources, methods, or constraints from one or more pillars, but no single pillar owns the workflow. This separation of concerns ensures that governance policies, modeling capabilities, and adaptive methods can evolve independently while remaining integrated through the operational workflow.

## 2.1.1 Pillar A: Conceptual Design and Governance

Pillar A serves as the design authority for the framework, defining the rules under which all operations proceed. This pillar establishes the objectives, success metrics, and regulatory requirements that guide surrogate development and maintenance. It determines when recalibration should be considered, what constitutes acceptable performance, and how decisions must be documented for regulatory compliance.

The contents of Pillar A include trigger policies that specify criteria indicating when recalibration should be evaluated, including thresholds on predictive uncertainty, prediction-observation residuals, and drift metrics. These policies define the conditions under which the framework transitions from routine monitoring to active evaluation of update needs. Pillar A also contains acceptance criteria—quantitative standards that define acceptable performance for operational deployment. These typically include error statistics at priority monitoring locations such as root mean square error targets, calibration of uncertainty estimates with prediction interval coverage probability near 90%, and spatial-temporal consistency with observed system behavior.

Rollback procedures form another essential component of Pillar A, providing protocols for responding when an attempted update fails to meet acceptance criteria. As defined in Section 3.1.5, rollback in this framework means withdrawal of surrogate use and escalation to full retraining, rather than reversion to a prior surrogate version—reflecting the conservative approach required for high-consequence environmental applications. Audit requirements ensure that all recalibration decisions are traceable and defensible through documentation standards that include logging trigger rationale, data sources used, evaluation results, and verification outcomes, consistent with DOE quality assurance requirements (DOE O 414.1D) and ASME NQA-1 software quality standards.

Data policies within Pillar A specify which measurements to assimilate, quality assurance and quality control standards, and data provenance requirements, ensuring that only validated data influence surrogate updates. Interpretability standards establish requirements for model explainability that support governance review and stakeholder confidence, following principles articulated in environmental modeling guidance. Success metrics provide alignment criteria that connect surrogate performance to DOE mission goals and site-specific compliance needs.

Governance does not merely constrain the framework—it defines what the other pillars do. Pillar A determines the trigger thresholds that Pillar C monitors, selects which learning strategies are appropriate for different situations, and decides whether results from Pillar B are acceptable for operational use. It is the design authority, not simply a set of guardrails.

## 2.1.2 Pillar B: Modeling Engines

Pillar B provides the computational foundation for the framework, managing the models that generate predictions and establish ground truth. This pillar contains both the high-fidelity physics-based simulator that serves as the authoritative reference and the deep-learning surrogate that enables fast operational inference.

The physics-based simulator represents the high-fidelity numerical model—such as PFLOTRAN, MODFLOW, STOMP, or TOUGH2—that serves as the truth generator for the framework. These simulators provide physically consistent predictions but require substantial computational resources, with individual runs potentially taking hours to days depending on model complexity. The physics model is used to generate targeted training data when the surrogate requires correction, ensuring that updates are grounded in first-principles physics.

The deep-learning surrogate is the fast inference model trained to emulate the physics simulator's input-output behavior. Architectures may include U-Net, U-FNO, LSTM, DeepONet, or diffusion networks, depending on the prediction task. Surrogates can generate predictions orders of magnitude faster than direct physics simulation, enabling real-time decision support. However, surrogates interpolate within their training domain and are subject to distribution drift and catastrophic forgetting when conditions evolve beyond their original training envelope.

Pillar B also maintains clear input-output contracts that define the interface between physics models and surrogates, ensuring consistent data formats, coordinate systems, and variable definitions across model types. Versioned artifacts provide model version control and management systems that track surrogate versions, training configurations, and associated metadata, enabling reproducibility and supporting rollback procedures when needed. Training data archives serve as repositories of physics simulation outputs and field observations used for surrogate training, organized with provenance metadata to support audit requirements.

The physics model remains the authoritative truth source throughout the framework's operation. The surrogate is a sophisticated emulator that provides computational efficiency, but its validity is always assessed relative to physics-based predictions and field observations. When the surrogate's domain of validity is exceeded, the physics model provides the ground truth needed for correction.

## 2.1.3 Pillar C: Recalibration Mechanisms

Pillar C supplies the adaptive intelligence for the framework, managing the techniques used for monitoring surrogate performance, detecting degradation, and orchestrating corrections. This pillar contains the methods library that the operational workflow draws upon to maintain surrogate accuracy over time.

Uncertainty quantification methods within Pillar C provide techniques for estimating predictive uncertainty, including Monte Carlo dropout, deep ensembles, Bayesian neural networks, and conformal prediction. These methods provide the diagnostic self-awareness needed to identify when surrogate predictions become unreliable. Drift detection algorithms offer statistical methods for identifying performance degradation, including residual monitoring, uncertainty inflation tracking, distributional drift tests such as the Kolmogorov-Smirnov test, and representation-level drift detection in latent spaces. These algorithms implement the trigger logic that initiates governance review.

Active learning strategies enable scenario selection methods that identify the most informative new physics simulations to run when correction is needed. Rather than random sampling, active learning targets conditions at decision boundaries, rare scenarios, or regions of high uncertainty where new data will maximally improve model performance. Continual learning methods provide techniques for updating the surrogate without full retraining, including Elastic Weight Consolidation, experience replay, and layer freezing. These methods enable incremental updates that preserve previously learned knowledge while adapting to new conditions, thereby avoiding catastrophic forgetting.

Multi-fidelity data fusion approaches combine information from multiple sources—field observations, physics model outputs at different resolutions, and surrogate predictions—to refine estimates and reduce uncertainty. Probability calibration encompasses post-hoc methods for ensuring that surrogate uncertainty estimates are well-calibrated, including temperature scaling, isotonic regression, and reliability diagram analysis. These techniques ensure that stated confidence intervals accurately reflect true prediction reliability.

Pillar C provides methods that the operational workflow uses. Pillar C does not contain or own the workflow—rather, it serves as a toolkit from which workflow steps draw appropriate techniques based on the situation. The workflow orchestrates when and how these methods are applied; Pillar C ensures the methods are available and properly maintained.

## 2.1.4 Complementary Roles of the Three Pillars

The three pillars are co-essential to the framework's operation, each playing a distinct and complementary role. Pillar A is the design authority: it defines the rules, sets the thresholds, and determines what constitutes acceptable performance. Without governance, the framework would lack the constraints needed for regulatory compliance and responsible deployment. Pillar B provides the computational foundation: it supplies the physics models that establish ground truth and the surrogates that enable fast inference. Without modeling engines, the framework would have nothing to maintain or correct. Pillar C supplies the adaptive intelligence: it provides the monitoring, detection, and correction methods that keep surrogates accurate over time. Without recalibration mechanisms, the framework would lack the ability to adapt to changing conditions.

No pillar should be viewed as more fundamental than the others—they are interdependent. Governance without models has nothing to govern; models without governance lack accountability; models without adaptation will drift; adaptation without governance may be inappropriate. The framework's value emerges from their integration.

## 2.1.5 Cross-Reference: Pillars and Workflow

The relationship between pillars and workflow steps is illustrated in Figure 2.1. Each workflow step, detailed in Section 2.2, draws from one or more pillars to accomplish its function.

```
            ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
            │   PILLAR A   │   │   PILLAR B   │   │   PILLAR C   │
            │    Rules     │   │    Models    │   │   Methods    │
            └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
                   │                  │                  │
    ═══════════════╪══════════════════╪══════════════════╪═══════════
    WORKFLOW       │                  │                  │
                   │                  │                  │
    MONITOR ───────┤                  │                  ├── UQ metrics
    DETECT ────────┤ thresholds       │                  ├── drift tests
    DECIDE ────────┤ governance       │                  │
    PREPARE ───────┤                  ├── physics        ├── active learning
    UPDATE ────────┤                  ├── surrogate      ├── continual learning
    CALIBRATE ─────┤ acceptance       │                  ├── calibration
    DEPLOY ────────┤ audit trail      ├── versioning     │
    ═══════════════╧══════════════════╧══════════════════╧═══════════
```

**Figure 2.1.** Cross-reference diagram showing how each workflow step draws resources from the three pillars. Pillar A provides governance constraints and acceptance criteria; Pillar B provides physics models and surrogates; Pillar C provides monitoring and adaptation methods.

This cross-reference structure ensures that every workflow step has clear access to the resources it needs, pillar responsibilities remain distinct and maintainable, the framework can evolve without disrupting the overall workflow, and audit trails can trace decisions back to specific pillar contents. The operational details of each workflow step, including the two-phase structure and decision logic, are presented in Section 2.2.
