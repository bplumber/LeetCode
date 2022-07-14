class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        dp = []
        for i in range(n):
            dp.append(-1)
        
        def hlp(i):
            if i <= -1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            op1 = a[i]+hlp(i-2)
            op2 = hlp(i-1)
            mx = max(op1, op2)
            dp[i] = mx
            return mx
        
        return hlp(n-1)