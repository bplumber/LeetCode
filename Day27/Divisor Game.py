class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [-1]*1001
        def hlp(n):
            if n==1:
                return 0
            if dp[n]!=-1:
                    return dp[n]
            for i in range(1,int(n**(1/2))+1):
                if n%i==0:
                    if hlp(n-i)==0:
                        dp[n]=1
                        return 1
            dp[n]=0
            return 0
        
        return hlp(n)