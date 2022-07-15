class Solution:
    def getPairsCount(self, arr, n, k):
        dick = {}
        ct = 0
        for i in arr:
            if i in dick:
                ct += dick[i]
            if k - i in dick:
                dick[k-i]+=1
            else:
                dick[k-i]=1
        return ct 