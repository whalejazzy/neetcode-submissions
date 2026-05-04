class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(amt, i):
            if (amt, i) in dp:
                return dp[(amt, i)]
            if amt == 0:
                return 1
            if amt < 0:
                return 0
            res = 0
            for j in range(i, len(coins)):
                res += dfs(amt - coins[j], j)
            dp[(amt, i)] = res
            return res

            

        return dfs(amount, 0)