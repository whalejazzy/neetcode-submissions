class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            n = len(nums)
            LIS = 1
            arr = [1] * n
            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if nums[i] < nums[j]:
                        arr[i] = max(arr[i], 1 + arr[j])



            return max(arr)
