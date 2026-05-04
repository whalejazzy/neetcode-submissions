class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums) 
        res = [1] * len(nums)
        for i, n in enumerate(nums[:len(nums) - 1]):# to the left of num[i]
            prefix[i+1] = prefix[i] * n
        
        for i in range(len(nums) - 1,0,-1):# to the right of num[i]
            suffix[i-1] = suffix[i] * nums[i]
            
        for i in range(len(prefix)):
            res[i] = prefix[i]*suffix[i]
        
        return res
            
