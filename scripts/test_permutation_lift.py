from wl_k import wl1_refinement, is_homogeneous
from overlap_proxy import triangle_count, max_triangles_through_vertex
from base_graphs import K4
from permutation_lift import permutation_lift

for k in [5,10,20]:
    adj = permutation_lift(K4(), k, seed=1)
    degs = sorted({len(adj[v]) for v in adj})
    colors = wl1_refinement(adj, rounds=15)
    print(
        f"k={k} n={len(adj)}",
        "deg=", degs,
        "WL1_hom=", is_homogeneous(colors),
        "triangles=", triangle_count(adj),
        "max_tri@v=", max_triangles_through_vertex(adj)
    )

