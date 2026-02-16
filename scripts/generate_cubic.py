import random

def random_cubic(n, seed=0, max_tries=20000):
    if n % 2 == 1:
        raise ValueError("n must be even for cubic pairing model")
    rng = random.Random(seed)
    stubs = []
    for v in range(n):
        stubs += [v, v, v]
    for _ in range(max_tries):
        rng.shuffle(stubs)
        edges = []
        ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i+1]
            if a == b:
                ok = False
                break
            if a > b:
                a, b = b, a
            edges.append((a, b))
        if not ok:
            continue
        if len(set(edges)) != len(edges):
            continue
        adj = {v: [] for v in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        if all(len(adj[v]) == 3 for v in range(n)):
            return adj
    raise RuntimeError("failed to generate simple cubic graph")

