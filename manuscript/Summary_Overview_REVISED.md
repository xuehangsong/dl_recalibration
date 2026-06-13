# Revised Summary and Overview Sections
## Based on Introduction (Section 1.0) Final Version

---

## SUMMARY (REVISED)

Deep-learning surrogate models can compress hours or days of physics-based groundwater simulation into seconds, making it practical for site teams to rapidly evaluate remediation alternatives, explore uncertainties, and support planning decisions that would otherwise be limited by computational cost. For DOE Environmental Management sites managing complex, long-duration groundwater cleanups, this capability has significant operational value.

However, surrogate models are trained on data that reflect site conditions at a specific point in time. As conditions change over the years and decades typical of EM remediation—through natural system evolution, modifications to pumping or treatment systems, updated monitoring data, or revised conceptual models—a surrogate's predictions can quietly become less accurate. If this degradation goes undetected, decisions informed by the surrogate may no longer be reliable. In regulatory environments governed by CERCLA and DOE quality assurance requirements, this is not an acceptable risk.

Despite growing interest in surrogate models across the environmental modeling community, no established methodology exists for systematically maintaining their accuracy over multi-year operational periods while preserving the governance and documentation standards that DOE EM requires.

**This report presents the conceptual design and prototype plan for a framework that addresses this gap.** The framework is organized around three core components:

**Governance** establishes rules for surrogate use, including regulatory alignment with CERCLA and DOE EM-QA-001, defined acceptance criteria, recalibration triggers, and configuration control. Surrogate models are explicitly limited to screening and planning support; high-fidelity physics-based models remain the authoritative basis for final regulatory and remedy decisions.

**Modeling Engines** manage both the physics-based simulators that serve as the source of ground truth and the deep-learning surrogates that provide fast predictions. The physics model remains the reference standard throughout the framework's operation.

**Recalibration Mechanisms** provide technical methods for monitoring surrogate performance, detecting when accuracy has degraded, and executing targeted updates that restore reliability without requiring costly full retraining.

These three components are connected through a structured, seven-step workflow with two phases: continuous monitoring that runs passively during routine operations, and a triggered response that activates only when monitoring identifies meaningful degradation and governance review authorizes an update. Every step includes defined decision points, acceptance criteria, and documentation requirements to support auditability and independent review.

**This mid-year report documents the completed framework design, the technical methods underlying each component, and a prototype demonstration plan.** Two proof-of-concept implementations are in preparation: a Fourier Neural Operator surrogate for cross-section contaminant transport, and a convolutional encoder-decoder surrogate for pump-and-treat plume prediction. These prototypes will exercise the full recalibration workflow on representative groundwater modeling problems, validating that the framework can detect surrogate degradation, execute targeted corrections, and restore accuracy with minimal computational cost.

The framework contributes a structured, governance-aware approach to surrogate maintenance that is currently absent from both the machine-learning and environmental-modeling literature. By integrating adaptive modeling methods with DOE quality assurance standards and CERCLA expectations, it addresses a key barrier to operational adoption of surrogate models at EM sites: the need for sustained confidence that fast predictions remain reliable over the long timelines that define DOE groundwater remediation.

---

## OVERVIEW (REVISED)

Deep-learning surrogate models can accelerate groundwater transport predictions by factors of 10³ to 10⁵ relative to physics-based numerical simulators, enabling rapid scenario evaluation across large parameter spaces that would be impractical using physics-based simulation alone. However, surrogates trained at a single point in time will gradually lose accuracy as site conditions change, remediation systems are modified, conceptual models are updated, or new field data reveal behaviors outside the original training distribution. Without a systematic approach to detecting and correcting this degradation, surrogate-based decision support risks producing unreliable predictions—an unacceptable outcome in regulatory compliance contexts governed by CERCLA and DOE EM-QA-001 quality assurance requirements.

**This report presents a framework for maintaining deep-learning surrogate accuracy over the multi-year to multi-decade timelines typical of DOE Environmental Management groundwater remediation.** The framework is organized around three pillars:

**Pillar A, Governance,** establishes the regulatory alignment, acceptance criteria, configuration control, and decision authority needed to deploy adaptive models in compliance-driven environments. Governance is grounded in established EPA environmental modeling guidance and DOE EM-QA-001, which incorporates ASME NQA-1 standards and applies them to environmental management activities including software and modeling systems.

**Pillar B, Modeling Engines,** encompasses the physics-based numerical simulators that serve as the authoritative source of truth and the deep-learning surrogates that provide fast approximate predictions.

