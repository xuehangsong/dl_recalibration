# 4. Implementation Roadmap

This section describes how the three-pillar framework (Section 2.1) and seven-step workflow (Section 2.2) translate into an operational system. Rather than prescribing specific software tools or platforms, we focus on what capabilities are needed and how they should be developed over time. The goal is to provide a roadmap that can guide implementation while remaining flexible to site-specific constraints and evolving technology.

The implementation must satisfy two sometimes competing demands. First, it must support the scientific workflow of monitoring, detecting drift, and executing recalibration when needed. Second, it must meet DOE governance requirements for traceability, reproducibility, and quality assurance. The design outlined here attempts to balance both demands while maintaining consistency with the framework architecture established in Section 2.

## 4.1 System Requirements

### 4.1.1 Operational Modes

The system operates in two distinct modes that place different demands on the architecture and reflect different phases of the surrogate lifecycle.

Offline mode encompasses initial surrogate development: generating training ensembles with the physics model, training the surrogate, calibrating uncertainty estimates, and validating against held-out data. This phase is computationally intensive, potentially requiring thousands of physics runs and GPU-hours of training, but is not time-critical. Offline work typically occurs on HPC resources with batch scheduling. In terms of the framework, offline mode establishes the initial Pillar B modeling engines before operational deployment. The methods described in Section 3.2 (physics-based models and surrogate architectures) and Section 3.3.1 (uncertainty quantification) are applied during this phase to produce a validated surrogate ready for deployment.

Online mode is the operational phase where the trained surrogate supports decision-making. The surrogate generates predictions on demand, the monitoring system tracks performance through the seven-step workflow, and recalibration is triggered when needed. Online operations require faster turnaround—predictions in seconds to minutes, diagnostic updates on a regular schedule such as daily or weekly, and recalibration decisions on a governed timeline such as quarterly review. Online components may run on more modest computing resources, though recalibration itself may require temporary access to HPC for new physics runs. The methods from Section 3.3.2 (trigger logic) and Section 3.1 (governance) are continuously active during online operations.

The architecture must support smooth transitions between modes. A surrogate developed offline must be deployable online without modification. Data collected during online operations must feed back into offline analysis when full retraining is needed. This bidirectional flow ensures that operational experience improves subsequent surrogate generations.

### 4.1.2 Pillar-Based Capabilities

Each pillar of the framework requires specific capabilities for implementation. Understanding these requirements helps ensure that the system architecture supports all aspects of the recalibration framework.

Pillar A (Governance) requires infrastructure for configuration management that tracks all surrogate versions with their training data, assumptions, and validation results. The system must maintain audit logging for all decisions, particularly at the DECIDE step where human judgment authorizes recalibration. Documentation generation capabilities must produce regulatory-compliant records that satisfy DOE quality assurance requirements. Human review interfaces must present diagnostic evidence clearly so that decision-makers can evaluate whether recalibration is warranted. The governance methods detailed in Section 3.1—including regulatory framework alignment, acceptance criteria, monitoring schedules, and configuration control—define what this infrastructure must support.

Pillar B (Modeling Engines) requires a physics model interface capable of communicating with high-fidelity simulators such as PFLOTRAN, MODFLOW, STOMP, or TOUGH2. This interface handles input file generation, job submission including HPC scheduling where needed, output parsing, and result archiving. The system must also provide surrogate training and inference infrastructure that can train neural network architectures (such as those described in Section 3.2.3), store trained models with version control, and generate predictions efficiently during operations. Data management capabilities must handle both simulation outputs and field observations, maintaining provenance for all data used in training or validation.

Pillar C (Recalibration Mechanisms) requires infrastructure for uncertainty quantification computation using the methods described in Section 3.3.1, including MC-Dropout, deep ensembles, or conformal prediction. Drift detection and monitoring capabilities must implement the trigger logic from Section 3.3.2, tracking performance metrics and evaluating drift indicators against governance-defined thresholds. When recalibration is triggered, the system must support active learning for scenario selection (Section 3.3.4) and continual learning for model updates (Section 3.3.3). Multi-fidelity data fusion (Section 3.3.5) and full retraining (Section 3.3.6) capabilities complete the recalibration toolkit.

### 4.1.3 Workflow Support

The implementation must support both phases of the seven-step workflow defined in Section 2.2.

