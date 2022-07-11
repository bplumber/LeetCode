class Solution:
    def countSquares(self, N):
        ct = 0
        chk = N**(1/2)
        if (chk*10)%10 == 0:
            return int(chk) - 1
        else:
            return int(chk)