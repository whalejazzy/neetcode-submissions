class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg = nums[0]
        pos = nums[0]
        glob = nums[0]
        for n in nums[1:]:
            oldneg = neg
            oldpos = pos
            neg = min(n, neg*n, oldpos*n)
            pos = max(n, pos*n, oldneg*n)
            glob = max(pos,neg, glob)
        return glob