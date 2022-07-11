class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # main = set()
        # nums.sort()
        # print(nums)
        # for i in range(0,len(nums)-2):
        #     for j in range(i,len(nums)-1):
        #         for k in range(j,len(nums)):
        #             if i!=j and j!=k and i!=k:
        #                 if nums[i]+nums[j]+nums[k]==0:
        #                     main.add(tuple([nums[i],nums[j],nums[k]]))
        # return main
        main = []
        nums.sort()
        i=0
        while i < len(nums)-3:
            target = -nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]==target:
                    mains.append(nums[i],nums[l], nums[r])
                if nums[l]+nums[r]>target:
                    while nums[r-1]==nums[r] and r-1>l:
                        r-=1
                    r-=1
                if nums[l]+nums[r]<target:
                    while nums[l+1]==nums[l] and r>l+1:
                        l+=1
                    l+=1
                while nums[i+1]==nums[i] and i+1<len(nums)-3:
                    i+=1
                i+=1
            return main
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                