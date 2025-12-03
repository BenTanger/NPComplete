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
    random.shuffle(cycle)

    # small weight for cycle edges
    # cycle_weights = [random.randint(10, 25) for _ in range(len(cycle))]

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            # check if (u, v) or (v, u) is in the cycle path
            weight = random.randint(10, 50)
            for idx in range(len(cycle)):
                a1 = cycle[idx]
                a2 = cycle[(idx + 1) % len(cycle)]
            #     if (u == a1 and v == a2) or (u == a2 and v == a1):
            #         # weight = cycle_weights[idx]
            #         break
            # if weight is None:
            #     weight = random.randint(26, 50)
            edges.append((u, v, weight))

    ind = cycle.index('a')
    corrected = cycle[ind:] + cycle[:ind]
    corrected.append('a')

    with open(f'test_cases/first/test_1_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')
            

    #2------------------------------------------------------------------------------
    random.shuffle(cycle)

    # small weight for cycle edges
    # cycle_weights = [random.randint(10, 25) for _ in range(len(cycle))]

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            # check if (u, v) or (v, u) is in the cycle path
            weight = random.randint(26, 50)
            for idx in range(len(cycle)):
                a1 = cycle[idx]
                a2 = cycle[(idx + 1) % len(cycle)]
            #     if (u == a1 and v == a2) or (u == a2 and v == a1):
            #         # weight = cycle_weights[idx]
            #         break
            # if weight is None:
            #     weight = random.randint(26, 50)
            edges.append((u, v, weight))

    ind = cycle.index('a')
    corrected = cycle[ind:] + cycle[:ind]
    corrected.append('a')

    with open(f'test_cases/second/test_2_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')
            

    #3----------------------------------------------------------------------------------
    random.shuffle(cycle)

    # small weight for cycle edges
    # cycle_weights = [random.randint(10, 25) for _ in range(len(cycle))]

    # Build full graph
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            u, v = vertices[i], vertices[j]
            # check if (u, v) or (v, u) is in the cycle path
            weight = random.randint(26, 50)
            for idx in range(len(cycle)):
                a1 = cycle[idx]
                a2 = cycle[(idx + 1) % len(cycle)]
            #     if (u == a1 and v == a2) or (u == a2 and v == a1):
            #         # weight = cycle_weights[idx]
            #         break
            # if weight is None:
            #     weight = random.randint(26, 50)
            edges.append((u, v, weight))

    ind = cycle.index('a')
    corrected = cycle[ind:] + cycle[:ind]
    corrected.append('a')

    with open(f'test_cases/third/test_3_{n}.txt', "w") as test_file:
            test_file.write(f'{len(vertices)} {len(edges)}\n')
            for u, v, w in edges:
                test_file.write(f'{u} {v} {w}\n')
            