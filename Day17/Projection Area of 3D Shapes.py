class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = 0
        for i in grid:
            for j in i:
                if j!=0:
                    x+=1
        y = []
        for i in range(len(grid)):
            y.append(0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]>y[j]:
                    y[j] = grid[i][j]
        y_sum = sum(y)
        z = 0
        for i in grid:
            z+=max(i)
        return x+y_sum+z
        