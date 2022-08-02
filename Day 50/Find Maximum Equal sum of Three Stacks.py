from typing import List


class Solution:
    def maxEqualSum(self, n1:int,n2:int,n3:int, s1 : List[int], s2 : List[int], s3 : List[int]) -> int:
        ss1 = sum(s1)
        ss2 = sum(s2)
        ss3 = sum(s3)
        i,j,k = 0,0,0
        fnd = 0
        while (i < n1 and j < n2 and k<n3):
            mx = max(ss1,ss2,ss3)
            if ss1 == ss2 == ss3:
                fnd = ss1
                break
            if ss1 == mx:
                if i < n1:
                    ss1-=s1[i]
                i+=1
            elif ss2 == mx:
                if j < n2:
                    ss2-=s2[j]
                j+=1
            elif ss3 == mx:
                if k < n3:
                    ss3-=s3[k]
                k+=1
        return fnd