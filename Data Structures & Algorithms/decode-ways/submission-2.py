class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1 ,-1):
            res = 0
            if s[i] != "0":
                res += dp[i + 1]
            if i + 1 < len(s) and int(s[i: i + 2]) > 9 and int(s[i: i + 2]) < 27:
                res += dp[i + 2]
            dp[i] = res
        return dp[0]