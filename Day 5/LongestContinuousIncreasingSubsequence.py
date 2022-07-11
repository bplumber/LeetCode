from collections import Counter
nums = [2,2,3,4]
nums = [1,3,5,4,7]
nums = [2,2,2,2]
nums = [1,3]
nums = [1,2,5,8,0]
sums = []
sum = 0
for i in range(len(nums)-1):
    if nums[i+1]>nums[i]:
        sum = (nums[i+1]-nums[i])
    else:
        sum = '-'
    sums.append(sum)
main = []
temp = []
for i in sums:
    if i == '-':
        main.append(temp)
        temp = []
    else:
        temp.append(i)
main.append(temp)
print(max(map(len, main))+1)