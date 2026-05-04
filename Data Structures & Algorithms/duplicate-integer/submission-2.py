class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for i in range(len(nums)):
            if (i+1) < len(nums) and nums[i] in nums[i+1:]:
                return True
         return False