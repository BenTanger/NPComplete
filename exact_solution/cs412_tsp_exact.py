# Make the inefficient solution that gives the exact right answer to the TPS problems

import sys
import time

def tsp(edges, vertices):

    vertices = sorted(vertices)
    length = len(vertices)

    start_time = time.time()

    # Set the vertices to an index
    index = {}
    for i in range(length):
        index[vertices[i]] = i

    # Create a matrix with all edges
    distance_matrix = [[0] * length for _ in range(length)]

    for start, end, weight in edges:
        index_start = index[start]
        index_end = index[end]
        distance_matrix[index_start][index_end] = weight
        distance_matrix[index_end][index_start] = weight

    # Variables to track the current best
    best_cost = None
    best_path = None

    # Recursive function to try all possible paths
    def traverse(path, used, current_cost):
        nonlocal best_cost, best_path

        if len(path) == length:
            total = current_cost + distance_matrix[path[-1]][path[0]]
            if best_cost is None or total < best_cost:
                best_cost = total
                best_path = path[:]
            return

        last = path[-1]
        for choice in range(length):
            if not used[choice]:
                new_cost = current_cost + distance_matrix[last][choice]

                # Fail early if new cost has already exceeded the current best cost
                if best_cost is not None and new_cost > best_cost:
                    return   
                
                used[choice] = True
                path.append(choice)
                traverse(path, used, new_cost)
                path.pop()
                used[choice] = False

    used = [False] * length
    used[0] = True
    traverse([0], used, 0)

    path = [vertices[i] for i in best_path] + [vertices[best_path[0]]]
    path_str = " ".join(path)
    out = f"{best_cost}\n{path_str}"
    return out

def main():
    edges = []
    vertices = set()
    n,m = input().split(" ")
    for _ in range(int(m)):
            start, end, weight = input().strip().split()
            weight = int(weight)
            edges.append((start, end, weight))
            vertices.add(start)
            vertices.add(end)
    print(tsp(edges, vertices))

if __name__ == "__main__":
    main()