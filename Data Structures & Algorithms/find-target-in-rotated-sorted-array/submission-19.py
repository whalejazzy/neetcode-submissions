class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r-l) // 2 + l
            print(m)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: #left side of array
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < target and nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
        return -1