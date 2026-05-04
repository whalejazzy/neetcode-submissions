class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def sol(grid):
            m = len(grid)
            n = len(grid[0])
            visit = set()
            hp = [(0, 0, 0)]
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            def isValid(x, y):
                return x >= 0 and y >= 0 and x < m and y < n and (x,y) not in visit
            while hp:
                eff, x, y = heapq.heappop(hp)
                if (x, y) == (m -1, n - 1):
                    return eff
                if (x, y) in visit:
                    continue
                
                visit.add((x, y))
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if isValid(nx, ny):
                        diff = abs(grid[x][y] - grid[nx][ny])
                        heapq.heappush(hp, (max(diff, eff), nx, ny))
        return sol(heights)