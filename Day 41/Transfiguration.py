class Solution:
    def transfigure(self, s, t):
        if len(s)!=len(t):
            return -1
        sm = 0
        for i in range(len(s)):
            sm+=ord(s[i])
            sm-=ord(t[i])
        if sm!=0:
            return -1
        res = 0
        i = len(s)-1
        j = i
        while i >= 0 and j >= 0:
            if s[i]!=t[j]:
                res+=1
            else:
                j-=1
            i-=1
        return res
