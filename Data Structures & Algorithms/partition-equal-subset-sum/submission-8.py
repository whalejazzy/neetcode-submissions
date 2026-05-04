class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        dp = {}
        if tot%2:
            return False
        def dfs(i, currSum):
            if currSum > tot//2 or i == len(nums):
                return False
            if currSum == tot//2:
                return True
            if (i,currSum) in dp:
                return dp[(i, currSum)]
            sol = dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)
            dp[(i, currSum)] = sol
            return sol

        return dfs(0, 0)

