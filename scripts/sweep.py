from generate_cubic import random_cubic
from wl_k import wl1_refinement, is_homogeneous
from overlap_proxy import triangle_count, max_triangles_through_vertex

def run():
    for n in [20, 30, 40, 50]:
        for seed in range(10):
            adj = random_cubic(n, seed=seed)
            colors = wl1_refinement(adj, rounds=8)
            hom = is_homogeneous(colors)
            t = triangle_count(adj)
            mt = max_triangles_through_vertex(adj)
            print(f"n={n} seed={seed} WL1_hom={hom} triangles={t} max_tri@v={mt}")

if __name__ == "__main__":
    run()

