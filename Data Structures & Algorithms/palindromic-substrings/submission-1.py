class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(len(s)):
            #odd
            l = i -1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l -= 1
                r += 1
            #even
            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l -= 1
                r += 1
        return res

            