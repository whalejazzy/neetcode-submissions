class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((p, d))
        hp = []
        heapq.heapify(hp)
        heapq.heappush(hp, (0, 0, src))
        visited = set()
        while hp:
            price, stops, loc = heapq.heappop(hp)
            
            if loc == dst:
                return price

            if (loc, stops) in visited:
                continue
            
            visited.add((loc, stops))

            for p, d in graph[loc]:
                if stops <= k:
                    heapq.heappush(hp, (price+p, stops + 1, d))
            
        return -1