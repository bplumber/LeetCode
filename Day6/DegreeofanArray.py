from collections import Counter
nums = [1,2,2,3,1]
dick = dict(Counter(nums))
mx = max(dick.values())
k_mx = []
for k,v in dick.items():
    if v == mx:
        k_mx.append(k)
mn = len(nums)
for i in k_mx:
    a = nums.index(i)
    nums_reverse = nums.copy()
    nums_reverse.reverse() 
    b = len(nums) - nums_reverse.index(i) - 1
    if (b-a+1) < mn:
        mn = b-a+1
print(mn)