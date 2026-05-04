class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         lst = set(nums)
         return len(nums) > len(lst)