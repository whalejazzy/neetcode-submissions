class Solution:
    def numDecodings(self, s: str) -> int:
        single = 1
        double = 1
	
        for i in range(len(s) - 1, -1, -1):
            temp = single
            if int(s[i]) == 0:
                single = 0
            if i + 1 < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                single += double
            double = temp

        return single
