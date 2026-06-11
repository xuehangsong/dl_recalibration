### 3.3.5 Multi-fidelity Data Fusion

Multi-fidelity modeling enhances surrogate accuracy and computational efficiency by combining inexpensive low-fidelity simulations with high-fidelity simulations and field observations. This approach enables broad coverage of the parameter space while anchoring predictions to high-accuracy data where available.

#### Fusion Strategies

Two mature strategies dominate the multi-fidelity literature:

1. **Autoregressive Gaussian-process and co-Kriging models** treat high-fidelity outputs as corrected versions of low-fidelity predictions (Kennedy & O'Hagan, 2000; Le Gratiet, 2013). These methods provide principled uncertainty propagation and are well-suited for problems with moderate dimensionality.

2. **Neural discrepancy models** learn nonlinear mappings between fidelity levels (Perdikaris et al., 2017). These approaches capture complex relationships that linear correction models cannot represent, enabling more flexible fidelity fusion.

Recent advances include physics-aware multi-fidelity networks that embed physical constraints directly into the learning architecture (Wen et al., 2021) and transfer learning approaches in which surrogates are pre-trained on large low-fidelity ensembles and fine-tuned using a smaller high-fidelity subset (Tang et al., 2022).

#### Fidelity Levels

In groundwater flow and reactive transport applications:

- **Low-fidelity (LF)**: Coarse-grid simulations (e.g., coarse PFLOTRAN or MODFLOW models) provide broad characterization of system variability across the parameter and operational space.
- **High-fidelity (HF)**: Fine-grid simulations or field observations anchor localized accuracy where precise predictions are required.

This combination achieves strong performance with orders-of-magnitude reduction in simulation cost compared to using high-fidelity data alone (Asher et al., 2015).

#### Fusion Process

The multi-fidelity fusion procedure integrates coarse simulations, fine simulations, and field data through a structured workflow:

1. **Identify fidelity levels and align datasets**, ensuring spatial, temporal, and unit consistency across LF, HF, and observational sources.

2. **Pre-train surrogate models on low-fidelity simulations**, exploiting their broad coverage of the parameter and operational space.

3. **Introduce high-fidelity data**—simulation or observational—and train a discrepancy model or co-Kriging structure so that predictions inherit LF global structure and HF local accuracy (Kennedy & O'Hagan, 2000; Perdikaris et al., 2017).

4. **Quantify fidelity-conditioned uncertainty**, expanding intervals where only LF information is available and narrowing them where HF evidence supports confidence, consistent with UQ strategies in Wen et al. (2021).

5. **Validate fused predictions** against withheld HF runs or independent observational periods to confirm improved performance over single-fidelity surrogates.

6. **Integrate the fused surrogate into the continual learning loop**, enabling more accurate drift detection, better-informed active learning selection, and more stable fine-tuning updates.

#### Integration with Recalibration Framework

Multi-fidelity methods integrate naturally with active learning and continual learning, enabling scalable refinement even under evolving operational regimes. When active learning identifies high-uncertainty regions, the framework can strategically deploy either LF or HF simulations based on the expected information gain and computational budget. The fused surrogate provides improved baseline predictions that enhance drift detection sensitivity and reduce false-positive recalibration triggers.
