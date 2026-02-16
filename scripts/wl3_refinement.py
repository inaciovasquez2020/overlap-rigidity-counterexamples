# scripts/wl3_refinement.py
#
# Minimal Weisfeiler–Leman 3-dimensional refinement.
# This is intentionally small and explicit (slow but clear),
# suitable only for small n (≈ 30–50 max).
#
# Input graph format:
#   adj : dict[v] -> set of neighbors
#
# Output:
#   coloring : dict[(i,j,k)] -> color id
#
# Also provides wl3_is_homogeneous()

from collections import defaultdict

def wl3_refine(adj, rounds=3):
    vertices = list(adj.keys())
    n = len(vertices)

    # index vertices for tuples
    idx = {v: i for i, v in enumerate(vertices)}
    inv = {i: v for v, i in idx.items()}

    # initial coloring: equality pattern + adjacency pattern
    color = {}
    next_color = {}
    palette = {}

    def base_color(i, j, k):
        vi, vj, vk = inv[i], inv[j], inv[k]
        eq = (i == j, j == k, i == k)
        adjp = (
            vj in adj[vi],
            vk in adj[vi],
            vk in adj[vj],
        )
        return (eq, adjp)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                color[(i, j, k)] = base_color(i, j, k)

    # iterative refinement
    for _ in range(rounds):
        palette.clear()
        next_color.clear()
        cid = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    sig = [
                        color[(i, j, k)]
                    ]

                    # substitute one coordinate at a time
                    for t in range(n):
                        sig.append(color[(t, j, k)])
                        sig.append(color[(i, t, k)])
                        sig.append(color[(i, j, t)])

                    sig = tuple(sig)

                    if sig not in palette:
                        palette[sig] = cid
                        cid += 1

                    next_color[(i, j, k)] = palette[sig]

        color, next_color = next_color, color

    return color


def wl3_is_homogeneous(coloring):
    vals = set(coloring.values())
    return len(vals) == 1

