# Consolidated review decisions

**Draft:** Framework_revised_20261028.docx  
**Purpose:** finish the report with the evidence currently available. The draft does not require new experiments to remain scientifically bounded.

| Decision | Current treatment and recommendation | What would support a stronger statement |
|---|---|---|
| **1. Which dataset and physical time interval did the adaptive-replay study use?** | Use indexed states **t** and **t + 1**. The earlier report says days 0–4, while the saved Word revision says years 0–4. Neither is assigned to the adaptive-replay experiment without its execution record. Recommend retaining the indexed wording until confirmed. | The executed data-generation configuration, snapshot times/units, dataset version, grid spacing, and trajectory manifest. |
| **2. Can the manuscript's figure-specific comparisons be combined?** | Keep the manuscript Figure 3, Figure 4, and Figure 5 comparisons separate. Retain the illustrative 30%/85% screen and the explicit calibration/final-validation hold. Recommend accepting this bounded presentation unless the underlying protocols can be reconciled. | Executed model configurations (including Model C), evaluation partitions, metric denominators, controller logs, seeds, predictions, checkpoints, and any independent calibration/final-test records. |
| **3. Is the descriptive literature treatment acceptable?** | Use 45 retained curated entries and charts computed directly from that table. Exclude two ambiguously mapped rows; replace the unauditable field-wide publication-count plot with the publication years of the curated entries. Recommend this reproducible treatment. | Exact identities for the inherited Yang 2018 generative entry and Chen 2022 monitoring entry, plus the original Web of Science export/query record if broader publication-count claims are to be restored. |

The three pillars, seven steps, and existing withdrawal/full-retraining governance policy are retained. No new operational acceptance policy has been approved by this revision. Final report number, release date, author list, and internal-manuscript attribution remain part of the normal author/publication review; the cover identifies this file as a revision draft.

## Recommended review route

1. Read the Summary and Section 6.4 to confirm the overall scientific message.
2. Review Section 5, especially the separate controller and RMSE comparisons and the CALIBRATE/DEPLOY hold.
3. Answer the three decisions above in one response. Use the tracked comparison for details of the supporting edits.

## Scope of the next research increment

The longer-term operational demonstration requires prospective detector evaluation, verified independent data partitions, a matched fixed-replay control, independent uncertainty calibration, an untouched final test, and a versioned promotion decision. These are research requirements, not unfilled prose placeholders in the revised report.
