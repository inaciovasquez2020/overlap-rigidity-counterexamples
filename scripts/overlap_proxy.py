def triangle_count(adj):
    n = len(adj)
    tri = 0
    for a in range(n):
        Na = set(adj[a])
        for b in adj[a]:
            if b <= a:
                continue
            Nb = set(adj[b])
            tri += len(Na & Nb)
    return tri // 3  # each triangle counted 3 times

def max_triangles_through_vertex(adj):
    n = len(adj)
    best = 0
    for v in range(n):
        Nv = set(adj[v])
        tv = 0
        for a in Nv:
            for b in Nv:
                if a < b and a in adj[b]:
                    tv += 1
        best = max(best, tv)
    return best

