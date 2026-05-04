class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,t in times:
            edges[u].append((v, t))
        minHeap = [(0, k)]
        print(edges)
        time = 0
        visit = set()
        while minHeap:
            t, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            time = max(t, time)
            visit.add(v)
            for v2, t2 in edges[v]:
                heapq.heappush(minHeap, (t+t2, v2))
        
        return time if len(visit) == n else -1 