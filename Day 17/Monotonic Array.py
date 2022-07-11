class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        while nums[0]==nums[1]:
            nums = nums[1:]
            if len(nums)==1:
                return True
        if nums[0] > nums[1]:
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
        return True

# Alternate Solution

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n1=sorted(nums)
        if n1==nums or n1==nums[::-1]:
            return True
        return False