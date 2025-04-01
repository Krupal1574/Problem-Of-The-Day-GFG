class Solution:
    def getMedian(self, arr):
        maxHeap, minHeap = [], []
        res = []

        for num in arr:
            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            if len(maxHeap) < len(minHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

            res.append(float(-maxHeap[0]) if len(maxHeap) > len(minHeap) else (-maxHeap[0] + minHeap[0]) / 2.0)
        
        return res