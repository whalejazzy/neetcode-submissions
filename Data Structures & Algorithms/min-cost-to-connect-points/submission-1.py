class Union:
            def __init__(self, n):
                self.par = list(range(n + 1))
                self.size = [1] *(n + 1)
            def find(self, node):
                if self.par[node] != node:
                    self.par[node] = self.find(self.par[node])
                return self.par[node]
            def union(self, u, v):
                p1, p2 = self.find(u), self.find(v)
                if p1 == p2:
                    return False
                if self.size[p1] >= self.size[p2]:
                    self.par[p2] = p1
                    self.size[p1] += self.size[p2]
                elif self.size[p1] < self.size[p2]:
                    self.par[p1] = p2
                    self.size[p2] += self.size[p1]
                return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = Union(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u,v):
                res += dist
        return res

        
                    
                    


        