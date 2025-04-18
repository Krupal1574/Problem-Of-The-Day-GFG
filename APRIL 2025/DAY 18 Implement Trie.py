class Trie:
    class N:
        def __init__(self): self.c, self.e = [None]*26, 0
    def __init__(self): self.r = self.N()
    def insert(self, w):
        n = self.r
        for ch in w:
            i = ord(ch)-97
            n.c[i] = n.c[i] or self.N()
            n = n.c[i]
        n.e = 1
    def search(self, w):
        n = self.r
        for ch in w:
            i = ord(ch)-97
            if not n.c[i]: return 0
            n = n.c[i]
        return n.e
    def isPrefix(self, w):
        n = self.r
        for ch in w:
            i = ord(ch)-97
            if not n.c[i]: return 0
            n = n.c[i]
        return 1
