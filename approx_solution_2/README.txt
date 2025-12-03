# Random Restart approximation

The Runtime is:
The runtime is O(V^3). The runtime of each part of the program is:

index mapping: O(V)             Each vertex is mapped to a dictionary
Distance_matrix: O(V^2)         Creates matrix of size O(n^2)
Calculate_tour_cost: O(V)       Loops through the path once 
swap: O(V)                      due to copything the path
random_restart O(V^2)           Loop iterates at most O(V) times, from iterations variable. In each iteration it calls swap and Calculate_tour_cost(both O(V))
main loop O(V)                  max_restarts variable is in O(V).

Each restart in the main loop calls random_restart therefore we get O(V^3)


To call the program:


To run with command line input:
python cs412_tsp_approx.py 

To run a specific test case:

python ApproxSolution.py file_number/file_name.txt
(ex. python3 ApproxSolution.py first/test_1_4.txt)

To run generate and run all test_cases:

bash test_cases/run_tests_cases.sh

Input tags:
-t: time limit to not exceed.
-p: degrees of parallelism