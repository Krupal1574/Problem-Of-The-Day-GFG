class Solution:
    def mirror(self, root):
        if not root:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left