#!/bin/bash

for i in $(seq 1 5000)
do
	echo "Initianting test instances of size $i"
	for j in $(seq 1 10)
	do
		echo "Instance $j of size $i"
	done
done
