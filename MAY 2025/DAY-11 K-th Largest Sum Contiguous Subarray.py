from typing import List
import heapq

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        min_heap = []
        
        n = len(arr)
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, curr_sum)
                else:
                    if curr_sum > min_heap[0]:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, curr_sum)
        
        return min_heap[0] 



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends
