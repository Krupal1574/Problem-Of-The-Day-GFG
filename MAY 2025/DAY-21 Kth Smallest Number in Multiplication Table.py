class Solution(object):
    def kthSmallest(self, m, n, k):
        def count_less_equal(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count
        
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
