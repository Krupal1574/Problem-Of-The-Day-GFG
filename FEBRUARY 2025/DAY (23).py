class Solution:
    def nextLargerElement(self, arr):
        s = []
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            while s and s[-1] <= val:
                s.pop()
            arr[i] = -1 if not s else s[-1]
            s.append(val)
        return arr