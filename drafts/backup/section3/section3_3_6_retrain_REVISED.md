### 3.3.6 Full Retraining

Full retraining is reserved for circumstances in which the existing surrogate is no longer representative of the physical system or operational domain. This approach provides a clean, traceable reset that aligns with DOE's emphasis on lifecycle documentation and reproducibility.

#### Trigger Conditions

Concept drift literature emphasizes that full retraining is appropriate when foundational assumptions underlying the surrogate no longer hold (Parisi et al., 2019; Sayed et al., 2025). Specific conditions that warrant full retraining include:

- **Regime shifts or major forcing changes** that fundamentally alter system behavior beyond the original training domain
- **Redefinition of the underlying physics model**, such as revised geologic interpretations or updated reaction networks
- **Recalibration of the numerical model** after incorporation of new hydrogeologic data or conceptual model updates (Laloy et al., 2017)
- **Major reconfiguration of pumping and boundary conditions** that invalidate the original training scenarios
- **Repeated fine-tuning failures** indicating that the training domain has materially shifted

Studies in multi-fidelity and physics-informed ML reinforce that when high-fidelity simulations deviate substantially from prior domains, incremental updates cannot maintain integrity, and a new baseline surrogate is needed (Wen et al., 2021).

#### Retraining Process

The retraining process proceeds through a formal set of steps:

1. **Verify retraining triggers**, including major operational changes, substantive updates to the physics model, or repeated fine-tuning failures indicating material domain shift.

2. **Redesign the training domain**, defining updated ranges of hydrofacies, operational scenarios, and boundary forcings consistent with new conceptual understanding.

3. **Generate a new ensemble of high-fidelity simulations**, supplemented where appropriate by low-fidelity runs to maintain broad coverage and accelerate sampling.

4. **Integrate recent field observations**, anchoring the surrogate to empirical system behavior.

5. **Train a new surrogate from scratch**, including UQ calibration, validation against benchmark scenarios, and documentation of performance improvements relative to the previous baseline.

6. **Designate the new model as the operational baseline**, while archiving the prior surrogate, training data, and diagnostic artifacts to preserve full scientific and regulatory traceability.

#### Governance Requirements

Full retraining is conducted under configuration control and subject to the same verification, validation, uncertainty calibration, and acceptance criteria as an initial deployment. The retrained surrogate is promoted to operational use only after all governance requirements are satisfied.

Key governance elements include:

- **Complete documentation** of trigger rationale, data sources, and design decisions
- **Archival of prior surrogate** and all associated training artifacts
- **Independent validation** against withheld data and benchmark scenarios
- **Formal acceptance review** before operational deployment

This conservative approach reflects DOE expectations for software lifecycle management in high-consequence environmental applications, ensuring that continued use of any surrogate is not permitted once validity is in question.
