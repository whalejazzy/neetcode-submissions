class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort(key=lambda x: x[1])
        if not intervals:
            return res
        
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
 
            if intervals[i][0] < prev:
                res += 1
            else:
                prev = intervals[i][1]
        return res