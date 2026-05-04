class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        if grid[0][0] == 1:
            return -1
        q.append((0, 0))
        l = 0
        dirs = [[1,0], [0, 1], [-1, 0], [0, -1], [-1, 1], [1,1], [-1, -1], [1, -1]]
        def isValid(x, y):
            return x >= 0 and y >=0 and x < len(grid) and y < len(grid[x])
        while q:
            levellen = len(q)
            print(q, l)
            for _ in range(levellen):
                x, y = q.popleft()
                if (x, y) == (len(grid) - 1,len(grid[0]) - 1):
                    return l+1
                grid[x][y] = 1
                for dx, dy in dirs:
                    if isValid(x+dx, y+dy) and grid[x+dx][y+dy] == 0:
                        q.append((x+dx, y+dy))
            l += 1
        return -1
                