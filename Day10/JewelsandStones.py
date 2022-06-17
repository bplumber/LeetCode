from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dick = dict(Counter(stones))
        st = set(dick.keys()).intersection(set(jewels))
        ct = 0
        for i in st:
            ct+=dick[i]
        return ct