class Solution:
    def majorityElement(self, a, n):
        if len(a)==1:
            return a[0]
        ct = 1
        mxel = -1
        a.sort()
        for i in range(1,n):
            if a[i-1]==a[i]:
                ct+=1
                if ct>int(n/2):
                    mxel = a[i]
            else:
                ct = 1
        return mxel