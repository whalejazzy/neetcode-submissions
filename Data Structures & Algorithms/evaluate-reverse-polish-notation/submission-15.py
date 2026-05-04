class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                val1 = stack.pop()
                val2 = stack.pop()
                newval = int(eval(val2 + token + val1))
                stack.append(str(newval))
            else:
                stack.append(token)
        return int(stack[-1])