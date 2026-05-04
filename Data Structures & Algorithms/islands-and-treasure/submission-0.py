class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, dist):
            if r >= 0 and r < len(grid) and c < len(grid[r]) and c >= 0:   
                if grid[r][c] >= dist:
                    grid[r][c] = min(grid[r][c], dist)
                    for dr, dc in directions:
                        dfs(r + dr, c + dc, dist + 1)
                
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        return
