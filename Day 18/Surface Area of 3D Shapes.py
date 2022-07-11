class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)
        temp = []
        for i in range(len(grid[0])):
            temp.append(0)
        grid.insert(0, temp)
        grid.append(temp)
        
        top, hori = 0, 0
        ver = temp.copy()
        for i in range(len(grid)-1):
            for j in range(len(grid[i])-1):
                if grid[i][j]!=0:
                    top+=1
                if grid[i][j+1]-grid[i][j]!=0:
                    hori+=abs(grid[i][j+1] - grid[i][j])
                if grid[i][j]-grid[i+1][j]!=0:
                    ver[j]+=abs(grid[i][j]-grid[i+1][j])
        return top*2 + hori + sum(ver)
        