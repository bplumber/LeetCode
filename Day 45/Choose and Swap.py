
class Solution:
    def chooseandswap (self, q):
        st = set()
        for i in q:
            st.add(i)
        st = sorted(list(st))
        a = []
        for i in q:
            a.append(i)
        for i in a:
            if i in st:
                st.remove(i)
            else:
                pass
            if len(st)==0:
                break
            x = st[0]
            if ord(x)<ord(i):
                for j in range(len(a)):
                    if a[j]==x:
                        a[j]=i
                    elif a[j]==i:
                        a[j]=x
                break
        return ''.join(a)