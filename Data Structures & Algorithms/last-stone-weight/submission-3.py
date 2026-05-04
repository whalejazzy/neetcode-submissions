class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if abs(x - y) > 0:
                heapq.heappush(heap, -abs(x-y))
        return 0 if len(heap) == 0 else -heap[0]
