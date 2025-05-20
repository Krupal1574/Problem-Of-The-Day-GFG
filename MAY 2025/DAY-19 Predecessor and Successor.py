class Solution:
    def findPreSuc(self, root, key):
        pre = suc = None
        curr = root
        while curr:
            if curr.data < key:
                pre = curr
                curr = curr.right
            else:
                curr = curr.left
        curr = root
        while curr:
            if curr.data > key:
                suc = curr
                curr = curr.left
            else:
                curr = curr.right
        return [pre, suc]
