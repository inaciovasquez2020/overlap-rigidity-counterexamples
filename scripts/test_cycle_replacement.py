from wl_k import wl1_refinement, is_homogeneous
from overlap_proxy import triangle_count, max_triangles_through_vertex
from base_graphs import K4
from cycle_replacement import cycle_replacement

for L in [4,6,8,10]:
    adj = cycle_replacement(K4(), L)
    colors = wl1_refinement(adj, rounds=10)
    print(
        f"L={L} n={len(adj)}",
        "WL1_hom=", is_homogeneous(colors),
        "triangles=", triangle_count(adj),
        "max_tri@v=", max_triangles_through_vertex(adj),
        "deg_set=", sorted({len(adj[v]) for v in adj})[:10]
    )

