class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (r - l) // 2 + l
        while l <= r:
            m = (r-l) // 2 + l
            if nums[l] < nums[r]:
                return nums[l]
            if nums[l] < nums[m]:
                l = m + 1
            else:
                l += 1
        return nums[m]