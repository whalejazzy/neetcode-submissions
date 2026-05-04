class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = heights[0]
        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0 and stack[-1][1] > h:
                start, height = stack.pop()
                res = max(res, height*(i - start))
            stack.append((start, h))
        while len(stack) > 0:
            s, height = stack.pop()
            res = max(res, height*(len(heights) - s))
        return res 