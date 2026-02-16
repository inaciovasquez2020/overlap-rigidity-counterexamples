from collections import defaultdict

def wl3_refine(adj, rounds=3):
    V = list(adj.keys())
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}

    colors = {(i, j, k): 0 for i in range(n) for j in range(n) for k in range(n)}

    for _ in range(rounds):
        sigs = {}
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    vi, vj, vk = V[i], V[j], V[k]
                    neigh_i = [idx[u] for u in adj[vi]]
                    neigh_j = [idx[u] for u in adj[vj]]
                    neigh_k = [idx[u] for u in adj[vk]]

                    bag = []
                    for a in neigh_i:
                        bag.append(colors[(a, j, k)])
                    for b in neigh_j:
                        bag.append(colors[(i, b, k)])
                    for c in neigh_k:
                        bag.append(colors[(i, j, c)])

                    sigs[(i, j, k)] = (
                        colors[(i, j, k)],
                        tuple(sorted(bag))
                    )

        canon = {}
        next_id = 0
        for key in sorted(sigs.keys()):
            s = sigs[key]
            if s not in canon:
                canon[s] = next_id
                next_id += 1

        colors = {k: canon[sigs[k]] for k in sigs}

    return colors


def wl3_is_homogeneous(colors):
    return len(set(colors.values())) == 1

