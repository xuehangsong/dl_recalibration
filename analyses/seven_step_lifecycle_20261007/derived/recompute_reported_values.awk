# Recompute only arithmetic derived from the manuscript's displayed rounded RMSE values.
# Usage: awk -f recompute_reported_values.awk
BEGIN {
  bh=0.58; br=10.04; ft_h=1.11; ft_r=3.92; fr_h=1.03; fr_r=1.21; ewc_h=5.45; ewc_r=1.22
  printf "calculation_id,result_percent\n"
  printf "DC-01,%.4f\n", (br-bh)/br*100
  printf "DC-02,%.4f\n", (ft_h-bh)/bh*100
  printf "DC-03,%.4f\n", (ft_r-br)/br*100
  printf "DC-04,%.4f\n", (fr_h-bh)/bh*100
  printf "DC-05,%.4f\n", (br-fr_r)/br*100
  printf "DC-06,%.4f\n", (ewc_h-bh)/bh*100
  printf "DC-07,%.4f\n", (br-ewc_r)/br*100
}
