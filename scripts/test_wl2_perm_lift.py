# scripts/test_wl2_perm_lift.py
#
# Test WL2 homogeneity and local cycle-rank on permutation lifts.
#
# Requires:
#   - wl2_refinement.py
#   - permutation_lift.py
#   - local_cycle_rank.py

from wl2_refinement import wl2_refine, wl2_is_homogeneous
from permutation_lift import permutation_lift
from local_cycle_rank import local_cycle_rank

def run():
    ks = [5, 10, 20, 40]
    R_vals = [2, 3]

    for k in ks:
        adj = permutation_lift(k)
        colors = wl2_refine(adj, rounds=5)
        hom = wl2_is_homogeneous(colors)

        for R in R_vals:
            lcr = local_cycle_rank(adj, R)
            print(
                f"k={k} R={R} "
                f"WL2_hom={hom} "
                f"local_cycle_rank={lcr}"
            )

if __name__ == "__main__":
    run()

