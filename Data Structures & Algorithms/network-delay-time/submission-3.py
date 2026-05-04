class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()
        maxtime = 0
        while heap:
            lenlevel = len(heap)
            for i in range(lenlevel):
                t, u = heapq.heappop(heap)
                
                if u in visited:
                    continue
                maxtime = max(t, maxtime)    
                visited.add(u)
                
                for vi, ti in edges[u]:
                    
                    heapq.heappush(heap, (t + ti, vi))
        return maxtime if len(visited) == n else -1


