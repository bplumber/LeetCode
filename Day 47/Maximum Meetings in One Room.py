from typing import List


class Solution:
    def maxMeetings(self, n : int, s : List[int], f : List[int]) -> List[int]:
        lt = []
        for i in range(n):
            lt.append([f[i],s[i], i+1])
        ans = []
        lt.sort(key=lambda val:val[0])
        ans.append(lt[0][2])
        lim = lt[0][0]
        for i in range(1,n):
            if lt[i][1]>lim:
                ans.append(lt[i][2])
                lim = lt[i][0]
        ans.sort()
        return ans