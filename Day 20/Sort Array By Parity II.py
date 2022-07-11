class Solution:
    def sortArrayByParityII(self, nums):
        for i in range(len(nums)-1):
            if i%2==0:
                if nums[i]%2!=0:
                    j = i+1
                    while nums[j]%2 != 0:
                        j+=1
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                if nums[i]%2 == 0:
                    j=i+1
                    while nums[j]%2==0:
                        j+=1
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
            