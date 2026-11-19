# Quantitative analysis of embedded manuscript figures

These calculations use numeric labels printed in the embedded figures of `Adaptive_Replay_Manuscript_2026_09_09.docx`. They are more detailed than the prose-only table, but remain figure-extracted evidence rather than raw-prediction reproduction. Values are rounded to the precision shown in the figures.

## Figure 1: regime threshold

The Mass90 size-change histogram labels the historical cutoff at the 40th percentile, score **0.133**, and the rare cutoff at the 97th percentile, score **0.329**. Thus the rare stress set begins at a Mass90 relative footprint-change score 2.47 times the historical cutoff (0.329/0.133). The rare cutoff is a response label based on consecutive reference plumes; it does not identify the operational cause or provide a prospective detector.

## Figure 4: physical metric changes

The baseline-to-method calculations are in `figure4_metric_changes.csv`. From the displayed values:

- Simple fine-tuning reduces rare RMSE by **61.0%**, rare plume-mass error by **69.5%**, rare peak error by **45.8%**, and rare Mass90 error by **49.5%**, while historical RMSE rises **91.4%** and the plotted historical peak-error metric rises **134.8%** (0.23 to 0.54).
- Fixed replay reduces rare RMSE by **87.9%**, rare plume-mass error by **94.4%**, rare peak error by **75.8%**, and rare Mass90 error by **73.4%**, while historical RMSE rises **77.6%** and the plotted historical peak-error metric rises **73.9%** (0.23 to 0.40).
- EWC reduces rare RMSE by **87.8%**, rare plume-mass error by **94.2%**, rare peak error by **76.1%**, and rare Mass90 error by **76.9%**, while historical RMSE rises **839.7%** and the plotted historical peak-error metric rises **778.3%** (0.23 to 2.02).

The figure caption and prose use the historical peak/Mass90 values differently from the visual labels, so metric-name mapping must be confirmed from the plotting code before treating these as separate physical quantities. The safe result is the numeric direction and magnitude shown in the figure, with labels preserved as printed.

## Figure 5: controller comparison

The plotted acceptance region is historical degradation <= **30%** and rare improvement >= **85%**. On that plotted rule, threshold adaptive forgetting (26.5%, 85.8%) and loss-balanced (21.1%, 85.5%) pass; fixed replay (80.4%, 88.9%) and loss-balanced + floor (38.1%, 87.3%) fail. This is a conditional result for the illustrative Figure 5 rule, not a final deployment decision. It also shows that the controller outcome is not uniformly “adaptive replay passes”: one adaptive variant fails the plotted gate.

The replay trajectory reaches **r = 0.8** and remains at that cap for most of the 100 plotted update epochs. This identifies the executed adaptive trajectory as high-replay after the initial ramp; it does not isolate scheduling benefit from replay amount. A fixed-replay-at-0.8 comparator with matched seed, update budget, and data exposure is required for that causal claim.

## Figure 3: fine-tuning and layer-freezing panels

Figure 3(a) labels a validation-style before/after pair of 0.49 to 0.67 µg/L historical RMSE and 9.20 to 1.20 µg/L rare RMSE. From the labels, historical error increases 36.7% while rare error decreases 87.0%. Figure 3(c) labels the baseline at 0.58/10.04, decoder-only fine-tuning at 1.11/3.92, and full-network tuning at 0.64/0.99 µg/L for historical/rare RMSE. Relative to the displayed baseline, the full-network pair is a 10.3% historical increase and a 90.1% rare reduction. This pair cannot be merged with the Figure 4 fixed-replay result until the manuscript identifies the exact protocol and model label.

For Figure 5, the acceptance margins are archived in `figure5_acceptance_margins.csv`. Threshold adaptive forgetting clears the historical boundary by 3.5 percentage points and the rare boundary by 0.8 points. Loss-balanced clears them by 8.9 and 0.5 points. Fixed replay misses the historical boundary by 50.4 points despite clearing the rare boundary by 3.9 points; loss-balanced-plus-floor misses historical retention by 8.1 points.
