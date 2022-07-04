class Solution:
	def valueEqualToIndex(self,arr, n):
		rt = []
		for i in range(n):
		    if i+1 == arr[i]:
		        rt.append(i+1)
	    return rt
