nums = [1,2,2,4]
print([sum(nums)-sum(list(set(nums))), int((len(nums)*(len(nums)+1))/2-sum(list(set(nums))))])