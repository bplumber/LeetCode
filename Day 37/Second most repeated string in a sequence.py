from collections import Counter
class Solution:
    def secFrequent(self, arr, n):
        dick = dict(Counter(arr))
        mx = sorted(dick.values())[-2]
        for k,v in dick.items():
            if v == mx:
                return k