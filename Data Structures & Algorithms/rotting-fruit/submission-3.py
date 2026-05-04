class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        time = -1
        fresh = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                elif grid[x][y] == 2:
                    q.append((x, y))
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        def isValid(x, y):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])
        while q:
            time += 1
            lenlevel = len(q)
            for i in range(lenlevel):
                x, y = q.popleft()
                for dx, dy in directions:
                    if isValid(x +dx, y +dy) and grid[x + dx][y+dy] == 1:
                        fresh -= 1
                        grid[x + dx][y + dy] = 2
                        q.append((x + dx, y + dy))
            


        return max(time, 0) if fresh == 0 else - 1