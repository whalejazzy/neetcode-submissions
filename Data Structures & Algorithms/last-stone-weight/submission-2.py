class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x = -heapq.heappop(minHeap)
            y = -heapq.heappop(minHeap)
            if x != y:
                heapq.heappush(minHeap, -abs(x - y))
        if len(minHeap) == 0:
            heapq.heappush(minHeap, 0) 
        return -minHeap[0]
