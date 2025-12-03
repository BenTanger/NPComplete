# Random Restarting 

import random
import time
import argparse

def swap(path):
    n = len(path)
    i, j = random.sample(range(n), 2)
    new_path = path[:]      
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def calculate_tour_cost(path, index, distance_matrix):
    total = 0
    for i in range(len(path) - 1):
        a = index[path[i]]
        b = index[path[i+1]]
        total += distance_matrix[a][b]
    total += distance_matrix[index[path[-1]]][index[path[0]]]
    return total

def tsp():

    parser = argparse.ArgumentParser(description="Approx TSP with optional restarts")
    parser.add_argument('filename', help='test file under ./test_cases/')
    parser.add_argument('--time-limit', '-t', type=float, default=10.0, help='time limit in seconds')
    parser.add_argument('--parallelism', '-p', type=int, default=1, help='degree of parallelism')
    parser.add_argument('--restarts', '-r', type=int, default=500, help='Maximum number of restarts')

    args = parser.parse_args()

    filename = args.filename
    time_limit = args.time_limit
    degree_parallelism = args.parallelism
    max_restarts = args.restarts


    edges = []
    vertices = []

    # Read in the graph
    with open(f'./test_cases/{filename}', "r") as input_file:
        size = input_file.readline().split()
        for _ in range(int(size[1])):
            start, end, weight = input_file.readline().strip().split()
            weight = int(weight)
            edges.append((start, end, weight))
            if start not in vertices:
                vertices.append(start)
            if end not in vertices:
                vertices.append(end)


    length = len(vertices)
    index = {}
    for i in range(length):
        index[vertices[i]] = i
    

    #Time limit parameters, bigger graphs will iterate longer.
    time_min = 1.0
    time_max = 600.0
    max_restarts = max(1, length**3) 
    iterations = max(10, 10 * length**2)

    time_limit = max(time_min, min(time_max,  length**3))

    # Create a matrix with all edges
    distance_matrix = [[0] * length for _ in range(length)]
    for start, end, weight in edges:
        index_start = index[start]
        index_end = index[end]
        distance_matrix[index_start][index_end] = weight
        distance_matrix[index_end][index_start] = weight

    def random_restart(path):
        random.shuffle(path)
        cur_best = float('inf')
        n = 0
        no_improvement = 0
        while n < length**2 and no_improvement < iterations:
            new_path = swap(path.copy())
            cur_weight = 0
            cur_time = 0
            cur_weight = calculate_tour_cost(new_path,index,distance_matrix)
            if cur_weight < cur_best:
                cur_best = cur_weight
                path = new_path
                no_improvement = 0
            else:
                no_improvement += 1
            n += 1
        return cur_best, path


    start_time = time.time()
    best_weight = float('inf')
    best_path = vertices.copy()
    num_restarts = 0
    while time.time() - start_time < time_limit and num_restarts < max_restarts:
        guess_best, path = random_restart(vertices.copy())
        if guess_best < best_weight:
            best_weight = guess_best
            best_path = path.copy()
            num_restarts = 0
        else:
            num_restarts += 1

    
    best_path.append(best_path[0])
    end_time = time.time()
    # Print out data for testing
    #print(f'Test: {filename}')
    #print(f'Cost: {best_weight}')
    #print(f'Path: {" ".join(best_path)}')
    #print(f'Runtime: {(end_time - start_time):.7f} seconds\n')

    # program output specifications
    out = f"{best_weight}\n{" ".join(best_path)}"
    return out



if __name__ == "__main__":
    print(tsp())