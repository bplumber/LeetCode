nums = [ 3, 10, 2, 1, 20 ]
temp = []
for _ in nums:
    temp.append(1)
for i in range(1,len(nums)):
    for j in range(0,i):
        if (nums[i] > nums[j]) and (temp[j]+1>temp[i]):
            temp[i]+=1
print(max(temp))