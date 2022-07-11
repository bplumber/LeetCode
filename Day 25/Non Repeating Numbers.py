#User function Template for python3

class Solution:
	def singleNumber(self, nums):
	    nums.sort()
		n = []
		i = 0
	    j = 1
	   	while i < len(nums)-2 and j < len(nums)-1:
		    if nums[i] == nums[j]:
		        i+=2
		        j+=2
		    else:
		        n.append(nums[i])
		        i+=1
		        j+=1
	    if len(n)==0:
	        n.append(nums[-2])
	        n.append(nums[-1])
	    elif len(n)==1:
	        n.append(nums[-1])
	    return n[0], n[1]