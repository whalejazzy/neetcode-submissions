class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digtoletter = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def dfs(i, curr):
            if i >= len(digits):
                if digits and len(curr) == len(digits):
                    res.append(curr[:])
                return
            for d in digtoletter[digits[i]]:
                curr += d
                dfs(i+1, curr)
                curr = curr[:-1]

        dfs(0, "")
        return res