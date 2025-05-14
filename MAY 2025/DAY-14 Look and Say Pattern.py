class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        current = "1"
        
        for _ in range(2, n + 1):
            next_term = ""
            i = 0
            while i < len(current):
                count = 1
                # Count how many times the same digit repeats
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    i += 1
                    count += 1
                # Append count and the digit itself
                next_term += str(count) + current[i]
                i += 1
            current = next_term
        
        return current

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends
