class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        sign = "" # could be ">" "<" or ""
        maxlen = 1
        for r in range(1, len(arr)):
            
            if (arr[r] > arr[r - 1] and sign == ">") or (arr[r] < arr[r - 1] and sign == "<"):
                l = r - 1
            elif arr[r] > arr[r - 1]:
                sign = ">"
            elif arr[r] < arr[r - 1]:
                sign = "<"
            elif arr[r] == arr[r - 1]:
                l = r

            
            
            maxlen = max(maxlen, r - l + 1)
        return maxlen