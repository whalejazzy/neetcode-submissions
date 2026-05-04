class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}
        for i, n in enumerate(nums):

            if target - n in lst:
                return [lst[target- n], i] 
            lst[n] = i