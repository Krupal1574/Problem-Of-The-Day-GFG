class Solution:
    def buildTree(self, inorder, preorder):
        m = {v: i for i, v in enumerate(inorder)}
        self.i = 0
        def f(l, r):
            if l > r:
                return None
            root = Node(preorder[self.i])
            self.i += 1
            pos = m[root.data]
            root.left = f(l, pos - 1)
            root.right = f(pos + 1, r)
            return root
        return f(0, len(inorder) - 1)