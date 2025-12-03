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

To run with test file:
python3 cs412_tsp_approx.py < test_cases/folder_name/test_{num1}_{num2}.txt
where folder_name = first, second, third, fourth, fifth
num1 = 1, 2, 3, 4, 5
num2 = 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17


To run generate and run all test_cases:
bash test_cases/run_tests_cases.sh

Input tags:
-t: time limit to not exceed
-p: degrees of parallelism

Example of calling program:
python3 cs412_tsp_approx.py -p 2 < optimal_test_cases/first/test_1_12.txt

output:
188
l a c d g i e f k j h b l