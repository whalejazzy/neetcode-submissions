class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-n, i) for i, n in enumerate(nums[:k])]
        heapq.heapify(heap)
        res = []
        res.append(-heap[0][0])
        l = 0
        for r in range(k, len(nums)):
            l += 1
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[r],r))
            if r == 6:
                print(nums[r], heap)
            res.append(-heap[0][0])
            

        return res
