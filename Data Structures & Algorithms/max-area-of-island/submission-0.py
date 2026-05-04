class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + sum([dfs(r + dr, c + dc) for dr, dc in directions])

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea