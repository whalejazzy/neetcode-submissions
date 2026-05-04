"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minhp = []
        for i in range(len(intervals)):
            heapq.heappush(minhp, (intervals[i].start, 1))
            heapq.heappush(minhp, (intervals[i].end, -1))
        cnt = maxcnt = 0
        while minhp:
            time, curr = heapq.heappop(minhp)
            while minhp and minhp[0][0] == time:
                curr += heapq.heappop(minhp)[1]
            cnt += curr
            maxcnt = max(maxcnt, cnt)	
        return maxcnt
