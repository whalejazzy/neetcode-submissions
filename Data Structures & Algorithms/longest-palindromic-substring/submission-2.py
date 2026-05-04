class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        reslen = 0
        for i in range(len(s)):
            #odd case
            rightind = i + 1
            leftind = i - 1
            currlen = 1
            while leftind >= 0 and rightind < len(s) and s[leftind] == s[rightind]:
                currlen += 2
                rightind += 1
                leftind -= 1
            if currlen > reslen:
                left = leftind +1
                right = rightind
                reslen = currlen
            
            #even case
            rightind = i
            leftind = i - 1
            currlen = 0
            while leftind >= 0 and rightind < len(s) and s[leftind] == s[rightind]:
                currlen += 2
                rightind += 1
                leftind -= 1
            if currlen > reslen:
                left = leftind +1
                right = rightind
                reslen = currlen

        return s[left: right]