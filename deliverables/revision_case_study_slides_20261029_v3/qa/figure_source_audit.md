# Figure numbers, data, and source-image audit

Audit date: 2026-10-29. This audit compares the current v3 deck with the actual embedded images and adjacent captions in `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx`. It does not validate model execution, raw prediction arrays, or independent test estimates.

**Result:** all 28 numeric data labels replotted in v3 match the displayed values in Yilin's original Figures 4(a) and 5(b,c). The two acceptance limits also match Figure 5(c). Slide 3 is a pixel-identical crop of Figure 2(b). The source contains unresolved inconsistencies, listed below; none should be silently repaired or pooled into a common experiment.

## Figure numbering and slide mapping

“Figure” means the original manuscript figure number; “Slide” means the v3 presentation slide number. In particular, the controller plot is **manuscript Figure 5(c), shown on v3 Slide 7**. V3 Slide 5 contains physical metrics from **manuscript Figure 4(a)**. Asset filename `05_controller_screen.png` records an earlier sequence and is not its current slide number.

| V3 slide | Visual | Exact manuscript source / report cross-reference | Treatment |
|---|---|---|---|
| 1 | Planned lifecycle and current evidence | Revised report §§2.2, 5.9 | New native conceptual diagram; not an original experimental figure |
| 2 | U-Net and retrospective regime selection | Manuscript methods and Figure 1 cutoffs; report §§5.1–5.5 | Native diagram. Original Figure 1 is the Mass90 distribution, not a source drawing of the entire workflow |
| 3 | Rare reference, baseline prediction, signed error | Figure 2(b), right-hand triplet; caption P0139 | Original-image crop only |
| 4 | Joint historical/rare RMSE | Figure 4(a), first two metric panels; report Table 10 / Figure 9 | Replot eight displayed scalar labels as four coordinate pairs; not a literal copy of original Figure 4(b) |
| 5 | Rare mass, peak, and Mass90 errors | Figure 4(a), the three rare physical-metric panels; report Table 11 | Replot twelve displayed labels as three point panels |
| 6 | Adaptive replay feedback | Equation 1, controller methods, Table 2; Figure 5(a) replay cap | Native conceptual feedback loop. It is not a numerical trajectory reconstruction |
| 7 | Controller acceptance screen | Figure 5(b) displayed values and Figure 5(c) coordinate/threshold definitions; report Table 9 / Figure 8 | Replot eight displayed scalar labels as four coordinate pairs; same threshold directions |
| 8 | Required calibration and test evidence | Report §§5.7–5.9 | Native evidence-boundary diagram |
| 9 | Planned next experiment | Report §5.10 and original trigger/UQ plan | Native plan, not a measured result |

Original Figure 3 is excluded from the main comparison because protocol/model identities remain unresolved. It is retained in the separate complete-source companion.

## Direct source identity

The DOCX image relationship and immediately following caption were checked; these mappings were not inferred from filenames alone. The existing `analyses/seven_step_lifecycle_20261007/source_extracts/embedded_figures/image2.png`, `image4.png`, and `image5.png` are byte-identical to their DOCX parts.

| Manuscript figure | DOCX part | Relationship | Pixel dimensions | SHA-256 |
|---|---|---|---|---|
| 1 | `word/media/image1.png` | `rId12` | 1562 × 939 | `de944beace604d00d4eac20afaa7afd13d7b30087e71dd0bb5fd98682027abc0` |
| 2 | `word/media/image2.png` | `rId13` | 1893 × 1259 | `933ef4f0d03d942501db57e5c63b807a66aac8cf902033bceb86c25f2d2697b4` |
| 3 | `word/media/image3.png` | `rId14` | 2169 × 657 | `26b8bd338133d392a667e0d01597010f6e8850dd517f5ffcd9c347dde0d1ff59` |
| 4 | `word/media/image4.png` | `rId15` | 2292 × 1383 | `624368f75b65d0660a746a591a125f3f7b0cbfdd3983bfb1fde01ec4d00bc121` |
| 5 | `word/media/image5.png` | `rId16` | 3214 × 854 | `0f5a3c45e568af53e900765d28f68da4d8a2adcb2a288ec609ae3af56fe7a9e5` |

Source DOCX SHA-256: `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`.

Full original captions, accepted-view image locations, exact extracted paths, and byte hashes are also recorded in `deliverables/revision_case_study_slides_20261029_v4/sources/original_figures/source_manifest.json` relative to the repository root. The complete source companion preserves all five original image parts without cropping or alterations.

