from base_graphs import K4
from permutation_lift import permutation_lift
from local_short_cycles import max_short_cycles

for kLift in [5,10,20,40]:
    adj = permutation_lift(K4(), kLift, seed=1)
    for (R,ell) in [(2,3),(2,4),(3,5),(3,6)]:
        best, v = max_short_cycles(adj, R, ell)
        print(f"k={kLift} R={R} ell={ell} max_cycles={best}")

