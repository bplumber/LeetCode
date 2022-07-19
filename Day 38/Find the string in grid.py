class Solution:
	def searchWord(self, grid, word):
        def hlp(grid, word, index, r, c, m, n, dir_r, dir_c):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r > m - 1 or c > n - 1:
                return False
            if grid[r][c]==word[index]:
                return hlp(grid, word, index+1, r+dir_r, c+dir_c, m, n, dir_r, dir_c)
            return False
        
        m = len(grid)
        n = len(grid[0])
        res = []
        x = [1,-1,0,0,1,-1,-1,1]
        y = [0,0,1,-1,-1,-1,1,1]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==word[0]:
                    for dir in range(8):
                        if hlp(grid, word, 1, i + y[dir], j + x[dir], m, n, y[dir], x[dir]):
                            res.append([i,j])
                            break
        return res