class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        curr = 0
        L = 0
        for R in range(len(nums)):
            curr += nums[R]
            while curr >= target:
                res = min(res, R - L + 1)
                curr -= nums[L]
                L += 1
        return res if res != len(nums) + 1 else 0
