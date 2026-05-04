class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if nums[i] + i >= len(nums) - 1:
                return True

            for j in range(i + 1, nums[i] + i + 1):
                print(j, nums[j])
                if dfs(j):
                    return True
            return False
        return dfs(0)