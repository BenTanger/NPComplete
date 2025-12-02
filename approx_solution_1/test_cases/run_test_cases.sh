#!/bin/bash

> test_cases/output.txt

echo "Generating Graphs"
python test_cases/graph_gen.py

for ((i=4; i<=17; i++))
do
    echo "Running test_1_$i"
    python ApproxSolution.py first/test_1_$i.txt >> test_cases/output.txt

    echo "Running test_2_$i"
    python ApproxSolution.py second/test_2_$i.txt >> test_cases/output.txt

    echo "Running test_3_$i"
    python ApproxSolution.py third/test_3_$i.txt >> test_cases/output.txt

    echo "Running test_4_$i"
    python ApproxSolution.py fourth/test_4_$i.txt >> test_cases/output.txt

    echo "Running test_5_$i"
    python ApproxSolution.py fifth/test_5_$i.txt >> test_cases/output.txt
done

echo "Transfering Data"
python test_cases/transfer.py