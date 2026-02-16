# test_wl2_perm_lift.py
# Test WL2 refinement and local cycle-rank proxy on permutation lifts

from wl2_refinement import wl2_refine, wl2_is_homogeneous
from permutation_lift import permutation_lift_cycle
from local_cycle_rank import local_cycle_rank

def run_test(k_values, R, rounds=3):
    for k in k_values:
        adj = permutation_lift_cycle(k)
        colors = wl2_refine(adj, rounds=rounds)
        wl2_hom = wl2_is_homogeneous(colors)
        lcr = local_cycle_rank(adj, R)
        degs = sorted({len(adj[v]) for v in adj})
        print(
            f"k={k} n={len(adj)} "
            f"deg={degs} "
            f"WL2_hom={wl2_hom} "
            f"local_cycle_rank(R={R})={lcr}"
        )

if __name__ == "__main__":
    ks = [5, 10, 20, 40]
    R = 3
    run_test(ks, R)

