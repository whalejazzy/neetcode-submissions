class Solution:
    def climbStairs(self, n: int) -> int : 
        dp = {}
        dp[1] = 1
        dp[2] = 2
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = dfs(i - 1) + dfs(i - 2)
            return dp[i]
        
        return dfs(n)
