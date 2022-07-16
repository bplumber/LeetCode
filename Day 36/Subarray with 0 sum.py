class Solution:
    def subArrayExists(self,arr,n):
        mp = set()
        sm = 0
        for i in range(n):
            sm += arr[i]
            if sm==0 or arr[i] == 0 or sm in mp:
                return True
            mp.add(sm)
        return False         