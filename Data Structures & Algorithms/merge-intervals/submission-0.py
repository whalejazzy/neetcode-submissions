class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        l = 0
        r = 0
        res = []
        while r < len(intervals):
            max_val = intervals[r][1]
            while r < len(intervals) - 1 and max_val >= intervals[r+1][0]:
                r += 1
                max_val = max(intervals[r][1], max_val)
            res.append([intervals[l][0], max_val])
            r += 1
            l = r
            
        return res