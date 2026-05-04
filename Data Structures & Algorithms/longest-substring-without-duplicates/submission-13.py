class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[i])
            res = max(res, len(substr))
        return res