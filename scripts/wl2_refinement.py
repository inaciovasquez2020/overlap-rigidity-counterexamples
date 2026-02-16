# scripts/wl2_refinement.py
#
# A minimal, explicit WL2 (2-dimensional Weisfeiler–Leman) refinement
# for simple undirected graphs given as adjacency lists.
#
# This is intentionally written for clarity and correctness, not speed.
# It is suitable for n ≲ 200 in stress tests.

from collections import defaultdict

def initial_pair_coloring(adj):
    """
    Initial WL2 coloring.
    Color ordered pairs (u, v) by:
      - diagonal vs off-diagonal
      - adjacency if u ≠ v
    """
    vertices = list(adj.keys())
    color = {}
    for u in vertices:
        for v in vertices:
            if u == v:
                color[(u, v)] = ("diag",)
            else:
                color[(u, v)] = ("edge",) if v in adj[u] else ("nonedge",)
    return color


def refine_once(adj, color):
    """
    One WL2 refinement step.

    New color of (u, v) is determined by the multiset:
      { (color(u, w), color(w, v)) : w ∈ V }
    together with the old color.
    """
    vertices = list(adj.keys())
    new_color = {}

    # build signatures
    signatures = {}
    for u in vertices:
        for v in vertices:
            sig = []
            for w in vertices:
                sig.append((color[(u, w)], color[(w, v)]))
            sig.sort()
            signatures[(u, v)] = (color[(u, v)], tuple(sig))

    # relabel canonically
    canon = {}
    next_id = 0
    for key, sig in signatures.items():
        if sig not in canon:
            canon[sig] = next_id
            next_id += 1
        new_color[key] = canon[sig]

    return new_color


def wl2_refine(adj, max_iter=20):
    """
    Run WL2 refinement to stabilization or until max_iter.
    Returns the stabilized coloring of ordered pairs.
    """
    color = initial_pair_coloring(adj)
    for _ in range(max_iter):
        new_color = refine_once(adj, color)
        if new_color == color:
            break
        color = new_color
    return color


def wl2_vertex_colors(adj, pair_color):
    """
    Collapse WL2 pair coloring to vertex colors
    by collecting the multiset of colors (v, w) for each v.
    """
    vcolors = {}
    for v in adj:
        sig = []
        for w in adj:
            sig.append(pair_color[(v, w)])
        sig.sort()
        vcolors[v] = tuple(sig)
    return vcolors


def wl2_is_homogeneous(adj):
    """
    Returns True iff WL2 assigns the same vertex color to all vertices.
    """
    pair_color = wl2_refine(adj)
    vcolors = wl2_vertex_colors(adj, pair_color)
    return len(set(vcolors.values())) == 1

