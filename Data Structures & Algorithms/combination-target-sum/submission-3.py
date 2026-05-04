class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, path):
            nonlocal res
            
            if i == len(nums) or curr > target:
                return
            
            if curr == target:
                res.append(path.copy())
                return
            
            path.append(nums[i])
            
            dfs(i,curr+nums[i], path)
            
            path.pop()
            
            dfs(i+1, curr, path)

        dfs(0,0,[])
        return res