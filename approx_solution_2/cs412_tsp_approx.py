# Random Restarting 

import random
import time
import argparse
import multiprocessing

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

def random_restart(path, index, distance_matrix, iterations, n, start_time, time_limit):
        tolerance = 5
        random.shuffle(path)
        cur_best = cur_best = calculate_tour_cost(path, index, distance_matrix)
        i = 0
        no_improvement = 0
        while time.time() - start_time < time_limit - tolerance and i < n**2 and no_improvement < iterations:
            new_path = swap(path.copy())
            cur_weight = 0

            cur_weight = calculate_tour_cost(new_path,index,distance_matrix)
            if cur_weight < cur_best:
                cur_best = cur_weight
                path = new_path
                no_improvement = 0
            else:
                no_improvement += 1
            i += 1
        return cur_best, path


def tsp(n, edges, vertices, time_limit, degree_parallelism, verbose):

    #Create vertex dict
    index = {}
    for i in range(n):
        index[vertices[i]] = i
    

    #Time limit parameters, bigger graphs will iterate longer.
    time_min = 1.0
    time_max = 55.0
    max_restarts = min(100 * n, 2000)
    iterations = min(50 * n, 5000)

    if time_limit is None:
        time_limit = max(time_min, min(time_max,  n**3))
    elif time_limit > 1:
        time_limit -= 1

    # Create a matrix with all edges
    distance_matrix = [[0] * n for _ in range(n)]
    for start, end, weight in edges:
        index_start = index[start]
        index_end = index[end]
        distance_matrix[index_start][index_end] = weight
        distance_matrix[index_end][index_start] = weight


    start_time = time.time()
    best_weight = float('inf')
    best_path = vertices.copy()
    num_restarts = 0

    # Create a worker pool for multiprocessing
    pool = None
    use_pool = degree_parallelism > 1
    if use_pool:
        pool = multiprocessing.Pool(processes=degree_parallelism)

    try:
        while time.time() - start_time < time_limit - 5 and num_restarts < max_restarts:
            args_list = [(vertices.copy(), index, distance_matrix, iterations, n, start_time, time_limit) for _ in range(degree_parallelism)]
            if use_pool:
                results = pool.starmap(random_restart, args_list)
            else:
                # No parallelism
                results = [random_restart(*args_list[0])]
            guess_best, path = min(results, key=lambda item: item[0]) # results is a list of (best_weight, path) tuples
            if guess_best < best_weight:
                best_weight = guess_best
                best_path = path.copy()
                num_restarts = 0
            else:
                num_restarts += 1

        closed_path = best_path + [best_path[0]]

        if verbose:
            end_time = time.time()
            #Print out data for testing
            print(f"vertices: {n}")
            print(f'Cost: {best_weight}')
            print(f'Path: {" ".join(closed_path)}')
            print(f'Runtime: {(end_time - start_time):.7f} seconds\n')
        else:
            # program output specifications
            path_str = " ".join(closed_path)
            out = f"{best_weight}\n{path_str}"
            print(out)
    finally:
        if pool is not None:
            pool.close()
            pool.join()

def main():
    parser = argparse.ArgumentParser(description="Approx TSP with optional time limit, and degrees parallelism")
    parser.add_argument('--time_limit', '-t', type=float, default=None, help='time limit in seconds')
    parser.add_argument('--parallelism', '-p', type=int, default=1, help='degrees of parallelism')
    parser.add_argument('--verbose', '-v', action='store_true', help='outputs test details')
    args = parser.parse_args()
    time_limit = args.time_limit
    degree_parallelism = args.parallelism
    verbose = args.verbose

    edges = []
    vertices = []
    n,m = input().split(" ")
    for _ in range(int(m)):
            start, end, weight = input().strip().split()
            weight = float(weight)
            edges.append((start, end, weight))
            if start not in vertices:
                vertices.append(start)
            if end not in vertices:
                vertices.append(end)
    tsp(int(n), edges, vertices, time_limit, degree_parallelism, verbose)




if __name__ == "__main__":
    main()