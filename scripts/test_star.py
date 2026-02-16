from wl_k import wl1_refinement, is_homogeneous
from overlap_proxy import triangle_count, max_triangles_through_vertex
from star_of_triangles import star_of_triangles

for m in [3,5,8,12]:
    adj = star_of_triangles(m)
    colors = wl1_refinement(adj, rounds=6)
    print(
        f"m={m}",
        "WL1_hom=", is_homogeneous(colors),
        "triangles=", triangle_count(adj),
        "max_tri@v=", max_triangles_through_vertex(adj)
    )

