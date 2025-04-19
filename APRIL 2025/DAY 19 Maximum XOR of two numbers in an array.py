class Solution:
    def maxXor(self, arr):
        class TrieNode:
            __slots__ = ['children']
            def __init__(self):
                self.children = [None, None]
        
        root = TrieNode()
        
        for num in arr:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        max_xor = 0
        for num in arr:
            node = root
            current_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                desired_bit = 1 - bit
                if node.children[desired_bit]:
                    current_xor |= (1 << i)
                    node = node.children[desired_bit]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, current_xor)
        return max_xor
