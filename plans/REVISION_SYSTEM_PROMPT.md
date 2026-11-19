# REVISION SYSTEM PROMPT

**Purpose:** This is the authoritative reference document that MUST be read before any revision work on the DL Recalibration Framework document.

**Version:** 1.1
**Last Updated:** 2025-03-19

---

## CRITICAL: READ THIS FIRST

**⚠️ MANDATORY: Read this entire system prompt at the START of every revision session.**

Before making ANY changes to this document, you MUST:
1. **Read this entire system prompt** (refresh your memory every session)
2. **Check the Change Log** (Section 11) to see what's already been done
3. Understand the document structure
4. Follow the style guidelines
5. Preserve all valuable content
6. Store unused content appropriately
7. **Update the Change Log** after completing any task

---

## 1. DOCUMENT OVERVIEW

### 1.1 Document Title
**Keeping Deep-Learning Surrogates Accurate for Long-Term Groundwater Remediation: Concept & Prototype Plan**

### 1.2 Document Type
- **DOE Technical Report** (NOT a peer-reviewed publication)
- **NOT a markdown technical file** (avoid heavy bullet points, bold formatting)
- Written in **professional prose** that reads like a formal report
- Suitable for DOE program managers, site operators, and technical reviewers

### 1.3 Core Concept
The framework addresses how to keep deep-learning surrogate models accurate over multi-decade groundwater remediation projects through:
- **Three Pillars** (management domains that define WHAT)
- **Seven-Step Workflow** (operational process that defines HOW)

**THE KEY INSIGHT:** Pillars define WHAT; Workflow defines HOW

---

## 2. DOCUMENT STRUCTURE

### 2.1 Final Section Layout

| Section | Title | Status | Source |
|---------|-------|--------|--------|
| Front Matter | Title, Abstract, Summary, Acknowledgments, Acronyms, TOC | Keep as-is | Framework_draft.docx |
| Section 1 | Introduction | Keep as-is | Framework_draft.docx (lines 339-356) |
| Section 2 | Framework Overview | ✅ COMPLETE | drafts/section2_1_pillars_REVISED.md, drafts/section2_2_workflow_REVISED.md |
| Section 3 | Methods | Needs streamlining | Framework_draft.docx + move literature to Appendix |
| Section 4 | Implementation Roadmap | ✅ COMPLETE | drafts/section5_REVISED_v3.md (renumber 5.x → 4.x) |
| Section 5 | Prototype and Case Study | Needs work | Framework_draft.docx Sections 4 + 6 (merged) |
| Section 6 | Future Work and Summary | Needs work | Framework_draft.docx Section 7 + new content |
| Appendix A | Surrogate Model Literature | NEW | Content moved from Section 3.2.3 |

### 2.2 Section Details

#### Section 1: Introduction (~18 lines)
- Problem statement: DL surrogates drift from reality
- Key challenges: Concept/distribution drift, data/compute scarcity, physical realism
- Motivation for adaptive strategies
- Document overview

#### Section 2: Framework Overview (~475 lines total)
- **2.1 Three-Pillar Architecture** (109 lines) - COMPLETE
- **2.2 Recalibration Workflow** (366 lines) - COMPLETE

#### Section 3: Methods (~400 lines after streamlining)
- **3.0** Introduction paragraph (NEW - 5 lines)
- **3.1** Governance Methods - Pillar A (~95 lines) - Keep as-is
- **3.2** Modeling Engine Methods - Pillar B (~50 lines after streamlining)
  - 3.2.1 Site Challenges (~10 lines) - Keep as-is
  - 3.2.2 Physics-Based Models (~10 lines) - Keep as-is
  - 3.2.3 Surrogate Landscape (~20 lines) - STREAMLINED (move ~60 lines to Appendix)
  - 3.2.4 Training Setup (~12 lines) - Keep as-is
