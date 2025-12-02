# Greedy approximation solution for the TSP problem

import sys
import time

def tsp():

    filename = sys.argv[1]

    edges = []
    vertices = set()

    # Read in the graph
    with open(f'./test_cases/{filename}', "r") as input_file:
        size = input_file.readline().split()
        for _ in range(int(size[1])):
            start, end, weight = input_file.readline().strip().split()
            weight = int(weight)
            edges.append((start, end, weight))
            vertices.add(start)
            vertices.add(end)

    vertices = sorted(vertices)
    length = len(vertices)

    start_time = time.time()

    # Set the vertices to an index
    index = {}
    for i in range(length):
        index[vertices[i]] = i

    # Create a matrix with all edges
    distance_matrix = [[float('inf')] * length for _ in range(length)]

    for start, end, weight in edges:
        index_start = index[start]
        index_end = index[end]
        distance_matrix[index_start][index_end] = weight
        distance_matrix[index_end][index_start] = weight

    # Greedy algorithm: always go to the nearest unvisited city
    visited = [False] * length
    path = [0]  # Start from vertex 0
    visited[0] = True
    total_cost = 0

    current = 0
    for _ in range(length - 1):
        nearest = -1
        min_distance = float('inf')
        
        # Find the nearest unvisited city
        for next_city in range(length):
            if not visited[next_city]:
                if distance_matrix[current][next_city] < min_distance:
                    min_distance = distance_matrix[current][next_city]
                    nearest = next_city
        
        # Move to the nearest city
        visited[nearest] = True
        path.append(nearest)
        total_cost += min_distance
        current = nearest

    # Return to the starting city
    total_cost += distance_matrix[current][path[0]]

    end_time = time.time()

    # Convert path indices back to vertex names
    path_names = [vertices[i] for i in path] + [vertices[path[0]]]

    # Print out data
    print(f'Test: {filename}')
    print(f'Cost: {total_cost}')
    print(f'Path: {" ".join(path_names)}')
    print(f'Runtime: {(end_time - start_time):.7f} seconds\n')

tsp()