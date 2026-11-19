# Source, number, and interpretation audit

**Result:** all **28 plotted outcome values** match Yilin's original manuscript figure labels. The current charts require no numerical correction. V4 preserves the plots and editable flowcharts, strengthens source attribution, and supplies all five original manuscript figures in a separate source companion.

This audit verifies source identity, transcription, arithmetic, axis/label interpretation, and the report-to-slide history. It does **not** independently reproduce model accuracy from simulation outputs. The inspected local evidence package does not contain the adaptive-replay raw predictions, executed configurations, seeds, trajectory manifest, or original metric/figure-generation code.

## The plot in your screenshot

The eight point coordinates come from the printed labels in **Yilin's Figure 5(b)**. The two decision boundaries and shading direction come from **Figure 5(c)**. None of the values were inferred from Figure 4 or fitted to the visual positions.

| Controller | Historical RMSE increase (%) | Rare RMSE reduction (%) | Meets the Figure 5 screen? |
|---|---:|---:|---|
| Fixed replay | 80.4 | 88.9 | No: historical increase exceeds 30% |
| Threshold adaptive forgetting | 26.5 | 85.8 | Yes |
| Loss-balanced | 21.1 | 85.5 | Yes |
| Loss-balanced + floor | 38.1 | 87.3 | No: historical increase exceeds 30% |

The redesigned chart changes colors, symbols, annotation placement, and the displayed axis range to x=0–90%, y=80–90%. It retains the exact values and the illustrative historical ≤30%, rare ≥85% screen. “Historical degradation” is labeled “Historical RMSE increase”; “rare improvement” is labeled “Rare RMSE reduction,” consistent with the manuscript's metric interpretation. Passing margins of 0.8 and 0.5 are **percentage points**, not percentage reductions.

## The other numerical results

All these values come from **Figure 4(a)**. RMSE units are µg/L; the last three columns are reported percentages.

| Configuration | Historical RMSE | Rare RMSE | Rare mass error | Rare peak error | Rare Mass90 error |
|---|---:|---:|---:|---:|---:|
| Baseline | 0.58 | 10.04 | 32.30 | 14.20 | 7.11 |
| Simple fine-tuning | 1.11 | 3.92 | 9.86 | 7.70 | 3.59 |
| Fixed replay | 1.03 | 1.21 | 1.82 | 3.43 | 1.89 |
| EWC | 5.45 | 1.22 | 1.88 | 3.40 | 1.64 |

The Figure 4 historical/rare RMSE scatter is our re-expression of these absolute values, not a reproduction of Figure 4(b)'s percentage axes. The physical-error dots reproduce the same Figure 4(a) labels. The source tables in `sources/` are transcriptions of displayed labels, not Yilin's raw experimental tables.

The fixed-replay changes stated in the notes are correctly calculated from Figure 4: `(1.03/0.58 − 1) × 100 = 77.5862%` historical increase; `(1 − 1.21/10.04) × 100 = 87.9482%` rare reduction. Rounding to one decimal yields 77.6% and 87.9%.

## Figure provenance

| Main slide | Where the visual/data originate | What was changed |
|---|---|---|
| 1 | Revised report lifecycle and evidence mapping; June plan | Native editable diagram; no experimental data |
| 2 | Manuscript §2.2, Figure 1, Eq. 1 | Native model/stress-selection diagram using reported 40%/3%, 0.133/0.329 |
| 3 | Original Figure 2(b), rare triplet | Crop only; original pixels, colorbars, labels, and aspect retained |
| 4 | Figure 4(a), eight RMSE labels | Absolute historical-versus-rare scatter; no data changed |
| 5 | Figure 4(a), twelve rare physical-error labels | Three aligned dot panels; no data changed |
| 6 | Eq. 1, controller methods, Table 2 | Native conceptual feedback loop; r is historical batch share, 1−r rare share |
| 7 | Figure 5(b) labels and Figure 5(c) boundaries | Restyled scatter shown in the screenshot; no data changed |
| 8 | Revised report §§5.7–5.9 | Native diagram of remaining evidence requirements |
| 9 | Original trigger/UQ plan plus October review | Planned experiment; fixed-r=0.8 is a proposed control |

