# scripts/local_cycle_rank.py
#
# Local cycle-rank / overlap proxies for bounded-radius neighborhoods.
# These are intentionally simple, FO-local, and computable on small graphs.
#
# Graph format: adj : dict[v] -> set of neighbors

from collections import deque, defaultdict

def bfs_ball(adj, root, R):
    """
    Return the induced subgraph on the radius-R ball around root.
    """
    visited = {root: 0}
    q = deque([root])

    while q:
        u = q.popleft()
        if visited[u] == R:
            continue
        for v in adj[u]:
            if v not in visited:
                visited[v] = visited[u] + 1
                q.append(v)

    ball = set(visited.keys())
    sub = {v: set() for v in ball}
    for v in ball:
        for w in adj[v]:
            if w in ball:
                sub[v].add(w)
    return sub


def count_edges(adj):
    """
    Number of undirected edges.
    """
    return sum(len(adj[v]) for v in adj) // 2


def count_vertices(adj):
    return len(adj)


def cycle_rank(adj):
    """
    Cycle rank = |E| - |V| + c,
    where c is number of connected components.
    """
    visited = set()
    comps = 0

    for v in adj:
        if v not in visited:
            comps += 1
            q = deque([v])
            visited.add(v)
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if w not in visited:
                        visited.add(w)
                        q.append(w)

    return count_edges(adj) - count_vertices(adj) + comps


def local_cycle_rank(adj, R):
    """
    Maximum cycle rank over all radius-R balls.
    """
    return max(cycle_rank(bfs_ball(adj, v, R)) for v in adj)


def local_short_cycles(adj, max_len=6):
    """
    Count short cycles through each vertex up to length max_len.
    Very naive DFS-based enumeration; small graphs only.
    """
    def dfs(start, u, depth, visited):
        if depth == 0:
            return 1 if start in adj[u] else 0
        cnt = 0
        for v in adj[u]:
            if v not in visited:
                cnt += dfs(start, v, depth - 1, visited | {v})
        return cnt

    per_v = {}
    for v in adj:
        total = 0
        for ell in range(3, max_len + 1):
            total += dfs(v, v, ell - 1, {v})
        per_v[v] = total // 2  # undirected correction
    return per_v

