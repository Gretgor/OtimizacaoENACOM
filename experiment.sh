#!/bin/bash

echo -n > EXP_RESULTS
for i in $(seq 1 2000)
do
	sum=0
	echo "Initianting test instances of size $i"
	for j in $(seq 1 10)
	do
		echo "Instance $j of size $i"
		echo "Generating..."
		python3 generate_instance.py $i > TEMP_INST
		echo "Executing..."
		{ time python3.7 investment.py < penis ; } 2> EXECUTION 1> /dev/null
		# Getting "real" time, no reason to use the other two that I can think of
		tempo=$(cat EXECUTION | grep real | cut -d"m" -f2 | cut -d"s" -f1 | sed s/,//g)
		sum=$((sum+tempo))
	done
	# Experiment results for the current size
	echo $i $((sum/10)) >> EXP_RESULTS
done
