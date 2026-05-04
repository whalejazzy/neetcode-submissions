class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        hmap = { '(':')', '{' :'}', '[' : ']'}
        stack = []
        for c in s:
            if c in hmap.keys():
                stack.append(c)
                print(stack)
            elif len(stack) and c == hmap[stack[-1]]:
                stack.pop()
            else:
                return False

        
        return not len(stack)