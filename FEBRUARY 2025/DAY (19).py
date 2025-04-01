class Solution:
    def mergeKLists(self, lists):
        heap = [(node.data, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = tail = Node(0)
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next, tail = node, node
            if node.next:
                heapq.heappush(heap, (node.next.data, i, node.next))
        return dummy.next