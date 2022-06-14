class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.reverse()
        while len(bits)>1:
            if bits[-1]==1:
                bits.pop()
                bits.pop()
            elif bits[-1]==0:
                bits.pop()
        if len(bits)==1:
            return True
            