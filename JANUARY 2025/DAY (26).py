class Solution:
    def removeLoop(self, head):
        visited = set()
        prev = None

        while head:
            # If the node is already visited, break the loop
            if head in visited:
                prev.next = None
                break
            visited.add(head)  # Mark the current node as visited
            prev = head
            head = head.next