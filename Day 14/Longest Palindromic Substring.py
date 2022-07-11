class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        mxs = ""
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > mx:
                    mxs = s[l:r+1]
                    mx = r-l+1
                l-=1
                r+=1
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > mx:
                    mxs = s[l:r+1]
                    mx = r-l+1
                l-=1
                r+=1
        return mxs