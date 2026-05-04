class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(-math.sqrt(p[0]**2 + p[1]**2), p) for p in points]
        heapq.heapify(dists)
        while len(dists) > k:
            heapq.heappop(dists)
        res = []
        
        for d in dists:
            res.append(d[1])
        return res