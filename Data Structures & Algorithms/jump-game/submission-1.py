class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {len(nums) - 1: True}
        def dfs(i):
            if i in dp:
                return dp[i]
            if nums[i] + i >= len(nums) - 1:
                dp[i] = True
                return True

            for j in range(i + 1, nums[i] + i + 1):
                print(j, nums[j])
                if dfs(j):
                    return True
            dp[i] = False
            return False
        return dfs(0)