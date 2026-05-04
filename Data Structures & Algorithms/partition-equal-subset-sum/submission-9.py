class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2:
            return False
        dp = {}

        def dfs(i, currSum):
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            if currSum == tot//2:
                return True
            if i == len(nums):
                return False
            
            res = dfs(i + 1, currSum) or dfs(i + 1, currSum + nums[i])
            dp[(i, currSum)] = res
            return res
        return dfs(0,0)