- **3.3** Recalibration Mechanism Methods - Pillar C (~320 lines) - Keep as-is
  - 3.3.1 Uncertainty Quantification (~40 lines)
  - 3.3.2 Trigger Logic (~140 lines)
  - 3.3.3 Continual Learning (~30 lines)
  - 3.3.4 Active Learning (~30 lines)
  - 3.3.5 Multi-fidelity Data Fusion (~35 lines)
  - 3.3.6 Fully Retrain (~30 lines)

#### Section 4: Implementation Roadmap (~277 lines)
- Renumber from 5.x to 4.x
- Source: drafts/section5_REVISED_v3.md
- COMPLETE - ready to use

#### Section 5: Prototype and Case Study (~300 lines)
- **5.0** Introduction (NEW)
- **5.1** Validation Framework (expand from ~15 to ~40 lines)
- **5.2** Prototype Implementations (~140 lines)
- **5.3** Case Study Design (~100 lines)
- **5.4** Expected Outcomes (~20 lines)

#### Section 6: Future Work and Summary (~100 lines)
- **6.1** Research Directions (~40 lines)
- **6.2** Operational Considerations (~30 lines)
- **6.3** Summary (~30 lines)

#### Appendix A: Surrogate Model Literature (~85 lines)
- Detailed architecture descriptions moved from Section 3.2.3
- CNN/U-Net literature
- FNO/U-FNO literature
- DeepONet literature
- Transformer literature
- Gaussian Process literature
- PINN literature
- Hybrid approaches literature

---

## 3. STYLE GUIDELINES

### 3.1 Document Style: DOE Technical Report

**DO:**
- Write in professional prose with complete sentences and paragraphs
- Use formal technical language appropriate for DOE reports
- Structure content with clear section headings and logical flow
- Include tables and figures where they aid understanding
- Use numbered lists sparingly and only for sequential steps or criteria
- Write in third person (the framework, the system, the approach)

**DO NOT:**
- Use heavy bullet points throughout (this is not a markdown technical file)
- Overuse bold formatting (reserve for key terms on first use)
- Write in first person (we, our)
- Use informal language or contractions
- Create dense walls of bullet points that don't read as prose

### 3.2 Formatting Conventions

**Headings:**
- Section: `# 1. Introduction`
- Subsection: `## 1.1 Background`
- Sub-subsection: `### 1.1.1 Problem Statement`

**Key Terms:**
- Bold on first use only: **continual learning**, **uncertainty quantification**
- Subsequent uses: continual learning, uncertainty quantification

**Cross-References:**
- Use explicit section references: "as described in Section 3.3.1"
- Link workflow steps to methods: "Step 2 (DETECT) employs the trigger logic from Section 3.3.2"

**Tables:**
- Use tables for structured comparisons (e.g., pillar-workflow cross-reference)
- Include table captions
- Keep tables readable (not too many columns)

**Figures:**
- Mermaid diagrams for workflows
- Include figure captions
- Reference figures in text

### 3.3 Tone and Voice

- **Authoritative but accessible:** Technical accuracy without unnecessary jargon
- **Forward-looking:** This is a framework design, not a completed system
- **Practical:** Focus on implementation considerations
- **Balanced:** Acknowledge limitations and open questions

---

## 4. CONTENT PRESERVATION RULES

### 4.1 Golden Rule
**NEVER lose valuable information from the original document.**

### 4.2 What to Preserve

**Always Keep:**
- Technical details about methods (UQ, continual learning, active learning, etc.)
- Specific parameter values and thresholds (e.g., 70-75% replay buffer, batch size 6-10)
- Regulatory references (CERCLA, DOE O 414.1D, NQA-1, EM-QA-001)
- Physics-based model names (MODFLOW, PFLOTRAN, eSTOMP, etc.)
- Surrogate model architectures (U-Net, FNO, DeepONet, etc.)
- Validation metrics and acceptance criteria
- Governance requirements and audit trail specifications
- Case study details (Hanford 200 West, PFLOTRAN baseline, etc.)

