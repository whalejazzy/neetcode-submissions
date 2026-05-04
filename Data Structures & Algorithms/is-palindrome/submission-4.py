class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace(",", "")
        s = s.replace(".", "")
        s = s.replace("'", "")
        s = s.replace(";", "")
        s = s.replace(":", "")
        s = s.lower()
        print(s, s[::-1])
        return s == s[::-1]