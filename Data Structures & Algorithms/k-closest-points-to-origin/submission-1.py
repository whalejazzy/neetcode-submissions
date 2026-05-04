class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = [[-math.sqrt(x**2 + y**2), [x,y]]  for x,y in points]

        heapq.heapify(lst)

        while len(lst) > k:
            heapq.heappop(lst)

        return [p[1] for p in lst]