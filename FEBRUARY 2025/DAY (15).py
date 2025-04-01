class Solution:
    def LCA(self, root, n1, n2):
        while root and (root.data > max(n1.data, n2.data) or root.data < min(n1.data, n2.data)):
            root = root.left if root.data > n1.data else root.right
        return root