class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)-1
        while end > 0 and nums[end] <= nums[end-1]:
            end -= 1
        
        if end > 0:
            pointer = len(nums)-1
            while nums[pointer] <= nums[end-1]:
                pointer -= 1
            
            nums[end-1], nums[pointer] = nums[pointer], nums[end-1]
            
        nums[end:] = reversed(nums[end:])