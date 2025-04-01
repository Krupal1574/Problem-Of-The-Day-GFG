class Solution:
    def isWordExist(self, b, w):
        def dfs(i, j, k):
            if k == len(w): return True
            if i < 0 or j < 0 or i >= len(b) or j >= len(b[0]) or b[i][j] != w[k]: return False
            t, b[i][j] = b[i][j], '#'
            f = any(dfs(i + dx, j + dy, k + 1) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])
            b[i][j] = t
            return f

        return any(dfs(i, j, 0) for i in range(len(b)) for j in range(len(b[0])) if b[i][j] == w[0])