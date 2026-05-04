class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        # 3 states at any point in time: -can buy
        #                                -holding
        #                                -cooldown
        # we need to store in each dp the current day as well as our state, then perform dfs

        def dfs(i, state):
            
            if (i, state) in dp:
                return dp[(i, state)]
            
            if i == len(prices):
                return 0
            
            if state == "canbuy":
                res = max(-prices[i] + dfs(i + 1, "holding"), 
                        dfs(i+1, "canbuy"))
                dp[(i, state)] = res
            elif state == "holding":
                
                res = max(dfs(i + 1, "holding"),
                        dfs(i+1, "cooldown") + prices[i])
                dp[(i, state)] = res

            else: #cooldown
                res = dfs(i+1, "canbuy")
                dp[(i, state)] = res
            return res
        sol = dfs(0,"canbuy")

        return sol
