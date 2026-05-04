class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = nums[0]
        for i, n in enumerate(nums[:-1]):
            if i == maxReach and n == 0:
                return False
            maxReach = max(i + n, maxReach)
        return True
            