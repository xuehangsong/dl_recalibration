# 5.0 Implementation Roadmap

This section describes how the three-pillar recalibration framework translates into a computational system. Rather than prescribing specific software tools or platforms, we focus on the functional architecture—what components are needed, how they interact, and what capabilities must be developed over time. The goal is to provide a roadmap that can guide implementation while remaining flexible to site-specific constraints and evolving technology.

The implementation must satisfy two sometimes competing demands. First, it must support the scientific workflow: running physics simulations, training and evaluating surrogates, quantifying uncertainty, and executing recalibration when needed. Second, it must meet DOE governance requirements for traceability, reproducibility, and quality assurance. The design outlined here attempts to balance both.

## 5.1 Computational Components and Their Relationship to the Framework

The recalibration framework described in Section 2 organizes the scientific approach into three pillars: Governance (Pillar A), Modeling Engines (Pillar B), and Recalibration Mechanisms (Pillar C). The seven-step operational workflow (Monitor → Detect → Select → Simulate → Fine-tune → Recalibrate UQ → Redeploy) defines how these pillars interact during operations. Translating this conceptual framework into software requires five functional components that map onto the pillars and enable the workflow.

The Physics Model Interface serves Pillar B by managing communication with high-fidelity simulators such as PFLOTRAN, MODFLOW, or STOMP. This component handles input file generation, job submission including HPC scheduling where needed, output parsing, and result archiving. When the workflow reaches Step 4 (targeted physics simulations), this interface executes the runs selected by active learning. The interface must accommodate different simulators without requiring changes to downstream components—a practical necessity given that different EM sites use different modeling tools.

The Surrogate Model Engine also serves Pillar B, handling surrogate model training, storage, and inference. During initial development, it ingests physics simulation outputs and produces a trained neural network such as U-FNO or U-Net. During operations, it loads a trained model and generates the predictions that feed into Step 1 (Monitor). When recalibration is triggered, this engine executes Step 5 (Fine-tune) by updating model weights using new training data. The engine must support model versioning so that previous surrogates can be retrieved for comparison or rollback analysis, a requirement that connects to Pillar A governance.

The Monitoring and Diagnostics Module implements Pillar C's uncertainty quantification and drift detection capabilities. This is the "watchdog" of the system, continuously comparing surrogate predictions against available observations, tracking uncertainty metrics, and evaluating drift indicators. The module directly supports Steps 1 and 2 of the workflow—monitoring performance and detecting when degradation exceeds acceptable thresholds. It implements the trigger logic described in Section 3.3.2, determining when prediction quality has degraded enough to warrant action. Outputs include diagnostic summaries, alert flags, and the evidence package needed to justify recalibration decisions under Pillar A governance.

The Recalibration Orchestrator coordinates Pillar C's active learning and continual learning mechanisms. When the monitoring module signals that an update is warranted, the orchestrator manages the response by coordinating Steps 3 through 7 of the workflow. It selects new simulation scenarios through active learning (Step 3), triggers physics runs through the Physics Model Interface (Step 4), assembles training data and invokes the Surrogate Model Engine for fine-tuning (Step 5), recalibrates uncertainty estimates (Step 6), and manages redeployment of the updated model (Step 7). The orchestrator enforces Pillar A governance throughout: no surrogate update is deployed without documented justification and verification against acceptance criteria.

The Data Management Layer underlies all components and serves all three pillars. It stores observations, simulation outputs, trained models, configuration settings, and audit logs. This layer ensures that every prediction can be traced back to its inputs, every recalibration decision can be reconstructed, and every model version can be retrieved. For DOE applications, this traceability is not optional—it is required by Pillar A for regulatory confidence and long-term stewardship.

## 5.2 Operational Modes

The system operates in two distinct modes that place different demands on the architecture.

Offline mode encompasses initial surrogate development: generating training ensembles with the physics model, training the surrogate, calibrating uncertainty estimates, and validating against held-out data. This phase is computationally intensive, potentially requiring thousands of physics runs and GPU-hours of training, but is not time-critical. Offline work typically occurs on HPC resources with batch scheduling. In terms of the framework, offline mode establishes the initial Pillar B modeling engines before operational deployment.

