from collections import Counter
class Solution:

    def longestKSubstr(self, s, k):
        if len(dict(Counter(s)))<k:
            return -1
        mx = -1
        d = {}
        for i in range(len(s)):
            if len(d)==k:
                ct = sum(d.values())
                if ct>mx:
                    mx=ct
            if len(d)>k:
                ct = sum(d.values())
                for j in range(i-ct, i):
                    d[s[j]]-=1
                    if d[s[j]]==0:
                        d.pop(s[j])
                        break
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        if len(d)==k:
            ct = sum(d.values())
            if ct>mx:
                mx=ct
        return mx