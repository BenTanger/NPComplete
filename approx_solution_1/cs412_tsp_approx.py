import sys
import time
import random

def tsp(edges, vertices):

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

    # Iterative randomized greedy approach: run multiple times with randomness
    best_cost = float('inf')
    best_path = []
    
    num_iterations = 500  # Number of random iterations to try
    
    for iteration in range(num_iterations):
        # Start from a random vertex
        start_vertex = random.randint(0, length - 1)
        
        visited = [False] * length
        path = [start_vertex]
        visited[start_vertex] = True
        total_cost = 0
        
        current = start_vertex
        for _ in range(length - 1):
            # Get all unvisited cities and their distances
            candidates = []
            distances = []
            
            for next_city in range(length):
                if not visited[next_city]:
                    distance = distance_matrix[current][next_city]
                    if distance != float('inf'):
                        candidates.append(next_city)
                        distances.append(distance)
            
            if not candidates:
                break
            
            # Sort candidates by distance and select from the top k nearest
            sorted_pairs = sorted(zip(distances, candidates))
            k = min(3, len(sorted_pairs))  # Consider top 3 nearest cities
            top_k = [city for _, city in sorted_pairs[:k]]
            
            # Randomly select from top k nearest cities
            next_city = random.choice(top_k)
            
            # Move to the selected city
            visited[next_city] = True
            path.append(next_city)
            total_cost += distance_matrix[current][next_city]
            current = next_city
        
        # Return to the starting city
        total_cost += distance_matrix[current][path[0]]
        
        # Update best solution if this is better
        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path.copy()

    # Convert path indices back to vertex names
    path_names = [vertices[i] for i in best_path] + [vertices[best_path[0]]]

    path_str = " ".join(path_names)
    out = f"{best_cost}\n{path_str}"
    return out

def main():
    edges = []
    vertices = set()
    n, m = input().split(" ")
    for _ in range(int(m)):
        start, end, weight = input().strip().split()
        weight = int(weight)
        edges.append((start, end, weight))
        vertices.add(start)
        vertices.add(end)
    print(tsp(edges, vertices))

if __name__ == "__main__":
    main()