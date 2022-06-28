class Solution:
    def countAndSay(self, n: int) -> str:
        x = 0
        while x < n:
            x+=1
            if x == 1:
                s = '1'
            else:
                tp = ''
                i = 0
                j = i+1
                while j!=len(s):
                    if s[i]!=s[j]:
                        tp+=str(j-i)
                        tp+=str(s[i])
                        i = j
                    j+=1
                tp+=str(j-i)
                tp+=(str(s[i]))
                s = tp
        return s    