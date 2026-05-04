class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [0, 1], [-1 ,0], [0, -1]]
        def isValid(x, y):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x])
        
        def dfs(x, y):
            grid[x][y] = 0
            res = 1
            for dx, dy in dirs:
                if isValid(x + dx, y + dy) and grid[x + dx][y + dy] == 1:
                    res += dfs(x + dx, y + dy)
                    
            return res
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea

