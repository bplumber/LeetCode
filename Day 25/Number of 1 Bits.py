class Solution:
	def setBits(self, N):
		return str(bin(N)).count('1')