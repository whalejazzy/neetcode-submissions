class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        tot = 0
        res = 0
        for n in nums:
            tot += n
            if tot - k in prefix:
                res += prefix[tot - k]
            prefix[tot] = prefix.get(tot, 0) + 1
        return res
            
            
