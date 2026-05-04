class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robs1 = 0
        robs2 = 0
        for i in range(len(nums)):
            temp = robs2
            robs2 = max(robs2, nums[i] + robs1)
            robs1 = temp
        
        return max(robs1, robs2)
