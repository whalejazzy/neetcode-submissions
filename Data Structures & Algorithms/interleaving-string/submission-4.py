class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def dfs(p1, p2, p3):
            if (p1,p2, p3) in cache:
                return cache[(p1,p2, p3)]
            if p3 == len(s3):
                return True
            tempp1 = p1
            tempp3 = p3
            if tempp1 < len(s1) and s3[tempp3] == s1[tempp1]:
                while tempp1 < len(s1) and s3[tempp3] == s1[tempp1]:
                    tempp1 += 1
                    tempp3 += 1
                if dfs(tempp1, p2, tempp3):
                    cache[(tempp1,p2, tempp3)] = True
                    return True
            tempp2 = p2
            tempp3 = p3
            if tempp2 < len(s2) and s3[tempp3] == s2[tempp2]:
                while tempp2 < len(s2) and s3[tempp3] == s2[tempp2]:
                    tempp2 += 1
                    tempp3 += 1
                if dfs(p1, tempp2, tempp3):
                    cache[(p1,tempp2, tempp3)] = True
                    return True
            cache[(p1,p2,p3)] = False
            return False
        return dfs(0,0,0)
            
                
            

