class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        res = [root.data] if root.left or root.right else []

        cur = root.left
        while cur:
            if cur.left or cur.right:
                res.append(cur.data)
            cur = cur.left if cur.left else cur.right

        def leaf_nodes(node):
            if not node:
                return
            leaf_nodes(node.left)
            if not node.left and not node.right:
                res.append(node.data)
            leaf_nodes(node.right)

        leaf_nodes(root)

        right_boundary = []
        cur = root.right
        while cur:
            if cur.left or cur.right:
                right_boundary.append(cur.data)
            cur = cur.right if cur.right else cur.left

        res += reversed(right_boundary)
        return res