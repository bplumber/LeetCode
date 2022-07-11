class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sa = sum(aliceSizes)
        sb = sum(bobSizes)
        x = (sb- sa) / 2
        b = set(bobSizes)
        for i in set(aliceSizes):
            if i+x in b:
                return [i, int(i+x)]