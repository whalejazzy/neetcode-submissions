class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        
        for n in nums[1:]:
            currSum = max(0, currSum)
            currSum += n
            maxSum = max(maxSum, currSum)
        return maxSum