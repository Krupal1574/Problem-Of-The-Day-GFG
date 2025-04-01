class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        res = []
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            if i >= k - 1:
                res.append(len(freq))
                freq[arr[i - k + 1]] -= 1
                if freq[arr[i - k + 1]] == 0:
                    del freq[arr[i - k + 1]]
        return res