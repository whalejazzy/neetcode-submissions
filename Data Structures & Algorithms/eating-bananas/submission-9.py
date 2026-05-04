class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def isValid(n):
            curr = 0
            for p in piles:
                curr += math.ceil(p/n)
                if curr > h:
                    return False
            return True
        res = r
        while l <= r:
            m = (r + l) //2
            if isValid(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res