class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        stack = []
        par = {"[":"]", "{":"}", "(":")"}
        for c in s:
            if c in par.keys():
                stack.append(c)
            elif stack and par[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return len(stack) == 0
