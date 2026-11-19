# Direct manuscript audit for the lifecycle case-study deck

Source: `method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx`  
SHA-256: `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`  
Extraction: `manuscript_accepted_full.txt`, `manuscript_accepted_paragraphs.json`, and `manuscript_equations.json`. Deleted/moved source text was excluded; insertions were retained.

## Evidence that strengthens the causal story

**The manuscript defines a validation-driven update loop.** Table 2 separates standard training from continual updating: validation monitors both rare-regime learning and historical forgetting, adjusts replay during update epochs, and test evaluates whether the updated surrogate satisfies criteria. Anchors: P0104–P0116. This supports an editable loop figure with an explicit hold-out boundary; do not show final test feeding the controller.

**Replay has a precise batch meaning.** Equation 1 is `B_update = r B_old + (1-r) B_new`; `B_old` contains historical low-change samples and `B_new` contains rare high-change samples. Anchors: P0060–P0066. Thus `r` is the historical share of an update batch. The displayed replay cap `r = 0.8` means high historical exposure in that run, not a generic “80% accuracy” or an old:new ratio.

**The adaptive feedback signal is explicit.** Forgetting is `RMSE_old,e / RMSE_old,0 − 1` on the historical validation set. If forgetting exceeds `alpha_high`, replay increases; if forgetting is below `alpha_low` and new-regime validation loss is improving, replay decreases. Anchors: P0074–P0081. The EMA threshold equations and their interpretation are in P0082–P0090. This supports a controller-loop diagram, but not a numeric recreation of the trajectory because parameter values and logs are incomplete.

**The experiment has two different causal levers.** Table 1 changes both update data and trainable capacity: simple fine-tuning updates the last decoder block/output layer (P0040–P0044), while replay, EWC, and adaptive replay use the full network (P0045–P0059). The deck must call Figure 4 a configuration comparison and avoid attributing every difference to replay alone.

**The physical failure mode is spatial.** Results state that rare-regime error concentrates around the plume body, high-gradient regions, and plume boundaries, indicating geometry/redistribution weakness rather than only concentration-magnitude error (P0137–P0140). Figure 2(b) is therefore useful as one faithful source crop; raw arrays are unavailable, so it should remain a representative example.

**The update question is explicitly multi-objective.** The manuscript says acceptable updating requires rare-regime improvement, bounded historical degradation, physical plume-metric errors, and lower full-order simulation burden (P0118–P0127). The first three are represented in the revised report; the fourth is a target/hypothesis, not a measured result. The text gives a stricter illustrative criterion of 1.05× historical RMSE and 0.80× rare RMSE (P0125–P0127), while Figure 5 uses 30%/85%; the deck should label all as exploratory and retain the report’s unresolved-threshold note.

**The conceptual workflow has a clear evidence boundary.** The manuscript’s online-maintenance discussion says flagged predictions are provisional; reliable targets come from full-order simulations, monitoring observations, or observation-assimilated estimates; updated surrogates are not redeployed automatically (P0168–P0170). This supports a closing validation/promotion slide without claiming deployment.

## Direct source inconsistencies to keep visible in notes

1. The abstract claims a transferable framework and post-deployment lifecycle, but the experiment is a synthetic offline U-Net update study (P0004, P0130–P0134, P0168–P0172). The revised report correctly narrows this.
2. Table 1 has visible corruption in Model E (“Starts rom”, “controlled relay”) (P0055–P0059). Do not reproduce that table verbatim.
3. Equation 5 for the loss-balanced controller is malformed/ambiguous in the source (P0091–P0103). Use the qualitative feedback loop only; do not typeset an invented formula.
4. Acceptance criteria conflict: P0125–P0127 gives 1.05×/0.80×, Figure 3 uses a 25% threshold, and Figure 5 uses illustrative 30%/85%. No single approved contract is evidenced.
5. Figure 4’s fixed-replay percentages calculated from rounded RMSE (77.6%/87.9%) differ from Figure 5’s reported controller pair (80.4%/88.9%). Keep the panels separate; provenance is unresolved.
6. The manuscript says “test” but does not provide a trajectory manifest, seeds, raw prediction arrays, checkpoint/hash, or calibration outputs. The revised report therefore stops at a governed CALIBRATE/DEPLOY hold.
7. The replay cap/trajectory is described in Figure 5, but its numeric controller parameters, initialization, update interval, and logs are not all present. The deck may state that the ratio reached the imposed cap; it must not redraw a numeric training trajectory.
8. Historical/rare partition thresholds use the response-derived Mass90 score and require `t+1` reference information (P0019–P0024). They support a retrospective stress partition, not prospective detector operating characteristics.

## Proposed v3 narrative (9-slide maximum)

1. **Planned lifecycle vs evidence in the revised case study** — native editable seven-step flow with evidence-status tags.
2. **How the offline stress test creates the update problem** — native U-Net/Thiem → `t+1` prediction → reference comparison → Mass90 response partition; rare top 3% and historical bottom 40%.
3. **Rare plume redistribution is the baseline failure mode** — faithful source Figure 2(b) rare triplet crop; no invented spatial field.
4. **The update comparison tests adaptation and retention together** — joint historical-vs-rare RMSE scatter from Figure 4; mention configuration/capacity caveat.
5. **The same Figure 4 comparison also changes physical plume metrics** — aligned dots for rare mass, peak, Mass90 errors, or a compact source-backed metric figure.
6. **Replay is a validation-feedback mechanism** — native editable loop from old/new batch mix (Eq.1) → update → old/new validation → forgetting rule → next `r`; keep final test outside loop.
7. **Controller outcomes produce two candidates under an illustrative screen** — Figure 5 acceptance scatter; separate provenance from Figure 4.
8. **The present evidence stops before calibration and promotion** — native editable candidate → independent calibration → untouched final test → versioned review; pending stages visually distinct.
9. **Next demonstration closes the original causal/evidence chain** — native editable planned experiment: declared change → ordered trajectories → frozen detector/decision → matched adaptive/fixed-r=0.8 update → calibration → final test/review.

The deck’s result is therefore: the revised report converts the original plan into a controlled case study with strongest evidence in UPDATE, partial/retrospective evidence for DETECT/DECIDE/PREPARE, and explicit CALIBRATE/DEPLOY holds. It should not be framed as a finished lifecycle or a generic bar-chart summary.
