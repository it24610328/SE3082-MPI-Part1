#!/bin/bash
# usage: ./run_timing.sh <program> <output.csv>
# runs 5 times per process count and writes the average time
PROG=$1
OUT=$2
echo "np,time" > "$OUT"
for NP in 1 2 4 8; do
  SUM=0
  for RUN in 1 2 3 4 5; do
    T=$(mpirun --oversubscribe -np $NP ./$PROG | grep "^Time" | awk '{print $3}')
    SUM=$(echo "$SUM + $T" | bc -l)
  done
  AVG=$(echo "$SUM / 5" | bc -l)
  printf "%d,%.6f\n" $NP $AVG >> "$OUT"
  echo "np=$NP avg time=$AVG"
done
