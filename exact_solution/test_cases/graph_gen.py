# Makes 5 graphs each of sizes 4 - 17

import random

for n in range(4, 18):

    # 26 vertices: 'a'..'z'
    vertices = [chr(ord('a') + i) for i in range(n)]

    # define a “special” cycle (any permutation you like; here: shuffle for example)
    full = ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z"]

    cycle = full[0:n]

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            weight = random.randint(10, 50)
            edges.append((u, v, weight))

    cycle.append('a')

    with open(f'test_cases/first/test_1_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')

    #2------------------------------------------------------------------------------

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            weight = random.randint(10, 50)
            edges.append((u, v, weight))

    cycle.append('a')

    with open(f'test_cases/second/test_2_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')

    #3----------------------------------------------------------------------------------

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            weight = random.randint(10, 50)
            edges.append((u, v, weight))

    cycle.append('a')

    with open(f'test_cases/third/test_3_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')

    #4----------------------------------------------------------------------------------

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            weight = random.randint(10, 50)
            edges.append((u, v, weight))

    cycle.append('a')

    with open(f'test_cases/fourth/test_4_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')

    #5----------------------------------------------------------------------------------

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            weight = random.randint(10, 50)
            edges.append((u, v, weight))

    cycle.append('a')

    with open(f'test_cases/fifth/test_5_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')