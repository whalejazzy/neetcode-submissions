class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = dp2 = 1
        for i in range(len(s) - 1, -1 ,-1):
            temp = dp1
            res = 0
            if s[i] != "0":
                res += dp1
            if i + 1 < len(s) and int(s[i: i + 2]) > 9 and int(s[i: i + 2]) < 27:
                res += dp2
            dp1 = res
            dp2 = temp
        return dp1