class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, tot):
            if (i, tot) in cache:
                return cache[(i, tot)]
            if tot == amount:
                return 1
            
            res = 0

            if tot + coins[i] <= amount:
                res += dfs(i, tot + coins[i])
            
            if i < len(coins) - 1:
                res += dfs(i + 1, tot)
            

            cache[(i, tot)] = res
            return res
        return dfs(0, 0)