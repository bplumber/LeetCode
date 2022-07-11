class Solution:
    def pivotIndex(self, nums):
        rt = [-1]
        l = 0
        r = len(nums)-1
        def help(nums, l, r):
            nonlocal rt
            if l < r:
                mid = (l+r)//2
                if sum(nums[:mid]) == sum(nums[mid+1:]):
                    rt.append(mid)
                help(nums, l, mid)
                help(nums, mid+1, r)
                return rt
        help(nums, 0, len(nums)-1)
        if sum(nums[:len(nums)-1])==0:
            rt.append(len(nums)-1)
        if len(rt)>1:
            rt = rt[1:]
        return min(rt)

#ALTERNATE SOLUTION

class Solution:
    def pivotIndex(self, nums):
        p = []
        for i in range(len(nums)):
            if i==0:
                p.append(nums[i])
            else:
                p.append(p[i-1]+nums[i])
        rt = -1
        for i in range(len(p)):
            if p[i] - nums[i] == p[len(p)-1] - p[i]:    
                return i
        return rt
    