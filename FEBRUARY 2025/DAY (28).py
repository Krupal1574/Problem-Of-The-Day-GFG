class Solution:
    def evaluate(self, arr):
        st = []
        for s in arr:
            if s in {"+", "-", "*", "/"}:
                b, a = st.pop(), st.pop()
                if s == "+": st.append(a + b)
                elif s == "-": st.append(a - b)
                elif s == "*": st.append(a * b)
                else: st.append(int(a / b))
            else:
                st.append(int(s))
        return st[-1]