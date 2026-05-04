class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        prefix = [0] * len(height)
        prefix[0] = height[0]
        suffix = [0] * len(height)
        suffix[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i-1], height[i])
        for i in range(len(suffix) - 2, -1 , -1):
            suffix[i] = max(suffix[i+1], height[i])
        trapped = 0
        for i in range(len(height)):
            trapped += min(prefix[i], suffix[i]) - height[i]
        return trapped
        