class Solution:
    def thirdLargest(self,a, n):
        a.sort()
        if len(a)<3:
            return -1
        return a[-3]
