# Numerical and figure-provenance audit — v3

Audited 2026-10-29 against the original `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx` (SHA-256 `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`). No deck edits were made by this audit.

**Result:** all 28 plotted scalar outcome values in v3—8 RMSE values, 12 physical-error values, and 8 controller percentages—match the printed labels in Yilin's original Figures 4 and 5. The current plots use Yilin's reported values, not newly simulated or fitted data. The spatial triplet is an original-pixel crop from Figure 2(b). Calculated percentage changes and screening margins also check out. The current deck has no identified wrong numerical outcome.

This verifies transcription, arithmetic, labels, and figure provenance. It does not reproduce the experiment from raw predictions, verify simulation counts against an archive, establish trajectory independence, or supply missing replicate uncertainty.

## Audit artifacts

- `numeric_value_ledger.csv`: 75 unique-value/provenance groups covering outcomes, setup values, definitions, margins, source colorbars, and presentation-only axis settings. Repeated values are mapped to all relevant slide locations rather than counted repeatedly.
- `numeric_provenance_checks.json`: source-media byte identities, outcome/arithmetic checks, PPTX notes/spec agreement, and figure-image byte identities.
- `rounding_interval_check.json`: Decimal arithmetic showing that the Figure 4 versus Figure 5 discrepancy cannot be explained solely by two-decimal RMSE rounding.

All five extracted source PNGs were compared byte-for-byte with `word/media/image1.png` through `image5.png` inside the source DOCX. All matched. The four figure images embedded in the delivered PPTX match their generated/cropped PNG files byte-for-byte. All nine PPTX notes match `deck_spec.json`.

## Source-to-slide inventory

| Slide | Numerical/evidence content | Exact origin | Audit result |
|---|---|---|---|
| 1 | Seven lifecycle steps and evidence classification | Revised report; manuscript discussion P0168–P0170 for broader managed updating | Synthesized editable diagram, not an experimental figure. No outcome numbers. |
| 2 | 128 × 100 mesh; 1–5 wells; 10,000 simulation runs | Manuscript P0016 | Literal manuscript-reported setup; raw counts not independently reproduced. |
| 2 | Historical bottom 40%; rare top 3%; cutoffs 0.133 and 0.329 | P0022; original Figure 1 legend (40th and 97th percentile) | Exact source labels. Inequalities on the slide are schematic at rounded cutoffs, not executable sample-selection code. |
| 2 | 90% mass definition; t and t+1; middle 57% | P0020–P0021; 100−40−3 | Definition/indices are sourced. 57% is a calculated complement, not a documented sample allocation. |
| 3 | Rare concentration scale 0–813.6 µg/L; signed residual scale ±169.4 µg/L | Original Figure 2(b), crop box (950,600,1893,1259) | Original axes, colorbars, pixels, and aspect retained. Source error sign is prediction minus reference. |
| 4 | Four historical/rare RMSE pairs | Original Figure 4(a); P0146–P0150 | All eight values exact. Absolute-RMSE scatter is a new presentation of printed values; it is not original Figure 4(b)'s percentage scatter. |
| 4 | Fixed-replay 77.6% historical increase and 87.9% rare reduction | Calculations from Figure 4(a) rounded labels | Correct arithmetic; not substituted for Figure 5 values. |
| 4 notes | Figure 3 full-network 0.64/0.99 µg/L | Original Figure 3(c) | Correct labels; deliberately excluded from ranking because Model C/protocol identity is unresolved. |
| 5 | Rare mass, peak, and Mass90 errors for four methods | Original Figure 4(a) printed bar labels | All 12 values exact. Replotted as aligned dots with separately labeled axes. |
| 6 | r historical fraction, 1−r rare fraction; forgetting relative to baseline | Eq. 1/P0063–P0066; Eq. 3/P0077–P0081 | Native diagram correctly distinguishes training mix and validation feedback; final testing stays outside the loop. |
| 6 | r=0.8 cap for most of 100 plotted epochs | Original Figure 5(a), blue curve and x-axis; P0152 | Source-supported visual statement. No trajectory reconstruction or exact cap-reaching epoch claimed. |
| 7 | Four controller historical-increase/rare-reduction pairs | Original Figure 5(b) printed labels; Figure 5(c) point positions | All eight values exact. Names are expanded for readability; no controller values change. |
| 7 | 30%/85% region; two passing outcomes; 3.5/8.9 and 0.8/0.5 point margins | Figure 5(c), P0153–P0154; arithmetic from Figure 5(b) | Correct conditional classification and margins. Thresholds remain illustrative. |
| 7 notes | 5%/20% Methods example and 25% Figure 3 tolerance | P0126 (1.05×/0.80×); Figure 3(b) and P0142–P0144 | Correct interpretation; inconsistency with Figure 5 is explicitly flagged. |
| 8 | Two candidates and missing calibration/final-test roles | Figure 5 classification; Table 2/P0111–P0116; report Sections 5.7–5.9 | Two is calculated under the illustrative screen. Required roles do not assert verified independent partitions. |
| 9 | Proposed fixed replay r=0.8 | Report next-test proposal motivated by Figure 5(a) | Planning value, not a completed control result. |

