class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        substr = set()
        for i in range(len(s)):
            while s[i] in substr:
                substr.remove(s[l])
                l+=1
            substr.add(s[i])
            res = max(res, len(substr))
        return res