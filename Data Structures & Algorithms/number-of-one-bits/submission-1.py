class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        res = 0

        for b in n[2:]:
            
            if b == "1":

                res += 1
            
            
        return res

            