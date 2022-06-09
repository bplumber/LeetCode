from collections import Counter
nums = [1,3,2,2,5,2,3,7]
dick = dict(Counter(nums))
temp = []
for i in sorted(dick):
  temp.append([i,dick[i]])
mx = 0
for i in range(len(temp)-1):
  if temp[i][0] == temp[i+1][0]-1:
      if mx < temp[i][1]+temp[i+1][1]:
            mx = temp[i][1]+temp[i+1][1]
print(mx)