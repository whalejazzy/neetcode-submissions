class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters = [0]*26
        for t in tasks:
            letters[ord(t) - ord("A")] += 1
        letters = [-l for l in letters if l > 0]
        heapq.heapify(letters)
        q = deque([])
        time = 0
        while len(letters) > 0 or len(q) > 0:
            time += 1
            if not letters:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(letters)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(letters, q.popleft()[0])
        return time