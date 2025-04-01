class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        d = {}
        ch = Node(head.data)
        chh = ch
        d[head] = ch

        h = head.next
        while h:
            nn = Node(h.data)
            chh.next = nn
            d[h] = nn
            h = h.next
            chh = nn

        h = head
        chh = ch
        while h:
            if h.random:
                chh.random = d[h.random]
            h = h.next
            chh = chh.next

        return ch