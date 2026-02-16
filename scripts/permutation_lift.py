import random

def permutation_lift(base_adj, k, seed=0):
    """
    k-lift via random permutations.
    Each base vertex v becomes (v,i), i in [0,k).
    Each base edge (u,v) gets a random matching.
    Degree is preserved exactly.
    """
    rng = random.Random(seed)
    base_vertices = sorted(base_adj.keys())
    idx = {v:i for i,v in enumerate(base_vertices)}

    def node(v,i):
        return idx[v]*k + i

    n = len(base_vertices) * k
    adj = {x: [] for x in range(n)}

    seen = set()
    for u in base_vertices:
        for v in base_adj[u]:
            a,b = sorted((u,v))
            if (a,b) in seen:
                continue
            seen.add((a,b))
            perm = list(range(k))
            rng.shuffle(perm)
            for i in range(k):
                uu = node(u,i)
                vv = node(v,perm[i])
                adj[uu].append(vv)
                adj[vv].append(uu)

    return adj

