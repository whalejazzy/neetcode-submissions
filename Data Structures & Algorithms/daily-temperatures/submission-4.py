class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            if stack and temperatures[stack[-1]] < t:
                while stack and temperatures[stack[-1]] < t:
                    idx = stack.pop()
                    res[idx] = i - idx
            stack.append(i)
        return res
