class Solution:
    def findMaxProduct(self,a, n):
        a.sort()
        mod=1000000000+7
        if len(a)==1:
            return a[0]
        if len(a)==2:
            if max(a)==0:
                return 0
        neg = 0
        for i in a:
            if i < 0:
                neg+=1
        x = 1
        if neg%2==0:
            for i in a:
                if i!=0:
                    x=(x*i)%mod
        else:
            j = 0
            for i in range(neg-1):
                x=(x*a[i])%mod
                j+=1
            for i in range(j+1,len(a)):
                if a[i]!=0:
                    x=(x*a[i])%mod
        return x
