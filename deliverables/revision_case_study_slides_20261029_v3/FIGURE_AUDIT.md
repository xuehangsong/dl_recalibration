# Figure and evidence audit

The v3 deck follows one scientific argument: which maintenance problem was selected, where the static model fails, what the update comparisons improve, why historical retention changes the decision, and what is still required.

| Slide | Central visual | Evidence and treatment |
|---|---|---|
| 1 | Native lifecycle/evidence map | Revised report Sections 2.2 and 5.9; source categories are distinct from completed operational steps. |
| 2 | Native controlled-stress workflow | Manuscript P0008–P0024, Eq. 1; Mass90 response selection requires the next reference state. Historical bottom 40% at 0.133, rare top 3% at 0.329. |
| 3 | Original rare-plume triplet | Crop of manuscript Figure 2(b), pixels/axes/scales/aspect preserved. Concentration max 813.6 µg/L; signed error ±169.4 µg/L. |
| 4 | Replotted joint RMSE scatter | Figure 4 pairs: 0.58/10.04, 1.11/3.92, 1.03/1.21, 5.45/1.22 µg/L. Configurations also differ in trainable layers. |
| 5 | Three aligned physical-error dot panels | Same Figure 4 comparison: rare mass, peak, Mass90. Separate labeled linear x scales; no bars, invented uncertainty, or connecting trajectories. |
| 6 | Native validation-feedback loop | Eq. 1, P0063–P0066; forgetting/feedback P0077–P0081; qualitative loss-balanced rule P0103; validation/test distinction P0111–P0116. |
| 7 | Replotted controller screen | Separate Figure 5 pairs: 80.4/88.9, 26.5/85.8, 21.1/85.5, 38.1/87.3%. Illustrative ≤30%/≥85% region. |
| 8 | Native validation boundary | Report Sections 5.7–5.9; independent calibration, final test, and review remain pending. |
| 9 | Native next-demonstration plan | Report Section 5.10; known change, ordered evaluation, frozen rules, matched updates, independent validation. Entire diagram is planned. |

The full original DOCX was freshly extracted in accepted view: 205 paragraph anchors, 7 OOXML tables including equation tables, and 46 OMML expressions. See `sources/evidence_audit.md` for provenance and limitations. Source references in notes use stable anchors from that extraction, not Word pagination.

No overarching titles or descriptive paragraphs are embedded in the plots/diagrams. Slide claims and captions are separate native text. Diagram node names, data labels, axes, and status legends are retained. All flowcharts are actual editable PowerPoint shapes and attached connectors.

The source spatial colormap is retained because raw fields are unavailable; colors are not treated as numerical data. The map is a representative baseline example, not a reproduced post-update result. The tightly packed Figure 4 spatial row remains excluded rather than clipping neighboring labels/colorbars.

The replay diagram represents training-batch mixing and validation feedback, not an operational online loop. Historical share is r; rare share is 1−r. Final-test data do not enter the controller. The source loss-balanced equation is incomplete, so no reconstructed formula is shown. Figure 5(a) reaches r=0.8 for most epochs; no synthetic trajectory is plotted. Matched fixed-ratio evidence is still needed to isolate scheduling benefit.

Figure 4 and Figure 5 use different reported comparisons and are never pooled. The 30%/85% screen is illustrative because other source sections use different tolerances. No replicate uncertainty, verified trajectory split, interval calibration, untouched final-test record, or promotion artifact is supplied. Physical errors do not establish compliance-well accuracy or remedy outcomes.