Phase 1 (Continuous Monitoring) implements Steps 1 through 3 of the workflow. The MONITOR step requires automated comparison of surrogate predictions against field observations, computing residuals and tracking uncertainty metrics over time. The DETECT step evaluates drift indicators against predefined thresholds, distinguishing transient anomalies from persistent degradation using the persistence filtering described in Section 3.3.2. The DECIDE step packages diagnostic evidence for governance review and records the authorization decision. Throughout Phase 1, the system maintains the trigger state logic—OK, WARNING, UPDATE, or ESCALATE—that guides operational decisions.

Phase 2 (Triggered Response) activates only when the DECIDE step authorizes an update, implementing Steps 4 through 7. The PREPARE step assembles training data, potentially using active learning to select high-value scenarios for new physics simulations. The UPDATE step fine-tunes surrogate weights using continual learning techniques that preserve previously learned knowledge. The CALIBRATE step ensures that uncertainty estimates remain well-calibrated after the update. The DEPLOY step validates the updated surrogate against acceptance criteria and, if successful, deploys it with full documentation. If validation fails, the system supports rollback procedures as defined in Section 3.1.5.

The methods detailed in Section 3 provide the technical foundation for all workflow steps. Rather than re-explaining these methods here, the implementation draws on them as needed: Section 3.3.1 for uncertainty quantification, Section 3.3.2 for trigger logic, Section 3.3.3 for continual learning, Section 3.3.4 for active learning, Section 3.3.5 for multi-fidelity fusion, and Section 3.3.6 for full retraining when incremental updates are insufficient.

## 4.2 Human Decision Points

Not everything should be automated. The framework includes explicit decision points where human judgment is required, reflecting Pillar A's emphasis on governance and accountability. The software architecture should make these decision points visible and provide the information needed to make them well.

### 4.2.1 Recalibration Approval

The most important decision point occurs at Step 3 (DECIDE) of the workflow. Even when automated diagnostics indicate drift, the decision to update a surrogate should involve human review. This is both a governance requirement under DOE quality assurance standards and a practical safeguard against false alarms. The monitoring system provides the evidence—drift metrics, historical trends, uncertainty inflation, and comparison to acceptance criteria—but humans make the call on whether to proceed with recalibration.

The decision options at this point include approving the update and proceeding to Phase 2, deferring pending additional evidence while continuing intensified monitoring, or rejecting with documented justification if the evidence is insufficient or the timing is inappropriate. Each decision must be recorded with rationale for regulatory transparency.

### 4.2.2 Acceptance Criteria Definition

Acceptance criteria define what "good enough" means for a given application—the error thresholds, uncertainty coverage requirements, and performance metrics that determine whether a surrogate is fit for purpose. Setting these criteria requires domain expertise that cannot be automated. Humans must understand site-specific risks, regulatory context, and the consequences of prediction errors to define appropriate thresholds.

The system evaluates surrogate performance against these criteria, but the criteria themselves emerge from human judgment informed by site characterization, regulatory requirements, and operational experience. Section 3.1.3 describes the types of acceptance criteria (accuracy metrics, uncertainty coverage, spatial and temporal consistency) but the specific threshold values must be determined by qualified personnel for each application.

### 4.2.3 Rollback Decisions

When an updated surrogate fails validation at Step 7 (DEPLOY), a rollback decision is required. As defined in Section 3.1.5, rollback means withdrawing the surrogate from operational use and reverting to physics-only analysis—not reverting to a previous surrogate version, since that version has already been flagged as degraded. This is a significant operational change that requires human authorization and documentation.

The decision to rollback acknowledges that the recalibration attempt was unsuccessful and that the surrogate cannot currently meet acceptance criteria. This triggers the ESCALATE state, which may lead to full retraining or, in some cases, a fundamental reassessment of whether a surrogate approach is appropriate for the application.

### 4.2.4 Full Retraining Triggers

The most consequential decision point arises when incremental updates repeatedly fail or when site conditions change fundamentally. The decision to abandon the current surrogate and retrain from scratch involves judgment about whether the surrogate's foundational assumptions remain valid. Perhaps the training distribution no longer represents current site conditions, or perhaps the surrogate architecture is inadequate for the prediction task.

Full retraining has major resource implications—potentially thousands of new physics simulations and significant computational effort—and should not be automated. Section 3.3.6 describes the technical process for full retraining, but the decision to initiate it requires human assessment of whether the investment is justified and whether the underlying approach remains sound.

## 4.3 Development Phases

