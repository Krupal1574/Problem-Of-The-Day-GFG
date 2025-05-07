class Solution:
    def Paths(self, root):
        res, curr = [], []
        def dfs(n):
            if not n: return
            curr.append(n.data)
            if not n.left and not n.right:
                res.append(curr.copy())
            else:
                dfs(n.left); dfs(n.right)
            curr.pop()
        dfs(root)
        return res
