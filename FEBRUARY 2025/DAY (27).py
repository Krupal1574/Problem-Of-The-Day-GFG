class Solution:
    def __init__(self):
        self.s, self.m = [], []

    def push(self, x):
        self.s.append(x)
        self.m.append(x if not self.m else min(x, self.m[-1]))

    def pop(self):
        if self.s: self.s.pop(), self.m.pop()

    def peek(self):
        return -1 if not self.s else self.s[-1]

    def getMin(self):
        return -1 if not self.m else self.m[-1]