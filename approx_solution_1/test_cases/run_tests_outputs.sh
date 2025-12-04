#!/bin/bash

# Clear output file
> approx_output_exact.txt

# Check if exact_tests directory exists
if [ ! -d "exact_tests" ]; then
    echo "Error: exact_tests directory not found"
    exit 1
fi

# Change to parent directory to run ApproxSolution.py with correct paths
cd ..

# Find all .txt files in test_cases/exact_tests directory and sort them
find test_cases/exact_tests -name "*.txt" -type f | sort | while read test_file; do
    # Get relative path from test_cases/exact_tests/
    rel_path="${test_file#test_cases/exact_tests/}"
    
    echo "Running $rel_path"
    
    # Run ApproxSolution.py (expects path relative to current dir with test_cases/ prefix)
    python ApproxSolution.py "${test_file#test_cases/}" >> test_cases/approx_output_exact.txt
done

echo "Results written to test_cases/approx_output_exact.txt"