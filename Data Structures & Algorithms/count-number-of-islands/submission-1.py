class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(row) for row in grid]
        res = 0
        def bfs(r, c):
            row = r + 1
            if row < len(grid) and not visited[row][c]:
                visited[row][c] = True
                if grid[row][c] == "1":
                    bfs(row, c)
            row = r - 1
            if row >= 0 and not visited[row][c]:
                visited[row][c] = True
                if grid[row][c] == "1":
                    bfs(row, c)
            col = c - 1
            if col >= 0 and not visited[r][col]:
                visited[r][col] = True
                if grid[r][col] == "1":
                    bfs(r, col) 
            col = c + 1
            if col <len(grid[r]) and not visited[r][col]:
                visited[r][col] = True
                if grid[r][col] == "1":
                    bfs(r, col) 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if visited[r][c] or grid[r][c] == "0":
                    continue
                else:
                    res += 1
                    bfs(r,c)
        return res