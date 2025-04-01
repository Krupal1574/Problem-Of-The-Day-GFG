class Solution:
    def getMaxArea(self, arr):
        stack, n, res = [], len(arr), 0
        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                h = arr[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res