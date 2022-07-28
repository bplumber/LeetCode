class Solution:

    def candyStore(self, candies,n,k):
        candies.sort()
        bt = 0
        i = 0
        mn = 0
        mx = 0
        while bt<n:
            mn+=candies[i]
            mx+=candies[n-1-i]
            bt+=(1+k)
            i+=1
        return [mn, mx]