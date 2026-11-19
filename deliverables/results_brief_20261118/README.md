# Pump-and-treat monitoring and forecast error

Open the [offline meeting brief](index.html) for the November 19 discussion. The [paired forecast-error figure](alarm_and_forecast_error.pdf) compares contraction and high-error detection on the same 733 cases. The [footprint ensemble](ensemble_footprint_occupancy.pdf) and the [full-cohort monitoring results](monitoring_trigger.pdf) give the physical context. All images are embedded in the HTML. The [meeting notes](RESULTS_SUMMARY.md) summarize the conclusion and its limits.

The [monitoring pilot](../../analyses/monitoring_pilot_20261118/) contains the case-level data, run records and source hashes. The earlier U-Net update comparison comes from the [October results deck](../results_slides_20261029/). Run `python3 build_ensemble_plot.py` and `python3 build_brief.py` with NumPy, SciPy and Matplotlib to regenerate the figures and offline page from the saved outputs.
