# Task: Section 3.3.5-3.3.6 Multi-fidelity and Full Retraining - Prose Revision

## Task ID: SECTION3_3_5_6_PROSE_V2
## Priority: HIGH

---

## 1. OBJECTIVE

Convert Section 3.3.5 (Multi-fidelity Data Fusion) and Section 3.3.6 (Full Retraining) from bullet-point style to flowing prose while preserving ALL citations and technical content.

---

## 2. INPUT FILES

### Original Manuscript (Source of Truth for Citations)
**File:** `manuscript/Framework_draft.docx`
**Lines:** 891-954 (Section 3.3.5 Multi-fidelity: Lines 891-924; Section 3.3.6 Full Retraining: Lines 925-954)
**Purpose:** Verify ALL citations are preserved from the original source

### Primary Source (Current Final Version)
**File:** `drafts/final/section3_FINAL.md`
**Lines:** 470-557

### Original Backup Revisions
**Files:**
- `drafts/backup/section3/section3_3_5_multifidelity_REVISED.md` (Multi-fidelity)
- `drafts/backup/section3/section3_3_6_retrain_REVISED.md` (Full Retraining)
**Purpose:** Cross-reference for any content that may have been condensed

### Earlier Merged Revision
**File:** `drafts/backup/section3_REVISED.md`
**Lines:** 117-138 (Section 3.3.5-3.3.6)
**Purpose:** Alternative phrasing reference

### Citation Reference
**File:** `plans/extracts/citations_section3.md`
**Section:** 3.3.5 Multi-fidelity Data Fusion (Lines 202-221) and 3.3.6 Full Retraining (Lines 223-235)

### Original Task Specifications
**Files:**
- `plans/tasks/task_section3_3_5_multifidelity.md`
- `plans/tasks/task_section3_3_6_retrain.md`
**Purpose:** Contains original source line references from manuscript and full citation lists

---

## 3. OUTPUT FILE

**Path:** `drafts/section3_v2/section3_3_5_6_multifidelity_retrain_v2.md`

---

## 4. CONVERSION TARGETS

### 4.1 Fusion Strategies (Lines 476-482)

**CURRENT:**
```markdown
Two mature strategies dominate the multi-fidelity literature:

1. **Autoregressive Gaussian-process and co-Kriging models** treat high-fidelity outputs as corrected versions of low-fidelity predictions (Kennedy & O'Hagan, 2000; Le Gratiet, 2013). These methods provide principled uncertainty propagation and are well-suited for problems with moderate dimensionality.

2. **Neural discrepancy models** learn nonlinear mappings between fidelity levels (Perdikaris et al., 2017). These approaches capture complex relationships that linear correction models cannot represent, enabling more flexible fidelity fusion.
```

**CONVERT TO:**
Prose paragraph describing both strategies without numbered list format:

```markdown
Two mature strategies dominate the multi-fidelity literature. Autoregressive Gaussian-process and co-Kriging models treat high-fidelity outputs as corrected versions of low-fidelity predictions (Kennedy & O'Hagan, 2000; Le Gratiet, 2013), providing principled uncertainty propagation well-suited for problems with moderate dimensionality. Neural discrepancy models learn nonlinear mappings between fidelity levels (Perdikaris et al., 2017), capturing complex relationships that linear correction models cannot represent and enabling more flexible fidelity fusion. Recent advances include physics-aware multi-fidelity networks that embed physical constraints directly into the learning architecture (Wen et al., 2021) and transfer learning approaches in which surrogates are pre-trained on large low-fidelity ensembles and fine-tuned using a smaller high-fidelity subset (Tang et al., 2022).
```

### 4.2 Fidelity Levels (Lines 487-490)

**CURRENT:**
```markdown
In groundwater flow and reactive transport applications:

- **Low-fidelity (LF)**: Coarse-grid simulations (e.g., coarse PFLOTRAN or MODFLOW models) provide broad characterization of system variability across the parameter and operational space.
- **High-fidelity (HF)**: Fine-grid simulations or field observations anchor localized accuracy where precise predictions are required.
```

**CONVERT TO:**
```markdown
In groundwater flow and reactive transport applications, low-fidelity sources such as coarse-grid PFLOTRAN or MODFLOW simulations provide broad characterization of system variability across the parameter and operational space, while high-fidelity sources including fine-grid simulations or field observations anchor localized accuracy where precise predictions are required. This combination achieves strong performance with orders-of-magnitude reduction in simulation cost compared to using high-fidelity data alone (Asher et al., 2015).
```

### 4.3 Fusion Process (Lines 496-507)

**CURRENT:**
```markdown
The multi-fidelity fusion procedure integrates coarse simulations, fine simulations, and field data through a structured workflow:

1. **Identify fidelity levels and align datasets**, ensuring spatial, temporal, and unit consistency across LF, HF, and observational sources.

2. **Pre-train surrogate models on low-fidelity simulations**, exploiting their broad coverage of the parameter and operational space.

3. **Introduce high-fidelity data**—simulation or observational—and train a discrepancy model or co-Kriging structure so that predictions inherit LF global structure and HF local accuracy (Kennedy & O'Hagan, 2000; Perdikaris et al., 2017).

4. **Quantify fidelity-conditioned uncertainty**, expanding intervals where only LF information is available and narrowing them where HF evidence supports confidence, consistent with UQ strategies in Wen et al. (2021).

5. **Validate fused predictions** against withheld HF runs or independent observational periods to confirm improved performance over single-fidelity surrogates.

6. **Integrate the fused surrogate into the continual learning loop**, enabling more accurate drift detection, better-informed active learning selection, and more stable fine-tuning updates.
```

