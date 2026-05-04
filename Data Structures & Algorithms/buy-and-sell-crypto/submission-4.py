class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for p in prices:
            buy = min(p, buy)
            profit = p - buy
            maxProfit = max(maxProfit, profit)
        return maxProfit