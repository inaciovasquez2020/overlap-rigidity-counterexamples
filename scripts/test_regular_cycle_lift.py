from wl_k import wl1_refinement, is_homogeneous
from overlap_proxy import triangle_count, max_triangles_through_vertex
from base_graphs import K4
from regular_cycle_lift import regular_cycle_lift

for L in [6,8,10,12]:
    adj = regular_cycle_lift(K4(), L)
    degs = sorted({len(adj[v]) for v in adj})
    colors = wl1_refinement(adj, rounds=12)
    print(
        f"L={L} n={len(adj)}",
        "deg=", degs,
        "WL1_hom=", is_homogeneous(colors),
        "triangles=", triangle_count(adj),
        "max_tri@v=", max_triangles_through_vertex(adj)
    )

