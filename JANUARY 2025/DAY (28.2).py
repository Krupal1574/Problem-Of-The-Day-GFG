class Solution:
    def findPermutation(self, s):
        s, res = ''.join(sorted(s)), []
        while s:
            res.append(s)
            s = self.next(s)
        return res

    def next(self, s):
        s = list(s)
        i = len(s) - 2
        while i >= 0 and s[i] >= s[i + 1]: i -= 1
        if i < 0: return None
        j = len(s) - 1
        while s[j] <= s[i]: j -= 1
        s[i], s[j] = s[j], s[i]
        return ''.join(s[:i + 1] + s[i + 1:][::-1])