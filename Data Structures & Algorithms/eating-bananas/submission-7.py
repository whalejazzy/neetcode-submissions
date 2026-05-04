class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        h_left = h
        def check(m):
            t = h
            for p in piles:
                cnt = math.ceil(p/m) 
                t -= cnt
            return t

        while l <= r:
            m = ((r - l) // 2) + l
            
            if check(m) >= 0:
                r = m - 1
                res = min(m, res)
            else:
                l = m + 1
        return res
        
        

