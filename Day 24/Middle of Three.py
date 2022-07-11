class Solution:
    def middle(self,A,B,C):
        if A>B and A>C:
            return max(B,C)
        if B>A and B>C:
            return max(A,C)
        return max(A,B)