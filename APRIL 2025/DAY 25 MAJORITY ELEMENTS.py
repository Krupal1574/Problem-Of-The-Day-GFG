

class Solution:
    def majorityElement(self, arr):
        # Step 1: Find the candidate using Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        
        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Step 2: Verify if the candidate is indeed the majority element
        count = 0
        for num in arr:
            if num == candidate:
                count += 1
        
        if count > len(arr) // 2:
            return candidate
        else:
            return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends