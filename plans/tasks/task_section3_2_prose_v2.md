# Task: Section 3.2 Modeling Engine Methods - Prose Revision

## Task ID: SECTION3_2_PROSE_V2
## Priority: HIGH

---

## 1. OBJECTIVE

Convert Section 3.2 (Modeling Engine Methods) from bullet-point style to flowing prose while preserving ALL citations and technical content.

---

## 2. INPUT FILES

### Original Manuscript (Source of Truth for Citations)
**File:** `manuscript/Framework_draft.docx`
**Lines:** 507-627 (Section 3.2 Modeling Engines)
**Purpose:** Verify ALL citations are preserved from the original source

### Primary Source (Current Final Version)
**File:** `drafts/final/section3_FINAL.md`
**Lines:** 108-237

### Original Backup Revision
**File:** `drafts/backup/section3/section3_2_modeling_engines_REVISED.md`
**Purpose:** Cross-reference for any content that may have been condensed

### Earlier Merged Revision
**File:** `drafts/backup/section3_REVISED.md`
**Lines:** 33-54 (Section 3.2)
**Purpose:** Alternative phrasing reference

### Citation Reference
**File:** `plans/extracts/citations_section3.md`
**Section:** 3.2 Modeling Engines (Lines 64-127)

### Original Task Specification
**File:** `plans/tasks/task_section3_2_modeling_engines.md`
**Purpose:** Contains original source line references from manuscript and full citation lists

---

## 3. OUTPUT FILE

**Path:** `drafts/section3_v2/section3_2_modeling_v2.md`

---

## 4. CONVERSION TARGETS

### 4.1 Site Challenges (Lines 117-124)

**CURRENT (bullet style):**
```markdown
The physical phenomena represented typically include:

- **Advection and dispersion** of dissolved species (Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016)
- **Sorption** onto solid phases and associated reaction processes
- **Non-Fickian plume spreading** from heterogeneity...
- **Back diffusion** from fine-grained units...
- **Density-driven flow** in systems impacted by DNAPL, LNAPL...
- **Engineered operations** including pump-and-treat wells...
```

**CONVERT TO:**
A flowing paragraph that integrates all phenomena with their citations:

```markdown
The physical phenomena represented typically include advection and dispersion of dissolved species (Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016), sorption onto solid phases and associated reaction processes, and non-Fickian plume spreading arising from heterogeneity and diffusion-controlled mass exchange between transmissive and low-permeability zones (Guo et al., 2021). Back diffusion from fine-grained units is recognized as a major control on plume persistence after source removal (Yang et al., 2016, 2017). Density-driven flow occurs in systems impacted by DNAPL or LNAPL (Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017) or by seawater intrusion (Werner et al., 2013; Xu et al., 2019). Engineered operations, including pump-and-treat wells, injection/extraction networks, and time-varying boundary conditions, must also be represented (Ko et al., 2005).
```

### 4.2 Physics Models Table (Lines 131-139)

**KEEP AS TABLE** - Tables are appropriate for structured model comparisons.

### 4.3 Computational Constraints (Lines 145-150)

**CURRENT:**
```markdown
Despite their fidelity, these simulators impose significant computational constraints:

- Individual forward runs can take **hours to days** on standard computing resources...
- Planning tasks often require **hundreds to thousands** of model evaluations...
- Interactive exploration of design space becomes impractical...
```

**CONVERT TO:**
Prose paragraph describing computational limitations.

### 4.4 Surrogate Family 1: CNN/U-Net (Lines 163-168)

**CURRENT:**
```markdown
Key citations:
- Attention U-Net for steady-state hydraulic head fields (Taccari et al., 2022)
- Image-to-image regression for multiphase flow (Mo et al., 2019)
- AR-ResUNet for dynamic multiphase flow and solute transport (Jiang et al., 2021)
- U-Net surrogate for transient groundwater flow inverse problems (Lauzon, 2024)
```

**CONVERT TO:**
Prose paragraph integrating citations:

```markdown
Representative applications include attention U-Net architectures for steady-state hydraulic head fields (Taccari et al., 2022), image-to-image regression for multiphase flow (Mo et al., 2019), autoregressive residual U-Net (AR-ResUNet) for dynamic multiphase flow and solute transport (Jiang et al., 2021), and U-Net surrogates for transient groundwater flow inverse problems (Lauzon, 2024).
```

### 4.5 Surrogate Family 2: Operator-Learning (Lines 177-181)

**CURRENT:**
```markdown
Key citations:
- U-FNO for CO₂-water multiphase systems (Wen et al., 2022)
- DeepONet for confined aquifer flow (Taccari et al., 2024)
- **GeoFUSE framework** for seawater intrusion: U-FNO achieves ~10⁵ speedup...
- Physics-informed U-FNO for climate stress testing at Savannah River Site (Wang et al., 2022)
```

**CONVERT TO:**
Prose paragraph with citations integrated.

### 4.6 Surrogate Family 3: Sequence Models (Lines 190-193)

**CONVERT TO:** Prose paragraph.

### 4.7 Surrogate Family 4: Generative Models (Lines 202-206)

**CONVERT TO:** Prose paragraph.

### 4.8 Surrogate Family 5: Regression Surrogates (Lines 215-219)

**CONVERT TO:** Prose paragraph.

### 4.9 Training Setup Table (Lines 225-230)

**KEEP AS TABLE** - Tables are appropriate for structured guidance.

---

## 5. MANDATORY CITATIONS

