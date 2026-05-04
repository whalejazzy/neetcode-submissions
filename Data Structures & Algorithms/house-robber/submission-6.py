class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robs = [0] *(len(nums))
        robs[0] = nums[0]
        robs[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            robs[i] = max(robs[i-1], nums[i] + robs[i - 2])
        print(robs)
        return max(robs[len(nums) - 1], robs[len(nums) -2])
