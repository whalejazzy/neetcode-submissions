class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key= lambda x: x[0])
        res = []
        l = 0
        r = 1
        while l < len(intervals):
            curr = intervals[l]

            while r < len(intervals) and curr[1] >= intervals[r][0]:
                curr[1] = max(curr[1], intervals[r][1])
                r += 1
            res.append(curr)
            l = r
        return res



