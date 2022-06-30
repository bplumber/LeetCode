class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        x = []
        for i in s:
            x.append(i)
        l = 0
        r = len(s)-1 
        while l < r:
            if x[l].isalpha() == True and x[r].isalpha() == True:
                x[l], x[r] = x[r], x[l]
                l+=1
                r-=1
            elif x[l].isalpha() == False and x[r].isalpha() == True:
                l+=1
            elif x[l].isalpha() == True and x[r].isalpha() == False:
                r-=1
            elif x[l].isalpha() == False and x[r].isalpha() == False:
                l+=1
                r-=1
        return ''.join(x)