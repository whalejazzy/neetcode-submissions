class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(curr):
            if curr in dp:
                return dp[curr]
        
            if curr == 0:
                return 0
            
            res = 1e9
            for c in coins:
                if curr - c >= 0:
                    res = min(res, dfs(curr -c) + 1)

            dp[curr] = res
            return res

        sol = dfs(amount)
        return sol if sol != 1e9 else -1


