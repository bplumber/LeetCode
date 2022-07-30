class Solution:
    def subArraySum(self,arr, n, s): 
        if s == 0:
            return [-1]
        i = 0 
        j = 0
        x = arr[0]
        pair = []
        while j < n and i < n:
            if x==s:
                pair = [i+1, j+1]
                break
            elif x < s:
                j+=1
                if j < n:
                    x+=arr[j]
            elif x > s:
                if i < n:
                    x-=arr[i]
                i+=1
        if len(pair)==0:
            return [-1]
        return pair
                