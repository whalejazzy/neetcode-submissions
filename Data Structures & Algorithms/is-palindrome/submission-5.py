class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        out = ""
        for c in s:
            if c.isalnum():
                out += c
        return (out == out[::-1])