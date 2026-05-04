class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def isValid(x, y):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])
        
        hp = [(grid[0][0], 0, 0)]
        heapq.heapify(hp)

        visited = set((0, 0))
        lvl = grid[0][0]
        
        while hp:
            newLvl, x, y = heapq.heappop(hp)
            lvl = max(newLvl, lvl)
            
            visited.add((x, y))
            
            if (x,y) == (len(grid) - 1, len(grid[0]) - 1):
                return lvl
            
            for dx, dy in dirs:
                X = x + dx
                Y = y + dy

                if isValid(X, Y) and (X, Y) not in visited:
                    heapq.heappush(hp, (grid[X][Y], X, Y))
        
        return lvl




            



