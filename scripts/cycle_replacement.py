def cycle_replacement(base_adj, L):
    # Replace each base vertex v by a cycle (v,0)...(v,L-1)
    # For each base edge (u,v), connect (u,0) -- (v,0)
    # Degree becomes deg_base(v)+2 at (v,0), and 2 elsewhere in the fiber.
    # This is not fully regular; it's a controlled locality stressor.

    base_vertices = sorted(base_adj.keys())
    idx = {v:i for i,v in enumerate(base_vertices)}
    nB = len(base_vertices)
    n = nB * L

    def node(v, i):
        return idx[v]*L + i

    adj = {k: [] for k in range(n)}

    # fiber cycles
    for v in base_vertices:
        for i in range(L):
            a = node(v,i)
            b = node(v,(i+1)%L)
            adj[a].append(b)
            adj[b].append(a)

    # lift base edges via port 0
    seen = set()
    for u in base_vertices:
        for v in base_adj[u]:
            a,b = sorted((u,v))
            if (a,b) in seen:
                continue
            seen.add((a,b))
            uu = node(u,0)
            vv = node(v,0)
            adj[uu].append(vv)
            adj[vv].append(uu)

    return adj

