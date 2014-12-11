#!/bin/bash

Cs="10.0 100.0 1000.0 10000.0 100000.0"
gammas="0.01 0.001 0.0001 0.00001 0.000001"

for C in $Cs
do
    for gamma in $gammas
    do
	scriptname="run-gaussian-c"$C$"-g"$gamma".script"
	echo "Submitting "$C" "$gamma
	echo "./svm-gaussian.py "$C" "$gamma > $scriptname
	qsub -cwd $scriptname &
    done
done
