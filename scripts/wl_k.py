# WL-k color refinement (k=1 baseline)
# This is intentionally simple and deterministic.

import itertools
from collections import defaultdict

def wl1_refinement(adj, rounds=5):
    n = len(adj)
    colors = [1] * n
    for _ in range(rounds):
        sigs = []
        for v in range(n):
            neigh_colors = sorted(colors[u] for u in adj[v])
            sigs.append((colors[v], tuple(neigh_colors)))
        # relabel canonically
        mp = {}
        new_colors = []
        next_id = 1
        for s in sigs:
            if s not in mp:
                mp[s] = next_id
                next_id += 1
            new_colors.append(mp[s])
        colors = new_colors
    return colors

def is_homogeneous(colors):
    return len(set(colors)) == 1

