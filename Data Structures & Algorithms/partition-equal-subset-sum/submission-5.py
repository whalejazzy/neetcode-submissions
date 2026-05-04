class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2:
            return False
        def dfs(i, currSum):
            if currSum > tot//2 or i == len(nums):
                return False
            if currSum == tot//2:
                return True
            
            return dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)

        return dfs(0, 0)

