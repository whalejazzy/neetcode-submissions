class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = minSum = nums[0]
        currMin = currMax = 0
        tot = 0
        for n in nums:
            currMin = min(0, currMin)
            currMin += n
            
            currMax = max(0, currMax)
            currMax += n

            minSum = min(minSum, currMin)
            maxSum = max(maxSum, currMax)
            tot += n
        #return maxSum
        return tot - minSum if (maxSum < (tot - minSum)) and tot > 0 else maxSum