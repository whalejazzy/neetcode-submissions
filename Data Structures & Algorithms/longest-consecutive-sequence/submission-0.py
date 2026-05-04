class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            cons = 1
            nxt = num + 1
            while nxt in nums:
                nxt += 1
                cons += 1
            if cons > out:
                out = cons
        return out