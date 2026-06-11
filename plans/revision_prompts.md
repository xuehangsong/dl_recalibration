# Revision Prompts — Step by Step
# ================================
# Save as: plans/revision_prompts.md
# Use these prompts IN ORDER, one per task/session
# Each task: agent writes MD → you review → next task
# Start every session with: "Read plans/design_decisions.md first"


================================================================
TASK 1: Read & Confirm Understanding
================================================================

Read the following files in this exact order:

1. `plans/design_decisions.md` — authoritative structural decisions
2. `manuscript/Framework_draft.docx` — the current main document
3. `plans/framework_alignment_analysis.md` — v1 analysis (read-only)
4. `plans/framework_alignment_analysis_v2.md` — v2 analysis (read-only)

After reading all files, write a brief summary to 
`drafts/understanding_check.md` confirming you understand:

- What the three pillars are (management domains, not workflow stages)
- What the revised 7-step, 2-phase workflow is
- The core principle (pillars = WHAT, workflow = HOW)
- How the workflow traverses the pillars (reference the diagrams)
- What needs to change in Sections 2 and 5
- What should NOT change (Section 3, original files)
- What was retained vs rejected from v1 and v2 analyses

Do NOT start writing revisions yet. Just confirm understanding.
Pause for my review.


================================================================
TASK 2: Revise Section 2.1 (Three Pillars)
================================================================

Read `plans/design_decisions.md` first.

Revise Section 2.1 (Three-Pillar Architecture). 
Save as `drafts/section2_1_pillars_REVISED.md`.

Requirements:
- Reframe pillars as "management domains"
- Pillar A manages rules & governance (design authority)
- Pillar B manages modeling engines (computational foundation)
- Pillar C manages adaptive methods (methods toolkit)
- Add paragraph explaining COMPLEMENTARY roles
- Include the core principle sentence: "The three pillars 
  define WHAT the framework manages; the recalibration workflow 
  defines HOW these elements interact."
- Emphasize: no pillar "owns" the workflow
- Include Diagram A (primary cross-reference diagram)
- Preserve all existing technical content and citations
- Keep same level of detail as original
- Write in academic/technical report style matching the document

Pause for my review before proceeding.


================================================================
TASK 3: Revise Section 2.2 (Workflow)
================================================================

Read `plans/design_decisions.md` first.
Also read `drafts/section2_1_pillars_REVISED.md` (approved v).

Revise Section 2.2 (Recalibration Workflow). 
Save as `drafts/section2_2_workflow_REVISED.md`.

Requirements:
- Replace old 7 steps with new 7 steps in 2 phases
- Phase 1: Continuous Monitoring (Steps 1-3: MONITOR, DETECT, DECIDE)
- Phase 2: Triggered Response (Steps 4-7: PREPARE, UPDATE, 
  CALIBRATE, DEPLOY)
- Step 3 (DECIDE) is NEW — emphasize human governance review
- For EACH step, explicitly note which pillar(s) it draws from
- Include Diagram B (phase-separated cross-reference diagram)
- Include the companion table (steps × pillars)
- Explain two update pathways:
  - Observation-driven (field data sufficient for Step 4)
  - Simulation-driven (active learning selects new physics runs)
- Include trigger state machine (OK → WARNING → UPDATE → ESCALATE)
- Write in academic/technical report style

Pause for my review before proceeding.


================================================================
TASK 4: Revise Section 5 (Implementation)
================================================================

Read these files first:
1. `plans/design_decisions.md`
2. `drafts/section2_1_pillars_REVISED.md` (approved)
3. `drafts/section2_2_workflow_REVISED.md` (approved)
4. `section5_Software_Architecture_REVISED.md` (current draft)

Completely rewrite Section 5. 
Save as `drafts/section5_REVISED_v2.md`.

Requirements:
- Organize by WORKFLOW PHASES (not by pillar, not by 5 components)
- Structure:
  5.1 Software Architecture Overview
      - Diagram: workflow steps mapped to software modules
      - Each module notes which pillar(s) it serves
      - Do NOT introduce "four layers" or new schemes
  5.2 Monitoring & Detection (supports Steps 1-3)
      - Performance tracking, UQ computation, drift detection
      - Decision support interface for governance review
  5.3 Model Update Pipeline (supports Steps 4-6)
      - Active learning sampler, physics model interface
      - Continual learning trainer, UQ calibration
  5.4 Deployment & Governance (supports Step 7)
      - Validation against acceptance criteria
      - Promotion to operations, audit logging, rollback
  5.5 Infrastructure & Development Phases
      - Data management and provenance
      - HPC integration, API design
      - Phase 1: Prototype → Phase 2: Integrated → Phase 3: Operational
- For each subsection, note which pillar(s) the software serves
- Preserve useful technical content from old Section 5
- Write in academic/technical report style

Pause for my review before proceeding.


================================================================
TASK 5: Consistency Check + Section 3 Light Touch
================================================================

Read `plans/design_decisions.md` first.
Then read ALL files in `drafts/` folder.

Part A — Section 3 Light Review:
- DO NOT restructure Section 3
- Check that pillar descriptions match revised Section 2.1 framing
- Check that workflow references match new 7-step, 2-phase workflow
- Note any minor terminology updates needed
- Save as `drafts/section3_consistency_notes.md`

Part B — Full Document Consistency Check:
- Are pillars described consistently across Sections 2, 3, and 5?
- Are workflow steps numbered and named consistently?
- Are cross-references correct?
- Does terminology match design_decisions.md?
- Are any figures/tables referenced that need updating?
- Save as `drafts/consistency_check.md`

Pause for my review before proceeding.


================================================================
TASK 6: Assemble & Convert
================================================================

Read `plans/design_decisions.md` first.
Then read ALL approved files in `drafts/` folder.

Step 1 — Assemble:
- Take `Framework_draft.docx` content as the base
- Replace Section 2.1 with approved `section2_1_pillars_REVISED.md`
- Replace Section 2.2 with approved `section2_2_workflow_REVISED.md`
- Replace Section 5 with approved `section5_REVISED_v2.md`
- Apply approved changes from `section3_consistency_notes.md`
- Apply fixes from `consistency_check.md`
- Keep ALL other sections unchanged
- Save as `Framework_REVISED_COMPLETE.md`

Step 2 — Convert to Word:
- Use pandoc if available:
  pandoc Framework_REVISED_COMPLETE.md -o Framework_REVISED_COMPLETE.docx
- If pandoc unavailable, note that user should convert manually
- DO NOT overwrite `Framework_draft.docx`

Step 3 — Final verification:
- Confirm all sections present
- Confirm no original content was lost
- Confirm all diagrams/tables included
- List any manual steps remaining (e.g., figure creation)

================================================================
END OF REVISION PROMPTS
================================================================