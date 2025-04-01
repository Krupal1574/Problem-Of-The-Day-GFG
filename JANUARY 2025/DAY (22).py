class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def addTwoLists(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        dummy = Node(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            summ = carry
            if l1:
                summ += l1.data
                l1 = l1.next
            if l2:
                summ += l2.data
                l2 = l2.next
            carry = summ // 10
            tail.next = Node(summ % 10)
            tail = tail.next

        res = self.reverse(dummy.next)
        while res and res.data == 0 and res.next:
            res = res.next
        return res