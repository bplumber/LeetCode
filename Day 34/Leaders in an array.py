class Solution:
    def leaders(self, a, n):
        ans = []
        mx = a[-1]
        ans.append(mx)
        for i in range(n-2,-1,-1):
           if  a[i] >= mx:
               ans.append(a[i])
               mx = a[i]
        return ans[::-1]