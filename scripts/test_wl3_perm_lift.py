# scripts/test_wl3_perm_lift.py
#
# Test WL3 refinement on permutation lifts.
# Assumes permutation_lift(base_adj, k) exists and returns adj dict.

from wl3_refinement import wl3_refine, wl3_is_homogeneous
from permutation_lift import permutation_lift
from base_graphs import cycle_graph

def run():
    base = cycle_graph(6)

    for k in [5, 10, 20]:
        adj = permutation_lift(base, k)
        coloring = wl3_refine(adj, rounds=2)
        hom = wl3_is_homogeneous(coloring)

        print(
            "k=", k,
            "n=", len(adj),
            "WL3_hom=", hom
        )

if __name__ == "__main__":
    run()

