class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        dick = {0:1}
        ans = 0
        p = 0
        for i in arr:
            p+=i
            if p in dick:
                ans+=dick[p]
            if p not in dick:
                dick[p]=1
            else:
                dick[p]+=1
        return ans
        #return: count of sub-arrays having their sum equal to 0