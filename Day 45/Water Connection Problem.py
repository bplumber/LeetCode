    class Solution:
        def solve(self, n, p ,a, b, d):
            i = 0
            while i < p:
                flag = 0
                for j in range(p):
                    if i!=j and a[j]!=0:
                        if a[i]==b[j]:
                            a[i] = a[j]
                            a[j] = 0
                            b[j] = 0
                            flag = 1
                            d[i] = min(d[i], d[j])
                            break
                        elif b[i] == a[j]:
                            b[i] = b[j]
                            a[j] = 0
                            b[j] = 0
                            flag = 1
                            d[i] = min(d[i], d[j])
                            break
                if flag == 0:
                    i+=1
            rt = []
            for i in range(p):
                if a[i]!=0 and a[i]!=b[i]:
                    rt.append([a[i], b[i], d[i]])
            return sorted(rt)