**Never Delete:**
- Method descriptions from Section 3
- Governance requirements from Section 3.1
- Trigger logic details from Section 3.3.2
- Continual learning strategies from Section 3.3.3
- Active learning approaches from Section 3.3.4

### 4.3 What Can Be Moved

**Move to Appendix A:**
- Detailed surrogate model literature reviews (~60-85 lines from Section 3.2.3)
- Extended architecture comparisons
- Historical context on model development

**Move to Unused Content File:**
- Redundant content that duplicates other sections
- Outdated information superseded by revisions
- Content that doesn't fit the restructured document

### 4.4 Unused Content Storage

Create and maintain: `drafts/unused_content.md`

Format:
```markdown
# Unused Content Archive

## Source: [Original Section]
### Reason: [Why removed]
### Content:
[Original text]

---
```

---

## 5. TERMINOLOGY CONSISTENCY

### 5.1 Required Terms

| Correct Term | Incorrect Alternatives |
|--------------|----------------------|
| Three-pillar architecture | Three pillars, pillar framework |
| Pillar A: Conceptual Design & Governance | Governance pillar, rules pillar |
| Pillar B: Modeling Engines | Models pillar, simulation pillar |
| Pillar C: Recalibration Mechanisms | Adaptive pillar, methods pillar |
| Seven-step workflow | 7-step process, recalibration cycle |
| Phase 1: Continuous Monitoring | Monitoring phase, detection phase |
| Phase 2: Triggered Response | Update phase, recalibration phase |
| MONITOR, DETECT, DECIDE, PREPARE, UPDATE, CALIBRATE, DEPLOY | Any other step names |

### 5.2 Key Concepts

- **Pillars = Management Domains** (NOT workflow stages)
- **Workflow = Operational Process** (traverses all pillars)
- **Continual learning** (NOT continuous learning)
- **Uncertainty quantification (UQ)** (NOT uncertainty estimation)
- **Drift detection** (NOT model degradation detection)
- **Recalibration** (NOT retraining, unless full retrain is meant)

---

## 6. REFERENCE FILES

### 6.1 Authoritative References (Read-Only)

| File | Purpose |
|------|---------|
| `plans/design_decisions.md` | Core architectural decisions |
| `manuscript/Framework_draft.docx` | Original source document |
| `plans/master_document_layout.md` | Complete restructuring plan |

### 6.2 Approved Revisions (Ready to Use)

| File | Section | Status |
|------|---------|--------|
| `drafts/section2_1_pillars_REVISED.md` | Section 2.1 | ✅ COMPLETE |
| `drafts/section2_2_workflow_REVISED.md` | Section 2.2 | ✅ COMPLETE |
| `drafts/section5_REVISED_v3.md` | Section 4 (renumber) | ✅ COMPLETE |

### 6.3 Planning Documents

| File | Purpose |
|------|---------|
| `plans/document_restructuring_plan.md` | Overall restructuring strategy |
| `plans/section3_restructuring_analysis.md` | Section 3 streamlining details |
| `plans/document_skeletons.md` | Structural outlines |

### 6.4 Working Files

| File | Purpose |
|------|---------|
| `drafts/unused_content.md` | Archive for removed content |
| `drafts/section3/` | Section 3 subsection revisions (directory) |
| `drafts/section3_FINAL.md` | Section 3 assembled (to create) |
| `drafts/section5_case_study_REVISED.md` | Section 5 revision (to create) |
| `drafts/section6_REVISED.md` | Section 6 revision (to create) |
| `drafts/appendix_a_REVISED.md` | Appendix A (to create) |

### 6.5 Task Files (NEW - Citation Preservation Approach)

