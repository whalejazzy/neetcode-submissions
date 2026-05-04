class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]* len(height)
        postfix = [0]* len(height)
        res = 0
        
        prefix[0] = height[0]
        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i-1], height[i])
        
        postfix[len(height) - 1] = height[len(height) - 1]
        for i in range(len(prefix) - 2, -1 ,-1):
            postfix[i] = max(postfix[i+1], height[i])  
        
        for i in range(len(height)):
            res += min(prefix[i],postfix[i]) - height[i]
       
        return res
