class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac = set()
        atl = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, path, prev):
            if r < 0  or c < 0 or r == len(heights) or c == len(heights[0]) or prev > heights[r][c] or (r, c) in path:
                return
            path.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, path, heights[r][c])
        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[r]) - 1, atl, heights[r][len(heights[r]) - 1])
        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights) - 1, c, atl, heights[len(heights) - 1][c])
        
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if (r, c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        
            