class Solution:
    def longestPalin(self, s):
        ct = 0
        tp = ""
        def chk(i):
            nonlocal ct, tp
            l = i
            r = i
            while l>0 and r<len(s)-1 and s[l-1]==s[r+1]:
                l-=1
                r+=1
            if len(s[l:r+1])>ct:
                tp = s[l:r+1]
                ct = len(s[l:r+1])
            if len(s)>1 and i+1<len(s) and s[i]==s[i+1]:
                l = i
                r = i+1
                while l>0 and r<len(s)-1 and s[l-1]==s[r+1]:
                    l-=1
                    r+=1
                if len(s[l:r+1])>ct:
                    tp = s[l:r+1]
                    ct = len(s[l:r+1])
                    # print(tp, i)
            
        for i in range(len(s)):
            chk(i)
        
        return tp