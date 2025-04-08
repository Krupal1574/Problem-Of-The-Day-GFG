class Solution:
    def dfs(self, g, vis, u):
        vis[u] = 1
        for v in g[u]:
            if not vis[v]: self.dfs(g, vis, v)

    def isBridge(self, V, edges, c, d):
        g = [[] for _ in range(V)]
        for u, v in edges:
            if (u, v) != (c, d) and (v, u) != (c, d):
                g[u].append(v)
                g[v].append(u)
        vis = [0] * V
        self.dfs(g, vis, c)
        return not vis[d]
