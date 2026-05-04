class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((-prob, v))
            graph[v].append((-prob, u))

        hp = graph[start_node]
        heapq.heapify(hp)
        totprob = 1
        
        visited = set([start_node])
        
        while hp:
            
            prb, nd = heapq.heappop(hp)

            visited.add(nd)

            if nd == end_node:
                return -prb
            
            for newprb, u in graph[nd]:
                if u not in visited:
                    heapq.heappush(hp, (-prb * newprb, u))
        return 0
