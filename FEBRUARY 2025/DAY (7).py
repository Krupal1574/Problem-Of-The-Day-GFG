class Solution:
    def inOrder(self, root):
        a = []
        def f(r):
            if r:
                f(r.left)
                a.append(r.data)
                f(r.right)
        f(root)
        return a