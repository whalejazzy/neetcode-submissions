class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        paths = cost
        for i in range(2, len(paths)):
            paths[i] = min(paths[i - 1], paths[i - 2]) + cost[i]
        return min(paths[len(paths) - 1], paths[len(paths) - 2])

        