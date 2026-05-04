class Solution:
    def rob(self, nums: List[int]) -> int:
        robs = [0] * (len(nums) + 2)
        
        for i in range(2, len(nums)+ 2):
            robs[i] = max(robs[i - 2] + nums[i - 2], robs[i - 1])
        return max(robs[len(robs) - 1], robs[len(robs) - 2])
            
            


