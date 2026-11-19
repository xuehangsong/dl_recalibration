# History, factual scope, and source-lineage audit

Audit date: 2026-10-29. Scope: the nine current v3 slide titles, captions, diagram labels, speaker notes, and source references, checked against the original manuscript, the revised report, the frozen Section 5, the earlier plan, and available Git history. This is a source/claim audit, not reproduction of model training or predictions. No deck files were edited in this audit.

## Finding

The current deck preserves the defensible history: a planned complete lifecycle now has an existing, controlled offline update study mapped onto it. The updated report does not represent new model runs, a completed prospective detector, an independently calibrated uncertainty model, or an operational deployment. No current numerical claim was found to have been imported from the old prototype's time axis, split, speedup, or active-learning targets.

Three provenance improvements are recommended, and one incorrect sentence was found in an older calculation ledger that is **not used by the current deck**. These are listed below. The numerical/source-image audit should remain the authority for direct visual transcription of Figure 1/2/4/5 labels; this audit checks their lineage and interpretation.

## Verified source identity and history

| Source | Verified identity and role | Boundary |
|---|---|---|
| `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx` | Internal manuscript titled *Adaptive Replay for U-Net Groundwater Plume Surrogates: Learning Rare Pump-and-Treat Dynamics Without Forgetting*. SHA-256 `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`. This exactly matches the manuscript hash in the October 7 analysis manifest and the v3 input manifest. | The filename labels the version `2026_09_09`; it does not independently establish a September 9 author revision date. DOCX core properties list creator/last modifier `Fang, Yilin`, created June 1, 2026, modified July 30, 2026, revision 475. These metadata can be stale. Do not call this a published paper or the latest author-approved version. |
| Accepted-view extraction in `sources/manuscript_accepted_full.txt` | Extracts the original file with insertions retained and deleted/moved-from text excluded; includes equations, tables, captions, and 205 paragraph anchors. The original DOCX contains 170 insertion and 46 deletion elements. | “Accepted view” describes extraction semantics, not evidence that a human approved all tracked edits. Cite the file/version and extraction view explicitly in provenance. |
| `plans/handoffs/trigger_uq_prototype_workflow_handoff.md` | Dated June 11, 2026 and present in Git commit `8496417` (“Add handoff for prototype trigger evaluation criteria”). Current SHA-256 `08f3d0a2ae47752f5d166681ab25be737be8373cbb923caba330cf2913fc9026`. Specifies controlled pumping change, detector evidence, active learning, update/retention, UQ, and governance. | These are planned evaluation categories and criteria, not completed results. |
| `drafts/final/section5_FINAL.md` at Git commit `29bf982` | June 12, 2026 committed prototype plan. Sections 5.1 and 5.3 explicitly propose one full cycle, a known pumping-regime change, detector evaluation, uncertainty calibration, and documented deployment review. | The current working file is modified; use the Git object when describing the earlier plan. Its heterogeneous generic scenario, 70/15/15 split, 1 m grid spacing, days 0–4, and expected efficiencies cannot establish the executed adaptive-replay protocol. |
| `analyses/seven_step_lifecycle_20261007/` | Existing October 7 evidence extraction, figure transcriptions, derived arithmetic, and missing-evidence specification. Its manuscript hash matches the current primary source. | It records analysis of reported values, not new experiments or independently reproduced predictions. Some old ledger wording/anchors are stale; see findings below. |
| `drafts/final/section5_FINAL_20261008_FROZEN.md` | SHA-256 `ea4075935fced71a3abc39954f4de15fde04cbb3803537edaad40ac793aba563`, matching v3's frozen-source assertion. | A frozen intermediate report reconstruction, not an independent experimental source. It remains unchanged. |
| `deliverables/report_revision_20261028/Framework_revised_20261028.docx` | SHA-256 `e4d9caf8b3d306b0d8f5278852bbdb53905f401e6fe952f02dce6aaaa184e8e1`. Clean revised report titled *Maintaining Deep-Learning Surrogate Accuracy for Long-Term Groundwater Remediation: Framework and Controlled Update Evidence*. No insertion/deletion elements. Section 5 working source is `section5_20261028.md`. | This report synthesizes the manuscript into lifecycle decisions; it is a secondary source for the experimental values. Its “hold” is the report's evidence assessment, not a record of operational model withdrawal. |

