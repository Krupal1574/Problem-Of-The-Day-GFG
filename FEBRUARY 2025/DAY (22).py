class Solution:
    def maxLength(self, s):
        st=[-1]; m=0
        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            else:
                st.pop()
                if not st: st.append(i)
                else: m = max(m, i - st[-1])
        return m