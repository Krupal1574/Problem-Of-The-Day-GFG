class Solution:
    def isCycle(self, V, edges):
        p = [-1]*V
        def f(x): return x if p[x]<0 else f(p[x])
        for u,v in edges:
            a, b = f(u), f(v)
            if a == b: return True
            if p[a] > p[b]: a,b = b,a
            p[a] += p[b]; p[b] = a
        return False
