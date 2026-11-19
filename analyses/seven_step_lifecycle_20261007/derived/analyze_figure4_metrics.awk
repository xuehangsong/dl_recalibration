BEGIN { FS=","; OFS="," }
NR==1 { for(i=2;i<=NF;i++) name[i]=$i; print "method,metric,baseline_value,method_value,relative_change_percent,interpretation"; next }
NR==2 { for(i=2;i<=NF;i++) b[i]=$i; next }
{ for(i=2;i<=NF;i++) {
  metric=name[i]
  if (i==2 || i==6) { pct=($i-b[i])/b[i]*100; interp=(pct>0?"degradation/increase":"reduction") }
  else { pct=(b[i]-$i)/b[i]*100; interp=(pct>0?"improvement":"worsening") }
  printf "%s,%s,%.4f,%.4f,%.4f,%s\n", $1, metric, b[i], $i, pct, interp
 } }
