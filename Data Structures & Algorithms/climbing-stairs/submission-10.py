class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev1 = 1
        prev2 = 2
        if n <= 2:
            return n
        for i in range(2,n):
            temp = prev2
            prev2 = prev2 + prev1
            prev1 = temp
        return prev2
