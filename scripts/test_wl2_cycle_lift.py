# scripts/test_wl2_cycle_lift.py
#
# Test WL2 homogeneity and local cycle-rank on regularized cycle lifts.
#
# Requires:
#   - wl2_refinement.py
#   - regular_cycle_lift.py
#   - local_cycle_rank.py

from wl2_refinement import wl2_refine, wl2_is_homogeneous
from regular_cycle_lift import regular_cycle_lift
from local_cycle_rank import local_cycle_rank

def run():
    L_vals = [6, 8, 10, 12]
    R_vals = [2, 3]

    for L in L_vals:
        adj = regular_cycle_lift(L)
        colors = wl2_refine(adj, rounds=5)
        hom = wl2_is_homogeneous(colors)

        for R in R_vals:
            lcr = local_cycle_rank(adj, R)
            print(
                f"L={L} R={R} "
                f"WL2_hom={hom} "
                f"local_cycle_rank={lcr}"
            )

if __name__ == "__main__":
    run()

