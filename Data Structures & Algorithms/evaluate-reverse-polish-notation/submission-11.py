class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+=*/-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(str(int(eval(val2 + t + val1))))
            else:
                stack.append(t)
            print(stack)
        return int(stack[-1])
