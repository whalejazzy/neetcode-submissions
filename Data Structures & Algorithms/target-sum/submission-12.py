class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1
        for i in range(len(nums)):
            for tot, cnt in dp[i].items():
                dp[i + 1][tot - nums[i]] += cnt
                dp[i + 1][tot + nums[i]] += cnt
        return dp[len(nums)][target]
        
        cache = {}
        def dfs(i, currSum):
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            if i == len(nums):
                return 1 if currSum == target else 0
            res = dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])

            cache[(i, currSum)] = res
            return res
        return dfs(0, 0)