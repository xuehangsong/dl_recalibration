## Source Figure 1

Figure 1. Relative sequential 90%-mass plume-size change distribution

The historical cutoff is the 40th percentile, s=0.133; the rare cutoff is the 97th percentile, s=0.329. The source title, histogram, annotations, and ensemble identifiers are retained as supplied. This requires reference plume information at t and t+1 and is not a prospective detector.

Source: method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx
File version label: 2026_09_09 (filename label; not an asserted revision or publication date).
DOCX SHA-256: 20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7
Image part: word/media/image1.png
Image SHA-256: de944beace604d00d4eac20afaa7afd13d7b30087e71dd0bb5fd98682027abc0

## Source Figure 2

Figure 2. Static baseline performance on historical and rare plume regimes. “Reference” denotes the full-order physics model concentration field, and “baseline prediction” denotes the concentration field predicted by the static U-Net surrogate.

The v4 main-deck rare triplet is a pixel-faithful crop from panel(b) of this figure. This complete image also retains panel(a) distributions and the historical spatial triplet. Historical concentrations reach917.9 ug/L and signed errors span±19.1 ug/L; the rare concentration maximum is813.6 ug/L and signed errors span±169.4 ug/L. Do not compare colors between regimes as if they share scales.

Source: method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx
File version label: 2026_09_09 (filename label; not an asserted revision or publication date).
DOCX SHA-256: 20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7
Image part: word/media/image2.png
Image SHA-256: 933ef4f0d03d942501db57e5c63b807a66aac8cf902033bceb86c25f2d2697b4

## Source Figure 3

Figure 3. Effect of fine-tuning on rare-regime adaptation and historical-regime retention. (a) RMSE before and after fine-tuning for historical low-change samples and rare high-change samples. (b) Historical-regime degradation plotted against rare-regime RMSE improvement for different update configurations. The dashed horizontal line indicates the 25% allowable degradation threshold. (c) Layer-freezing comparison showing RMSE for the baseline model, decoder-only fine-tuning, and full-network tuning.

Preserved for source audit, not pooled into the main-deck ranking. Figure3(a) displays baseline historical/rare RMSE0.49/9.2, whereas Figure3(c) displays0.58/10.04. Figure3(c) labels a full-network ModelC pair0.64/0.99; its relationship to Figure4 configurations is unresolved. Figure3(b) uses a25% historical degradation boundary, while Figure5 uses30%/85%. The main deck keeps these protocols separate.

Source: method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx
File version label: 2026_09_09 (filename label; not an asserted revision or publication date).
DOCX SHA-256: 20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7
Image part: word/media/image3.png
Image SHA-256: 26b8bd338133d392a667e0d01597010f6e8850dd517f5ffcd9c347dde0d1ff59

## Source Figure 4

Figure 4. Comparison of continual-learning strategies for rare-regime adaptation and historical-regime retention using fine tuning (FT), fixed replay, and elastic weight consolidation (EWC). (a) Scalar performance metrics for the baseline U-Net, simple fine-tuning, fixed replay, and elastic weight consolidation (EWC). Metrics include historical-regime RMSE, rare-regime RMSE, rare-regime plume-mass error, rare-regime peak-concentration error, historical-regime Mass90 error, and rare-regime Mass90 error. (b) Stability–plasticity tradeoff for the update strategies, where the x-axis shows rare-regime RMSE improvement and the y-axis shows historical-regime degradation relative to the baseline. Points farther to the right indicate greater rare-regime adaptation, whereas lower points indicate better retention of historical-regime performance. (c) Representative rare-regime plume predictions and error maps for the baseline, simple fine-tuning, fixed replay, and EWC models. Error is computed as predicted minus reference concentration.

Main-deck RMSE and rare physical-metric replots use only the directly labeled numbers in panel(a). The image labels the historical physical metric Peak error(hist,%), but the Figure4 caption calls it historical Mass90 error. That ambiguous historical column is omitted from main-deck replotting. Panel(c) is an original spatial comparison; raw arrays/sample identifier are unavailable. Colors and annotation crowding are preserved as supplied.

Source: method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx
File version label: 2026_09_09 (filename label; not an asserted revision or publication date).
DOCX SHA-256: 20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7
Image part: word/media/image4.png
Image SHA-256: 624368f75b65d0660a746a591a125f3f7b0cbfdd3983bfb1fde01ec4d00bc121

## Source Figure 5

Figure 5. Adaptive replay control and acceptance-region analysis. Panel (a) shows the update trajectory, where the replay ratio (rt) increases in response to historical-regime forgetting and reaches the imposed replay-ratio cap. Panel (b) compares final historical-regime degradation and rare-regime improvement across fixed and adaptive replay controllers. Panel (c) shows the acceptance region defined by maximum allowable historical degradation and minimum required rare-regime improvement, points inside the shaded region satisfy both criteria for surrogate redeployment.

Main-deck controller coordinates use panel(b) labels and match panel(c): fixed replay (80.4,88.9), threshold adaptive/forgetting (26.5,85.8), loss-balanced (21.1,85.5), and loss-balanced+floor (38.1,87.3), as historical degradation %, rare improvement %. The current replot retains these values and directions but changes colors/markers and zooms the axes. Panel(a) is preserved as the original image, not reconstructed from an inferred numeric trajectory. Its magenta dotted line is labeled Acceptance threshold (30%) but lies near the red forgetting-axis zero tick, below20%, rather than between20% and40%. The threshold placement or axis normalization is unresolved; the plotting code is unavailable, so this is an observed source-plot inconsistency rather than a diagnosed code error. The main deck uses the clearly displayed replay-ratio cap, not the suspect threshold trace. The high replay cap alone does not isolate adaptive scheduling benefit. Passing the illustrative panel(c) screen does not establish deployment readiness.

Source: method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx
File version label: 2026_09_09 (filename label; not an asserted revision or publication date).
DOCX SHA-256: 20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7
Image part: word/media/image5.png
Image SHA-256: 0f5a3c45e568af53e900765d28f68da4d8a2adcb2a288ec609ae3af56fe7a9e5
