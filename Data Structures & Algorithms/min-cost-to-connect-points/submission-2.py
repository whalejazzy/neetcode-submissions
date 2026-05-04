class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {p: [] for p in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        hp = [(0, 0)]
        res = 0 
        visit = set()
        heapq.heapify(hp)
        while len(visit) < n:
            cost, node = heapq.heappop(hp)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neiCost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(hp, (neiCost, nei))
        return res

