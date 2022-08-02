class Solution:
    def findMinSum(self, a,b,n):
        a.sort()
        b.sort()
        mn = 0
        for i, j in zip(a,b):
            mn += abs(i-j)
        return mn