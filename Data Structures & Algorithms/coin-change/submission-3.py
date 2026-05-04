class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(cnt):
            if cnt == 0:
                return 0
            if cnt in dp:
                return dp[cnt]
            res = 1e9
            for c in coins:
                if cnt - c >= 0:
                    res = min(res, 1 + dfs(cnt - c))
            dp[cnt] = res
            return res
        sol = dfs(amount)
        return sol if sol != 1e9 else -1
            