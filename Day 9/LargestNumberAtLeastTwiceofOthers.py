class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind = nums.index(max(nums))
        if len(nums)==1:
            return 0
        max_num = nums.pop(ind)
        if max(nums) <= max_num/2:
            return ind
        else:
            return -1