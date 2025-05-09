#User function Template for python3

class Solution:
    
    # Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        s = list(s)
        result = s[:]
        
        def dfs(index, k):
            nonlocal result
            if k == 0 or index == len(s):
                return

            # Find the maximum digit from current index onward
            max_digit = max(s[index:])
            
            # If current digit is already the max, move to next position
            if s[index] == max_digit:
                dfs(index + 1, k)
                return

            # Try swapping current index with all positions i > index where digit == max_digit
            for i in range(len(s) - 1, index, -1):
                if s[i] == max_digit:
                    # Swap
                    s[index], s[i] = s[i], s[index]
                    
                    # Update result if new string is larger
                    current = ''.join(s)
                    if current > ''.join(result):
                        result = current
                    
                    # Recurse
                    dfs(index + 1, k - 1)
                    
                    # Backtrack
                    s[index], s[i] = s[i], s[index]

        dfs(0, k)
        return ''.join(result)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends
