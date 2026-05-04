class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        def dfs(arr):

            if tuple(arr) in cache:
                return cache[tuple(arr)]
            if len(arr) == 1:
                return arr[0]
            res = 0
            for i in range(len(arr)):
                if i == 0:
                    res = max(res, dfs(arr[1:]) + arr[i]* arr[i + 1])
                elif i == len(arr) - 1:
                    res = max(res, dfs(arr[:len(arr) - 1])+ arr[i] * arr[i - 1])
                else:
                    res = max(res, dfs(arr[:i] + arr[i+1:]) + arr[i] *arr[i - 1] * arr[i + 1])
            cache[tuple(arr)] = res 
            return res
        return dfs(nums)
            