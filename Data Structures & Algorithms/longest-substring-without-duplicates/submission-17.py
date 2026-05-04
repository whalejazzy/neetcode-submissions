class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        longest = 0
        l = 0
        r = 0
        while r < len(s):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            
            substr.add(s[r])
            r += 1
            longest = max(longest, r - l)
            
        return longest