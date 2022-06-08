nums = [1,4,3,2]
nums.sort()
temp = 0
for i in range(0,len(nums),2):
  temp+=nums[i]
print(temp)