class Solution:
    def leftRight(self, arr, n):
        if max(arr)>=n:
            return 0
        rt = 1
        x = [-1]*n
        for i in arr:
            if x[i]==-1:
                x[i]=i
            elif x[n-i-1]==-1:
                x[n-i-1] = i
            else:
                rt = 0
        return rt