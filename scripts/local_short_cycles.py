from collections import deque

def ball_vertices(adj, root, R):
    seen = {root}
    q = deque([(root,0)])
    while q:
        v,d = q.popleft()
        if d == R:
            continue
        for u in adj[v]:
            if u not in seen:
                seen.add(u)
                q.append((u,d+1))
    return seen

def count_cycles_len_k_in_ball(adj, root, R, k):
    # brute-force DFS counting simple cycles of length k passing through root, restricted to ball
    B = ball_vertices(adj, root, R)
    Bset = set(B)

    count = 0
    def dfs(path, last):
        nonlocal count
        if len(path) == k:
            if root in adj[last]:
                count += 1
            return
        for nxt in adj[last]:
            if nxt not in Bset:
                continue
            if nxt in path:
                continue
            dfs(path+[nxt], nxt)

    for nb in adj[root]:
        if nb in Bset:
            dfs([root, nb], nb)

    # each cycle counted twice (two directions)
    return count // 2

def max_short_cycles(adj, R, k):
    best = 0
    arg = 0
    for v in adj:
        c = count_cycles_len_k_in_ball(adj, v, R, k)
        if c > best:
            best = c
            arg = v
    return best, arg