Implementing the full framework is a multi-year effort. A phased approach delivers value incrementally while building toward the complete vision. Each phase builds on the previous one, with lessons learned informing subsequent development.

### 4.3.1 Phase 1: Prototype Demonstration

The immediate objective is to demonstrate that the recalibration concept works by completing one full cycle on a synthetic or simplified test case.

The scope of Phase 1 includes developing a single surrogate architecture—such as U-FNO for 2D cross-section transport or U-Net for pump-and-treat plume prediction—trained on synthetic physics model outputs. Basic uncertainty quantification using MC-Dropout or deep ensembles provides predictive uncertainty estimates. Simple threshold-based drift detection identifies when performance has degraded. The recalibration workflow is executed manually: a researcher runs diagnostics, decides an update is needed, generates new training data through targeted physics simulations, fine-tunes the model using continual learning techniques, recalibrates uncertainty estimates, and validates results against acceptance criteria. The work is documented in Jupyter notebooks or Python scripts that capture each step.

The key deliverable is a working demonstration showing before-and-after performance when the surrogate is updated in response to simulated drift. This demonstration proves that the seven-step workflow can improve surrogate performance and that the methods from Section 3 work together as intended.

Success is measured by completing the full MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY cycle with documented performance improvement. At this phase, there is no persistent software system—just reproducible code that proves the concept.

### 4.3.2 Phase 2: Integrated Framework

Building on the prototype, the objective of Phase 2 is to create reusable software components that can operate on realistic site data with governance-compliant documentation.

The scope expands to include modular Python packages for each core capability, with documented interfaces and test coverage. These packages can be installed and used independently or together. Automated drift detection runs on a schedule and generates diagnostic reports without manual intervention. A scripted recalibration workflow executes the necessary steps with minimal manual effort once a decision to update has been made. Configuration management tracks model versions, training data provenance, and parameter settings. Multiple surrogate architecture options are supported, allowing comparison of different approaches for a given prediction task.

Deliverables include installable packages that implement the framework components, automated diagnostic reports that summarize surrogate performance and drift indicators, and a governance dashboard prototype that presents decision-relevant information for human review. The system produces documentation that meets DOE quality assurance requirements for traceability and reproducibility.

Success is measured by the framework operating on representative site data—either from an actual EM site or from realistic synthetic scenarios—with all governance requirements satisfied. At this phase, the system still requires a technically skilled operator comfortable with Python and command-line tools, but routine operations are largely automated. The operator's role shifts from executing steps to reviewing outputs and making decisions.

### 4.3.3 Phase 3: Operational System

The full vision is a system that can be deployed at an EM site and operated by staff who are not ML specialists. The objective is acceptance for operational use under DOE quality assurance requirements.

The scope includes a persistent monitoring service that runs continuously, ingests new observations as they arrive, and maintains an up-to-date picture of surrogate performance. A user interface—likely web-based—presents diagnostics, alerts, and decision options in an accessible format so that analysts can review model status, examine historical performance, and initiate recalibration workflows without writing code. The system supports multiple surrogates for different prediction tasks with coordinated monitoring and updating. Integration with site data systems allows observations to flow automatically from field sensors and laboratory results into the monitoring pipeline.

Deliverables include a production-quality implementation meeting all DOE software quality requirements, training materials for site operators, and maintenance and support procedures. Full regulatory documentation demonstrates compliance with DOE O 414.1D and NQA-1 requirements.

Success is measured by the framework being accepted for operational use at one or more DOE EM sites, with site staff able to operate the system for routine monitoring and governance personnel able to make informed recalibration decisions based on system outputs. This phase requires significant software engineering effort and should be informed by experience from earlier phases. Specific technology choices should be deferred until requirements are better understood through operational experience.

## 4.4 Technical Considerations

### 4.4.1 Computational Requirements

The framework spans a wide range of computational demands that must be accommodated by the implementation architecture.

Physics simulations are the most expensive component. A single PFLOTRAN run for a 2D cross-section case takes minutes; a full 3D site model may take hours. Generating training ensembles of hundreds to thousands of runs requires HPC access with batch scheduling. Recalibration updates need fewer runs—typically tens selected by active learning—but still benefit from parallel execution.

Surrogate training requires GPU resources for efficient execution. Initial training of a U-FNO or U-Net model may take hours on a modern GPU. Fine-tuning for recalibration is faster, typically minutes to an hour, but still benefits from GPU acceleration. Training can occur on HPC GPU nodes, cloud resources, or dedicated workstations depending on availability.

