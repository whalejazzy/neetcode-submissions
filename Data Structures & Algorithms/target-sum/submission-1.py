class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, currSum):
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            if i == len(nums):
                if currSum == target:
                    return 1
                else: 
                    return 0
            res = dfs(i+1, currSum - nums[i]) + dfs(i+1, currSum + nums[i])
            cache[(i, currSum)] = res
            return res
        
        return dfs(0, 0)
