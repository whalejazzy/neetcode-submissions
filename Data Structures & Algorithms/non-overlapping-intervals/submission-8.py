class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        prev = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
                if start >= prev:
                    prev = end
                else:
                    res += 1
                    
        return res