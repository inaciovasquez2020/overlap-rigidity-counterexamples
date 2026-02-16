# wl2_refinement.py
# Minimal Weisfeiler–Leman 2-dimensional refinement for simple undirected graphs.
# Graph format: adjacency dict {v: set(neighbors)}

from collections import defaultdict

def normalize_pair(u, v):
    return (u, v) if u <= v else (v, u)

def initial_colors(adj):
    """
    Initial WL2 colors for ordered pairs (u,v).
    Use (deg(u), deg(v), adj(u,v)).
    """
    deg = {u: len(adj[u]) for u in adj}
    colors = {}
    for u in adj:
        for v in adj:
            colors[(u, v)] = (deg[u], deg[v], 1 if v in adj[u] else 0)
    return relabel(colors)

def relabel(colors):
    """
    Canonical relabeling to consecutive integers.
    """
    uniq = {}
    next_id = 0
    out = {}
    for k, c in colors.items():
        if c not in uniq:
            uniq[c] = next_id
            next_id += 1
        out[k] = uniq[c]
    return out

def wl2_step(adj, colors):
    """
    One WL2 refinement step.
    For each ordered pair (u,v), aggregate over all w:
      multiset of (color(u,w), color(w,v))
    """
    new_colors = {}
    for u in adj:
        for v in adj:
            bag = []
            for w in adj:
                bag.append((colors[(u, w)], colors[(w, v)]))
            bag.sort()
            new_colors[(u, v)] = (colors[(u, v)], tuple(bag))
    return relabel(new_colors)

def wl2_refine(adj, max_iters=10):
    """
    Run WL2 until stabilization or max_iters.
    Returns final colors and number of iterations used.
    """
    colors = initial_colors(adj)
    for it in range(max_iters):
        new_colors = wl2_step(adj, colors)
        if new_colors == colors:
            return colors, it
        colors = new_colors
    return colors, max_iters

def is_wl2_homogeneous(adj, max_iters=10):
    """
    Check if all diagonal pairs (v,v) end with the same color.
    Proxy for WL2-homogeneity.
    """
    colors, _ = wl2_refine(adj, max_iters=max_iters)
    diag_colors = {colors[(v, v)] for v in adj}
    return len(diag_colors) == 1

if __name__ == "__main__":
    # simple sanity check
    # triangle
    adj = {
        0: {1, 2},
        1: {0, 2},
        2: {0, 1},
    }
    print("WL2 homogeneous:", is_wl2_homogeneous(adj))

