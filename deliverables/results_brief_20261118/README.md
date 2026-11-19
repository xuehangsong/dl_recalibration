# Pump-and-treat monitoring and forecast error

Open the [offline meeting brief](index.html) with the [map of the three 16-site layouts](sensor_layout_comparison.png). Follow the maps through the plume changes, then compare how well the sites warned of a shrinking plume and a large forecast error. The [speaker notes](RESULTS_SUMMARY.md) follow the five figures in order. All images are embedded in the HTML.

The [monitoring pilot](../../analyses/monitoring_pilot_20261118/) contains the case-level data, run records and source hashes. The earlier U-Net update comparison comes from the [October results deck](../results_slides_20261029/). Run `python3 build_ensemble_plot.py` and `python3 build_brief.py` with NumPy, SciPy and Matplotlib to regenerate the figures and offline page from the saved outputs. The [sensor layout comparison](sensor_layout_comparison.pdf) shows what “original,” “central,” and “perimeter” mean.
