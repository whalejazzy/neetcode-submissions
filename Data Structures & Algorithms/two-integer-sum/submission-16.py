class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, n in enumerate(nums):
            if n in idx:
                return [idx[n], i]
            idx[target - n] = i
            
