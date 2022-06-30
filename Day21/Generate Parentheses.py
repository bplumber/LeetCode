class Solution:
    def generateParenthesis(self, n: int):
        s = ''
        ret = []
        
        def backtrack(o, c):
            nonlocal s, ret
            if o == c == n:
                ret.append(s)
                return
            if o < n:
                s+='('
                backtrack(o+1, c)
                s = s[:-1]
            if c<o:
                s+=')'
                backtrack(o, c+1)
                s=s[:-1]
        backtrack(0,0)
        return ret