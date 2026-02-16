from wl_k import wl1_refinement, is_homogeneous

# triangle
adj_triangle = {
    0: [1,2],
    1: [0,2],
    2: [0,1],
}

colors = wl1_refinement(adj_triangle)
print("triangle homogeneous:", is_homogeneous(colors))

