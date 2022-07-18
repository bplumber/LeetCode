class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dick = {}
        def hlp(s):
            nonlocal dick
            if len(s)==0:
                return True
            if s in dick:
                return dick[s]
            for i in range(1,len(s)+1):
                if s[0:i] in wordDict and hlp(s[i:]):
                    dick[s[i:]]=True
                    return True
            dick[s]=False
            return False
        
        return hlp(s)