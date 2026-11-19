# Monitoring pilot for the November 19 discussion

**Can concentration changes at a small set of monitoring locations flag impending plume change?** We tested a fixed 4 × 4 grid of ideal monitoring locations in 10,000 archived eSTOMP pump-and-treat trajectories. We set thresholds on 5,000 reference cases and evaluated the other 5,000. Each alarm used information through snapshot 2 to flag a large change from snapshot 2 to 3 in the area enclosing 90% of plume mass.

| Rule | Events detected / 142 | False alarms / 4,858 non-events | Events per alarm |
|---|---:|---:|---:|
| Large concentration change across 16 locations | 0 / 142 | 229 / 4,858 (4.7%) | 0 / 229 |
| Large previous full-field footprint change | 140 / 142 (98.6%) | 230 / 4,858 (4.7%) | 140 / 370 (37.8%) |

All 142 large changes were contractions. Median RMS concentration change at the monitoring locations was 15.1 archive concentration units in those cases and 27.5 in the other cases. A rule looking for a large increase in this score missed the events. The full-field comparator benefited from persistence in the same footprint metric used to define the event. It also required complete plume maps and raised more false alarms than true alarms.

**Decision for the demonstration.** Leave the high-RMS alarm out of the proposed recalibration trigger for this case. Use the full-field rule as a simulation benchmark. A sparse rule still needs to show which alerts correspond to consequential U-Net errors on paired cases. The experiment covers one interval, one layout, and noise-free simulated observations.

**Meaningful image for discussion.** The companion ensemble footprint plot shows the cell-wise fraction of event and non-event trajectories inside the Mass90 footprint at snapshots 2 and 3. Event cases contract from an average of 572 to 353 cells, while other cases contract from 914 to 782 cells. This makes the event definition visible and shows why the full-field benchmark has signal. It is a retrospective footprint summary, not a calibrated ensemble prediction or U-Net uncertainty plot.

**Prior update evidence.** In Yilin's separate Figure 4 comparison, fixed replay reduced rare-regime RMSE from 10.04 to 1.21 µg/L and raised historical RMSE from 0.58 to 1.03 µg/L. These are measured update outcomes from the earlier study. The new pilot does not establish how those outcomes would have changed under either warning rule.
