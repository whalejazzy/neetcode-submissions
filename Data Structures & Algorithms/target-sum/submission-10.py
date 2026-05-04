class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        
        for i in range(1, len(nums) + 1):
            for currsum, cnt in dp[i - 1].items():
                dp[i][currsum + nums[i - 1]] += cnt
                dp[i][currsum - nums[i - 1]] += cnt
        return dp[len(nums)][target]