class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s.lower():
            if ord(c) >= ord('a') and ord(c) <= ord('z') or (ord(c) >= ord('0') and ord(c) <= ord('9')):
                res+= c
        print(res)
        return res== res[::-1]