class Solution:
    def Maximize(self, a, n): 
        mod = 1000000000+7
        result = 0
        a.sort()
        for i in range(n):
            result = (result + (i*a[i]))%mod
        return result