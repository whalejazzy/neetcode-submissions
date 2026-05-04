class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = {}
        lst2 = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                lst1[s[i]]= lst1.get(s[i], 0) + 1
                lst2[t[i]]= lst2.get(t[i], 0) + 1
        return lst1 == lst2