# local_cycle_rank.py
# Local cycle-rank proxy for bounded-radius neighborhoods.
# Graph format: adjacency dict {v: set(neighbors)}

from collections import deque

def bfs_ball(adj, root, R):
    """
    Return induced subgraph on vertices within distance <= R of root.
    """
    dist = {root: 0}
    q = deque([root])
    while q:
        v = q.popleft()
        if dist[v] == R:
            continue
        for u in adj[v]:
            if u not in dist:
                dist[u] = dist[v] + 1
                q.append(u)
    verts = set(dist.keys())
    sub = {v: set(adj[v]) & verts for v in verts}
    return sub

def count_edges(adj):
    """
    Count undirected edges in adjacency dict.
    """
    return sum(len(adj[v]) for v in adj) // 2

def connected_components(adj):
    """
    Number of connected components.
    """
    seen = set()
    comps = 0
    for v in adj:
        if v in seen:
            continue
        comps += 1
        stack = [v]
        seen.add(v)
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return comps

def cycle_rank(adj):
    """
    Cycle rank = E - V + C (cyclomatic number).
    """
    V = len(adj)
    if V == 0:
        return 0
    E = count_edges(adj)
    C = connected_components(adj)
    return E - V + C

def local_cycle_rank(adj, R):
    """
    Max cycle rank over all radius-R balls.
    """
    max_rank = 0
    for v in adj:
        ball = bfs_ball(adj, v, R)
        r = cycle_rank(ball)
        if r > max_rank:
            max_rank = r
    return max_rank

def local_cycle_rank_profile(adj, R):
    """
    Return dict v -> cycle_rank(ball(v,R)).
    """
    prof = {}
    for v in adj:
        ball = bfs_ball(adj, v, R)
        prof[v] = cycle_rank(ball)
    return prof

if __name__ == "__main__":
    # sanity check: cycle C4
    adj = {
        0: {1, 3},
        1: {0, 2},
        2: {1, 3},
        3: {0, 2},
    }
    print("local cycle rank R=1:", local_cycle_rank(adj, 1))
    print("local cycle rank R=2:", local_cycle_rank(adj, 2))

