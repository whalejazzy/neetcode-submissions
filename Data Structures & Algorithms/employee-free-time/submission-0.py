class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        hp = []
        for i, employee in enumerate(schedule):
            if employee:
                start = employee[0].start
                heapq.heappush(hp, (start, i, 0))
        res = []
        if not hp:
            return []
        maxtime = hp[0][0]
        while hp:
            time, empID, idx = heapq.heappop(hp)
            if maxtime < time:
                res.append(Interval(maxtime, time))
            maxtime = max(maxtime, schedule[empID][idx].end)
            if idx + 1 < len(schedule[empID]):
                next_interval = schedule[empID][idx + 1]
                heapq.heappush(hp, (next_interval.start, empID, idx + 1))
        return res