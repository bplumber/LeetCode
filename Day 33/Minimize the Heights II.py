class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        small = arr[0]+k
        large = arr[n-1]-k
        ans = arr[n-1] - arr[0]
        for i in range(n-1):
            mn = min(small, arr[i+1]-k)
            mx = max(large, arr[i]+k)
            if mn < 0:
                continue
            ans = min(ans, mx-mn)
        return ans