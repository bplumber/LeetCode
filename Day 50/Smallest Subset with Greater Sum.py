class Solution:
    def minSubset(self, a,n):
        a.sort()
        sm = sum(a)
        mx = 0
        ct = 0 
        for i in range(n-1,-1,-1):
            mx+=a[i]
            sm-=a[i]
            ct+=1
            if mx > sm:
                break
        return ct