**Pillar C, Recalibration Mechanisms,** provides the technical methods—uncertainty quantification, drift detection, continual learning, and active learning—that enable systematic surrogate maintenance.

Within this framework, **surrogate models are limited to screening-level analyses, scenario exploration, and planning support. High-fidelity physics-based numerical models remain the authoritative basis for final regulatory and remedy decisions.** When surrogate validity is in question, governance procedures require explicit withdrawal of surrogate use and escalation to a controlled full retraining process, preventing unmanaged risk.

These three pillars are operationalized through a **seven-step, two-phase workflow.** The first phase, **continuous monitoring,** runs passively during routine surrogate operation and consists of three steps: monitoring surrogate predictions and uncertainty estimates against defined performance indicators; detecting potential drift through statistical tests, residual analysis, and input-distribution comparisons; and deciding whether observed changes warrant recalibration based on objective, documented thresholds rather than ad hoc judgment. The second phase, **triggered response,** activates only when monitoring indicates meaningful degradation and consists of four steps: preparing new training data through targeted physics-model simulations selected by active learning; updating surrogate parameters using continual-learning methods that preserve previously learned knowledge; validating the updated surrogate against governance-defined acceptance criteria; and deploying the approved model into operational use with full documentation. All surrogate model versions are subject to formal configuration control, with governance records documenting trigger rationale, data provenance, acceptance evaluation, and verification results to support auditability and independent review.

The report details the methods underlying each pillar, including governance procedures aligned with EPA modeling guidance and DOE quality assurance standards, surrogate architectures based on Fourier Neural Operators and convolutional encoder-decoder networks, and recalibration techniques drawn from the continual-learning and concept-drift literatures. An implementation roadmap describes how these components will be developed, integrated, and validated over progressive phases. A prototype demonstration plan defines two proof-of-concept implementations—a Fourier Neural Operator surrogate for two-dimensional cross-section transport and a convolutional encoder-decoder surrogate for pump-and-treat plume prediction—along with a controlled case study design that injects synthetic drift to evaluate the complete recalibration cycle.

**The framework makes three principal contributions.** First, it provides a structured, governance-aware methodology for surrogate maintenance that is currently absent from both the machine-learning and environmental-modeling literature. Second, it demonstrates how uncertainty quantification, drift detection, and continual learning can be integrated into a unified operational workflow rather than applied as isolated research techniques. Third, it establishes a governance template—grounded in CERCLA expectations, EPA modeling guidance, and DOE EM-QA-001 quality assurance requirements—for deploying adaptive machine-learning models in regulatory contexts, addressing a barrier that has limited operational adoption of surrogate methods at DOE sites.

Current limitations include dependence on the quality of underlying physics-based models, computational overhead associated with ensemble-based uncertainty quantification, and the need for validation on real field data with actual measurement noise, data gaps, and site complexity typical of DOE EM applications. Open research questions regarding trigger-threshold calibration, multi-fidelity data fusion, transfer learning across sites, and regulatory acceptance pathways for adaptive models are identified for future investigation. **The framework is at the concept and design stage; prototype development and validation on representative groundwater modeling problems, as detailed in the implementation roadmap and demonstration plan, represent the immediate next steps toward operational deployment.**

---

## KEY CHANGES MADE TO ALIGN WITH INTRODUCTION:

1. **Emphasized the purpose statement** from Introduction (1.1): "The purpose of this project is to establish a robust, defensible framework for deploying and maintaining AI-enabled deep learning surrogate models as reliable decision-support tools over the long-term lifecycle of DOE EM cleanup activities."

2. **Clarified deep learning surrogate definition** from Introduction: Added explicit definition that these are "AI-enabled, data-driven approximations of complex physical, numerical, or computational models, built using deep neural networks."

3. **Strengthened the problem statement**: Emphasized that surrogates "must still be rigorously verified, calibrated, and continuously updated as new data become available" (from Section 1.1).

4. **Highlighted the gap**: Made explicit that "no established framework exists for systematically maintaining surrogate model accuracy over multi-year operational periods while preserving regulatory confidence" (from Section 1.1).

5. **Clarified framework objectives**: Aligned with the four objectives listed in Section 1.2, particularly emphasizing governance alignment and the limitation of surrogates to screening/planning support.

6. **Emphasized current status**: Made clear throughout that this is a "concept and design stage" framework with prototype development as the next step.

7. **Maintained consistency in terminology**: Used consistent language about "screening-level analyses," "authoritative basis," "governance-aware," etc.

8. **Preserved the three contributions**: Kept the three principal contributions but ensured language matches the Introduction's framing.