| File | Purpose |
|------|---------|
| `plans/extracts/citations_section3.md` | Pre-extracted citations with line numbers |
| `plans/tasks/task_section3_1_governance.md` | Task requirements for Section 3.1 |
| `plans/tasks/task_section3_2_modeling_engines.md` | Task requirements for Section 3.2 |
| `plans/tasks/task_section3_3_1_uq.md` | Task requirements for Section 3.3.1 |
| `plans/tasks/task_section3_3_2_trigger.md` | Task requirements for Section 3.3.2 |
| `plans/tasks/task_section3_3_3_continual.md` | Task requirements for Section 3.3.3 |
| `plans/tasks/task_section3_3_4_active.md` | Task requirements for Section 3.3.4 |
| `plans/tasks/task_section3_3_5_multifidelity.md` | Task requirements for Section 3.3.5 |
| `plans/tasks/task_section3_3_6_retrain.md` | Task requirements for Section 3.3.6 |

---

## 7. IMPLEMENTATION BREAKDOWN

### 7.1 Implementation Order (With Dependencies)

**⚠️ IMPORTANT:** Sections must be revised in dependency order. Each section may reference terminology and concepts from earlier sections.

```
DEPENDENCY GRAPH:

Section 2.1 (Pillars) ──────────────────────────────────────┐
     │                                                       │
     ▼                                                       │
Section 2.2 (Workflow) ─────────────────────────────────────┤
     │                                                       │
     ├──────────────────┬───────────────────┐               │
     ▼                  ▼                   ▼               │
Section 3 (Methods)  Section 4 (Roadmap)  Appendix A       │
     │                  │                   │               │
     └──────────────────┼───────────────────┘               │
                        ▼                                   │
              Section 5 (Case Study) ◄──────────────────────┤
                        │                                   │
                        ▼                                   │
              Section 6 (Future Work) ◄─────────────────────┘
                        │
                        ▼
                 Final Assembly
```

### 7.2 Task List (In Order)

| Order | Task | Depends On | Input Files | Output File | Status |
|-------|------|------------|-------------|-------------|--------|
| 1 | Section 2.1 Style Conversion | None | drafts/section2_1_pillars_REVISED.md | drafts/section2_1_FINAL.md | ⬜ Pending |
| 2 | Section 2.2 Style Conversion | Task 1 | drafts/section2_2_workflow_REVISED.md | drafts/section2_2_FINAL.md | ⬜ Pending |
| 3 | Section 3 Streamlining | Tasks 1-2 | Framework_draft.docx (lines 409-954) | drafts/section3_REVISED.md | ⬜ Pending |
| 4 | Appendix A Creation | Task 3 | Content extracted from Section 3 | drafts/appendix_a_REVISED.md | ⬜ Pending |
| 5 | Section 4 Renumbering + Style | Tasks 1-2 | drafts/section5_REVISED_v3.md | drafts/section4_REVISED.md | ⬜ Pending |
| 6 | Section 5 (Case Study) | Tasks 3-5 | Framework_draft.docx (Sections 4+6) | drafts/section5_case_study_REVISED.md | ⬜ Pending |
| 7 | Section 6 (Future Work) | Tasks 1-6 | Framework_draft.docx (Section 7) + new | drafts/section6_REVISED.md | ⬜ Pending |
| 8 | Final Assembly | All above | All revised drafts | manuscript/Framework_RESTRUCTURED.md | ⬜ Pending |

#### Task 1: Section 2.1 Style Conversion (FOUNDATION)

**Read First:**
- This system prompt
- `drafts/section2_1_pillars_REVISED.md`
- `plans/design_decisions.md` (Section 2 guidance)

**Actions:**
1. Convert bullet-point heavy format to DOE report prose style
2. Maintain all technical content and pillar definitions
3. Keep cross-reference table but ensure it reads professionally
4. Verify terminology matches Section 5.1 of this prompt
5. Ensure "Pillars define WHAT" principle is clear

**Output:** `drafts/section2_1_FINAL.md`

---

#### Task 2: Section 2.2 Style Conversion

**Read First:**
- This system prompt
- `drafts/section2_2_workflow_REVISED.md`
- `drafts/section2_1_FINAL.md` (for terminology consistency)

**Actions:**
1. Convert bullet-point heavy format to DOE report prose style
2. Maintain all workflow step definitions and details
3. Keep Mermaid diagram and cross-reference table
4. Verify terminology matches Section 2.1 and this prompt
5. Ensure "Workflow defines HOW" principle is clear

