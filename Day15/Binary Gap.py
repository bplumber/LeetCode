class Solution:
    def binaryGap(self, n: int) -> int:
        s = str(bin(n))[2:]
        dif = 0
        prev = 0
        for i in range(len(s)):
            if s[i]=='1':
                if dif <= i - prev:
                    dif = i - prev
                prev = i
        return dif