Online mode is the operational phase where the trained surrogate supports decision-making. The surrogate generates predictions on demand, the monitoring module tracks performance through the seven-step workflow, and recalibration is triggered when needed. Online operations require faster turnaround—predictions in seconds to minutes, diagnostic updates on a regular schedule such as daily or weekly, and recalibration decisions on a governed timeline such as quarterly review. Online components may run on more modest computing resources, though recalibration itself may require temporary access to HPC for new physics runs.

The architecture must support smooth transitions between modes. A surrogate developed offline must be deployable online without modification. Data collected during online operations must feed back into offline analysis when full retraining is needed.

## 5.3 Human Decision Points

Not everything should be automated. The framework includes explicit decision points where human judgment is required, reflecting Pillar A's emphasis on governance and accountability.

Recalibration approval is the most important decision point. Even when automated diagnostics indicate drift, the decision to update a surrogate should involve human review. This is both a governance requirement and a practical safeguard against false alarms. The monitoring module provides the evidence; humans make the call.

Acceptance criteria definition requires domain expertise that cannot be automated. Humans define what "good enough" means for a given application—the error thresholds, uncertainty coverage requirements, and performance metrics that determine whether a surrogate is fit for purpose. The system evaluates against these criteria, but setting them requires understanding of site-specific risks and regulatory context.

Rollback decisions arise when an updated surrogate fails validation. As defined in Section 3.1.5, rollback means withdrawing the surrogate from operational use and reverting to physics-only analysis. This is a significant operational change that requires human authorization and documentation.

Full retraining triggers represent the most consequential decision. When incremental updates repeatedly fail or when site conditions change fundamentally, the decision to abandon the current surrogate and retrain from scratch involves judgment about whether the surrogate's foundational assumptions remain valid. This decision has major resource implications and should not be automated.

The software architecture should make these decision points visible and provide the information needed to make them well.

## 5.4 Development Phases

Implementing the full framework is a multi-year effort. We propose a phased approach that delivers value incrementally while building toward the complete vision.

### Phase 1: Prototype Demonstration

The immediate goal is to demonstrate that the recalibration concept works. This means developing a single surrogate architecture—U-FNO for the 2D cross-section case, U-Net for pump-and-treat—trained on synthetic PFLOTRAN outputs. The recalibration workflow will be executed manually: a researcher runs diagnostics, decides an update is needed, generates new training data, fine-tunes the model, and validates results. The work will be documented in Jupyter notebooks or Python scripts that capture each step. The key deliverable is a small demonstration showing before-and-after performance when the surrogate is updated in response to simulated drift.

At this phase, there is no persistent software system—just reproducible code that proves the concept. The deliverable is a working example, not a deployable tool.

### Phase 2: Integrated Framework

Building on the prototype, the next phase creates reusable software components. This includes modular Python packages for each core component, with documented interfaces and test coverage. These packages can be installed and used independently or together. The phase also delivers automated drift detection that runs on a schedule and generates diagnostic reports without manual intervention, along with a scripted recalibration workflow that executes the necessary steps with minimal manual effort once a decision to update has been made. Configuration management capabilities will track model versions, training data provenance, and parameter settings.

At this phase, the system still requires a technically skilled operator who is comfortable with Python and command-line tools, but routine operations are largely automated. The operator's role shifts from executing steps to reviewing outputs and making decisions.

### Phase 3: Operational System

The full vision is a system that can be deployed at an EM site and operated by staff who are not ML specialists. This includes a persistent monitoring service that runs continuously, ingests new observations as they arrive, and maintains an up-to-date picture of surrogate performance. A user interface, likely web-based, would present diagnostics, alerts, and decision options in an accessible format so that analysts can review model status, examine historical performance, and initiate recalibration workflows without writing code. The system would support multiple surrogates for different prediction tasks with coordinated monitoring and updating, and would integrate with site data systems so that observations flow automatically from field sensors and laboratory results into the monitoring pipeline.

