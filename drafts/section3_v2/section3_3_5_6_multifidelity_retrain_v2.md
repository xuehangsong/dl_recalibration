## 3.3.5 Multi-fidelity Data Fusion

Multi-fidelity modeling enhances surrogate accuracy and computational efficiency by combining inexpensive low-fidelity simulations with high-fidelity simulations and field observations. This approach enables broad coverage of the parameter space while anchoring predictions to high-accuracy data where available.

### Fusion Strategies

Two mature strategies dominate the multi-fidelity literature. Autoregressive Gaussian-process and co-Kriging models treat high-fidelity outputs as corrected versions of low-fidelity predictions (Kennedy & O'Hagan, 2000; Le Gratiet, 2013), providing principled uncertainty propagation well-suited for problems with moderate dimensionality. Neural discrepancy models learn nonlinear mappings between fidelity levels (Perdikaris et al., 2017), capturing complex relationships that linear correction models cannot represent and enabling more flexible fidelity fusion.

Recent advances include physics-aware multi-fidelity networks that embed physical constraints directly into the learning architecture (Wen et al., 2021) and transfer learning approaches in which surrogates are pre-trained on large low-fidelity ensembles and fine-tuned using a smaller high-fidelity subset (Tang et al., 2022).

### Fidelity Levels

In groundwater flow and reactive transport applications, low-fidelity sources such as coarse-grid PFLOTRAN or MODFLOW simulations provide broad characterization of system variability across the parameter and operational space, while high-fidelity sources including fine-grid simulations or field observations anchor localized accuracy where precise predictions are required. This combination achieves strong performance with orders-of-magnitude reduction in simulation cost compared to using high-fidelity data alone (Asher et al., 2015).

### Fusion Process

The multi-fidelity fusion procedure integrates coarse simulations, fine simulations, and field data through a structured workflow. The process begins by identifying fidelity levels and aligning datasets to ensure spatial, temporal, and unit consistency across low-fidelity, high-fidelity, and observational sources. Surrogate models are then pre-trained on low-fidelity simulations, exploiting their broad coverage of the parameter and operational space.

High-fidelity data—whether from simulation or observation—is subsequently introduced to train a discrepancy model or co-Kriging structure, allowing predictions to inherit low-fidelity global structure while achieving high-fidelity local accuracy (Kennedy & O'Hagan, 2000; Perdikaris et al., 2017). The framework quantifies fidelity-conditioned uncertainty by expanding intervals where only low-fidelity information is available and narrowing them where high-fidelity evidence supports confidence, consistent with UQ strategies described by Wen et al. (2021).

Fused predictions are validated against withheld high-fidelity runs or independent observational periods to confirm improved performance over single-fidelity surrogates. Finally, the fused surrogate is integrated into the continual learning loop, enabling more accurate drift detection, better-informed active learning selection, and more stable fine-tuning updates.

### Integration with Recalibration Framework

Multi-fidelity methods integrate naturally with active learning and continual learning, enabling scalable refinement even under evolving operational regimes. When active learning identifies high-uncertainty regions, the framework can strategically deploy either LF or HF simulations based on the expected information gain and computational budget. The fused surrogate provides improved baseline predictions that enhance drift detection sensitivity and reduce false-positive recalibration triggers.

## 3.3.6 Full Retraining

Full retraining is reserved for circumstances in which the existing surrogate is no longer representative of the physical system or operational domain. This approach provides a clean, traceable reset that aligns with DOE's emphasis on lifecycle documentation and reproducibility.

### Trigger Conditions

Concept drift literature emphasizes that full retraining is appropriate when foundational assumptions underlying the surrogate no longer hold (Parisi et al., 2019; Sayed et al., 2025). Specific conditions that warrant full retraining include regime shifts or major forcing changes that fundamentally alter system behavior beyond the original training domain, redefinition of the underlying physics model such as revised geologic interpretations or updated reaction networks, recalibration of the numerical model after incorporation of new hydrogeologic data or conceptual model updates (Laloy et al., 2017), major reconfiguration of pumping and boundary conditions that invalidate the original training scenarios, and repeated fine-tuning failures indicating that the training domain has materially shifted.

Studies in multi-fidelity and physics-informed ML reinforce that when high-fidelity simulations deviate substantially from prior domains, incremental updates cannot maintain integrity, and a new baseline surrogate is needed (Wen et al., 2021).

### Retraining Process

The retraining process proceeds through a formal sequence of steps. First, retraining triggers are verified, including major operational changes, substantive updates to the physics model, or repeated fine-tuning failures indicating material domain shift. The training domain is then redesigned, defining updated ranges of hydrofacies, operational scenarios, and boundary forcings consistent with new conceptual understanding.

A new ensemble of high-fidelity simulations is generated, supplemented where appropriate by low-fidelity runs to maintain broad coverage and accelerate sampling. Recent field observations are integrated to anchor the surrogate to empirical system behavior. A new surrogate is trained from scratch, including UQ calibration, validation against benchmark scenarios, and documentation of performance improvements relative to the previous baseline. Finally, the new model is designated as the operational baseline, while the prior surrogate, training data, and diagnostic artifacts are archived to preserve full scientific and regulatory traceability.

### Governance Requirements

Full retraining is conducted under configuration control and subject to the same verification, validation, uncertainty calibration, and acceptance criteria as an initial deployment. The retrained surrogate is promoted to operational use only after all governance requirements are satisfied.

Key governance elements include complete documentation of trigger rationale, data sources, and design decisions; archival of prior surrogate and all associated training artifacts; independent validation against withheld data and benchmark scenarios; and formal acceptance review before operational deployment.

This conservative approach reflects DOE expectations for software lifecycle management in high-consequence environmental applications, ensuring that continued use of any surrogate is not permitted once validity is in question.
