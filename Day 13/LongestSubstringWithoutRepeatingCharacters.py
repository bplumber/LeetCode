class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        tp = ""
        mx = 0
        for i in range(len(s)):
            if s[i] not in tp:
                tp+=s[i]
            else:
                if len(tp)>mx:
                    mx = len(tp)
                while s[i] in tp:
                    tp = tp[1:]
                tp+=s[i]
        if len(tp)>mx:
            mx = len(tp)
        if len(tp)==len(s):
            return len(s)
        return mx