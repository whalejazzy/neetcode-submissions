class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(m):
            t = h
            for p in piles:
                t -= math.ceil(p/m)
            return t
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (r-l)// 2 + l
            if check(m)>= 0:
                r = m - 1
                res = min(m, res)
            else:
                l = m + 1
        return res
