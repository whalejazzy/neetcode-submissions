class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if len(nums) else 0
        res = nums[:]
        res[1]= max(res[0], res[1])
        for i in range(2, len(nums)):
            res[i] = max(res[i] + res[i -2], res[i - 1])
        return max(res[len(nums) - 1], res[len(nums) - 2])
