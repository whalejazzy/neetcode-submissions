class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        res = []
        i = 0
        newstart, newend = newInterval

        while i < len(intervals) and newstart > intervals[i][1]:
            res.append(intervals[i])
            i += 1
            
        newstart = min(intervals[i][0], newstart) if i < len(intervals) else newstart
        while i < len(intervals) and newend >= intervals[i][0]:
            newend = max(newend, intervals[i][1])
            i += 1
            
        res.append([newstart, newend])
        res.extend(intervals[i:])
        return res
