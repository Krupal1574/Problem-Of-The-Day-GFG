class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                c = 1
                while (fast := fast.next) != slow:
                    c += 1
                return c
        return 0