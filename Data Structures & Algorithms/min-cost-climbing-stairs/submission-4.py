class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr = [1000] * len(cost)
        curr[0] = cost[0]
        curr[1] = cost[1]
        for i in range(2 ,len(cost)):
            curr[i] = min(curr[i - 1], curr[i - 2])  + cost[i]
        return min(curr[len(cost) - 1], curr[len(cost) - 2])