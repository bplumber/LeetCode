class Solution:
	def editDistance(self, s, t):
		m = len(s)
        n = len(t)
        grid = []
        for i in range(m+1):
            temp = []
            for j in range(n+1):
                temp.append(0)
            grid.append(temp)
            
        for i in range(len(grid[0])):
            grid[0][i] = i
        for i in range(len(grid)):
            grid[i][0] = i
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1]) + 1
        
        return grid[m][n]