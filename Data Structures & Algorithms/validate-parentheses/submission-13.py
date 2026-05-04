class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in dct.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and dct[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0