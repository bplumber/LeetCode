class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        res = []
        for i in s1:
            if i not in s2:
                res.append(i)
        for i in s2:
            if i not in s1:
                res.append(i)
        temp = []
        for i in res:
            if s2.count(i) == 1 or s1.count(i) == 1:
                temp.append(i)
        return temp