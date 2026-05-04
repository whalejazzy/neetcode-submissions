class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, wt in times:
            graph[src].append((wt, dst))
        
        visited = set([k])
        hp = graph[k]
        heapq.heapify(hp)
        while hp and len(visited) < n:
            wt, src = heapq.heappop(hp)
            
            visited.add(src)
            
            if len(visited) == n:
                return wt
            
            for newwt, dst in graph[src]:
                if dst not in visited:
                    heapq.heappush(hp, (newwt + wt, dst))
        return -1