Available Git history establishes the June plan but does not version the manuscript, analysis package, frozen October snapshot, or deliverables: those are currently untracked in this working tree. File hashes establish their inspected identities. Do not present a Git commit as provenance for those uncommitted artifacts.

## Current slide claim check

| Slide | Source/claim check | Result |
|---|---|---|
| 1 — planned cycle to controlled update | The June handoff and committed June prototype plan support the stated original intent. Revised report §5.9 maps the available evidence. Baseline aggregates, retrospective Mass90 selection, an illustrative screen, selected cases/replay, and update comparisons are correctly distinguished from completed lifecycle operations. | Supported. Add the dated original-plan citation to notes for direct history traceability. |
| 2 — rare-change case study | Manuscript P0014–P0024 supplies the analytical preprocessing, 128 × 100 mesh, 1–5 extraction wells, nominal 10,000 physics runs, response-based partition, and 90%-mass footprint definition. Figure 1 supplies cutoff labels. The study says uniform porosity and hydraulic conductivity, so it is a homogeneous synthetic case. | Supported. The deck correctly avoids importing days/years, trajectory counts, 70/15/15, field or heterogeneous validation, or an observed pumping-change cause. Adding “homogeneous synthetic” to notes would sharpen scope. |
| 3 — baseline spatial example | Manuscript P0137–P0140 and Figure 2 identify a static-baseline rare-regime example with full-order reference. Error localization is reported around plume body, gradients, and boundaries. The crop remains an example rather than a distributional or post-update result. | Supported. No claim of a reproduced spatial field, sample identity, or universal failure mechanism. |
| 4 — recovery/retention tradeoff | Figure 4 is one configuration comparison. Table 1 P0042/P0047/P0052 differs in trainable layers; the deck explicitly states this. Derived 77.6%/87.9% use the Figure 4 baseline and remain separate from Figure 5. | Supported. The 0.64/0.99 Figure 3 pair is correctly excluded because Model C/protocol identity is unresolved. |
| 5 — rare physical metrics | The three metrics come from the same Figure 4 comparison and are not operational remedy outcomes. P0124 defines Mass90 as a cell count containing 90% of mass. Center-of-mass and exceedance-area quantities appear in Methods but have no displayed numerical results used here. | Supported. No spatial-overlap, translation, compliance-well, uncertainty, or mass-removal-performance claim is inferred from these percentages. |
| 6 — replay mechanism | P0063–P0066 gives `B_update = r B_old + (1−r) B_new`. P0077–P0081 uses historical validation forgetting and the stricter decrease condition (below lower tolerance **and** rare validation loss improving). P0111–P0116 separates validation feedback from final testing. P0093's loss-balanced equation is incomplete. | Supported. Diagram is conceptual and gives historical share `r`, rare share `1−r`; final test does not feed the controller. A capped trajectory does not identify causal scheduling benefit. |
| 7 — controller screen | Figure 5's four points are a separate reported comparison. P0153–P0154 labels 30% and 85% as examples. P0126 instead uses 5% and 20%; Figure 3 uses 25%. The deck makes this inconsistency explicit and treats the two passing variants as candidates. | Supported. No approved contract, blanket adaptive-replay pass, significance, or robustness claim. |
| 8 — missing calibration/final validation | Revised report §§5.7–5.9 and manuscript Table 2 support distinct validation/calibration/final-test roles. The manuscript describes test evaluation but does not supply an executed split manifest, prediction interval evidence, checkpoints, or a promotion record. | Supported with wording refinement recommended below: absence from the reviewed package is stronger evidence than an assertion of nonexistence everywhere. |
| 9 — next demonstration | The original plan supports known-change detection and a full governed cycle. The matched `r = 0.8` control is a later inference documented in the frozen October Section 5 and revised report §5.6, motivated by Figure 5's cap; it is not a June planned comparator or an executed control. | Supported. The slide explicitly labels the experiment planned and does not claim cost/speedup or active-learning gains. |

## Findings and recommended actions

### H1 — make manuscript version wording exact (provenance improvement)

Current slide footers say “Manuscript,” which is not false, but readers cannot identify the file without the package. Recommended full source line in the notes/README: “Yilin Fang, internal manuscript file `Adaptive_Replay_Manuscript_2026_09_09.docx` (filename version label; accepted-view extraction; SHA-256 in `sources/input_sha256.json`).” Use the manuscript title when a formal source name is needed. Do not infer publication, author approval of inserted text, or the latest revision date from the filename or DOCX core properties.

