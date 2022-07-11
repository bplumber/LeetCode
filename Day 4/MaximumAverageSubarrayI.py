nums = [1,12,-5,-6,50,3] 
k = 4
mx = current = sum(nums[:k])
for i in range(k,len(nums)):
    current += nums[i] - nums[i-k]
    if current>mx:
        mx = current
print(mx/k)