**CONVERT TO:**
Prose paragraphs describing the workflow without numbered list:

```markdown
The multi-fidelity fusion procedure integrates coarse simulations, fine simulations, and field data through a structured workflow. The process begins by identifying fidelity levels and aligning datasets to ensure spatial, temporal, and unit consistency across low-fidelity, high-fidelity, and observational sources. Surrogate models are then pre-trained on low-fidelity simulations, exploiting their broad coverage of the parameter and operational space.

High-fidelity data—whether from simulation or observation—is subsequently introduced to train a discrepancy model or co-Kriging structure, allowing predictions to inherit low-fidelity global structure while achieving high-fidelity local accuracy (Kennedy & O'Hagan, 2000; Perdikaris et al., 2017). The framework quantifies fidelity-conditioned uncertainty by expanding intervals where only low-fidelity information is available and narrowing them where high-fidelity evidence supports confidence, consistent with UQ strategies described by Wen et al. (2021).

Fused predictions are validated against withheld high-fidelity runs or independent observational periods to confirm improved performance over single-fidelity surrogates. Finally, the fused surrogate is integrated into the continual learning loop, enabling more accurate drift detection, better-informed active learning selection, and more stable fine-tuning updates.
```

### 4.4 Trigger Conditions (Lines 520-525)

**CURRENT:**
```markdown
Specific conditions that warrant full retraining include:

- **Regime shifts or major forcing changes** that fundamentally alter system behavior beyond the original training domain
- **Redefinition of the underlying physics model**, such as revised geologic interpretations or updated reaction networks
- **Recalibration of the numerical model** after incorporation of new hydrogeologic data or conceptual model updates (Laloy et al., 2017)
- **Major reconfiguration of pumping and boundary conditions** that invalidate the original training scenarios
- **Repeated fine-tuning failures** indicating that the training domain has materially shifted
```

**CONVERT TO:**
Prose paragraph listing conditions inline.

### 4.5 Retraining Process (Lines 533-543)

**CURRENT:**
```markdown
The retraining process proceeds through a formal set of steps:

1. **Verify retraining triggers**, including major operational changes, substantive updates to the physics model, or repeated fine-tuning failures indicating material domain shift.

2. **Redesign the training domain**, defining updated ranges of hydrofacies, operational scenarios, and boundary forcings consistent with new conceptual understanding.

3. **Generate a new ensemble of high-fidelity simulations**, supplemented where appropriate by low-fidelity runs to maintain broad coverage and accelerate sampling.

4. **Integrate recent field observations**, anchoring the surrogate to empirical system behavior.

5. **Train a new surrogate from scratch**, including UQ calibration, validation against benchmark scenarios, and documentation of performance improvements relative to the previous baseline.

6. **Designate the new model as the operational baseline**, while archiving the prior surrogate, training data, and diagnostic artifacts to preserve full scientific and regulatory traceability.
```

**CONVERT TO:**
Prose paragraphs describing the process without numbered list.

### 4.6 Governance Requirements (Lines 550-554)

**CURRENT:**
```markdown
Key governance elements include:

- **Complete documentation** of trigger rationale, data sources, and design decisions
- **Archival of prior surrogate** and all associated training artifacts
- **Independent validation** against withheld data and benchmark scenarios
- **Formal acceptance review** before operational deployment
```

**CONVERT TO:**
Prose sentence with inline list.

---

## 5. MANDATORY CITATIONS

### Multi-fidelity Citations
| Citation | Context |
|----------|---------|
| Kennedy & O'Hagan, 2000 | Co-Kriging, autoregressive GP |
| Le Gratiet, 2013 | Autoregressive GP |
| Perdikaris et al., 2017 | Neural discrepancy models |
| Asher et al., 2015 | Cost reduction |
| Wen et al., 2021 | Physics-aware networks, UQ strategies |
| Tang et al., 2022 | Transfer learning |

### Full Retraining Citations
| Citation | Context |
|----------|---------|
| Parisi et al., 2019 | Concept drift literature |
| Sayed et al., 2025 | Concept drift literature |
| Laloy et al., 2017 | Numerical model recalibration |
| Wen et al., 2021 | Domain deviation |

---

## 6. VERIFICATION CHECKLIST

After completing the revision, verify:

- [ ] All multi-fidelity citations preserved (6 citations)
- [ ] All full retraining citations preserved (4 citations)
- [ ] Fusion strategies clearly described
- [ ] Fidelity levels (LF/HF) explained
- [ ] Six-step fusion process maintained (as prose)
- [ ] Five trigger conditions preserved
- [ ] Six-step retraining process maintained (as prose)
- [ ] Governance requirements preserved
- [ ] No bullet points or numbered lists
- [ ] Section structure (3.3.5, 3.3.6) maintained

---

## 7. STYLE NOTES

- Convert all numbered lists to flowing prose paragraphs
- Use transitional phrases like "The process begins by...", "Subsequently...", "Finally..."
- Maintain technical precision
- Keep the logical sequence of steps even in prose form
- Integrate citations naturally at the point of relevant claims
