class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:])==0:
            return 0
        for i in range(len(nums)-2):
            if sum(nums[:i+1]) == sum(nums[i+2:]):
                return i+1
        if sum(nums[:-1])==0:
            return len(nums)-1
        else:
            return -1

# ALTERNATE SOLUTION

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        right_sum = sum(nums)
        
        left_sum = 0
        
        
        for i in range(0,len(nums)):
            right_sum = right_sum - nums[i]
            if (left_sum == right_sum):
                return i
            
            
            left_sum = left_sum + nums[i]
            
        return -1