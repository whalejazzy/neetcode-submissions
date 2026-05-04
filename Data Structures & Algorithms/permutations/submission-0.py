class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        selected = [False]*len(nums)
        def backtrack(curr, selected):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not selected[i]:
                    curr.append(nums[i])
                    selected[i] = True
                    backtrack(curr, selected)
                    selected[i] = False
                    curr.pop()
        backtrack([], selected)
        return res
