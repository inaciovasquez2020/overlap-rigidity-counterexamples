from permutation_lift import permutation_lift
from wl3_refinement import wl3_refine, wl3_is_homogeneous
from local_cycle_rank import local_cycle_rank

def run():
    for k in [5, 10, 20]:
        adj = permutation_lift(k)
        colors = wl3_refine(adj, rounds=3)
        hom = wl3_is_homogeneous(colors)
        rank = local_cycle_rank(adj, R=3, ell=6)
        degs = sorted({len(adj[v]) for v in adj})
        print(
            "k=", k,
            "n=", len(adj),
            "deg=", degs,
            "WL3_hom=", hom,
            "cycle_rank=", rank
        )

if __name__ == "__main__":
    run()

