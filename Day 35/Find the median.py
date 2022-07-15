class Solution:
	def find_median(self, v):
		v.sort()
		if len(v)%2!=0:
		    return v[len(v)//2]
	    else:
		    f = v[len(v)//2]
		    s = v[(len(v)//2)-1]
	        return (f+s)//2