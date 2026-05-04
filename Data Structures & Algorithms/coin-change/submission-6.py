class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def dfs(amt):
            if amt in dp:
                return dp[amt]
            if amt == 0:
                return 0
            res = 1e9
            for c in coins:
                if amt - c >= 0:
                    res = min(res,1 + dfs(amt - c))
                    
            dp[amt] = res
            return dp[amt]
       
        sol = dfs(amount)
        return sol if sol != 1e9 else -1
