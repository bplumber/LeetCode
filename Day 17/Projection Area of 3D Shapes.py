class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = 0
        z = 0
        y = []
        for i in range(len(grid)):
            y.append(0)
        for i in range(len(grid)):
            z+=max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j]!=0:
                    x+=1
                if grid[i][j]>y[j]:
                    y[j] = grid[i][j]
        return x+sum(y)+z
        