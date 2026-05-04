class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = currMin = currMax = 0
        minSum = maxSum = nums[0]
        for n in nums:
            currMax = max(currMax, 0)
            currMin = min(currMin, 0)

            currMax += n
            currMin += n
            totalSum += n

            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
        return maxSum if (totalSum ==  minSum or maxSum > (totalSum - minSum)) else totalSum - minSum

