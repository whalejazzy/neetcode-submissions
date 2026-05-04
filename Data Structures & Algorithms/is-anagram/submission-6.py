class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = {}
        hmap2 = {}
        if len(s) != len(t):
            return False
        for c in s:
            hmap1[c] = hmap1.get(c,0) + 1
        for c in t:
            hmap2[c] = hmap2.get(c,0) + 1
        return hmap1==hmap2
