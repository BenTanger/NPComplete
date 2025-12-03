#!/bin/bash

> test_cases/output.txt

#echo "Generating Graphs"
python test_cases/graph_gen.py

for ((i=4; i<=17; i++))
do
    echo "Running test_1_$i"
    python cs412_tsp_approx.py < test_cases/first/test_1_$i.txt >> test_cases/output.txt -v

    echo "Running test_2_$i"
    python cs412_tsp_approx.py < test_cases/second/test_2_$i.txt >> test_cases/output.txt -v 

    echo "Running test_3_$i"
    python cs412_tsp_approx.py < test_cases/third/test_3_$i.txt >> test_cases/output.txt -v 

    echo "Running test_4_$i"
    python cs412_tsp_approx.py < test_cases/fourth/test_4_$i.txt >> test_cases/output.txt -v

    echo "Running test_5_$i"
    python cs412_tsp_approx.py < test_cases/fifth/test_5_$i.txt >> test_cases/output.txt -v
done

echo "Transfering Data"
python test_cases/transfer.py
