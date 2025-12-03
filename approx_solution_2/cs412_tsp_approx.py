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

def tsp(edges, vertices, time_limit):

    length = len(vertices)
    index = {}
    for i in range(length):
        index[vertices[i]] = i
    

    #Time limit parameters, bigger graphs will iterate longer.
    time_min = 1.0
    time_max = 600.0
    max_restarts = max(1, length * 50) 
    iterations = max(200, length**2)

    if time_limit is None:
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
        cur_best = cur_best = calculate_tour_cost(path, index, distance_matrix)
        n = 0
        no_improvement = 0
        while n < length**2 and no_improvement < iterations:
            new_path = swap(path.copy())
            cur_weight = 0
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

    
    closed_path = best_path + [best_path[0]]

    # program output specifications
    path_str = " ".join(closed_path)
    out = f"{best_weight}\n{path_str}"
    return out

def main():
    parser = argparse.ArgumentParser(description="Approx TSP with optional time limit")
    parser.add_argument('--time-limit', '-t', type=float, default=None, help='time limit in seconds')
    args = parser.parse_args()
    time_limit = args.time_limit

    edges = []
    vertices = []
    n,m = input().split(" ")
    for _ in range(int(m)):
            start, end, weight = input().strip().split()
            weight = int(weight)
            edges.append((start, end, weight))
            if start not in vertices:
                vertices.append(start)
            if end not in vertices:
                vertices.append(end)
    print(tsp(edges, vertices, time_limit))

if __name__ == "__main__":
    main()