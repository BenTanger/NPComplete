Runtime is O(v^2) becuase we don't check every possible path.
Instead we go to the nearest neighbor and mark them as we go
so we don't return to a visited neighbor.

If in the approx_solution directory:

    To run directly:
    python ApproxSolution.py File_Number/Test_Name.txt

    To Run Script:
    bash test_cases/run_test_cases.sh