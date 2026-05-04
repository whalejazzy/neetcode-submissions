class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            rob1 = rob2 = 0
            for n in arr:
                temp = rob2
                rob2 = max(rob1 + n, rob2)
                rob1 = temp
            return max(rob1, rob2)
        return max(helper(nums[1:]), helper(nums[:len(nums) - 1]))