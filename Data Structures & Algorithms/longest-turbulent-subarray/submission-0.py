class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [[1]* len(arr) for _ in range(2)]
        maxval = 1
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                dp[1][i] = dp[0][i-1] + 1
                
            if arr[i - 1] < arr[i]:
                dp[0][i] = dp[1][i-1] + 1
            maxval = max(dp[1][i], maxval)
            maxval = max(dp[0][i], maxval)
        return maxval