## Direct numerical comparisons

Figure 4(a), units µg/L for RMSE and reported % for physical errors:

| Configuration | Historical RMSE | Rare RMSE | Rare mass error | Rare peak error | Rare Mass90 error |
|---|---:|---:|---:|---:|---:|
| Baseline | 0.58 | 10.04 | 32.30 | 14.20 | 7.11 |
| Simple fine-tuning | 1.11 | 3.92 | 9.86 | 7.70 | 3.59 |
| Fixed replay | 1.03 | 1.21 | 1.82 | 3.43 | 1.89 |
| EWC | 5.45 | 1.22 | 1.88 | 3.40 | 1.64 |

Figure 5(b), coordinates used in the user's screenshot and v3 slide 7:

| Controller | Historical RMSE increase (%) | Rare RMSE reduction (%) | Historical margin to 30 (points) | Rare margin above 85 (points) | Screen |
|---|---:|---:|---:|---:|---|
| Fixed replay | 80.4 | 88.9 | −50.4 | 3.9 | Fails historical limit |
| Threshold adaptive forgetting | 26.5 | 85.8 | 3.5 | 0.8 | Passes |
| Loss-balanced | 21.1 | 85.5 | 8.9 | 0.5 | Passes |
| Loss-balanced + floor | 38.1 | 87.3 | −8.1 | 2.3 | Fails historical limit |

For slide 7, colors, marker shapes, annotation positions, and displayed axis range were redesigned. Yilin's Figure 5(c) uses an x-axis tick range 0–100 and y-axis tick range 80–100; v3 uses 0–90 and 80–90 to enlarge the region containing all four points. The boundary values, shading direction, data coordinates, and classifications are unchanged. Labeling the footer **“Replotted from Yilin manuscript Fig. 5(b,c)”** would make this provenance clearer without changing the attractive plot.

## Reconciliation findings

1. **Figure 4 and Figure 5 cannot be silently treated as one experiment.** Figure 4 fixed replay implies (1.03/0.58−1)×100 = 77.5862% historical increase and (1−1.21/10.04)×100 = 87.9482% rare reduction. Figure 5 reports 80.4% and 88.9%. Under nearest-0.01 rounding of Figure 4 inputs, possible historical increase is about 75.2137–80.0000%, and possible rare reduction is about 87.8924–88.0040%. Thus rounding alone cannot produce Figure 5's pair. Raw panel-specific denominators/protocols are needed. V3 already keeps them separate.

2. **Trainable capacity differs in the source comparison.** Table 1 lists last decoder/output layers for simple fine-tuning (P0042), but full-network updating for fixed replay/EWC/adaptive (P0047/P0052/P0057). V3 correctly calls these configuration results and includes the caveat. It should not claim that replay alone caused every difference.

3. **The source's historical physical-metric panel has a caption conflict.** Figure 4(a) labels it historical peak error, whereas P0149 calls it historical Mass90 error. V3 excludes that column; retain the exclusion pending source clarification.

4. **Figure 3 has separate/unresolved comparisons.** Panel 3(a) prints 0.49/9.20 before and 0.67/1.20 after, unlike Figure 4's baseline. Panel 3(c) prints a full-network Model C pair 0.64/0.99. V3 does not combine these with Figure 4. This is appropriate until model and evaluation identities are established.

5. **Acceptance criteria are inconsistent in the manuscript.** Methods P0126 uses historical ≤1.05×baseline and rare ≤0.80×baseline (5% degradation/20% improvement), Figure 3 uses 25% historical tolerance, and Figure 5 uses 30%/85%. The present screening plot accurately uses Figure 5, not a single preregistered acceptance contract.

6. **One historical analysis-table error exists outside the current deck.** `analyses/seven_step_lifecycle_20261007/derived/reported_value_calculations.csv`, row DC-01, calculates (10.04−0.58)/10.04 = 94.2231% but describes it as “Rare-regime RMSE is 94.2% higher than historical baseline.” That description has the wrong denominator/direction. Correct statements are **rare RMSE is 17.3103 times historical RMSE**, or **1631.0345% higher**, or **historical RMSE is 94.2231% lower than rare RMSE**. This erroneous sentence is not used in v3. Preserve the historical record and issue an explicit correction rather than silently relying on it.

## Recommendation

Keep the current result plots: they already use Yilin's exact reported figure labels and improve legibility. Make their footers explicit about **replotting from reported labels**, and include original Figure 4(a) and Figure 5(b,c) as source/reference panels or an accompanying source sheet. Original figures can be used directly for spatial fields/distributions where raw values are unavailable. Do not describe the transcribed CSVs as Yilin's raw experiment files.

Retain the current split between measured reported outcomes, arithmetic derived from rounded labels, conceptual diagrams, and planned validation. The remaining accuracy limitation is the unavailable experiment-level provenance, not a discovered error in the current plotted numbers.
