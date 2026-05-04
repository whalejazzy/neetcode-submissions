class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        

        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[l] = height[l]
        suffix[r] = height[r]
        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i-1], height[i])
        for i in range(len(prefix) - 2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        area = 0
        for i in range(len(height)):
            area += min(prefix[i],suffix[i]) - height[i]
        return area