## Figure 2(b): faithful spatial crop

The v3 crop is `(left, top, right, bottom) = (950, 600, 1893, 1259)` in original image pixels, producing 943 × 659 pixels. A pixel-by-pixel RGB comparison using `ImageChops.difference` returned no differing pixels. The retained view includes the full rare-regime reference, baseline prediction, signed residual, axes, panel labels, colorbars, and aspect ratio.

- Concentration maximum: **813.6 µg/L** for both reference and baseline prediction.
- Signed error: **prediction minus reference**, with colorbar limits **−169.4 to +169.4 µg/L**.
- Historical panels excluded from the crop use different scales: maximum **917.9 µg/L** and residual limits **±19.1 µg/L**. Cross-regime color comparisons would therefore be invalid.
- No raw concentration arrays, sample identifier, or regenerated spatial field were used. Source resolution, original colormaps, and source label crowding remain as supplied.

## Figure 4(a): all 20 replotted values

Every number in this table was checked against the labels in the original image and against `figure4_metric_values.csv`; the current rendered Slides 4 and 5 display the same values.

| Configuration | Historical RMSE (µg/L) | Rare RMSE (µg/L) | Rare mass error (%) | Rare peak error (%) | Rare Mass90 error (%) |
|---|---:|---:|---:|---:|---:|
| Baseline | 0.58 | 10.04 | 32.30 | 14.20 | 7.11 |
| Simple fine-tuning | 1.11 | 3.92 | 9.86 | 7.70 | 3.59 |
| Fixed replay | 1.03 | 1.21 | 1.82 | 3.43 | 1.89 |
| EWC | 5.45 | 1.22 | 1.88 | 3.40 | 1.64 |

The source uses bars for panel (a); v3 uses an RMSE scatter and physical-metric points. This changes presentation, not the reported values. V3 Slide 4 axes are **historical RMSE** and **rare RMSE**, both lower being better. Original Figure 4(b) instead uses rare RMSE improvement versus historical degradation, with right/lower being better; v3 must not be described as an unchanged copy of that panel.

V3 expands “Simple FT” to “Simple fine-tuning”; “EWC” remains the elastic weight consolidation configuration. Colors and marker shapes differ from the source but labels are explicit. No source histogram, uncertainty, run variability, or training path is inferred from the rounded aggregate numbers.

## Figure 5(b,c): acceptance-plot audit

| Original panel label | V3 label | Historical degradation / RMSE increase (%) | Rare improvement / RMSE reduction (%) | Meets ≤30% and ≥85% |
|---|---|---:|---:|---|
| `fixed` / Fixed replay | Fixed replay | 80.4 | 88.9 | No |
| `forgetting` / Threshold adaptive (forgetting) | Threshold adaptive | 26.5 | 85.8 | Yes |
| `loss_balanced` / Loss balanced | Loss-balanced | 21.1 | 85.5 | Yes |
| `loss_balanced_floor` / Loss balanced + floor | Loss-balanced + floor | 38.1 | 87.3 | No |

The screenshot discussed by the user corresponds to this acceptance-plot mapping; the root session confirmed the same four coordinate pairs. The direct primary-source audit here uses original `image5.png`, panels (b) and (c), plus the rendered v3 Slide 7.

Both original Figure 5(c) and v3 use x = historical degradation, y = rare improvement. The threshold intersection remains **(30,85)**, with the acceptable quadrant to the **upper left**. V3 uses x limits 0–90 and y limits 80–90 to resolve the four points; the original panel's labeled axes extend to 100% on both axes. This is an explicit zoom, not a numerical transformation. It preserves all four displayed outcomes. Colors/markers are restyled; no controller is renamed to a different method.

The two passing rare-improvement margins are **0.8 percentage points** and **0.5 percentage points**, as the caption states. Historical margins are 3.5 and 8.9 percentage points. These are deterministic differences of rounded displayed numbers, not uncertainty estimates or evidence of robust acceptance.

## Source issues retained, not repaired

