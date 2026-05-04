class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = currMin = 0
        globMax = globMin = nums[0]
        tot = 0
        
        for n in nums:
            currMax = max(0, currMax)
            currMin = min(0, currMin)

            currMax += n
            currMin += n
            tot += n


            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)

            print(globMax, globMin)
        
        return globMax if (globMax > (tot - globMin) or (globMax < (tot - globMin) and tot - globMin == 0)) else (tot - globMin)