from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        if len(deck)==1:
            return False
        dick = dict(Counter(deck))
        temp = dick.values()
        mn = min(temp)
        if mn <= 1:
            return False
        for i in range(2, mn):
            chk = 0
            for j in temp:
                if j%i==0:
                    chk+=1
            if chk == len(temp):
                return True
            chk = 0
        for i in temp:
            if i%mn!=0:
                return False
        return True