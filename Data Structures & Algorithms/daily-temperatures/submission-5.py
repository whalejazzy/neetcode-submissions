class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                print(t, stack[-1][0])
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((t, i))
        return res

