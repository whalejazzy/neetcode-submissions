class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"
        for t in tokens:
            if t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                res = str(int(eval(op1+t+op2)))
                stack.append(res)
            else:
                stack.append(t)
        return int(stack[-1])