### Physics Model Citations
| Model | Citation |
|-------|----------|
| MODFLOW | Harbaugh, 2005 |
| MT3DMS | Zheng and Wang, 1999 |
| PFLOTRAN | Hammond et al., 2014 |
| eSTOMP | White and Oostrom, 2003 |
| TOUGH2 | Pruess et al., 1999 |
| PARFLOW | Maxwell et al., 2015 |
| HYDRUS | Šimůnek et al., 2016 |

### Site Challenge Citations
| Topic | Citation |
|-------|----------|
| Advection/dispersion | Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016 |
| Non-Fickian | Guo et al., 2021 |
| Back diffusion | Yang et al., 2016, 2017 |
| DNAPL/LNAPL | Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017 |
| Seawater intrusion | Werner et al., 2013; Xu et al., 2019 |
| Pump-and-treat | Ko et al., 2005 |
| Monte Carlo | Rubin, 2003 |

### Surrogate Model Citations
| Family | Citations |
|--------|-----------|
| CNN/U-Net | Taccari et al., 2022; Mo et al., 2019; Jiang et al., 2021; Lauzon, 2024 |
| FNO/U-FNO | Li et al., 2020; Wen et al., 2022; Taccari et al., 2024; Jiang et al., 2025; Wang et al., 2022 |
| Sequence | Chen et al., 2021; Anshuman and Eldho, 2023; Li et al., 2025 |
| Generative | Graham and Chen, 2020; Miele and Linde, 2025; Wang et al., 2025b,c |
| Regression | Asher et al., 2015; Siade et al., 2020; Shams et al., 2021; Marrel and Iooss, 2024 |
| Review | Luo et al., 2023 |

---

## 6. VERIFICATION CHECKLIST

After completing the revision, verify:

- [ ] All 7 physics model citations preserved
- [ ] All site challenge citations preserved
- [ ] All surrogate family citations preserved
- [ ] Physics Models table retained
- [ ] Training Setup table retained
- [ ] GeoFUSE ~10⁵ speedup mentioned
- [ ] No bullet points except where explicitly allowed
- [ ] Section structure (3.2.1 through 3.2.4) maintained

---

## 7. STYLE NOTES

- Each surrogate family should have a brief architectural description followed by integrated citations
- Maintain the "Architecture:" and "Use case:" format as introductory sentences, not bullet points
- Keep technical precision (e.g., "orders-of-magnitude speedup")
- Reference Appendix A for detailed literature review

---

## 8. IMPORTANT: RELATIONSHIP WITH APPENDIX A

**Appendix A** (`drafts/final/appendix_a_FINAL.md`) contains the detailed surrogate model literature review. Section 3.2.3 in the main text should remain a **summary overview**, NOT expand into Appendix-level detail.

### Level of Detail Guidelines

| Aspect | Section 3.2.3 (Main Text) | Appendix A |
|--------|---------------------------|------------|
| **Purpose** | Framework context - which surrogates fit which use cases | Comprehensive literature review |
| **Length per family** | 3-5 sentences | Multiple paragraphs |
| **Citations** | 3-5 key citations per family | Extensive citations with discussion |
| **Technical depth** | Architecture type + use case + brief description | Full methodology, comparisons, benchmarks |

### What to Preserve in Section 3.2.3

1. **Brief family descriptions** - Keep the 2-3 sentence architectural descriptions
2. **Use case mapping** - Maintain the "Architecture:" and "Use case:" information
3. **Key citations** - Convert bullet lists to prose but keep the same ~4 citations per family
4. **Appendix reference** - Preserve Line 234: "Detailed paper-by-paper analysis of surrogate modeling literature is provided in Appendix A"

### What NOT to Do

- Do NOT expand descriptions to Appendix-level detail
- Do NOT add citations beyond what's currently in the section
- Do NOT duplicate content that belongs in Appendix A
- Do NOT remove the Appendix A reference

### Example Conversion (Family 1)

**CURRENT:**
```markdown
### Family 1: Convolutional Encoder-Decoder Models

**Architecture:** U-Net, ResNet variants
**Use case:** High-resolution spatial fields (heads, salinity, plume extent)

These networks treat spatial fields as images and learn direct mappings from input fields (hydraulic conductivity, boundary conditions, pumping patterns) to output fields. Convolutions preserve interfaces, sharp fronts, and channelized structures.

Key citations:
- Attention U-Net for steady-state hydraulic head fields (Taccari et al., 2022)
- Image-to-image regression for multiphase flow (Mo et al., 2019)
- AR-ResUNet for dynamic multiphase flow and solute transport (Jiang et al., 2021)
- U-Net surrogate for transient groundwater flow inverse problems (Lauzon, 2024)
```

**CONVERT TO:**
```markdown
### Family 1: Convolutional Encoder-Decoder Models

Convolutional encoder-decoder architectures such as U-Net and ResNet variants are well-suited for predicting high-resolution spatial fields including hydraulic heads, salinity distributions, and plume extents. These networks treat spatial fields as images and learn direct mappings from input fields (hydraulic conductivity, boundary conditions, pumping patterns) to output fields, with convolutions preserving interfaces, sharp fronts, and channelized structures. Representative applications include attention U-Net architectures for steady-state hydraulic head fields (Taccari et al., 2022), image-to-image regression for multiphase flow (Mo et al., 2019), autoregressive residual U-Net for dynamic multiphase flow and solute transport (Jiang et al., 2021), and U-Net surrogates for transient groundwater flow inverse problems (Lauzon, 2024).
```

**Note:** This maintains the same level of detail and citations as the original - just converted to prose format.
