#!/usr/bin/env python3

import random

def _add_edge(adj, u, v):
    if u == v:
        return
    adj[u].add(v)
    adj[v].add(u)

def cycle_graph(n):
    adj = {i: set() for i in range(n)}
    for i in range(n):
        _add_edge(adj, i, (i + 1) % n)
    return adj

def permutation_lift(base_adj, k, seed=0):
    """
    Random k-lift of an undirected base graph.

    Vertices: (v, i) for v in base vertices, i in {0..k-1}.
    For each undirected base edge {u,v}, choose a random permutation pi on [k],
    then add edges (u,i) -- (v, pi(i)) for all i.

    Returns adjacency dict keyed by (v,i) tuples.
    """
    rng = random.Random(seed)
    base_vertices = list(base_adj.keys())

    adj = {}
    for v in base_vertices:
        for i in range(k):
            adj[(v, i)] = set()

    seen = set()
    for u in base_vertices:
        for v in base_adj[u]:
            if u == v:
                continue
            e = (u, v) if u < v else (v, u)
            if e in seen:
                continue
            seen.add(e)

            perm = list(range(k))
            rng.shuffle(perm)

            for i in range(k):
                _add_edge(adj, (u, i), (v, perm[i]))

    return adj

def relabel_to_int(adj):
    """
    Convert tuple-vertex adjacency to integer-labeled adjacency 0..n-1.
    Useful for WL implementations expecting small ints.
    """
    verts = list(adj.keys())
    idx = {v: i for i, v in enumerate(verts)}
    out = {idx[v]: set() for v in verts}
    for v in verts:
        for w in adj[v]:
            out[idx[v]].add(idx[w])
    return out

def degree_set(adj):
    return sorted({len(adj[v]) for v in adj})

def sanity_counts(adj):
    n = len(adj)
    m2 = sum(len(adj[v]) for v in adj)
    m = m2 // 2
    return n, m

if __name__ == "__main__":
    base = cycle_graph(10)

    for k in [50, 100, 200]:
        adj = permutation_lift(base, k, seed=1)
        n, m = sanity_counts(adj)
        print("k=", k, "n=", n, "m=", m, "deg_set=", degree_set(adj))

        adj_int = relabel_to_int(adj)
        n2, m2 = sanity_counts(adj_int)
        print("  relabeled:", "n=", n2, "m=", m2, "deg_set=", degree_set(adj_int))

