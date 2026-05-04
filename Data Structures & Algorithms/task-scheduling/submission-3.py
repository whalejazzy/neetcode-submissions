class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters =[0]*26
        for t in tasks:
            letters[ord(t) - ord('A')] += 1
        maxHeap = [-l for l in letters if l > 0]
        heapq.heapify(maxHeap)
        time = 0
        q = deque([])
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][0]
            else:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    q.append((time + n, task))
            if q and q[0][0] == time:
                task = q.popleft()[1]
                heapq.heappush(maxHeap, task)
        return time
