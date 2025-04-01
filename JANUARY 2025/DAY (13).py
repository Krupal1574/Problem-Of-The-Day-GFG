class Solution:
    def maxWater(self, arr):
        l, r, res = 0, len(arr) - 1, 0
        while l < r:
            res = max(res, (r - l) * (arr[l] if arr[l] < arr[r] else arr[r]))
            l, r = (l + 1, r) if arr[l] < arr[r] else (l, r - 1)
        return res