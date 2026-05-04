class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,subset):
            nonlocal res
            res.append(subset.copy())
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.remove(nums[j])
        backtrack(0, [])
        return res