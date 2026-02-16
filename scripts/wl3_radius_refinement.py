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

def canonical_triple(a, b, c):
    return tuple(sorted((a, b, c)))

def wl3_radius_refine(adj, R, rounds=5):
    """
    WL3 refinement restricted to radius-R balls.
    Colors are assigned to vertex triples (a,b,c)
    using only local information.
    """

    # initial color: equality pattern + distances
    triples = []
    for a in adj:
        for b in adj:
            for c in adj:
                triples.append((a, b, c))

    colors = {}
    next_id = 0

    for (a, b, c) in triples:
        eq = (a == b, b == c, a == c)
        colors[(a, b, c)] = (eq,)

    for _ in range(rounds):
        sigs = {}
        for (a, b, c) in triples:
            ball = (
                induced_ball(adj, a, R)
                | induced_ball(adj, b, R)
                | induced_ball(adj, c, R)
            )

            neigh_sigs = []

            for x in ball:
                neigh_sigs.append(
                    (
                        colors.get((x, b, c)),
                        colors.get((a, x, c)),
                        colors.get((a, b, x)),
                    )
                )

            sigs[(a, b, c)] = (colors[(a, b, c)], tuple(sorted(neigh_sigs)))

        # relabel
        new_colors = {}
        color_map = {}
        next_id = 0

        for t in sigs:
            s = sigs[t]
            if s not in color_map:
                color_map[s] = next_id
                next_id += 1
            new_colors[t] = color_map[s]

        colors = new_colors

    return colors

def wl3_radius_is_homogeneous(adj, R, rounds=5):
    colors = wl3_radius_refine(adj, R, rounds)
    seen = set(colors.values())
    return len(seen) == 1

if __name__ == "__main__":
    # simple sanity test: cycle graph
    def cycle_graph(n):
        adj = {i: set() for i in range(n)}
        for i in range(n):
            adj[i].add((i - 1) % n)
            adj[i].add((i + 1) % n)
        return adj

    for R in [1, 2, 3]:
        G = cycle_graph(12)
        print("R=", R, "WL3_radius_hom=", wl3_radius_is_homogeneous(G, R))

