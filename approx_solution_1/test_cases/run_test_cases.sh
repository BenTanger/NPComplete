#!/bin/bash

> test_cases/output.txt

echo "Generating Small Graphs (test_1 to test_4)"
python test_cases/graph_gen.py

echo "Generating Large Graphs (test_5)"
python test_cases/big_graph_gen.py

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
done

# Run large graph tests (550, 600, 650, 700, 750, 800, 850, 900, 950, 1000)
for ((i=550; i<=1000; i+=50))
do
    echo "Running test_5_$i"
    python ApproxSolution.py big_graphs/test_5_$i.txt >> test_cases/output.txt
done

echo "Transfering Data"
python test_cases/transfer.py