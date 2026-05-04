class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # elif s == t:
        #     return s
        tCount, sCount = {}, {}
        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
        
        matches = 0
        for c in tCount.keys():
            if c in sCount.keys():
                matches += (1 if sCount[c] >= tCount[c] else 0)
        
        l = 0
        res = ""
        res_len = 1001
        for r in range(len(t), len(s)):
            while l < r and (s[l] not in tCount or sCount[s[l]] != tCount[s[l]]):
                sCount[s[l]] -= 1
                l += 1
            if matches == len(tCount.keys()):
                if len(s[l:r]) < res_len:
                    res_len = len(s[l:r])
                    res = s[l:r]
                sCount[s[l]] -= 1
                matches -= 1
                l += 1
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in tCount.keys():
                matches += (1 if sCount[s[r]] == tCount[s[r]] else 0)
        while l < len(s) and (s[l] not in tCount or sCount[s[l]] != tCount[s[l]]):
                sCount[s[l]] -= 1
                l += 1
        if matches == len(tCount.keys()):
            if len(s[l:]) < res_len:
                res_len = len(s[l:])
                res = s[l:]
        return res