**Output:** `drafts/section2_2_FINAL.md`

---

#### Task 3: Section 3 Streamlining (REVISED APPROACH - v2)

**⚠️ CRITICAL: Citation Preservation Required**

The previous approach lost ALL citations from Section 3. The new approach uses:
1. **Task-specific requirement files** in `plans/tasks/`
2. **Pre-extracted citations** in `plans/extracts/citations_section3.md`
3. **Subsection-by-subsection processing** to manage context window

**New Task Files (execute in order):**
| Task File | Section | Output |
|-----------|---------|--------|
| `plans/tasks/task_section3_1_governance.md` | 3.1 Governance | `drafts/section3/section3_1_governance_REVISED.md` |
| `plans/tasks/task_section3_2_modeling_engines.md` | 3.2 Modeling Engines | `drafts/section3/section3_2_modeling_engines_REVISED.md` |
| `plans/tasks/task_section3_3_1_uq.md` | 3.3.1 UQ | `drafts/section3/section3_3_1_uq_REVISED.md` |
| `plans/tasks/task_section3_3_2_trigger.md` | 3.3.2 Trigger Logic | `drafts/section3/section3_3_2_trigger_REVISED.md` |
| `plans/tasks/task_section3_3_3_continual.md` | 3.3.3 Continual Learning | `drafts/section3/section3_3_3_continual_REVISED.md` |
| `plans/tasks/task_section3_3_4_active.md` | 3.3.4 Active Learning | `drafts/section3/section3_3_4_active_REVISED.md` |
| `plans/tasks/task_section3_3_5_multifidelity.md` | 3.3.5 Multi-fidelity | `drafts/section3/section3_3_5_multifidelity_REVISED.md` |
| `plans/tasks/task_section3_3_6_retrain.md` | 3.3.6 Full Retrain | `drafts/section3/section3_3_6_retrain_REVISED.md` |

**Workflow for Each Subsection:**
1. Load the task file first (contains mandatory citations, key concepts, style requirements)
2. Load relevant portion of `plans/extracts/citations_section3.md`
3. Load ONLY the source lines specified in the task file
4. Revise while checking citation preservation checklist
5. Verify all mandatory citations appear in output

**Final Assembly:**
After all subsections are complete, assemble into `drafts/section3_FINAL.md`

**Output:** `drafts/section3/` (subsections) → `drafts/section3_FINAL.md` (assembled)

---

#### Task 4: Appendix A Creation

**Read First:**
- This system prompt
- `plans/section3_restructuring_analysis.md`
- Framework_draft.docx lines 533-612

**Actions:**
1. Extract detailed surrogate model literature from Section 3.2.3
2. Organize by model family (CNN, FNO, DeepONet, etc.)
3. Preserve all technical details and citations
4. Write in DOE report prose style

**Output:** `drafts/appendix_a_REVISED.md`

---

#### Task 5: Section 4 Renumbering + Style

**Read First:**
- This system prompt
- `drafts/section5_REVISED_v3.md`
- `drafts/section2_2_FINAL.md` (for workflow terminology)

**Actions:**
1. Change all 5.x references to 4.x
2. Update any cross-references to other sections
3. Verify workflow step references match Section 2.2
4. Convert to DOE report prose style if needed

**Output:** `drafts/section4_REVISED.md`

---

#### Task 6: Section 5 (Prototype & Case Study)

**Read First:**
- This system prompt
- `plans/master_document_layout.md` (Section 5 details)
- Framework_draft.docx lines 955-1384 (old Section 4)
- Framework_draft.docx lines 1245-1384 (old Section 6)
- All completed section drafts (for cross-references)

**Actions:**
1. Create introduction paragraph
2. Expand validation framework section
3. Merge prototype implementations from old Section 6
4. Add case study design section
5. Add expected outcomes section
6. Ensure workflow step references throughout
7. Write in DOE report prose style

