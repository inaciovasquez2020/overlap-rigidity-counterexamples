def star_of_triangles(m):
    # vertex 0 is the hub
    adj = {0: []}
    v = 1
    for i in range(m):
        a, b = v, v+1
        adj.setdefault(a, [])
        adj.setdefault(b, [])
        adj[0].extend([a, b])
        adj[a].extend([0, b])
        adj[b].extend([0, a])
        v += 2
    return adj

