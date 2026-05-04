class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        sign = ""
        maxLen = 0
        L = 0
        R = 1

        while R < len(arr):
            if sign == ">":
                if arr[R] > arr[R - 1]:
                    L = R - 1
                elif arr[R] == arr[R-1]:
                    sign = ""
                    L = R
                else:
                    sign = "<"
            elif sign == "<":
                if arr[R] < arr[R - 1]:
                    L = R - 1
                elif arr[R] == arr[R-1]:
                    sign = ""
                    L = R
                else:
                    sign = ">"
            else:
                if arr[R] > arr[R - 1]:
                    sign = ">"
                elif arr[R] == arr[R-1]:
                    sign = ""
                    L = R
                else:
                    sign = "<"
            maxLen = max(maxLen, R - L + 1)
            R += 1
        return maxLen
        



