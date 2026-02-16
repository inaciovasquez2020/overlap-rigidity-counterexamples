from wl2_refinement import wl2_refine, wl2_is_homogeneous
from regular_cycle_lift import regular_cycle_lift
from local_cycle_rank import local_cycle_rank

def run_test(L_values, R, rounds=3):
    for L in L_values:
        adj = regular_cycle_lift(L)
        colors = wl2_refine(adj, rounds=rounds)
        wl2_hom = wl2_is_homogeneous(colors)
        lcr = local_cycle_rank(adj, R)
        degs = sorted({len(adj[v]) for v in adj})
        print(
            f"L={L} n={len(adj)} "
            f"deg={degs} "
            f"WL2_hom={wl2_hom} "
            f"local_cycle_rank(R={R})={lcr}"
        )

if __name__ == "__main__":
    Ls = [4, 6, 8, 10, 12]
    R = 3
    run_test(Ls, R)

