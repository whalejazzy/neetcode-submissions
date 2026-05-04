class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]* len(nums)
        right = [1]*len(nums)
        res = [1]*len(nums)
        for i in range(len(nums) - 1):
            left[i+1] = left[i]*nums[i]
        for i in range(len(nums) - 1, 0, -1):
            right[i-1] = right[i]* nums[i]
        for i in range(len(nums)):
            res[i] = left[i]*right[i]
        return res