**Output:** `drafts/section5_case_study_REVISED.md`

---

#### Task 7: Section 6 (Future Work & Summary)

**Read First:**
- This system prompt
- `plans/master_document_layout.md` (Section 6 details)
- Framework_draft.docx lines 1385-1415 (old Section 7)
- All completed section drafts (for summary references)

**Actions:**
1. Create research directions subsection
2. Create operational considerations subsection
3. Create summary subsection
4. Reference all three pillars and seven-step workflow
5. Maintain forward-looking tone
6. Write in DOE report prose style

**Output:** `drafts/section6_REVISED.md`

---

#### Task 8: Final Assembly

**Read First:**
- This system prompt
- All revised draft files
- `plans/master_document_layout.md`

**Actions:**
1. Assemble all sections in order
2. Verify cross-references are correct
3. Check terminology consistency
4. Ensure smooth transitions between sections
5. Generate table of contents

**Output:** `manuscript/Framework_RESTRUCTURED.md`

---

## 8. QUALITY CHECKLIST

Before completing any revision, verify:

### 8.1 Content Checklist
- [ ] All valuable information preserved
- [ ] No technical details lost
- [ ] Unused content archived in `drafts/unused_content.md`
- [ ] Cross-references to other sections are correct

### 8.2 Style Checklist
- [ ] Written in DOE report prose style
- [ ] Minimal bullet points (only where appropriate)
- [ ] Bold used sparingly (key terms on first use only)
- [ ] Third person voice throughout
- [ ] Professional, formal tone

### 8.3 Terminology Checklist
- [ ] Three pillars named correctly
- [ ] Seven workflow steps named correctly (MONITOR, DETECT, etc.)
- [ ] Phase 1/Phase 2 terminology used correctly
- [ ] "Pillars define WHAT; Workflow defines HOW" principle maintained

### 8.4 Structure Checklist
- [ ] Section numbers match new structure
- [ ] Subsection hierarchy is logical
- [ ] Tables have captions
- [ ] Figures have captions and are referenced in text

---

## 9. COMMON MISTAKES TO AVOID

1. **Converting prose to bullet points** - This is a report, not a technical spec
2. **Losing specific parameter values** - Keep all numbers (70-75%, batch size 6-10, etc.)
3. **Deleting governance content** - Regulatory alignment is critical for DOE
4. **Mixing pillar and workflow concepts** - Pillars are domains, workflow is process
5. **Using inconsistent terminology** - Always use the exact terms from Section 5.1
6. **Forgetting cross-references** - Link workflow steps to methods sections
7. **Over-formatting** - Avoid excessive bold, italics, or nested lists
8. **Ignoring the unused content archive** - Always save removed content

---

## 10. CONTACT AND UPDATES

This system prompt should be updated when:
- Document structure changes
- New style guidelines are established
- Terminology decisions are revised
- New reference files are created

---

## 11. CHANGE LOG

**⚠️ IMPORTANT:** Update this log after completing each task. This helps future sessions understand what has been done.

### Log Format
```
### [Date] - Task [N]: [Task Name]
**Status:** Completed / In Progress / Blocked
**Output File:** [filename]
**Changes Made:**
- [Brief description of changes]
**Notes:**
- [Any issues or decisions made]
```

### Change History

### 2026-10-07 - Task 10: Integrated seven-step lifecycle case-study rewrite
**Status:** Completed
**Output File:** `drafts/final/section5_FINAL.md`
**Changes Made:**
- Reorganized Section 5 as one connected pump-and-treat case-study narrative.
- Connected baseline monitoring, Mass90 stress detection, old/new decision screening, regime-selected preparation, update comparisons, calibration, and deployment gating.
- Added the quantitative transition trace and preserved figure-level results with explicit evidence boundaries.
**Notes:**
- The available evidence ends at a governed CALIBRATE/DEPLOY hold because adaptive-replay uncertainty and untouched final-test artifacts are not available.


### 2026-10-08 - Task 11: Final reader-facing copy edit and FNO removal
**Status:** Completed
**Output File:** `drafts/final/section5_FINAL.md`; `drafts/section5_yilin_results_update_draft.md`
**Changes Made:**
- Kept Section 5 centered on the pump-and-treat U-Net and removed FNO/internal-routing language from the case-study text.
- Clarified that the available evidence is an offline baseline/update evaluation, not prospective monitoring or completed deployment.
- Added UQ terminology, framework replay guidance of approximately 70–75%, and captions for the two quantitative tables.
- Preserved the illustrative status of the Figure 5 acceptance screen and the governed CALIBRATE/DEPLOY hold.
**Notes:**
- The working and final Section 5 files are byte-for-byte aligned and ready for copy into the report.


### 2026-10-08 - Task 12: Section 5 version freeze and legacy-content disposition
**Status:** Completed
**Output File:** `drafts/final/section5_FINAL_20261008_FROZEN.md`; `analyses/seven_step_lifecycle_20261007/section5_legacy_content_disposition.md`
**Changes Made:**
- Preserved the current U-Net lifecycle section as a dated frozen snapshot.
- Recorded which earlier Section 5 material remains relevant, belongs in framework/roadmap sections, or should stay archive-only.
- Established that future Section 5 edits must use a new dated file.
**Notes:**
- The earlier Section 5 files remain preserved; they should not be merged back wholesale into the quantitative U-Net case study.


### 2026-10-07 - Task 9: Seven-step lifecycle evidence audit and Section 5 update
**Status:** In Progress
**Output File:** `drafts/final/section5_FINAL.md`; `analyses/seven_step_lifecycle_20261007/`
**Changes Made:**
- Added a quantitative evidence-status table for MONITOR, DETECT, DECIDE, PREPARE, UPDATE, CALIBRATE, and DEPLOY.
- Integrated Yilin's manuscript-reported RMSE and adaptive-replay results while separating reported values from rounded-value calculations and framework criteria.
- Recorded the UQ, tipping-point-inspired diagnostics, persistence, active-learning, replay, efficiency, split, and deployment evidence requirements.
- Created a dated source manifest, evidence matrix, inconsistency register, analysis specification, and execution log.
**Notes:**
- Current evidence supports a controlled UPDATE demonstration and retrospective rare-regime stress case; complete CALIBRATE and DEPLOY claims remain blocked pending raw artifacts and governance records.
- The FY26 data-package discussion was excluded per project direction.


### 2025-03-19 - Task 1: Section 2.1 Style Conversion
**Status:** Completed
**Output File:** `drafts/section2_1_FINAL.md`
**Changes Made:**
- Converted bullet-point lists to flowing prose paragraphs
- Reduced bold formatting (key terms not bolded throughout)
- Added proper subsection numbering (2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5)
- Added figure caption for cross-reference diagram (Figure 2.1)
- Maintained all technical content and terminology
- Preserved ASCII diagram for pillar-workflow cross-reference
**Notes:**
- Original file preserved at `drafts/section2_1_pillars_REVISED.md`
- No content moved to unused archive (all content retained)

---

### 2025-03-19 - Task 2: Section 2.2 Style Conversion
**Status:** Completed
**Output File:** `drafts/section2_2_FINAL.md`
**Changes Made:**
- Converted all bullet-point lists to flowing prose paragraphs
- Reduced bold formatting significantly (key terms not bolded throughout)
- Added proper subsection numbering (2.2.1 through 2.2.6)
- Added figure captions (Figure 2.2 for state machine, Figure 2.3 for workflow)
- Added table caption (Table 2.1 for pillar cross-reference)
- Maintained all technical content, workflow steps, and terminology
- Preserved ASCII diagrams (state machine and workflow visualization)
- Preserved cross-reference table
**Notes:**
- Original file preserved at `drafts/section2_2_workflow_REVISED.md`
- No content moved to unused archive (all content retained)

---

