class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(tot):
            if tot == amount:
                return 0
            if tot in cache:
                return cache[tot]
            res = float('inf')
            for c in coins:
                if tot + c <= amount:
                    res = min(1 + dfs(tot + c), res)
            cache[tot] = res
            return res
        res = dfs(0)
        return res if res != float('inf') else -1