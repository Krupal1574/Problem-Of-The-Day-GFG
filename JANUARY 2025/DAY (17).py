class Solution:
    def productExceptSelf(self, arr):
        product, zero_count = 1, arr.count(0)
        if zero_count > 1:
            return [0] * len(arr)
        for x in arr:
            if x != 0:
                product *= x
        return [product if x == 0 else 0 if zero_count else product // x for x in arr]