class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        #t = grid[0][0]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            visit.add((r,c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR, newC) in visit or newR < 0 or newR > N -1 or newC < 0 or newC > N - 1:
                    continue
                heapq.heappush(minHeap, (max(t, grid[newR][newC]), newR, newC))
        return t


            