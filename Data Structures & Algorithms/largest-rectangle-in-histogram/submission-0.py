class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rect = 0
        for i, h in enumerate(heights):
            prev = None
            while stack and stack[-1]['height'] > h:
                prev = stack.pop()
                rect = max(rect, prev['height']*(i - prev['index']))
            if prev:
                stack.append({'height':h, 'index':prev['index']})
            else:
                stack.append({'height':h, 'index': i})
        print(stack)
        while stack:
            pair = stack.pop()
            rect = max(rect, (len(heights) - pair['index']) * pair['height'])
        return rect