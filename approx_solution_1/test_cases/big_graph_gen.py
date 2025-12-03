# Makes 10 graphs of size >= 550 and  size < 1000
import random

for graph_num in range(10):
    n = 550 + (graph_num * 50)  # 550, 600 ... 1000

    # Generate vertex names: v0, v1, v2, ..., v(n-1)
    vertices = [f'v{i}' for i in range(n)]
    
    # Create a random cycle
    cycle = vertices.copy()
    random.shuffle(cycle)
    
    # Build full graph (complete graph)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            weight = random.randint(10, 50)
            edges.append((u, v, weight))
    
    # Write to file
    filename = f'test_cases/big_graphs/test_5_{n}.txt'
    with open(filename, "w") as test_file:
        test_file.write(f'{len(vertices)} {len(edges)}\n')
        for u, v, w in edges:
            test_file.write(f'{u} {v} {w}\n')
    