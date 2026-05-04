class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        val = heap[0]
        for _ in range(k):
            val = heapq.heappop(heap)
        return -val

            