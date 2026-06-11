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

## Summary

The governance framework ensures that deep-learning surrogate models are integrated into DOE Environmental Management groundwater remediation workflows in a controlled, transparent, and regulator-aligned manner. Key principles include:

- Governance grounded in established EPA and DOE quality assurance standards (CERCLA, DOE O 414.1D, DOE EM-QA-001, NQA-1, EPA QA/G-5M, EPA/100/K-09/003)
- Surrogate use limited to screening- and planning-level decision support
- Primacy of high-fidelity physics-based numerical models for final regulatory and remedy decisions
- Objective acceptance criteria and documented recalibration triggers
- Formal configuration control with full auditability
- Explicit withdrawal and retraining procedures when surrogate validity is in question

Collectively, this governance foundation enables efficient use of advanced modeling tools to support long-term remediation planning while maintaining scientific rigor, operational stability, and regulatory confidence.
