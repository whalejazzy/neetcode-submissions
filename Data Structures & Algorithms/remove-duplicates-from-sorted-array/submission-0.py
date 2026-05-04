class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        while L < len(nums) - 1:
            if nums[L] == nums[L + 1]:
                R = L + 1
                while R < len(nums) and nums[R] == nums[L]:
                    R += 1

                for _ in range(R - L - 1):

                    nums.pop(L)
            L += 1
        return len(nums)

