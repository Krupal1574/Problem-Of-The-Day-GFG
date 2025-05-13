class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        
        # Optimization: C(n, r) == C(n, n - r)
        r = min(r, n - r)
        
        result = 1
        for i in range(1, r + 1):
            result = result * (n - r + i) // i
        
        return result

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends
