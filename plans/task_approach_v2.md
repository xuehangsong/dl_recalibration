# Revised Task Approach v2: Context-Aware Document Revision

## Problem Statement

The previous revision approach failed because:
1. **Lost all citations** - 50+ inline citations stripped out
2. **Lost specific technical values** - "70-75% replay buffer", "batch size 6-10", regulatory codes
3. **Content became generic** - No research foundation, reads like textbook not DOE report
4. **No task-specific guidance** - Single large prompt couldn't preserve details

## Design Principles for New Approach

### 1. Context Window Management
- **Small, focused tasks** - One subsection at a time (e.g., 3.3.1 not all of 3.3)
- **Pre-extracted critical content** - Citations and values in separate files loaded per task
- **Minimal prompt overhead** - Task file contains only what's needed

### 2. High-Fidelity Content Preservation
- **Citation extraction files** - All citations pre-extracted with context
- **Value extraction files** - All specific numbers, thresholds, regulatory codes
- **Mandatory preservation rules** - Checklist before completion

### 3. Structure Preservation
- **Keep existing design decisions** - `plans/design_decisions.md` remains authoritative
- **Keep section structure** - From `plans/master_document_layout.md`
- **Style conversion only** - Don't rewrite content, convert format

---

## New File Structure

```
plans/
├── REVISION_SYSTEM_PROMPT.md      # Master reference (simplified)
├── task_approach_v2.md            # This file
├── design_decisions.md            # Keep as-is
├── master_document_layout.md      # Keep as-is
│
├── tasks/                         # NEW: Task-specific requirement files
│   ├── task_3.1_governance.md
│   ├── task_3.2.1_site_challenges.md
│   ├── task_3.2.2_physics_models.md
│   ├── task_3.2.3_surrogate_landscape.md
│   ├── task_3.3.1_uq.md
│   ├── task_3.3.2_trigger_logic.md
│   ├── task_3.3.3_continual_learning.md
│   ├── task_3.3.4_active_learning.md
│   ├── task_3.3.5_multifidelity.md
│   ├── task_3.3.6_full_retrain.md
│   └── ...
│
├── extracts/                      # NEW: Pre-extracted critical content
│   ├── citations_section3.md      # All citations from Section 3
│   ├── values_section3.md         # All specific values from Section 3
│   ├── citations_section5.md
│   └── ...

drafts/
├── section3/                      # NEW: Subsection drafts
│   ├── 3.1_governance_REVISED.md
│   ├── 3.2.1_site_challenges_REVISED.md
│   ├── 3.2.2_physics_models_REVISED.md
│   ├── 3.2.3_surrogate_landscape_REVISED.md
│   ├── 3.3.1_uq_REVISED.md
│   └── ...
├── section3_FINAL.md              # Assembled from subsections
```

---

## Task File Template

Each task file follows this structure:

```markdown
# Task: Revise Section X.Y.Z - [Title]

## Source
- **File:** manuscript/Framework_draft.docx
- **Lines:** [start]-[end]
- **Word count:** ~[N] words

## Output
- **File:** drafts/sectionX/X.Y.Z_[name]_REVISED.md
- **Target length:** ~[N] lines

## Required Reading (Load These Files)
1. `plans/extracts/citations_sectionX.md` (citations to preserve)
2. `plans/extracts/values_sectionX.md` (values to preserve)
3. `plans/design_decisions.md` Section [N] (structure guidance)

## Style Requirements
- Convert bullet points to prose paragraphs
- Reduce bold formatting (key terms first use only)
- Maintain third person voice
- Keep all technical specificity

## MANDATORY: Content to Preserve
### Citations (must appear in output)
- (Author et al., Year) - context
- ...

### Specific Values (must appear in output)
- "70-75% replay buffer"
- "batch size 6-10"
- ...

### Regulatory References (must appear in output)
- DOE O 414.1D
- ...

## Completion Checklist
- [ ] All citations from list preserved
- [ ] All specific values preserved
- [ ] All regulatory references preserved
- [ ] Converted to prose style
- [ ] Section numbers correct
- [ ] Cross-references updated
```

---

## Workflow Per Task

1. **Load task file** - Contains everything needed for that subsection
2. **Load extract files** - Citations and values to preserve
3. **Load source content** - Only the specific lines needed
4. **Revise** - Style conversion while preserving all content
5. **Verify** - Check all items in preservation lists appear in output
6. **Save** - To subsection draft file

---

## Section 3 Breakdown (Example)

| Task ID | Subsection | Source Lines | Est. Length | Priority |
|---------|------------|--------------|-------------|----------|
| 3.1 | Governance Methods | 409-504 | ~95 lines | High |
| 3.2.1 | Site Challenges | 509-519 | ~10 lines | Medium |
| 3.2.2 | Physics-Based Models | 521-531 | ~10 lines | Medium |
| 3.2.3 | Surrogate Landscape | 533-612 | ~80 lines | High |
| 3.2.4 | Training Setup | 615-626 | ~12 lines | Low |
| 3.3.1 | UQ Methods | 639-680 | ~40 lines | High |
| 3.3.2 | Trigger Logic | 683-826 | ~140 lines | High |
| 3.3.3 | Continual Learning | 827-858 | ~30 lines | High |
| 3.3.4 | Active Learning | 861-889 | ~30 lines | High |
| 3.3.5 | Multi-fidelity | 891-924 | ~35 lines | High |
| 3.3.6 | Full Retrain | 925-954 | ~30 lines | Medium |

---

## Benefits of This Approach

1. **Context window efficient** - Load only what's needed per task
2. **Citation preservation guaranteed** - Explicit checklist per task
3. **Parallelizable** - Different subsections can be done independently
4. **Verifiable** - Clear success criteria per task
5. **Recoverable** - If one task fails, others unaffected
6. **Maintains structure** - Design decisions preserved in separate file

---

## Next Steps

1. Create `plans/extracts/citations_section3.md` - Extract all citations from Section 3
2. Create `plans/extracts/values_section3.md` - Extract all specific values
3. Create task files for each Section 3 subsection
4. Update REVISION_SYSTEM_PROMPT.md to reference new approach
5. Execute tasks one by one
