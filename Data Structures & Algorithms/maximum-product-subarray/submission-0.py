class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = max(nums)
        for n in nums:
            tmp = n * currMax

            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            res = max(currMax, currMin, res)
        return res