def regular_cycle_lift(base_adj, L):
    """
    Replace each base vertex v by a cycle of length L.
    For each base edge (u,v), connect fibers using a perfect matching
    between the cycles so that every vertex has the same degree.
    """

    base_vertices = sorted(base_adj.keys())
    nB = len(base_vertices)
    idx = {v:i for i,v in enumerate(base_vertices)}

    def node(v,i):
        return idx[v]*L + i

    n = nB * L
    adj = {k: [] for k in range(n)}

    # fiber cycles
    for v in base_vertices:
        for i in range(L):
            a = node(v,i)
            b = node(v,(i+1)%L)
            adj[a].append(b)
            adj[b].append(a)

    # distribute base edges evenly around the cycle
    for u in base_vertices:
        du = len(base_adj[u])
        ports = list(range(L))
        for j,v in enumerate(base_adj[u]):
            i = ports[j % L]
            a = node(u,i)
            b = node(v,(i+L//2)%L)
            adj[a].append(b)
            adj[b].append(a)

    return adj

