class Solution:
    def missingNum(self, arr):
        x = 0
        for i, v in enumerate(arr):
            x ^= v ^ (i + 1)
        return x ^ (len(arr) + 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends