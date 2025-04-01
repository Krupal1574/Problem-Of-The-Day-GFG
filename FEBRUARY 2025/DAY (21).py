class Solution:
    def isBalanced(self, s):
        st = []
        for c in s:
            if c in "({[": st.append(c)
            elif not st or abs(ord(st[-1]) - ord(c)) > 2: return False
            else: st.pop()
        return not st