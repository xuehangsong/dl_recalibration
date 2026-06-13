# Task: Section 3.1 Governance Methods - Prose Revision

## Task ID: SECTION3_1_PROSE_V2
## Priority: HIGH

---

## 1. OBJECTIVE

Convert Section 3.1 (Governance Methods) from bullet-point style to flowing prose while preserving ALL citations and technical content.

---

## 2. INPUT FILES

### Original Manuscript (Source of Truth for Citations)
**File:** `manuscript/Framework_draft.docx`
**Lines:** 409-504 (Section 3.1 Governance Essentials)
**Purpose:** Verify ALL citations are preserved from the original source

### Primary Source (Current Final Version)
**File:** `drafts/final/section3_FINAL.md`
**Lines:** 1-107

### Original Backup Revision
**File:** `drafts/backup/section3/section3_1_governance_REVISED.md`
**Purpose:** Cross-reference for any content that may have been condensed

### Earlier Merged Revision
**File:** `drafts/backup/section3_REVISED.md`
**Lines:** 1-32 (Section 3.1)
**Purpose:** Alternative phrasing reference

### Citation Reference
**File:** `plans/extracts/citations_section3.md`
**Section:** 3.1 Governance Essentials (Lines 9-61)

### Original Task Specification
**File:** `plans/tasks/task_section3_1_governance.md`
**Purpose:** Contains original source line references from manuscript

---

## 3. OUTPUT FILE

**Path:** `drafts/section3_v2/section3_1_governance_v2.md`

**Note:** Create the `drafts/section3_v2/` directory if it doesn't exist.

---

## 4. CONVERSION TARGETS

### 4.1 Model Usage Scope (Lines 21-26)

**CURRENT (bullet style):**
```markdown
Surrogate models are intended primarily to support **screening-level analyses**, including:

- Rapid evaluation of alternative remediation scenarios
- Sensitivity analyses and uncertainty exploration
- Preliminary planning studies
```

**CONVERT TO (prose style):**
```markdown
Surrogate models are intended primarily to support screening-level analyses, including rapid evaluation of alternative remediation scenarios, sensitivity analyses and uncertainty exploration, and preliminary planning studies.
```

### 4.2 Acceptance Criteria (Lines 37-42)

**CURRENT:**
```markdown
**Acceptance criteria** typically include:

- Quantitative performance metrics (e.g., error statistics at priority monitoring locations)
- Calibration of uncertainty estimates (e.g., empirical coverage of prediction intervals)
- Spatial and temporal consistency with observed plume behavior
- Stability of performance over time under routine operational conditions
```

**CONVERT TO:**
Merge into a flowing sentence that lists these criteria inline with appropriate connectors.

### 4.3 Recalibration Triggers (Lines 44-48)

**CURRENT:**
```markdown
**Recalibration triggers** are defined to detect meaningful degradation in surrogate performance or applicability:

- Sustained increases in prediction residuals
- Inflation or miscalibration of uncertainty estimates
- Documented changes in boundary conditions or operational regimes...
```

**CONVERT TO:**
Merge into prose paragraph.

### 4.4 Monitoring Schedule Table (Lines 58-62)

**KEEP AS TABLE** - Tables are appropriate for structured comparisons.

### 4.5 Configuration Control (Lines 69-72)

**CURRENT:**
```markdown
All surrogate model versions are subject to formal configuration control, including:

- Version tracking
- Documentation of training data and assumptions
- Preservation of prior approved models
```

**CONVERT TO:**
Inline list within prose sentence.

### 4.6 Rollback Conditions (Lines 82-87)

**CURRENT:**
```markdown
Under a rollback condition:

1. Neither the updated surrogate nor the prior surrogate is permitted...
2. Surrogate-based decision support is explicitly suspended
3. Analytical support reverts exclusively to the high-fidelity physics-based numerical model
4. Rollback automatically triggers escalation to a governed full retraining process
```

**CONVERT TO:**
Prose paragraph describing the sequence of actions.

### 4.7 Governance Summary (Lines 98-104)

**CURRENT:**
```markdown
Key principles include:

- Governance grounded in established EPA and DOE quality assurance standards...
- Surrogate use limited to screening- and planning-level decision support
- Primacy of high-fidelity physics-based numerical models...
- Objective acceptance criteria and documented recalibration triggers
- Formal configuration control with full auditability
- Explicit withdrawal and retraining procedures...
```

**CONVERT TO:**
Prose paragraph summarizing key principles.

---

## 5. MANDATORY CITATIONS

These citations MUST appear in the output:

| Citation | Context |
|----------|---------|
| CERCLA | Regulatory foundation |
| EPA 540-R-01-007 | Superfund Five-Year Reviews |
| EPA/100/K-09/003 | Environmental Models Guidance |
| DOE O 414.1D Chg 2 | Quality Assurance |
| DOE EM-QA-001 | Environmental Management QA |
| ASME NQA-1 Subpart 2.7 | Software Quality Requirements |
| EPA 540-G-89-004 | RI/FS Guidance |
| EPA QA/G-5M | Modeling QA |

---

## 6. VERIFICATION CHECKLIST

After completing the revision, verify:

- [ ] All 8 regulatory citations preserved
- [ ] Rollback definition preserved (withdrawal from operational use, not version reversion)
- [ ] Monitoring schedule table retained
- [ ] No bullet points except where explicitly allowed
- [ ] All technical content preserved
- [ ] Prose flows naturally and reads well
- [ ] Section structure (3.1.1 through 3.1.5) maintained

---

## 7. STYLE NOTES

- Use active voice where possible
- Integrate citations naturally into sentences
- Use connectors like "including," "such as," "specifically," "in particular"
- Maintain DOE Technical Report tone (formal, precise, not conversational)
- Keep paragraphs focused on single topics
