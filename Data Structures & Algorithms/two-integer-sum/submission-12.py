class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i,n in enumerate(nums):
            if pair.get(n, -1) >= 0:
                return [pair[n], i]
            pair[target - n] = i
            
