class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tmap = {}
        smap = {}
        res = ""
        length = 10000
        if len(t) > len(s):
            return ""
        def check(smap, tmap):
            for c in tmap.keys():
                if c not in smap or smap[c] < tmap[c]:
                    return False
            return True
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        l = 0
        r = 0
        
        while r < len(s):
            
            smap[s[r]] = smap.get(s[r], 0) + 1
            r += 1
            while check(smap, tmap):
                res = s[l: r] if (r - l + 1) < length else res
                length = min(length, r - l + 1)
                smap[s[l]] -= 1
                l += 1
                
        return res
        
        