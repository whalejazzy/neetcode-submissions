class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-/*":
                val1 = stack.pop()
                val2 = stack.pop()
                newval = str(int(eval(val2 + t + val1)))
                stack.append(newval)
            else:
                stack.append(t)
        return int(stack[-1])