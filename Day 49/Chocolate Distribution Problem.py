class Solution:

    def findMinDiff(self, a,n,m):
        a.sort()
        mn = a[m-1]-a[0]
        x = mn
        i = 1
        j = i+m-1
        while j < n:
            x = a[j]-a[i]
            if x<mn:
                mn = x
            i+=1
            j+=1
        return mn