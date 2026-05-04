class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def isValid(x, y):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) 
        
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                       
        INF = 2147483647
        level = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if level < grid[i][j]:
                    grid[i][j] = level
                for dx, dy in dirs:
                    a = i + dx
                    b = j + dy
                    if isValid(a, b) and grid[a][b] == INF:
                        q.append((a, b))
            level += 1
    

