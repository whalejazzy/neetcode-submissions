class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {n:[] for n in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        tot = 0
        minHeap = [(0, 0)]
        visit = set()
        while len(visit) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            tot += cost
            for cst, pt in adj[point]:
                if pt not in visit:
                    heapq.heappush(minHeap, (cst, pt))
            
        return tot