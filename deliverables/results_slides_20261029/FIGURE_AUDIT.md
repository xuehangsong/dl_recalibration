# Figure and evidence audit

Scope: seven slides for a simple internal discussion of the updated results. Literature, general framework diagrams, and implementation plans are excluded.

The figures are replotted from the reported numerical labels in the September 9, 2026 adaptive-replay manuscript and the verified October 28 report revision. They are not independent reproductions from raw predictions. The embedded manuscript Figures 4 and 5 were inspected visually and checked against the archived originals by hash.

| Slide | Visual | Audit and treatment |
|---|---|---|
| 1 | Baseline historical/rare RMSE | 0.58 and 10.04 µg/L; ratio 17.3. Common zero-based axis. |
| 2 | RMSE comparison | Preserve all four Figure 4 configurations and values. Separate zero-based historical/rare panels improve readability; numerical axis limits are explicit. |
| 3 | Three rare-regime plume metrics | Retain mass, peak, and Mass90 error labels and values from Figure 4. Exclude the historical plume-metric column because source labels and prose conflict. |
| 4 | Controller acceptance plot | Preserve all four Figure 5 outcomes. Only threshold adaptive forgetting and loss-balanced satisfy the illustrative ≤30% historical / ≥85% rare conditions. No deployment approval is implied. |
| 5 | Rare-improvement margins | Calculate 85.8−85 = 0.8 and 85.5−85 = 0.5 percentage points. No confidence intervals or significance claims are inferred. |
| 6 | Comparison provenance | Keep Figure 4's calculated 77.6% / 87.9% fixed-replay pair separate from Figure 5's reported 80.4% / 88.9%. Do not assume rounding reconciles the difference. |
| 7 | Candidate status | Show the two screened candidates and the pending calibration, final-test, and promotion-review requirements. This is an evidence-status diagram, not a completed deployment record. |

The spatial plume panels and adaptive-replay trajectory are not recreated from pixels: the underlying arrays and controller logs were not supplied in the report evidence package. The separate Figure 3 full-network result is not merged into Figure 4 because configuration labels and protocol equivalence remain unresolved. No new training, synthetic measured data, error bars, prospective detection performance, active-learning benefit, or speedup claim is added.

All figure images contain only labels, axes, legends, and data. Slide-level claims and short captions remain separate editable PowerPoint text. Speaker notes carry detailed sources and caveats. Every slide contains exactly one image; each replot is also supplied as PNG, SVG, and PDF.

Source hashes, copied numerical tables, and machine-readable figure treatment are in `sources/`. Native PowerPoint rendering and structural checks are in `qa/`.
