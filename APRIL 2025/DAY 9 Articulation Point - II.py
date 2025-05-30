class Solution:
    def articulationPoints(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        disc = [-1] * V
        low = [-1] * V
        vis = [False] * V
        ap = [False] * V
        time = [0]

        def dfs(u, p):
            vis[u] = True
            disc[u] = low[u] = time[0] = time[0] + 1
            children = 0
            for v in adj[u]:
                if not vis[v]:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if p != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != p:
                    low[u] = min(low[u], disc[v])
            if p == -1 and children > 1:
                ap[u] = True

        for i in range(V):
            if not vis[i]:
                dfs(i, -1)
        res = [i for i, val in enumerate(ap) if val]
        return res if res else [-1]
