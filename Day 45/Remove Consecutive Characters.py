class Solution:
    def removeConsecutiveCharacter(self, s):
        x = s[0]
        i, j = 0, 0
        while j < len(s):
            if s[i]==s[j]:
                j+=1
            else:
                i = j
                x+=s[i]
        return x