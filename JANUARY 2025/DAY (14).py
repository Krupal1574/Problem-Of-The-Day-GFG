class Solution:
    def findEquilibrium(self, arr):
        total, prefix = sum(arr), 0
        for i, val in enumerate(arr):
            total -= val
            if prefix == total:
                return i
            prefix += val
        return -1