1. **Figure 5(a) threshold placement:** its magenta dotted line is labeled “Acceptance threshold (30%)” but appears near zero on the red forgetting axis, below the 20% tick rather than between 20% and 40%. This is an observed source-plot inconsistency in threshold placement or axis normalization. The plotting code is unavailable, so it is not a diagnosed code error. Main v3 uses the visible replay-ratio cap at `r = 0.8`, not the suspect threshold trace. The complete-source companion flags this anomaly separately while preserving the original image unchanged.
2. **Figure 4 historical physical metric:** the image labels that panel “Peak error (hist, %),” with 0.23, 0.54, 0.40, and 2.02; its caption calls it historical-regime Mass90 error. V3 excludes this ambiguous column. The rare mass, peak, and Mass90 panels used in Slide 5 have clear matching labels.
3. **Figure 3 protocol conflicts:** panel (a) shows baseline historical/rare values 0.49/9.2, while panel (c) shows 0.58/10.04. Full-network Model C at 0.64/0.99 is not pooled with Figure 4. Figure 3's 25% historical limit differs from Figure 5's illustrative 30%/85% screen; the methods also give another illustrative contract.
4. **Figure 4 versus Figure 5 fixed replay:** the Figure 4 rounded RMSE pair yields approximately 77.6% historical increase and 87.9% rare reduction; Figure 5 reports 80.4% and 88.9%. Do not replace Figure 5's labels with the Figure 4-derived percentages. Denominators, splits, exposure, and executed configurations remain unresolved; rounding alone is not assumed to explain this.
5. **Causal attribution:** simple fine-tuning and replay/EWC differ in trainable layers as well as update procedure. The displayed comparisons support configuration-specific results; the diagrams and captions must not attribute the whole difference to replay alone.
6. **Spatial update maps:** complete Figure 4(c) gives original before/after maps and remains valuable source evidence, but panel-level crops can cut or crowd adjacent colorbar/Y-axis labels. With no raw arrays, no recolored or reconstructed version is justified. Preserve the complete original in the source companion.

## Retaining original figures without weakening presentation clarity

Keep the audited v3/v4 main-slide style and the exact original Figure 2(b) crop. Supply a separate **five-slide source companion**, one complete original figure per slide, with native source attribution and brief discrepancy notes outside each image. This maximizes access to Yilin's original figures, preserves every panel and original annotation, and keeps the internal-meeting narrative readable. A side-by-side comparison on the main slides would halve image size and reduce readability; it is unnecessary once values and hashes are documented.

The source companion has now been built at `deliverables/revision_case_study_slides_20261029_v4/Yilin_original_figures_20261029.pptx`. Its build checks validate all five embedded image hashes against their DOCX parts, one image per slide, zero picture cropping, preserved aspect ratios, and in-slide bounds. Microsoft PowerPoint rendering and visual review pass: five PDF pages, five previews, no native text overflow or out-of-bounds shapes, and two existing PowerPoint presentations preserved. Checks are recorded in `v4/qa/source_companion_delivery_verification.json` and `v4/qa/source_companion_powerpoint_verification.json`. The source companion does not endorse the source's unresolved acceptance/deployment claims.

## Audited artifact hashes

| Artifact | SHA-256 |
|---|---|
| V3 `Updated_case_study_20261029_v3.pptx` | `8d68c941ee31ba40cbc353381dd07baf75d832ced18f8770cf88639c3b582340` |
| `figure4_metric_values.csv` | `c127acbb22310773f591b06a328354c97ecc97d129597e7a09ed4e8383acba89` |
| `figure5_controller_values.csv` | `40a975ebe0c60630d4a142974c0e8dfabc2605d18b9f8fac6becacf63418e073` |
| V3 `figures/03_rare_spatial_example.png` | `dde09e17d9c3246d01fe9ef8c8392be27e4d0a6176e6a8b2d5eef1c9ed3bf943` |
| V3 `figures/04_joint_rmse.png` | `42975a3b15a4c9bb9d57b12f9c5e2c2d76f4cd92181737c5ec211b84e9ccf0ab` |
| V3 `figures/05_rare_physical_errors.png` | `51dc08980c0ce07de5b8fef2aff705b658b3410e7724af636f0dab8f52236932` |
| V3 `figures/05_controller_screen.png` | `52dd949149f213785de065d9245c6ee9efe56c98f5193ab893a147e33e595d51` |
| `deliverables/report_revision_20261028/section5_20261028.md` | `65538283781912e1ae77d8ab9d135e06b311e4934600e75c617dd6b7a7e64974` |

Hashes identify this audit snapshot; future revisions require rechecking mappings and recalculating hashes. Frozen report files and original source figures were not edited.