### H2 — scope missing-evidence statements to the reviewed package (minor wording refinement)

Slide 8 currently says “There are no predictive intervals ... untouched final-test record ... for these outcomes.” The surrounding context makes the intended evidence boundary clear, but a more exact statement is: “The reviewed manuscript and report package provide no predictive intervals, calibrated coverage/width results, independent calibration parameters, untouched final-test record, checkpoint identity, or versioned promotion decision for these outcomes.” Manuscript P0123 and Table 2 explicitly discuss test sets; the missing item is independently auditable test provenance and an untouched promotion evaluation, not evidence that no testing was performed.

### H3 — cite the specific historical plan (minor traceability improvement)

Slides 1 and 9 refer to the “original plan”/“original trigger/UQ plan.” Add the exact June 11 handoff filename and date in their notes. Cite `29bf982:drafts/final/section5_FINAL.md` for the earlier detailed demonstration objectives when documenting history. The matched fixed-0.8 control should continue to be sourced to the October analysis/revision, not attributed to the June handoff.

### H4 — old calculation-ledger sentence is wrong; current deck is unaffected (source-package defect)

`analyses/seven_step_lifecycle_20261007/derived/reported_value_calculations.csv`, row `DC-01`, uses `(10.04−0.58)/10.04 = 94.2231%` but describes it as “Rare-regime RMSE is 94.2% higher than historical baseline.” That interpretation uses the wrong reference denominator. Correct alternatives are:

- Historical RMSE is 94.2% lower than rare-regime RMSE.
- Rare-regime RMSE is `10.04 / 0.58 = 17.31` times historical RMSE.
- Rare-regime RMSE is `(10.04−0.58)/0.58 × 100 = 1631.0%` higher than historical RMSE.

The revised report uses the correct approximately 17.3-times statement. The current v3 deck does not use the incorrect 94.2%-higher claim or load this calculation ledger. Correct the ledger before future reuse; do not reinterpret its number as a model-update effect.

### H5 — use fresh anchors instead of older extraction-line anchors (traceability note)

`source_extracts/yilin_reported_results.csv` refers to earlier extraction line numbers and sometimes §2.1 for dataset details that are §2.2 in the accepted-view manuscript. It also says cap value requires verification, which has been superseded by inspection of Figure 5. The fresh P anchors and original embedded figures are the direct sources for v3. The `historical_peak_error` header in the old Figure 4 CSV remains semantically ambiguous against the manuscript's historical Mass90 caption; v3 correctly excludes that column. Do not silently treat it as a resolved metric.

## Existing caveats that remain necessary

- Figure 4 and Figure 5 percentage pairs are not interchangeable. Manuscript labels, panel-specific denominators, splits, and executed configurations still require reconciliation.
- The Figure 4 comparison changes update capacity as well as replay/regularization; it cannot isolate replay as the sole cause of all differences.
- The response partition requires the next reference field and does not establish prospective detection, causal operational drivers, or detector operating characteristics.
- Nominal simulation count and percentile definitions do not establish independent trajectory counts or exact selected sample counts.
- Original prototype days 0–4 and partially assembled-report years 0–4 are incompatible; indexed states are the defensible current presentation.
- Source aggregate labels provide no replicate distributions, seeds, or inferential uncertainty. Visually close EWC/replay metrics do not establish statistical equivalence.
- A reported ratio reaching 0.8 does not verify actual sampled exposure or show that adaptive scheduling beats an exposure-matched constant control.
- Calibration and deployment diagrams show required roles. They do not certify that independent partitions or operational promotion artifacts exist.
- The report's “hold” is the result of this evidence reconstruction. No operational withdrawal/rollback is claimed.

## Read-only verification performed

- Read all nine current slide claims/captions/notes in `scripts/build_deck.py` and `speaker_notes.md`, plus every native diagram label in `scripts/native_diagrams.py`.
- Cross-checked direct manuscript paragraph/equation/table/caption anchors, the revised Section 5, the frozen Section 5, the June handoff, and committed June prototype text.
- Verified primary manuscript, revised report, frozen snapshot, and handoff SHA-256 values against v3's recorded input manifest.
- Inspected DOCX core properties and revision-element counts to distinguish version labeling from approval/publication status.
- Inspected current Git status and relevant path history; no source or deck edits were made.
