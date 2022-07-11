# Solution 1

nums = [1,2,3,4]
numss = nums.copy()
if max(nums) > 0:
    a = max(nums, key=abs)
    if abs(a) in nums:
        a = abs(a)
    nums.remove(a)
    b = max(nums, key=abs)
    if abs(b) in nums:
        b = abs(b)
    nums.remove(b)
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        c = max(nums)
    else:
        c = max(nums, key=abs)
else:
    a = max(nums)
    nums.remove(a)
    b = max(nums)
    nums.remove(b)
    c = max(nums)
    nums.remove(c)
d,e,f=0,0,0
if min(numss)<0:
    d = min(numss)
    numss.remove(d)
if min(numss)<0:
    e = min(numss)
    numss.remove(e)
f = max(numss)
print(max(a*b*c, d*e*f))

# Solution 2
num = [1,2,3,4]
num.sort()
print(max(num[0]*num[1]*num[-1],num[-1]*num[-2]*num[-3]))
