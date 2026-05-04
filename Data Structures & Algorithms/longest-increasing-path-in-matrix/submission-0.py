class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        m = len(matrix)
        n = len(matrix[0])
        maxval = 1

        def isValid(x, y):
            return x >= 0 and y >= 0 and x < m and y < n
        
        def dfs(x, y):
            nonlocal maxval

            if (x, y) in cache:
                return cache[(x,y)]
        
            res = 1
            for dx, dy in dirs:
                i, j = x + dx, y + dy
                
                if isValid(i, j) and matrix[i][j] > matrix[x][y]:
                    res = max(res, 1 + dfs(i,j))
            cache[(x,y)] = res
            maxval = max(maxval, res)
            return res
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return maxval


