This phase requires significant software engineering effort and should be informed by experience from earlier phases. Specific technology choices should be deferred until requirements are better understood through operational experience.

## 5.5 Technical Considerations

### Computational Requirements

The framework spans a wide range of computational demands. Physics simulations are the most expensive component. A single PFLOTRAN run for the 2D cross-section case takes minutes; a full 3D site model may take hours. Generating training ensembles of hundreds to thousands of runs requires HPC access with batch scheduling. Recalibration updates need fewer runs, typically tens selected by active learning, but still benefit from parallel execution.

Surrogate training requires GPU resources. Initial training of a U-FNO or U-Net model may take hours on a modern GPU. Fine-tuning for recalibration is faster, typically minutes to an hour, but still benefits from GPU acceleration. Training can occur on HPC GPU nodes, cloud resources, or dedicated workstations depending on availability.

Inference and monitoring are lightweight. A trained surrogate generates predictions in milliseconds. Diagnostic calculations including residuals, uncertainty metrics, and drift statistics are similarly fast. These operations can run on standard computing resources.

The architecture should not assume that all components run on the same hardware. Physics simulations may run on one HPC system, training on another, and monitoring on a third. Data must flow between these environments reliably.

### Interoperability

Simulator coupling is a practical challenge. Physics simulators were not designed with ML workflows in mind. The framework must work with simulators as they are, typically through file-based interfaces: generate input files, run the simulator, parse output files. This is less elegant than API-based coupling but far more practical given the diversity of simulators in use across EM sites.

Data formats should follow existing conventions where possible. Simulation outputs are often in domain-specific formats such as PFLOTRAN HDF5 or MODFLOW binary. The framework should read these directly rather than requiring format conversion. For internal data including trained models, diagnostic logs, and configuration files, standard formats provide adequate interoperability.

Reproducibility requires that every result can be regenerated from archived inputs. This means versioning not just code but also training data, model weights, configuration files, and random seeds. The data management layer must support this without imposing excessive overhead on routine operations.

### Quality Assurance Alignment

DOE quality assurance requirements including DOE O 414.1D and NQA-1 apply to software used in decision support. Configuration control requires that every deployed component have a defined version, that changes be documented and reviewed, and that the system be able to report exactly what software versions produced a given result. Verification and validation require that each component be tested against defined acceptance criteria before deployment, with test results documented and retained. Traceability requires that audit logs record what data was used, what computations were performed, and what results were produced, with these logs retained for the project lifetime. Corrective action procedures must define how problems are diagnosed, how fixes are implemented, and how fix effectiveness is verified.

These requirements do not dictate specific technologies but do constrain how the software is developed and operated. The architecture should make compliance straightforward rather than burdensome.

## 5.6 Open Design Questions

Several technical decisions remain to be resolved through prototype development and stakeholder input.

Surrogate architecture selection is an open question. The prototype explores both U-FNO and U-Net approaches. Which performs better for EM-relevant problems? Should different architectures be used for different prediction tasks? How do architecture choices affect recalibration efficiency?

Uncertainty quantification method selection requires evaluation. Section 3.3.1 describes several UQ approaches including MC dropout, deep ensembles, and conformal prediction. Which provides the best trade-off between computational cost and calibration quality for this application?

Trigger threshold calibration needs empirical grounding. The drift detection framework in Section 3.3.2 defines metrics but not specific thresholds. How should thresholds be set for a given site? How sensitive are outcomes to threshold choices?

Update frequency and scope involve trade-offs that are not yet understood. How often should recalibration occur? Should updates be small and frequent or larger and less frequent? What determines whether incremental fine-tuning is sufficient versus full retraining?

Deployment environment decisions affect technology choices and security considerations. Where will the operational system run? On-site servers? PNNL infrastructure? Cloud resources? These questions are best answered through experience with the prototype and early operational deployments rather than through upfront design decisions.