Original Figures 1–5 are included **unaltered** in `Yilin_original_figures_20261029.pptx/.pdf` and as byte-identical PNGs under `sources/original_figures/`. The original source titles and plotting conventions are preserved there for inspection. The main presentation keeps the simpler style.

## Issues found and how they are handled

1. **One old percentage interpretation was wrong.** The October 7 ledger DC-01 calls rare RMSE “94.2% higher” while dividing by rare RMSE. The correct statement is rare RMSE is **17.31× historical RMSE**, or **1631.0% higher**; alternatively, historical RMSE is **94.2% lower than rare RMSE**. Neither v3 nor the revised report uses that incorrect sentence. `analyses/seven_step_lifecycle_20261007/ERRATA_20261029.md` records the correction while preserving the archive.

2. **Figure 4 and Figure 5 have unreconciled fixed-replay values.** Figure 4 yields 77.6%/87.9%; Figure 5 prints 80.4%/88.9%. Nearest-0.01 rounding of Figure 4 inputs permits only about 75.2137–80.0000% historical increase and 87.8924–88.0040% rare reduction. Rounding alone therefore cannot explain Figure 5. Their panel-specific protocol, split, denominator, or a source error must be resolved from original artifacts. The deck keeps the panels separate.

3. **Acceptance criteria vary within the manuscript.** Methods illustrates 5% historical degradation/20% rare improvement; Figure 3 uses 25% historical tolerance; Figure 5 uses 30%/85%. The deck accurately uses Figure 5's own illustrative screen, not an approved universal gate.

4. **Figure 5(a) contains an unresolved threshold-line placement.** The dotted line labeled “Acceptance threshold (30%)” appears near the zero tick of the forgetting axis, not at 30%. Its axis assignment/scaling requires the original plotting code. The main scatter uses Figures 5(b,c), not that line. The source companion preserves the original and notes the issue separately.

5. **One Figure 4 physical-metric label conflicts with its caption.** The historical panel says “Peak error,” while the manuscript caption calls it historical Mass90 error. That ambiguous historical column is excluded. The three rare metrics used on slide 5 are consistent with their displayed labels.

6. **Update capacity changes across configurations.** Table 1 lists decoder/output-only updates for simple fine-tuning and full-network updates for replay/EWC/adaptive. The results compare configurations; they cannot attribute every difference solely to replay. Slide 4 and notes state this.

7. **Figure 3 is not merged with Figure 4.** Figure 3(a) uses a different baseline pair, while Figure 3(c) includes a full-network 0.64/0.99 pair with unresolved model/protocol identity. The source companion includes Figure 3 for inspection; it does not add those values to the main ranking.

8. **Missing evidence is scoped to the reviewed package.** The manuscript describes test sets, but their untouched/independent status cannot be audited without the manifest and logs. Calibration, detector performance, promotion, scheduling benefit, and efficiency remain unverified; the deck does not convert that missing evidence into completed results.

## History and source identity

The primary file is `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx`, SHA-256 `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`. Its image bytes match the October 7 extracted figures. The accepted-view extraction retains inserted text and excludes deleted/moved-from text; this is an extraction convention, not proof of author acceptance. The filename's date is a version label. Publication status and a latest author-approved revision are not inferred.

A bounded scan of all **22 nonlock DOCX versions** under `method_manuscript/` found the same five empirical figures byte-for-byte and identical accepted-view Figure 1–5 captions. This includes the undated manuscript, the selected file, and the file labeled `2026_09_10_precise_native_word`. No alternate plotted-data version was found in these local files. The full inventory and reproducible scan are in `qa/manuscript_version_figure_lineage.md/.json`.

The original trigger/UQ plan is traceable to the June 11 handoff (Git `8496417`) and the June prototype at `29bf982:drafts/final/section5_FINAL.md`. October's analysis and report revision map Yilin's existing offline results onto that larger plan. The matched fixed-ratio-0.8 control is an October review proposal, not a completed comparison or a June-plan result. The current manuscript/report/deliverable files are untracked locally, so their identity is established here by hashes rather than a Git commit.

Detailed numerical checks, the 75-group provenance ledger, source-history review, image audit, rendering checks, and hash manifests are under `qa/` and `sources/`. The prior deck and source documents remain unchanged.
