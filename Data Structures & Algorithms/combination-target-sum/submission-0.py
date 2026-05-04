class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        solution = []
        def dfs(i):
            s = sum(solution)
            if i >= len(nums) or s >= target:
                if s == target:
                    res.append(solution.copy())
                return
            solution.append(nums[i])
            dfs(i)
            solution.pop()
            dfs(i+1)
        dfs(0)
        return res