### 2025-03-19 - Task 3: Section 3 Streamlining
**Status:** Completed
**Output File:** `drafts/section3_REVISED.md`
**Changes Made:**
- Added introduction paragraph referencing Appendix A for detailed surrogate literature
- Converted Section 3.1 (Governance Methods) to prose with 5 subsections (3.1.1-3.1.5)
- Converted Section 3.2 (Modeling Engine Methods) to prose with 4 subsections
- Streamlined Section 3.2.3 (Surrogate Model Landscape) from ~80 lines to ~20 lines
- Converted Section 3.3 (Recalibration Mechanism Methods) to prose with 6 subsections (3.3.1-3.3.6)
- All technical content preserved; detailed surrogate literature moved to Appendix A
**Notes:**
- Original content from Framework_draft.docx lines 405-954
- Surrogate model literature details (Web of Science methodology, detailed model family reviews, Figure 4 heatmap) moved to Appendix A

---

### 2025-03-19 - Task 4: Appendix A Creation
**Status:** Completed
**Output File:** `drafts/appendix_a_REVISED.md`
**Changes Made:**
- Created Appendix A with detailed surrogate model literature moved from Section 3.2.3
- Section A.1: Literature Review Methodology (Web of Science search approach)
- Section A.2: Detailed review of 6 surrogate model families (A.2.1-A.2.6)
- Section A.3: Literature Analysis Summary with Figure A.1 reference
- Section A.4: Implications for Framework Design
**Notes:**
- Content sourced from Framework_draft.docx Section 3.2.3 (lines 533-612)
- Cross-referenced with Section 3.2.3 in main document

---

### 2025-03-19 - Task 5: Section 4 Renumbering + Style
**Status:** Completed
**Output File:** `drafts/section4_REVISED.md`
**Changes Made:**
- Renumbered from Section 5 to Section 4 (all subsections 4.1-4.7)
- Converted bullet-point lists to flowing prose paragraphs
- Reduced bold formatting (removed bold from inline terms)
- Updated cross-references (Section 6 → Section 5 for case study references)
- Preserved Table 4.1 (Workflow Capabilities and Supporting Methods)
- Maintained all technical content and method references
**Notes:**
- Source file: `drafts/section5_REVISED_v3.md`
- All Section 3 method references preserved

---

### 2025-03-19 - Task 6: Section 5 (Prototype & Case Study)
**Status:** Completed
**Output File:** `drafts/section5_case_study_REVISED.md`
**Changes Made:**
- Created new Section 5 merging content from original Sections 4 and 6
- Section 5.1: Validation Framework with 5 subsections (metrics, thresholds)
- Section 5.2: Prototype Implementations (U-FNO, U-Net) with workflow integration
- Section 5.3: Case Study Design (scenario, data sources, recalibration demo)
- Section 5.4: Evaluation Plan (baseline comparison, effectiveness, efficiency)
- Section 5.5: Development Timeline (three phases aligned with Section 4.5)
- Section 5.6: Summary
- All content in DOE report prose style
**Notes:**
- Source content from Framework_draft.docx Sections 4 and 6
- New content added for validation framework and case study design
- Cross-references to Sections 2.2, 3, and 4.5

---

### 2025-03-19 - Task 7: Section 6 (Future Work & Summary)
**Status:** Completed
**Output File:** `drafts/section6_REVISED.md`
**Changes Made:**
- Created Section 6 with introduction and 4 main subsections
- Section 6.1: Research Roadmap (short-term, medium-term, long-term goals)
- Section 6.2: Expected Impact (scientific, operational, broader applications)
- Section 6.3: Limitations and Open Questions (limitations, research areas, governance)
- Section 6.4: Conclusion (framework contributions, key takeaways, path forward)
- All content in DOE report prose style
**Notes:**
- Source content from Framework_draft.docx lines 1387-1394 + new content
- Cross-references to three-pillar architecture and seven-step workflow

---

**Last Updated By:** Code Mode
**Date:** 2025-03-19
**Version:** 1.6

---

*END OF SYSTEM PROMPT*