Inference and monitoring are lightweight by comparison. A trained surrogate generates predictions in milliseconds. Diagnostic calculations—residuals, uncertainty metrics, drift statistics—are similarly fast. These operations can run on standard computing resources without specialized hardware.

The architecture should not assume that all components run on the same hardware. Physics simulations may run on one HPC system, training on another, and monitoring on a third. Data must flow between these environments reliably, with appropriate handling of different file systems, network configurations, and security boundaries.

### 4.4.2 Interoperability

Simulator coupling presents a practical challenge because physics simulators were not designed with ML workflows in mind. The framework must work with simulators as they are, typically through file-based interfaces: generate input files according to simulator specifications, run the simulator as a subprocess or batch job, and parse output files to extract results. This approach is less elegant than API-based coupling but far more practical given the diversity of simulators in use across EM sites. The Physics Model Interface component must accommodate different simulators—PFLOTRAN, MODFLOW, STOMP, TOUGH2, and others—without requiring changes to downstream components.

Data formats should follow existing conventions where possible. Simulation outputs are often in domain-specific formats such as PFLOTRAN HDF5 or MODFLOW binary files. The framework should read these directly rather than requiring format conversion that could introduce errors or lose information. For internal data—trained models, diagnostic logs, configuration files—standard formats such as JSON, YAML, and PyTorch checkpoints provide adequate interoperability.

Reproducibility requires that every result can be regenerated from archived inputs. This means versioning not just code but also training data, model weights, configuration files, and random seeds. The data management layer must support this requirement without imposing excessive overhead on routine operations. Every prediction should be traceable to the specific surrogate version, training data, and configuration that produced it.

### 4.4.3 Quality Assurance Alignment

DOE quality assurance requirements—including DOE O 414.1D and NQA-1—apply to software used in decision support for environmental management. These requirements do not dictate specific technologies but do constrain how the software is developed and operated. The architecture should make compliance straightforward rather than burdensome.

Configuration control requires that every deployed component have a defined version, that changes be documented and reviewed before deployment, and that the system be able to report exactly what software versions produced a given result. This applies to surrogate models, monitoring algorithms, and the framework software itself.

Verification and validation require that each component be tested against defined acceptance criteria before deployment, with test results documented and retained. For surrogate models, this means validation against held-out data and comparison to physics model predictions. For software components, this means unit tests, integration tests, and documented test coverage.

Traceability requires that audit logs record what data was used, what computations were performed, and what results were produced. These logs must be retained for the project lifetime—potentially decades for long-term remediation sites. The data management layer must support efficient storage and retrieval of audit information.

Corrective action procedures must define how problems are diagnosed, how fixes are implemented, and how fix effectiveness is verified. When a surrogate fails validation or produces unexpected results, the system must support root cause analysis and documented resolution.

## 4.5 Summary

This implementation roadmap translates the three-pillar framework and seven-step workflow into operational capabilities through a structured development approach.

The system requirements are organized around what each pillar needs for implementation, with clear distinction between offline development and online operations. Pillar A requires governance infrastructure for configuration management, audit logging, and human review interfaces. Pillar B requires physics model interfaces and surrogate training infrastructure. Pillar C requires monitoring, drift detection, and recalibration capabilities. The workflow support ensures that both continuous monitoring (Steps 1-3) and triggered response (Steps 4-7) phases can be executed with appropriate automation and human oversight.

Four explicit human decision points preserve governance accountability: recalibration approval at the DECIDE step, acceptance criteria definition, rollback decisions when validation fails, and full retraining triggers when incremental updates are insufficient. These decision points ensure that human judgment remains central to surrogate management despite automation of routine operations.

The phased development approach—from prototype demonstration through integrated framework to operational system—provides progressive capability building with lessons learned informing each subsequent phase. This approach manages risk while delivering value incrementally.

Technical considerations address computational requirements spanning HPC physics simulations to lightweight inference, interoperability with existing simulators and data systems, and alignment with DOE quality assurance requirements. The architecture accommodates site-specific constraints while maintaining consistent workflow and governance structure.

The framework enables adaptive surrogate management that maintains prediction accuracy over multi-year remediation timelines while meeting DOE quality assurance and regulatory requirements. By combining automated monitoring with human decision points, the implementation balances operational efficiency with the accountability required for environmental management applications.
