class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
        def isValid(x, y):
            return x >= 0 and y >=0 and x < len(grid) and y < len(grid[0])
        def dfs(x, y):
            if grid[x][y] == "0":
                return
            grid[x][y] = "0"
            for dx, dy in dirs:
                if isValid(x + dx, y + dy):
                    dfs(x + dx, y + dy)
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x, y)
        return res
