class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if len(nums) > 0 else 0
        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = curr
            curr = max(prev + nums[i], curr)
            prev = temp
        return curr

