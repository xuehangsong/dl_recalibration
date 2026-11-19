# November 19 research discussion

**Does plume contraction tell us when the U-Net needs attention?** On 733 evaluation cases with an archived snapshot-3 forecast, the full-field alarm detected 23 of 24 large plume contractions and 10 of 45 high forecast errors. Only six cases met both outcome definitions. The alarm identified a group with a higher error risk, but missed 35 of the 45 high-error cases. Use the [paired comparison figure](alarm_and_forecast_error.pdf) to open the discussion.

| Snapshot-2 full-field rule | High error at snapshot 3 | Median spatial RMSE |
|---|---:|---:|
| Alarm | 10 / 55 (18.2%) | 0.59 µg/L |
| No alarm | 35 / 678 (5.2%) | 0.55 µg/L |

High error means at least 1.164 µg/L spatial RMSE, the 95th percentile over the 758 paired reference forecasts. The original 16-site high-RMS rule caught one of the 45 high-error cases and issued 39 alerts. All thresholds were determined on reference data. The earlier U-Net study split model data by snapshot. In the paired evaluation, 716 of the 733 trajectories had another snapshot in training. The analysis covers one synthetic case family, one forecast interval and ideal observations.

**What did placement change?** Across all 5,000 pilot evaluation trajectories, the original layout caught 0 of 142 contractions and raised 229 false alarms. The central layout caught 105 and raised 261 false alarms using the same 16-site RMS rule. The perimeter layout never fired. On the 733 paired forecasts, the central rule caught 11 of 45 high errors and issued 61 alarms. The alternative layouts were chosen after inspecting the ensemble and evaluated on the same split. The [footprint ensemble](ensemble_footprint_occupancy.pdf) shows where the 90%-mass footprints contracted.

**What can we conclude about recalibration?** The full-field signal could prioritize a small set of forecasts for review. Its low coverage of high-error cases leaves a substantial gap for a recalibration trigger. A useful next demonstration would compare a frozen update policy with a no-update baseline on completely held-out trajectories and measure both future error and historical retention. Yilin’s separate replay study illustrates the tradeoff. Fixed replay reduced rare-regime RMSE from 10.04 to 1.21 µg/L, while historical RMSE rose from 0.58 to 1.03 µg/L. Those are outcomes of a separate update experiment.

[Offline brief](index.html) · [Methods, per-case data and execution records](../../analyses/monitoring_pilot_20261118/README.md)
