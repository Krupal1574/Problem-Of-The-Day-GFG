class Solution:
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head
        current = head
        new_head = None
        tail = None
        while current:
            group_prev = None
            group_curr = current
            count = 0
            while current and count < k:
                next_node = current.next
                current.next = group_prev
                group_prev = current
                current = next_node
                count += 1
            if not new_head:
                new_head = group_prev
            if tail:
                tail.next = group_prev
            tail = group_curr
        return new_head