class Solution:
    def floydWarshall(self, d):
        n, inf = len(d), 100000000
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k] < inf and d[k][j] < inf and d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
