#!/usr/bin/env python3

from collections import defaultdict
import itertools

def induced_ball(adj, center, R):
    visited = {center}
    frontier = {center}
    for _ in range(R):
        new = set()
        for v in frontier:
            new |= adj[v]
        new -= visited
        visited |= new
        frontier = new
    return visited

def equality_pattern(xs):
    k = len(xs)
    return tuple(xs[i] == xs[j] for i in range(k) for j in range(i+1, k))

def fo4_local_types(adj, R, rounds=5):
    """
    Computes FO^4 local types via 4-variable WL-style refinement
    restricted to radius-R neighborhoods.
    """

    vertices = list(adj.keys())
    tuples = list(itertools.product(vertices, repeat=4))

    colors = {}
    for t in tuples:
        colors[t] = (equality_pattern(t),)

    for _ in range(rounds):
        sigs = {}
        for (a, b, c, d) in tuples:
            ball = (
                induced_ball(adj, a, R)
                | induced_ball(adj, b, R)
                | induced_ball(adj, c, R)
                | induced_ball(adj, d, R)
            )

            ext = []
            for x in ball:
                ext.append((
                    colors[(x, b, c, d)],
                    colors[(a, x, c, d)],
                    colors[(a, b, x, d)],
                    colors[(a, b, c, x)],
                ))

            sigs[(a, b, c, d)] = (colors[(a, b, c, d)], tuple(sorted(ext)))

        new_colors = {}
        cmap = {}
        next_id = 0
        for t in sigs:
            s = sigs[t]
            if s not in cmap:
                cmap[s] = next_id
                next_id += 1
            new_colors[t] = cmap[s]

        colors = new_colors

    return colors

def fo4_is_homogeneous(adj, R, rounds=5):
    colors = fo4_local_types(adj, R, rounds)
    return len(set(colors.values())) == 1

if __name__ == "__main__":
    # sanity checks

    def cycle_graph(n):
        adj = {i: set() for i in range(n)}
        for i in range(n):
            adj[i].add((i - 1) % n)
            adj[i].add((i + 1) % n)
        return adj

    def star_graph(n):
        adj = {i: set() for i in range(n)}
        for i in range(1, n):
            adj[0].add(i)
            adj[i].add(0)
        return adj

    G1 = cycle_graph(12)
    G2 = star_graph(12)

    for R in [1, 2, 3]:
        print("cycle R=", R, "FO4_hom=", fo4_is_homogeneous(G1, R))
        print("star  R=", R, "FO4_hom=", fo4_is_homogeneous(G2, R))

